def ft_filter(function, iterable):
    """Return an iterator yielding those items of iterable \
for which function(item)
        is true. If function is None, return the items that are true."""
    if function is None:
        return iter([x for x in iterable if x])
    return iter([x for x in iterable if function(x)])
