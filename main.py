import re


def parse_this():
    with open("input.txt", "r") as f, open("new_file.txt", "w") as n:
        for line in f:
            line.strip()
            result = re.sub("[^a-z\s]", "", line, 0, re.IGNORECASE | re.MULTILINE)
            n.write(result)


def add_text():
    with open("new_file1.txt", "r") as file, open("new_file2.txt", "w") as new:
        for line in file:
            new.write(f"<item>{line}<\item>\n")


if __name__ == '__main__':
    parse_this()
    add_text()
