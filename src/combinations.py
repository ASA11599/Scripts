#!usr/bin/python3

import sys

class Char_digit:

    alphabet: list = []

    def __init__(self, left):
        self.value: int = 0
        self.times_counted = 0
        self.left = left

    def count_up(self):
        self.value += 1
        if self.value == len(Char_digit.alphabet):
            self.value = 0
            self.times_counted += 1
            if self.left != None:
                self.left.count_up()

    def get_char(self):
        return Char_digit.alphabet[self.value]

def get_args(arg_list: list) -> dict:
    # First element is this file's name
    arg_list.pop(0)
    key_indices: list = []
    for index in range(len(arg_list)):
        if arg_list[index][0] == '-':
            key_indices.append(index)
    return { arg_list[key_indices[ki_i]][1:] : (arg_list[(key_indices[ki_i] + 1):key_indices[ki_i + 1]] if ki_i < (len(key_indices) - 1) else arg_list[(key_indices[ki_i] + 1):]) for ki_i in range(len(key_indices)) }

def on_invalid_input():
    print("Please provide arguments as such: -a [available letters] -n [word length]")
    print("Example: -a xyz -n 2")
    print(">> xy")
    print(">> xz")
    print(">> yx")
    print(">> xy")
    print(">> yz")
    print(">> zx")
    print(">> zy")

def valid_combination(combination: str, alphabet: list) -> bool:
    # This function can be used to filter combinations
    return True

def get_combination(a: str, n: int) -> list:
    result: list = []
    char_digit_list: list = [Char_digit(None) for _ in range(n)]
    for i in range(n):
        char_digit_list[n - 1 - i].left = char_digit_list[n - 1 - i - 1] if (i <= (n - 1)) else None
    while char_digit_list[0].times_counted == 0:
        combination: str = ''
        ls_char_digit: Char_digit = char_digit_list[n - 1]
        for cd in char_digit_list:
            combination += cd.get_char()
        if valid_combination(combination, Char_digit.alphabet):
            result.append(combination)
            print("Found: " + combination)
        ls_char_digit.count_up()
    return result

if __name__ == "__main__":

    args: dict = get_args(sys.argv)

    if ('a' in args.keys()) and ('n' in args.keys()):
        if (len(args['a']) == 1) and (len(args['n']) == 1):
            Char_digit.alphabet = [char for char in args['a'][0]]
            res: list = get_combination(args['a'][0], int(args['n'][0]))
            '''
            for c in res:
                print(c)
            '''
        else:
            on_invalid_input()
    else:
        on_invalid_input()
