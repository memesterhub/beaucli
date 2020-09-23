# CONSTANTS
FOREGROUND_ATTRS = {
    "reset": u"\u001b[0m",
    "hidden": u"\u001b[8m",
    "default": u"\u001b[39m",
    "black": u"\u001b[30m",
    "red": u"\u001b[31m",
    "green": u"\u001b[32m",
    "yellow": u"\u001b[33m",
    "blue": u"\u001b[34m",
    "magenta": u"\u001b[35m",
    "cyan": u"\u001b[36m",
    "light_gray": u"\u001b[37m",
    "dark_gray": u"\u001b[90m",
    "light_red": u"\u001b[91m",
    "light_green": u"\u001b[92m",
    "light_yellow": u"\u001b[93m",
    "light_blue": u"\u001b[94m",
    "light_magenta": u"\u001b[95m",
    "light_cyan": u"\u001b[96m",
    "white": u"\u001b[97m"
}

BACKGROUND_ATTRS = {
    "reset": u"\u001b[0m",
    "hidden": u"\u001b[8m",
    "red": u"\u001b[41m",
    "yellow": u"\u001b[43m"
}

# FOREGROUND TOOLS

def fore(string="", style="default", colorType="normal"):
    """
    fore() is a function that styles your text's foreground

    Args:
        string (str): your string
        style (str): the style
        colorType (str): the color selecting type (NOTE: the default and only until now is "normal")

    Example:
        input: fore("Hello Shell!", "red")
        output: Hello Shell!
        (NOTE: it will return in the red color as this was the style we provided)
    Returns:
        (str): returns the string you gave styled with the style you gave
    """
    if colorType == "normal":
        if FOREGROUND_ATTRS.get(style) != None:
            return "%s%s%s" % (FOREGROUND_ATTRS[style], string, FOREGROUND_ATTRS["reset"])
        else:
            return "the style %s doesn't exist please see the docs Coming Soon!" % (style)

def back(string="", style="default", colorType="normal"):
    """
    back() is a function that styles your text's background

    Args:
        string (str): your string
        style (str): the style
        colorType (str): the color selecting type (NOTE: the default and only until now is "normal")

    Example:
        input: fore("Hello Shell!", "red")
        output: Hello Shell!
        (NOTE: it will return in the red color as this was the style we provided)
    Returns:
        (str): returns the string you gave styled with the style you gave
    """
    if colorType == "normal":
        if BACKGROUND_ATTRS.get(style) != None:
            return "%s%s%s" % (BACKGROUND_ATTRS[style], string, BACKGROUND_ATTRS["reset"])
        else:
            return "the style %s doesn't exist please see the docs Coming Soon!" % (style)
