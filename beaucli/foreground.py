def printfgc(args, color):
    print(f"{color()}{args}{reset()}")

def reset():
    """returns reseted shell ANSI value"""
    return u"\u001b[0m"

def default():
    """returns default shell ANSI value"""
    return u"\u001b[39m"

def red():
    """returns magenta shell ANSI value"""
    return u"\u001b[31m"

def yellow():
    """returns magenta shell ANSI value"""
    return u"\u001b[33m"

def green():
    """returns magenta shell ANSI value"""
    return u"\u001b[32m"

def blue():
    """returns magenta shell ANSI value"""
    return u"\u001b[34m"

def magenta():
    """returns magenta shell ANSI value"""
    return u"\u001b[35m"

def cyan():
    """returns cyan shell ANSI value"""
    return u"\u001b[36m"
