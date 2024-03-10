import sys


class WC:
    def __init__(self, filename):
        self.filename = filename

    def count(self, print_lines=False, print_words=False, print_bytes=False, print_chars=False):
        line_count = 0
        word_count = 0
        char_count = 0

        with open(self.filename, 'r') as file:
            for line in file:
                line_count += 1
                word_count += len(line.split())
                char_count += len(line)

        if print_lines and print_words and print_bytes and print_chars:
            print(line_count, word_count, char_count, self.filename)
        else:
            if print_lines:
                print(line_count, self.filename)
            if print_words:
                print(word_count, self.filename)
            if print_bytes or print_chars:
                print(char_count, self.filename)


def main():
    filename = input("Enter filename: ")
    wc = WC(filename)

    print_lines = "-l" in sys.argv or len(sys.argv) == 1
    print_words = "-w" in sys.argv or len(sys.argv) == 1
    print_bytes = "-m" in sys.argv or "-c" in sys.argv or len(sys.argv) == 1
    print_chars = "-c" in sys.argv or len(sys.argv) == 1

    wc.count(print_lines=print_lines, print_words=print_words,
             print_bytes=print_bytes, print_chars=print_chars)


if __name__ == "__main__":
    main()
