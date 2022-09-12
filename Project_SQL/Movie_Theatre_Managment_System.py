import mysql.connector

connection = mysql.connector.connect(host="localhost", user="root", password="pranav05")
mycursor = connection.cursor()

mycursor.execute("create database if not exists Movie_Theatre_School_Project")
mycursor.execute("use Movie_Theatre_School_Project")

def check_exists(id, table):
    mycursor.execute(f"select * from {table}")

    for i in mycursor:
        if i[0] == id:
            mycursor.fetchall()
            return True
    return False

#Creating Tables-----------------------------------------------------------------------------------------
mycursor.execute("create table if not exists user(user_id int primary key auto_increment, name varchar(30), status varchar(20), DOJ Date, username varchar(10), password varchar(25))")
mycursor.execute("create table if not exists customer(customer_id int primary key auto_increment, name varchar(30), phone_number char(14), email varchar(40), membership varchar(8) default 'bronze')")
mycursor.execute("create table if not exists movie(Movie_id int primary key auto_increment, name varchar(30), duration_mins int, pg_rating varchar(5),release_date date)")
mycursor.execute("create table if not exists theatre_hall(hall_id int primary key auto_increment, type varchar(10), num_seats int)")
mycursor.execute("create table if not exists screening(screening_id int primary key auto_increment, movie_id int not null references movie(movie_id), hall_id int not null references theatre_hall(hall_id), start_time char(5), date_screening date, ticket_price int)")
mycursor.execute("create table if not exists ticket(ticket_id int primary key auto_increment, customer_id int not null references customer(customer_id), screening_id int not null references screening(screening_id), seat_no varchar(3))")
try:
    mycursor.execute("insert into user values(1, 'Test_User', 'admin', '2022-01-01', 'user1', '1234')")
    connection.commit()
except:
    pass

try:
    mycursor.execute("insert into customer values(1, 'testcust1', '+971-501234567', '1@gmail.com','bronze')")
    mycursor.execute("insert into customer values(2, 'testcust2', '+971-551234567', '2@gmail.com','silver')")
    mycursor.execute("insert into customer values(3, 'testcust3', '+971-581234567', '3@gmail.com','gold')")
    mycursor.execute("insert into customer values(4, 'testcust4', '+971-521234567', '4@gmail.com','platinum')")
    connection.commit()
except:
    pass

#Tickets-----------------------------------------------------------------------------------------------------
def book_seats():
    print("Test Customer ID's: 1 - Bronze, 2 - Silver, 3 - Gold, 4 - Platinum")
    customer_id = int(input("Enter Customer ID: "))
    if not check_exists(customer_id, "customer"):
        print("Customer ID Not Found")
        return
    
    screening_id = int(input("Enter Screening ID: "))
    if not check_exists(screening_id, "screening"):
        print("Screening ID Not Found")
        return

    seat_no = input("Enter Seat Number: ")

    if not(seat_no[-1].isalpha() and seat_no[:-1].isnumeric()):
        print("Error: Not A Valid Seat Number")
        return

    mycursor.execute(f"select seat_no from ticket where screening_id={screening_id}")

    for i in mycursor:
        if seat_no == i[0]:
            print("Seat Already Booked")
            mycursor.fetchall()
            return
    
    mycursor.execute(f"select ticket_price from screening where screening_id={screening_id}")
    price = mycursor.fetchone()[0]

    mycursor.execute(f"select membership from customer where customer_id={customer_id}")
    membership = mycursor.fetchone()[0]

    price -= membership_discounts[membership] * price/100

    print(f"Price Of Booking: {price} ({membership_discounts[membership]}% {membership} Membership Discount)")
    
    ch = input("Confirm Booking?(y/n): ").lower()

    if ch == 'y':
        mycursor.execute("select * from ticket")
        mycursor.fetchall()

        if mycursor.rowcount <= 0:
            mycursor.execute(f"insert into ticket values(1, {customer_id}, {screening_id}, '{seat_no}')")
            connection.commit()
            return

        mycursor.execute(f"insert into ticket(customer_id, screening_id, seat_no) values({customer_id}, {screening_id}, '{seat_no}')")
        connection.commit()        

        update_membership(customer_id)

def search_booking():
    menu = "Search By:-\n1. Customer ID\n2. Screening ID\nInput: "
    ch = input(menu)

    if ch == '1':
        cust_id = int(input("Enter Customer ID: "))
        mycursor.execute(f"select * from ticket where customer_id={cust_id}")
    elif ch == '2':
        screen_id = int(input("Enter Screening ID: "))
        mycursor.execute(f"select * from ticket where screening_id={screen_id}")
    else:
        print("Error: Invalid Input")
        return

    recs = mycursor.fetchall()

    if mycursor.rowcount > 0:
        for i in recs:
            print(i)
    else:
        print("No Ticekts Found")

def cancel_booking():
    id = int(input("Enter Ticket ID To Cancel: "))

    if not check_exists(id, "ticket"):
        print("Ticket ID Not Found")
        return
    
    mycursor.execute(f"select customer_id from ticket where ticket_id={id}")
    cust_id = mycursor.fetchone()[0]

    mycursor.execute(f"delete from ticket where ticket_id={id}")
    connection.commit()

    update_membership(cust_id)

#Customer----------------------------------------------------------------------------------------------------
membership_discounts = {"bronze": 0, "silver": 5, "gold": 10, "platinum": 20}

def add_customer():
    name = input("Enter Customer Name: ")
    phone = input("Enter Phone Number (+971-): ")
    if len(phone) != 9:
        print("Error: Please Enter A Valid Phone Number")
        return
    email = input("Enter Email ID: ")
    

    mycursor.execute("select * from customer")
    mycursor.fetchall()

    if mycursor.rowcount <= 0:
        mycursor.execute(f"insert into customer(customer_id, name, phone_number, email) values(1, '{name}', '+971-{phone}', '{email}')")
        connection.commit()
        return

    mycursor.execute(f"insert into customer(name, phone_number, email) values('{name}', '+971-{phone}', '{email}')")
    connection.commit()

def search_customer():
    menu = "Search by:-\n1. Name\n2. Phone number\nInput: "
    ch = input(menu)

    if ch == '1':
        name = input("Enter Name: ")
        mycursor.execute(f"select * from customer where name like '%{name}%'")
    elif ch == '2':
        phone = input("Enter Phone Number (+971-): ")
        if len(phone) != 9:
            print("Error: Please Enter A Valid Phone Number")
            return
        mycursor.execute(f"select * from customer where phone_number='{phone}'")
    else:
        print("Error: Invalid Input")
        return
    
    recs = mycursor.fetchall()

    if mycursor.rowcount > 0:
        for i in recs:
            print(i)
    else:
        print("No Customer Found")

def update_customer():
    id = int(input("Enter Customer ID To Update: "))
    if not check_exists(id, "customer"):
        print("Customer ID Not Found")
        return
    
    menu = "Update:-\n1. Phone Number\n2. Email\nInput: "
    ch = input(menu)

    if ch == '1':
        phone = input("Enter New Phone Number: ")
        mycursor.execute(f"update customer set phone_number='{phone}' where customer_id={id}")
    elif ch == '2':
        email = input("Enter New Email: ")
        mycursor.execute(f"update customer set email='{email}' where customer_id={id}")
    else:
        print("Error: Invalid Input")
        return

    connection.commit()

def update_membership(id):
    mycursor.execute(f"select * from ticket where customer_id={id}")
    num_bookings = len(mycursor.fetchall())

    new_membership = "bronze"

    if num_bookings >= 10:
        new_membership = "silver"
    if num_bookings >= 50:
        new_membership = "gold"
    if num_bookings >= 100:
        new_membership = "platinum"
    
    mycursor.execute(f"update customer set membership='{new_membership}' where customer_id={id}")
    connection.commit()

def delete_customer():
    id = int(input("Enter Customer ID To Delete: "))

    if not check_exists(id, "customer"):
        print("Customer ID Not Found")
        return
    
    mycursor.execute(f"delete from customer where customer_id={id}")
    connection.commit()

#Screening----------------------------------------------------------------------------------------------
def add_screening():
    movie_id = int(input("Enter Movie ID: "))
    if not check_exists(movie_id, "movie"):
        print("Movie ID Not Found")
        return

    hall_id = int(input("Enter Hall ID: "))
    if not check_exists(hall_id, "theatre_hall"):
        print("Hall ID Not Found")
        return
    
    start_time = input("Enter start time: ")
    date = input("Enter Date Of Screening: ")
    price = int(input("Enter Ticket Price: "))
    
    mycursor.execute("select * from screening")
    mycursor.fetchall()

    if mycursor.rowcount <= 0:
        mycursor.execute(f"insert into screening values(1, {movie_id}, {hall_id}, '{start_time}', '{date}', {price})")
        connection.commit()
        return


    mycursor.execute(f"insert into screening(movie_id, hall_id, start_time, date_screening, ticket_price) values({movie_id}, {hall_id}, '{start_time}', '{date}', {price})")
    connection.commit()

def search_screening():
    menu = "Search By:-\n1. Movie ID\n2. Hall ID\nInput: "
    ch = input(menu)

    if ch == '1':
        movie_id = int(input("Enter Movie ID: "))
        mycursor.execute(f"select * from screening where movie_id={movie_id}")
    elif ch == '2':
        hall_id = int(input("Enter Hall ID: "))
        mycursor.execute(f"select * from screening where hall_id={hall_id}")
    else:
        print("Error: Invalid Input")
        return

    recs = mycursor.fetchall()

    if mycursor.rowcount > 0:
        for i in recs:
            print(i)
    else:
        print("No Screenings Found")

def cancel_screening():
    id = int(input("Enter Screening ID: "))

    if not check_exists(id, "screening"):
        print("Screening Not Found")

    mycursor.execute(f"delete from screening where screening_id={id}")
    connection.commit()

#Movie---------------------------------------------------------------------------------------------------
def add_movie():
    m_name = input("Enter Movie Name: ")
    dur_mins = int(input("Enter Duration Of The Movie: "))
    pg_rating = input("Enter PG-rating (G, PG, PG13, R, NC-17): ")
    rel_date = input("Enter Release Date: ")

    if pg_rating.upper() not in ('G', 'PG', 'PG13', 'R', 'NC-17'):
        print("Error: Incorrect PG Rating")
        return

    mycursor.execute("select * from movie")
    mycursor.fetchall()

    if mycursor.rowcount <= 0:
        mycursor.execute("insert into movie values(1, '{}',{},'{}','{}')".format(m_name,dur_mins,pg_rating,rel_date))
        connection.commit()
        return

    mycursor.execute("insert into movie(name, duration_mins, pg_rating, release_date) values('{}',{},'{}','{}')".format(m_name,dur_mins,pg_rating,rel_date))
    connection.commit()

def search_movie():
    menu = "Search By:-\n1. Name\n2. Release Date\nInput: "
    ch = input(menu)

    if ch == '1':
        name = input("Enter Movie Name: ")
        mycursor.execute(f"select * from movie where name like '%{name}%'")
    elif ch == '2':
        date = input("Enter Release Date: ")
        mycursor.execute(f"select * from movie where release_date='{date}'")
    else:
        print("Error: Invalid Input")
        return
    recs = mycursor.fetchall()

    if mycursor.rowcount > 0:
        for i in recs:
            print(i)
    else:
        print("No Movie Found")

def delete_movie():
    id = int(input("Enter Movie ID To Delete: "))

    if not check_exists(id, "movie"):
        print("Movie Not Found")
        return
    
    mycursor.execute(f"delete from movie where movie_id={id}")
    connection.commit()

#Hall----------------------------------------------------------------------------------------------------
def add_hall():
    type_ = input("Enter Hall Type(2D, 3D, Max, Outdoor): ")
    num_seats = int(input("Enter Number Of Seats: "))

    if type_.lower() not in ("2d", "3d", "max", "outdoor"):
        print("Error: Invalid Hall Type")
        return
    
    mycursor.execute("select * from theatre_hall")
    mycursor.fetchall()

    if mycursor.rowcount <= 0:
        mycursor.execute(f"insert into theatre_hall values(1, '{type_}', {num_seats})")
        connection.commit()
        return

    mycursor.execute(f"insert into theatre_hall(type, num_seats) values('{type_}', {num_seats})")
    connection.commit()

def search_hall():
    type_ = input("Enter Hall Type: ")

    mycursor.execute(f"select * from theatre_hall where type='{type_}'")

    recs = mycursor.fetchall()

    if mycursor.rowcount > 0:
        for i in recs:
            print(i)
    else:
        print("No Halls Found")

def delete_hall():
    id = int(input("Enter Hall ID: "))

    if not check_exists(id, "theatre_hall"):
        print("Hall Not Found")

    mycursor.execute(f"delete from theatre_hall where hall_id={id}")
    connection.commit()

#User----------------------------------------------------------------------------------------------------
def add_user():
    name=input("Enter User Name: ")
    status=input("Enter User Status: ")
    DOJ=input("Enter User DOJ: ")
    username=input("Enter Username: ")
    password=input("Enter Password: ")

    if status not in ("cashier", "manager", "admin"):
        print("Error: Invalid Status")
        return

    mycursor.execute("insert into user(name, status, DOJ, username, password) values('{}','{}','{}','{}','{}')".format(name,status,DOJ,username,password))
    connection.commit()

def search_user():
    menu = "Search By:-\n1. Name\n2. Status\nInput: "
    ch = input(menu)

    if ch == '1':
        name = input("Enter Name: ")
        mycursor.execute(f"select * from user where name like '%{name}%'")
    elif ch == '2':
        status = input("Enter Status: ")
        mycursor.execute(f"select * from user where status='{status}'")
    else:
        print("Error: Invalid Input")
        return

    recs = mycursor.fetchall()

    if mycursor.rowcount > 0:
        for i in recs:
            print(i)
    else:
        print("No Users Found")

def update_user():
    id=int(input("Enter User ID To Update: "))
    
    if not check_exists(id, "user"):
        print("User ID Not Found")
        return
    
    menu = "Update:-\n1. Status\n2. Username\n3. Password\nInput: "
    ch = input(menu)

    if ch == '1':
        status = input("Enter New Status: ")

        if status.lower() not in ("cashier", "manager", "admin"):
            print("Error: Invalid Status")
            return

        mycursor.execute(f"update user set status='{status}' where user_id={id}")
    elif ch == '2':
        username = input("Enter New Username: ")
        mycursor.execute(f"update user set username='{username}' where user_id={id}")
    elif ch == '3':
        password = input("Enter New Password: ")
        mycursor.execute(f"update user set password='{password}' where user_id={id}")
    else:
        print("Error: Invalid Input")
        return

    connection.commit()

def delete_user():
    id = int(input("Enter User ID To Delete: "))

    if not check_exists(id, "user"):
        print("User ID Not Found")
        return
    
    mycursor.execute(f"delete from user where user_id={id}")
    connection.commit()

def login():
    print("*********************** Movie Theatre Management System ***********************")
    print("Test Credentials (Admin): user1, 1234")
    user = input("Username: ")
    pwd = input("Password: ")

    mycursor.execute(f"select status, name, password from user where username='{user}'")

    rec = mycursor.fetchone()

    if rec:
        if pwd == rec[2]:
            print(f"Welcome {rec[1]}")
            return rec[0]
        else:
            print("Error: Wrong Password")
            return 0
    else:
        print("Error: Wrong Username")
        return 0

def admin_menu():
    main_menu = """1. Manage Tickets
2. Manage Customers
3. Manage Screenings
4. Manage Movies
5. Manage Theatre Halls
6. Manage Users
7. Logout
8. Exit
Input: """

    ticket_menu = """1. Book Tickets
2. Search Boookings
3. Cancel Bookings
4. Back
Input: """

    customer_menu = """1. Add Customer
2. Search Customer Details
3. Update Customer Details
4. Delete Customer Records
5. Back
Input: """

    screening_menu = """1. Add Screening
2. Search Screenings
3. Cancel Screening
4. Back
Input: """
    
    movie_menu = """1. Add Movie
2. Search Movies
3. Delete Movie
4. Back
Input: """

    hall_menu = """1. Add Theatre Hall
2. Search Theatre Hall Details
3. Delete Theatre Hall
4. Back
Input: """

    user_menu = """1. Add User
2. Search User Details
3. Update User Details
4. Delete User
5. Back
Input: """

    ch = input(main_menu)

    if ch == '1':
        while True:
            ch = input(ticket_menu)

            if ch == '1':
                book_seats()
            elif ch == '2':
                search_booking()
            elif ch == '3':
                cancel_booking()
            elif ch == '4':
                break
            else:
                print("Error: Invalid Input")
    elif ch == '2':
        while True:
            ch = input(customer_menu)

            if ch == '1':
                add_customer()
            elif ch == '2':
                search_customer()
            elif ch == '3':
                update_customer()
            elif ch == '4':
                delete_customer()
            elif ch == '5':
                break
            else:
                print("Error: Invalid Input")
    elif ch == '3':
        while True:
            ch = input(screening_menu)

            if ch == '1':
                add_screening()
            elif ch == '2':
                search_screening()
            elif ch == '3':
                cancel_screening()
            elif ch == '4':
                break
            else:
                print("Error: Invalid Input")
    elif ch == '4':
        while True:
            ch = input(movie_menu)

            if ch == '1':
                add_movie()
            elif ch == '2':
                search_movie()
            elif ch == '3':
                delete_movie()
            elif ch == '4':
                break
            else:
                print("Error: Invalid Input")
    elif ch == '5':
        while True:
            ch = input(hall_menu)

            if ch == '1':
                add_hall()
            elif ch == '2':
                search_hall()
            elif ch == '3':
                delete_hall()
            elif ch == '4':
                break
            else:
                print("Error: Invalid Input")
    elif ch == '6':
        while True:
            ch = input(user_menu)

            if ch == '1':
                add_user()
            elif ch == '2':
                search_user()
            elif ch == '3':
                update_user()
            elif ch == '4':
                delete_user()
            elif ch == '5':
                break
            else:
                print("Error: Invalid Input")
    elif ch == '7':
        return main()
    elif ch == '8':
        return
    else:
        print("Error: Invalid Input")
    
    return admin_menu()

def manager_menu():
    main_menu = """1. Manage Tickets
2. Manage Customers
3. Manage Screenings
4. Manage Movies
5. Manage Theatre Halls
6. Logout
7. Exit
Input: """

    ticket_menu = """1. Book Tickets
2. Search Boookings
3. Cancel Bookings
4. Back
Input: """

    customer_menu = """1. Add Customer
2. Search Customer Details
3. Update Customer Details
4. Delete Customer Records
5. Back
Input: """

    screening_menu = """1. Add Screening
2. Search Screenings
3. Cancel Screening
4. Back
Input: """
    
    movie_menu = """1. Search Movie
2. Back
Input: """

    hall_menu = """1. Search Theatre Hall Details
2. Back
Input: """

    ch = input(main_menu)

    if ch == '1':
        while True:
            ch = input(ticket_menu)

            if ch == '1':
                book_seats()
            elif ch == '2':
                search_booking()
            elif ch == '3':
                cancel_booking()
            elif ch == '4':
                break
            else:
                print("Error: Invalid Input")
    elif ch == '2':
        while True:
            ch = input(customer_menu)

            if ch == '1':
                add_customer()
            elif ch == '2':
                search_customer()
            elif ch == '3':
                update_customer()
            elif ch == '4':
                delete_customer()
            elif ch == '5':
                break
            else:
                print("Error: Invalid Input")
    elif ch == '3':
        while True:
            ch = input(screening_menu)

            if ch == '1':
                add_screening()
            elif ch == '2':
                search_screening()
            elif ch == '3':
                cancel_screening()
            elif ch == '4':
                break
            else:
                print("Error: Invalid Input")
    elif ch == '4':
        while True:
            ch = input(movie_menu)

            if ch == '1':
                search_movie()
            elif ch == '2':
                break
            else:
                print("Error: Invalid Input")
    elif ch == '5':
        while True:
            ch = input(hall_menu)

            if ch == '1':
                add_hall()
            elif ch == '2':
                break
            else:
                print("Error: Invalid Input")
    elif ch == '6':
        return main()
    elif ch == '7':
        return
    else:
        print("Error: Invalid Input")
    
    return manager_menu()

def cashier_menu():
    main_menu = """1. Manage Tickets
2. Manage Customers
3. Manage Screenings
4. Manage Movies
5. Manage Theatre Halls
6. Logout
7. Exit
Input: """

    ticket_menu = """1. Book Tickets
2. Search Boookings
3. Cancel Bookings
4. Back
Input: """

    customer_menu = """1. Add Customer
2. Search Customer Details
3. Update Customer Details
4. Delete Customer Records
5. Back
Input: """

    screening_menu = """1. Search Screenings
2. Back
Input: """
    
    movie_menu = """1. Search Movie
2. Back
Input: """

    hall_menu = """1. Search Theatre Hall Details
2. Back
Input: """

    ch = input(main_menu)

    if ch == '1':
        while True:
            ch = input(ticket_menu)

            if ch == '1':
                book_seats()
            elif ch == '2':
                search_booking()
            elif ch == '3':
                cancel_booking()
            elif ch == '4':
                break
            else:
                print("Error: Invalid Input")
    elif ch == '2':
        while True:
            ch = input(customer_menu)

            if ch == '1':
                add_customer()
            elif ch == '2':
                search_customer()
            elif ch == '3':
                update_customer()
            elif ch == '4':
                delete_customer()
            elif ch == '5':
                break
            else:
                print("Error: Invalid Input")
    elif ch == '3':
        while True:
            ch = input(screening_menu)

            if ch == '1':
               search_screening()
            elif ch == '2':
                break
            else:
                print("Error: Invalid Input")
    elif ch == '4':
        while True:
            ch = input(movie_menu)

            if ch == '1':
                search_movie()
            elif ch == '2':
                break
            else:
                print("Error: Invalid Input")
    elif ch == '5':
        while True:
            ch = input(hall_menu)

            if ch == '1':
                add_hall()
            elif ch == '2':
                break
            else:
                print("Error: Invalid Input")
    elif ch == '6':
        return main()
    elif ch == '7':
        return
    else:
        print("Error: Invalid Input")
    
    return cashier_menu()

def main():
    while True:
        ch = input("1. Login\n2. Exit\nInput: ")

        if ch == '1':
            status = login()
            while status == 0:
                status = login()

            if status == "admin":
               return admin_menu()
            elif status == "manager":
                return manager_menu()
            else:
                return cashier_menu()
        elif ch == '2':
            return
        else:
            print("Error: Invalid Input")

main()
connection.close()
