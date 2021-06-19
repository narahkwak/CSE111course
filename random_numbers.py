import random

def append_random_numbers(numbers_list, quantity):
    for i in range(0,quantity):
        numbers_list.append(round(random.uniform(0,1000), 1))
        return numbers_list

def main():
    randnums = [16.2, 75.1, 52.3]
    randnums.append(append_random_numbers(randnums, 1 ))
    print(randnums)

main()