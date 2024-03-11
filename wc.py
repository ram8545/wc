import sys


class WC:
    def __init__(self, filename):
        self.filename = filename

    def count(self, print_lines=False, print_words=False, print_bytes=False, print_chars=False):
        try:
            line_count = 0
            word_count = 0
            char_count = 0

            if self.filename == '-':
                return ("No such file or directory")
            else:
                file = open(self.filename, 'r')

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
            return line_count, word_count, char_count
        except:
            pass

def Convert(string):
    li = list(string.split(" "))
    return li


def wc_main(file_lists):
    try:
        file_list = Convert(file_lists)
        total_line_count = 0
        total_word_count = 0
        total_char_count = 0
        total_filename = 'total'
        for filename in file_list:
            wc = WC(filename)

            print_lines = "-l" in sys.argv or len(sys.argv) == 1
            print_words = "-w" in sys.argv or len(sys.argv) == 1
            print_bytes = "-m" in sys.argv or "-c" in sys.argv or len(sys.argv) == 1
            print_chars = "-c" in sys.argv or len(sys.argv) == 1

            line_count, word_count, char_count = wc.count(print_lines=print_lines, print_words=print_words,
                    print_bytes=print_bytes, print_chars=print_chars)
            total_line_count += line_count
            total_word_count += word_count
            total_char_count += char_count
        if len(file_list) > 1:
            if print_lines and print_words and print_bytes and print_chars:
                print(total_line_count, total_word_count, total_char_count, total_filename)
            else:
                if print_lines:
                    print(total_line_count, total_filename)
                if print_words:
                    print(total_word_count, total_filename)
                if print_bytes or print_chars:
                    print(total_char_count, total_filename)
            return total_line_count, total_word_count, total_char_count
        else:
            return line_count, word_count, char_count
    except:
            return ("No such file or directory")


if __name__ == "__main__":
    wc_main('example.txt example2.txt')
