import re
import regex


numbers = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
pattern = fr"({'|'.join(numbers)}|\d)"


def main():
    re_pattern = re.compile(pattern)
    regex_pattern = regex.compile(pattern, regex.REVERSE)

    sum_of_numbers = 0
    with open("input.txt") as file:
        for line in map(str.rstrip, file):
            first_num = re.search(re_pattern, line)
            last_num = regex.search(regex_pattern, line)
            sum_of_numbers += get_number_from_match(first_num) * 10 + get_number_from_match(last_num)

    print(f"result: {sum_of_numbers}")


def get_number_from_match(match: re.Match) -> int:
    textual_repr = match[0]
    if textual_repr.isdigit():
        return int(textual_repr)
    return numbers.index(textual_repr) + 1


if __name__ == "__main__":
    main()
