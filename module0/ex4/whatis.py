import sys


def safe_int(s, error_value=None):
    try:
        return int(s)
    except ValueError:
        return error_value


def main():
    if len(sys.argv) == 1:
        return
    assert len(sys.argv) <= 2, "more than one argument is provided"

    try:
        nbr = int(sys.argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer")
    if nbr % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


try:
    main()
except AssertionError as e:
    print("AssertionError:", e)
