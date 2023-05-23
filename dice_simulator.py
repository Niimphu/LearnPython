from random import randint


def generate_numbers(size, count) -> int:
    total = 0
    for i in range(count):
        result = randint(1, size)
        total = total + result
        if not print_sum:
            print(result)
    return total


dice_size = 6
dice_count = 2
print_sum = False

dice_sum = generate_numbers(dice_size, dice_count)
if print_sum:
    print(dice_sum)