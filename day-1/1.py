sum_of_numbers = 0

with open("input.txt") as file:
    for line in map(str.rstrip, file):
        for char in line:
            if char.isdigit():
                first_digit = char
                break
        for char in reversed(line):
            if char.isdigit():
                last_digit = char
                break

        sum_of_numbers += int(first_digit + last_digit)

print(sum_of_numbers)
