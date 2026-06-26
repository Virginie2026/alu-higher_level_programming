#!/usr/bin/python3
print("".join("{:c}".format(i).lower() if (122 - i) % 2 == 0 else "{:c}".format(i).upper() for i in range(122, 96, -1)), end="")
