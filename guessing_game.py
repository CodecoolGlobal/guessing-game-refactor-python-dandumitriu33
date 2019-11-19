import random


def populate_list(limit):
    lst = []
    lst.append(random.randint(1, limit))
    lst.append(random.randint(1, limit))
    lst.append(random.randint(1, limit))
    lst.append(random.randint(1, limit))
    lst.append(random.randint(1, limit))
    lst.append(random.randint(1, limit))
    lst.append(random.randint(1, limit))
    lst.append(random.randint(1, limit))
    lst.append(random.randint(1, limit))
    lst.append(random.randint(1, limit))
    return lst


def guess(list_letter, limit):
    for i in range(10):
        g = int(input(f"Enter an integer from 1 to {limit}: "))
        while list_letter[i] != g:
            if g < list_letter[i]:
                print("guess is low")
                g = int(input(f"Enter an integer from 1 to {limit}: "))
            elif g > list_letter[i]:
                print("guess is high")
                g = int(input(f"Enter an integer from 1 to {limit}: "))
            else:
                break
        print("you guessed it!")


def main():
    a = populate_list(99)
    b = populate_list(49)
    guess(a, 99)
    guess(b, 49)


main()
