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
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    valid_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    status_codes = {code: 0 for code in valid_codes}
    total_size = 0
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            try:
                file_size = int(parts[-1])
                total_size += file_size
            except (IndexError, ValueError):
                pass

            try:
                status_code = parts[-2]
                if status_code in status_codes:
                    status_codes[status_code] += 1
            except IndexError:
                pass

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

        print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise
