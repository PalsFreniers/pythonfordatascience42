import sys
import ft_filter as ft


def makeAssertError(s: str):
    """
        this function write an assertion error befor exiting
        s -- the message for the error
    """
    print(f'AssertionError: {s}')
    exit()


def main():
    """
        this is the main function of the program
        this program takes Two arguments: str, int
        it filter the string filtering the word with len
        greater than the interger argument
    """
    if len(sys.argv) != 3:
        makeAssertError('the arguments are bad')
    try:
        lenght = int(sys.argv[2])
        words = sys.argv[1].split(' ')
        print([x for x in ft.ft_filter(lambda w: len(w) > lenght, words)])
    except ValueError:
        makeAssertError('the arguments are bad')


if __name__ == '__main__':
    main()
