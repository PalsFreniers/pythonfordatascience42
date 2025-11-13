import sys


def makeAssertError(s: str):
    """
        this function write an assertion error befor exiting
        s -- the message for the error
    """
    print(f'AssertionError: {s}')
    exit()


def main():
    """
        This is the main function of the program
        this program take a string and print a morse version
    """
    NESTED_MORSE = {
            ' ': '/',
            'A': '.-',
            'B': '-...',
            'C': '-.-.',
            'D': '-..',
            'E': '.',
            'F': '..-.',
            'G': '--.',
            'H': '....',
            'I': '..',
            'J': '.---',
            'K': '-.-',
            'L': '.-..',
            'M': '--',
            'N': '-.',
            'O': '---',
            'P': '.--.',
            'Q': '--.-',
            'R': '.-.',
            'S': '...',
            'T': '-',
            'U': '..-',
            'V': '...-',
            'W': '.--',
            'X': '-..-',
            'Y': '-.--',
            'Z': '--..',
            '1': '.----',
            '2': '..---',
            '3': '...--',
            '4': '....-',
            '5': '.....',
            '6': '-....',
            '7': '--...',
            '8': '---..',
            '9': '----.',
            '0': '-----'
    }
    if len(sys.argv) != 2:
        makeAssertError('the arguments are bad')
    try:
        morse = ' '.join([NESTED_MORSE[x] for x in sys.argv[1].upper()])
        print(morse)
    except KeyError:
        makeAssertError('the arguments are bad')


if __name__ == '__main__':
    main()
