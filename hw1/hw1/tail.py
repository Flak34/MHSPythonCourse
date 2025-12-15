import sys
from collections import deque

def tail_stream(stream, n=10):
    buf = deque(maxlen=n)
    for line in stream:
        buf.append(line)
    return buf


def tail_file(path, n=10):
    with open(path, 'r', encoding='utf-8') as f:
        return tail_stream(f, n)


def main():
    files = sys.argv[1:]

    if files:
        multiple = len(files) > 1

        for i, path in enumerate(files):
            try:
                lines = tail_file(path, 10)

                if multiple:
                    print(f"==> {path} <==")

                sys.stdout.writelines(lines)

                if multiple and i < len(files) - 1:
                    print()

            except FileNotFoundError:
                print(f"tail: {path}: No such file or directory", file=sys.stderr)
            except IOError as e:
                print(f"tail: {path}: {e}", file=sys.stderr)
    else:
        sys.stdout.writelines(tail_stream(sys.stdin, 17))


if __name__ == '__main__':
    main()