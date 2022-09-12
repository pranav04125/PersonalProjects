from samples import samples
import random
import time
import threading
import msvcrt

current_sample = random.choice(samples) 
print('\n' + current_sample + "\n")

taking_input = True
user_string = ""

def get_words():
    global user_string
    while taking_input:
        typed_char = msvcrt.getwche()
        user_string += typed_char

def timer(seconds):
    global taking_input
    time.sleep(seconds)
    taking_input = False

input_thread = threading.Thread(target=get_words)
timer_thread = threading.Thread(target=lambda: timer(15))
input_thread.start()
timer_thread.start()

input_thread.join()
timer_thread.join()

user_string = user_string.strip()

num_letters_correct = 0

for i, v in enumerate(user_string):
    if v == current_sample[i]:
        num_letters_correct += 1

print("Speed ")