# generator written for generating log/manual testing purposes. does not affect actual code/testing logic

import random
import string
import sys


log_filename = "machine.i.log"
pat = "himynameisangel"

def generate_pattern(limit, percent):
    curr = ""
    target = limit * percent
    not_pattern_count = 0
    pattern_count = 0

    while (pattern_count < target and not_pattern_count < limit - target):
        random_number = random.randint(0, 1)
        if (random_number == 0): #lines without given pattern
            not_pattern_count += 1
            for _ in range(limit):
                curr += random.choice(string.ascii_lowercase)
            curr += "\n"
        else: #lines with given pattern
            pattern_count += 1
            pos = random.randint(0, limit - len(pat))
            for i in range(limit):
                if i == pos:
                    curr += pat
                else:
                    curr += random.choice(string.ascii_lowercase)

            curr += "\n"
        
    while (pattern_count < target):
        pattern_count += 1
        pos = random.randint(0, limit - len(pat))
        for i in range(limit):
            if i == pos:
                curr += pat
            else:
                curr += random.choice(string.ascii_lowercase)
        curr += "\n"

    while (not_pattern_count < limit - target):
        not_pattern_count += 1
        for _ in range(limit):
            curr += random.choice(string.ascii_lowercase)
        curr += "\n"
    
    return curr

def write_log(input):
    with open(log_filename, "a") as log_file:
        log_file.write(input)

if __name__ == '__main__':
    with open(log_filename, "w") as log_file:
        pattern = generate_pattern(int(sys.argv[1]), float(sys.argv[2]))
        write_log(pattern)
