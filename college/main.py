def split_string(st, param):
	tokens = st.split(param)
	
	for token in tokens:
		print(token)

	print("first token")
	print(tokens[0])

def main():
	st = input("Enter string: ")
	param = input("Enter delimiter: ")

	split_string(st, param)

main()