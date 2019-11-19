import random


def populate_list(how_many_items, limit):
    '''
    Populates the given list with random numbers up to the limit,
    the given number of times.
    '''
    lst = []
    for i in range(how_many_items):
        lst.append(random.randint(1, limit))
    return lst


def guess(working_list, limit):
    '''
    Guessing function, waits for user input, evaluates the guess
    and prints clues or the successful guess message.
    '''
    for i in range(10):
        input_message = f"Enter an integer from 1 to {limit}: "
        number_guess = int(input(input_message))
        while working_list[i] != number_guess:
            if number_guess < working_list[i]:
                print("The guess is low.")
                number_guess = int(input(input_message))
            elif number_guess > working_list[i]:
                print("The guess is high.")
                number_guess = int(input(input_message))
            else:
                break
        print("You guessed it! \nNew round.")


def main():
    '''
    Main function that establishes the program flow.
    First populates lists and then runs the guessing section for each.
    '''
    list_a = populate_list(10, 99)
    list_b = populate_list(10, 49)
    guess(list_a, 99)
    guess(list_b, 49)


main()
