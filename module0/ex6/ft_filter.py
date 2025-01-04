def ft_filter(function, iterable):
    if function is None:
        return [item for item in iterable if item]
    else:
        return [item for item in iterable if function(item)]


ft_filter.__doc__ = filter.__doc__
