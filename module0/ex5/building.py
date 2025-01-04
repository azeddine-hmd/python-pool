import sys


def parse_text() -> str:
    """get text from commandline argument or standard input"""
    if len(sys.argv) == 1:
        try:
            text = input("what is the text to count?\n")
            text += " "
        except EOFError:
            pass
        except Exception:
            raise AssertionError("something bad happen")
    else:
        text = sys.argv[1]
    return text


class CharCount:
    upper: int = 0
    lower: int = 0
    digit: int = 0
    space: int = 0
    punct: int = 0

    def __str__(self):
        return (
            f"CharCount("
            f"upper={self.upper}, "
            f"lower={self.lower}, "
            f"digit={self.digit}, "
            f"space={self.space}, "
            f"punct={self.punct}"
            f")"
        )

    def total(self):
        return self.upper + self.lower + self.digit + self.space + self.punct


def count_text(text: str) -> CharCount:
    """count the different types of characters

    count these type of characters:
    upper case, lower case, digit, space and punctuation marks
    """
    char_count = CharCount()
    for char in text:
        if char.isupper():
            char_count.upper += 1
        elif char.islower():
            char_count.lower += 1
        elif char.isdigit():
            char_count.digit += 1
        elif char.isspace():
            char_count.space += 1
        elif char.isprintable():
            char_count.punct += 1
    return char_count


def main():
    assert len(sys.argv) <= 2, "more than one argument is provided"
    text = parse_text()
    char_count = count_text(text)
    print(f"The text contains {char_count.total()} characters:")
    print(f"{char_count.upper} upper letters")
    print(f"{char_count.lower} lower letters")
    print(f"{char_count.punct} punctuation marks")
    print(f"{char_count.space} spaces")
    print(f"{char_count.digit} digits")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print("AssertionError:", e)
