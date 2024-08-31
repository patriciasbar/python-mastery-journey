def do_stuff(num):
    try:
        if num != None:
            return int(num + 5)
        else:
            raise TypeError
    except TypeError as e:
        return e

