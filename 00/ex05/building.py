import sys


def main():
    """
        This is the main Function of the program
        this program counts the number of characters (case, dpace, digit, ...)
        and prints everything to the terminal
    """
    text = ''
    if len(sys.argv) == 1:
        text = input('What is the text to count?\n') + '\n'
    else:
        text = sys.argv[1]
    upper = sum(c.isupper() for c in text)
    lower = sum(c.islower() for c in text)
    space = sum(c.isspace() for c in text)
    digit = sum(c.isdigit() for c in text)
    punct = len(text) - upper - lower - space - digit
    print(f'The text contains {len(text)} characters:')
    print(f'{upper} upper letters')
    print(f'{lower} lower letters')
    print(f'{punct} ponctuation marks')
    print(f'{space} spaces')
    print(f'{digit} digits')
    pass


if __name__ == '__main__':
    main()
