#!/usr/bin/python3
"""Script that reads stdin line by line and computes log statistics."""
import sys


def print_stats(total_size, status_codes):
    """Print the accumulated file size and status code counts.

    Args:
        total_size (int): the cumulative file size.
        status_codes (dict): mapping of status code to occurrence count.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    valid_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    total_size = 0
    status_codes = {}
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) < 2:
                continue
            status_code = parts[-2]
            file_size = parts[-1]
            try:
                file_size = int(file_size)
            except ValueError:
                continue
            if status_code not in valid_codes:
                continue

            total_size += file_size
            status_codes[status_code] = status_codes.get(status_code, 0) + 1
            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)
    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise
