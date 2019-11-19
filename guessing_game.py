import random


def populate_list(how_many_items, limit):
    lst = []
    for i in range(how_many_items):
        lst.append(random.randint(1, limit))
    return lst


def guess(working_list, limit):
    for i in range(10):
        number_guess = int(input(f"Enter an integer from 1 to {limit}: "))
        while working_list[i] != number_guess:
            if number_guess < working_list[i]:
                print("guess is low")
                number_guess = int(input(f"Enter an integer from 1 to {limit}: "))
            elif number_guess > working_list[i]:
                print("guess is high")
                number_guess = int(input(f"Enter an integer from 1 to {limit}: "))
            else:
                break
        print("you guessed it!")


def main():
    list_a = populate_list(10, 99)
    list_b = populate_list(10, 49)
    guess(list_a, 99)
    guess(list_b, 49)


main()
