import sys

def count_file_stats(stream):
    chunk_size = 65536
    line_count, word_count, byte_count = 0, 0, 0
            
    while True:
        chunk = stream.read(chunk_size)
        if not chunk:
            break

        byte_count += len(chunk)
        line_count += chunk.count(b'\n')
        word_count += len(chunk.split())
                    
    return (line_count, word_count, byte_count)


def format_output(lines, words, bytes_count, filename=None):
    output = f"{lines:8}{words:8}{bytes_count:8}"
    if filename:
        output += f" {filename}"
    return output


def main():
    if len(sys.argv) > 1:
        files = sys.argv[1:]
        total_lines = 0
        total_words = 0
        total_bytes = 0
        
        for file_path in files:
            try:
                with open(file_path, "rb") as file:
                    stats = count_file_stats(file)
                    if stats is not None:
                        lines, words, bytes_count = stats
                        total_lines += lines
                        total_words += words
                        total_bytes += bytes_count
                        print(format_output(lines, words, bytes_count, file_path))
            except FileNotFoundError:
                print(f"wc: {file_path}: No such file or directory", file=sys.stderr)
            except IOError as e: 
                print(f"wc: {file_path}: {e}", file=sys.stderr)
        
        if len(files) > 1:
            print(format_output(total_lines, total_words, total_bytes, "total"))
    else:
        stats = count_file_stats(sys.stdin.buffer)
        lines, words, bytes_count = stats
        print(format_output(lines, words, bytes_count))


if __name__ == '__main__':
    main()