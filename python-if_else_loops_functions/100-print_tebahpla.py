#!/usr/bin/python3
print("".join(chr(i).lower() if (122 - i) % 2 == 0 else chr(i).upper() for i in range(122, 96, -1)), end="")
