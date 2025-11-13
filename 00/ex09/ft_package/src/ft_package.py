import os


def count_in_list(lst, s):
    """
        Count the number of iteration of a certain value in a list
    """
    return sum(True for s2 in lst if s == s2)


def ft_tqdm(lst):
    """
        Decorate an iterable object, returning an iterator which acts exactly
        like the original iterable, but prints a dynamically updating
        progressbar every time a value is requested.

        Parameters
        ----------
        iterable  : iterable, optional
            Iterable to decorate with a progressbar.
            Leave blank to manually manage the updates.

        Returns
        -------
        out  : decorated iterator.
    """
    cols = os.get_terminal_size().columns
    for x in lst:
        percent = x * 100 / lst.stop
        step = f'{x}/{lst.stop}'
        totalBarLen = cols - 7 - len(step)
        bar = '█' * int(totalBarLen * percent / 100)
        rest = ' ' * int(totalBarLen * (100 - percent) / 100)
        fmt = f'{f"{int(percent)}%":>4s}|{bar}{rest}| {step}'
        print(f'{fmt}{" " * (cols - len(fmt))}', end='\r')
        yield
    percent = 100
    step = f'{lst.stop}/{lst.stop}'
    totalBarLen = cols - 7 - len(step)
    bar = '█' * int(totalBarLen * percent / 100)
    rest = ' ' * int(totalBarLen * (100 - percent) / 100)
    fmt = f'100%|{bar}{rest}| {step}'
    print(f'{fmt}{" " * (cols - len(fmt))}', end='\r')


def makeAssertError(s: str):
    """
        this function write an assertion error befor exiting
        s -- the message for the error
    """
    print(f'AssertionError: {s}')
    exit()
