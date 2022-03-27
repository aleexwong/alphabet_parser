import re


def parse_this():
    """
    removes all chars except a-z!
    :return: text file.
    """
    with open("input.txt", "r") as file, open("new_file.txt", "w") as new:
        for line in file:
            line.strip()
            result = re.sub("[^a-z\s]", "", line, 0, re.IGNORECASE | re.MULTILINE)
            new.write(result)


def add_text():
    """
    add additional text needed.
    :return: text file.
    """
    with open("new_file1.txt", "r") as file, open("new_file2.txt", "w") as new:
        for line in file:
            if line.strip() != '':
                new.write(f"<item>{line}</item>""\n")


if __name__ == '__main__':
    parse_this()
    # manual data fixing required? pycharm uses TAB + SHIFT to undent and TAB to indent
    add_text()
