#!/usr/bin/python3

import sys

def get_hex_list(filename: str) -> list:
    try:
        with open(filename, "rb") as f:
            hex_str: str = f.read().hex()
        hex_bytes = [(hex_str[index] + hex_str[index + 1]) for index in range(len(hex_str)) if index%2 == 0]
        return hex_bytes
    except FileNotFoundError:
        raise FileNotFoundError

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Provide two files")
    else:
        f1: str = sys.argv[1]
        f2: str = sys.argv[2]
        try:
            f1_hex_bytes: list = get_hex_list(f1)
            f2_hex_bytes: list = get_hex_list(f2)
            len_f1: int = len(f1_hex_bytes)
            len_f2: int = len(f2_hex_bytes)
            if len_f1 != len_f2:
                print(f1 + str(" is ") + str(len_f1) + " bytes")
                print(f2 + str(" is ") + str(len_f2) + " bytes")
                print("They cannot be the same")
            else:
                diff_bytes: int = 0
                for i in range(len_f1):
                    if f1_hex_bytes[i] != f2_hex_bytes[i]:
                        diff_bytes += 1
                if diff_bytes == 0:
                    print("They are the same")
                else:
                    print("They are not the same: " + str(diff_bytes) + " different byte" + ("s" if diff_bytes > 1 else ""))
        except FileNotFoundError:
            print("Unable to locate one or both files")
