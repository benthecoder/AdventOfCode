## Day 2: Password Philosophy

## Part 1
Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

```
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
```

Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?

## Part 2

While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

- 1-3 a: abcde is valid: position 1 contains a and position 3 does not.
- 1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
- 2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

How many passwords are valid according to the new interpretation of the policies?

---

## Solution

### Part 1

```python
def read(line):
    string = line.rstrip().replace(':', '').split(' ')
    num_1, num_2 = map(int, string[0].split('-'))
    letter = string[1]
    pw = string[2]
    return num_1, num_2, letter, pw

def sol_1(line):
    min, max, letter, pw = read(line)
    if min <= pw.count(letter) <= max:
        return 1
    return 0

def sol_2(line):
    pos_1, pos_2, letter, pw = read(line)
    if (pw[pos_1 - 1] == letter) != (pw[pos_2 - 1] == letter):
        return 1
    return 0

def counts():
    count_1, count_2 = 0, 0
    with open("input.txt", "r") as f:
        for line in f:
            count_1 += sol_1(line)
            count_2 += sol_2(line)
    return f"Part 1: {count_1} \nPart 2: {count_2}"

if __name__ == "__main__":
    print(counts())

# Output
# Part 1: 622
# Part 2: 263
```

Run the solution in [repl](https://repl.it/@benthecoder/day2aoc)

## Resources

This problem was mostly about regex, and I used there references to complete the problem.

* [regex cheatsheet](https://www.debuggex.com/cheatsheet/regex/python)
* [learnbyexample regex](https://learnbyexample.github.io/python-regex-cheatsheet/) - using re module