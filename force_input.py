# write a function that forces the user to enter a multiple of 6 number
# use try, except to catch valid inputs
def multiple_of_6():
    """
    Returns a multiple of 6, keeps asking otherwise.
    :return: int
    """
    while True:
        try:
            n = input('Please give me a multiple of 6: ')
            n = int(n)

            if n % 6 == 0:
                return n
            else:
                print("That is not a multiple of 6.")
        except ValueError:
            print("That is not a valid number. Please enter an integer.")

multiple_of_6()
