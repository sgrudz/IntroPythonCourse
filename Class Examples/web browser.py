# We want to launch a random fun website

import random
import webbrowser

def launch_website(random_number):
    if random_number == 1:
        webbrowser.open("https://www.facebook.com/")
    if random_number == 2:
        webbrowser.open("http://www.tinybuddhayoga.com/")
    if random_number == 3:
        webbrowser.open("https://www.aloyoga.com/")

random_num = random.randint(1, 3)
print(random_num)
launch_website(random_num)
