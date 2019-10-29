"""
Merge two dicts into one.
Print an alphabet table {char: ascii} in this routine.
"""


def main():
    alphabet = {}
    upper_cases = {chr(c): c for c in range(ord('A'), ord('Z') + 1)}
    lower_cases = {chr(c): c for c in range(ord('a'), ord('z') + 1)}
    alphabet.update(upper_cases)
    alphabet.update(lower_cases)
    for c, a in upper_cases.items():
        print(c, a)


if __name__ == '__main__':
    main()
