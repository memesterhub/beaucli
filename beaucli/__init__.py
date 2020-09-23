# CONSTANTS
FOREGROUND_ATTRS = {
    "reset": u"\u001b[0m",
    "hidden": u"\u001b[8m",
    "red": u"\u001b[31m",
    "yellow": u"\u001b[33m"
}

# FOREGROUND TOOLS

def fore(string, style):
    """
    fore() is a function that styles your text's foreground

    Args:
        string (str): your string
        style (str): the style

    Example:
        input: fore("Hello Shell!", "red")
        output: Hello Shell!
        (NOTE: it will return in the red color as this was the style we provided)
    Returns:
        (str): returns the string you gave styled with the style you gave
    """

    if FOREGROUND_ATTRS.get(style) != None:
        return "%s%s%s" % (FOREGROUND_ATTRS[style], string, FOREGROUND_ATTRS["reset"])
    else:
        return "the style %s doesn't exist please see the docs Coming Soon!" % (style)

if __name__ ==  "__main__":
    i = fore("Hello in red ", "red")
    print(i)
