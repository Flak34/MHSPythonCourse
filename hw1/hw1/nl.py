import sys

def number_lines(input_file):
    line_number = 1
    for line in input_file:
        print(f"{line_number:6}\t{line}", end="", file=sys.stdout)
        line_number += 1

def main():
    if len(sys.argv) > 1:
        try:
            with open(sys.argv[1], 'r', encoding='utf-8') as f:
                number_lines(f)
        except FileNotFoundError:
            print(f"nl: {sys.argv[1]}: No such file or directory", file=sys.stderr)
            sys.exit(1)
        except IOError as e:
            print(f"nl: {sys.argv[1]}: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        number_lines(sys.stdin)


if __name__ == '__main__':
    main()