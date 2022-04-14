import random
def generate_lotto_number():
    numbers=[0,0,0,0,0,0,0]
    for i in range(len(numbers)):
        numbers[i]=random.randint(0,9)
    return numbers
def display_lotto_number(list):
    for i in range (len(list)-1):
        print(list[i],end=", ")
    print(list[len(list)-1])
for i in range(20):
    display_lotto_number(generate_lotto_number())