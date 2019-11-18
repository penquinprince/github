def foo():
    "Have this method return true"
    return True


def concatenadd(a, b):
    """Change the following line such that this function
    returns the concatenation of a and b if they contain strings, and the sum
    if they contains ints or floats
    """
    c = a + b
    return c


def cf_color(frogs, clutch):
    cfc = "white"
    if 0 <= frogs <= 2:
        cfc = "blue"
        if clutch >= 0:
            cfc = "green"
        if clutch >= frogs:
            cfc = "yellow"
    elif 0 >= frogs >= -2:
        cfc = "black"
        if clutch >= 0:
            cfc = "orange"
        if frogs + clutch >= -2:
            cfc = "red"
    return cfc


def collatz(n):
    """
    Indent this code correctly
    such that it computes the number of steps needed
    to reach 1 (https://oeis.org/A006577)
    """
    counter = 0
    if not isinstance(n, int):
        if isinstance(n, float):
            n = int(n)
        else:
            print("Input is not a number")
            return None
    if n >= 1:
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            counter += 1
        return counter
    else:
        print("Value input too low")
        return None


def even_steven(word):
    """This function returns a string with every second letter of
    the word, starting at the second letter."""
    new_word = ""
    for i in range(0, len(word)):
        new_word.append(word[i+1])
        i += 2
    return new_word


def extend_e(word):
    """This function inserts the letter 'e' after each vowel in word."""
    vowels = "aeiouyAEIOUY"
    new_word = ""
    for i in range(0, len(word)):
        if word[i] in vowels:
            new_word = new_word + word[i]
            new_word = new_word + "e"
        else:
            new_word = new_word + word[i]

    return new_word


def reply2argument(argument):
    """Given an input string it will return an argument."""
    words = argument.split()
    reply = ""
    if words[0] == 'Yes,':
        reply = 'No! '
    if words[0] == 'No':
        reply = 'Yes! '

    if argument[-1:] == '?':
        reply += 'None of your business. '
    elif 'I' in words:
        reply += "No, you aren't."
    elif 'you' in words or 'You' in words:
        reply += "No, I'm not. "
    elif 'It' in words or 'it' in words:
        reply += "No, it isn't."
    elif "this" in words or "This" in words:
        reply += "No, not true. "
    else:
        reply += "Ooooh! "
        reply += extend_e(argument)

    return reply


def argument_clinic():
    """This function will repeatedly ask for input, and try to
    be argumentative about it. It stops if the user types 42."""
    pass
    print("---> You're welcome.")
    return None






