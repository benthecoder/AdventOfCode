import re


def read_file(file):
    with open(file, 'r') as f:
        file = f.read().split('\n\n')
    return file


def sol_1(passports):
    info = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    count = 0
    for passport in passports:
        keys = set(map(lambda x: x.split(':')[0], passport.split()))

        if keys.issuperset(info):
            count += 1

    return count


def filter_key(passports):
    info = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid = []
    for passport in passports:
        pass_dict = {k_v.split(':')[0]: k_v.split(':')[1]
                     for k_v in passport.split()}

        if set(pass_dict.keys()).issuperset(info):
            valid.append(pass_dict)

    return valid


def sol_2(passports):
    count = 0

    for pass_dict in filter_key(passports):

        try:
            byr_n = int(pass_dict['byr'])
            iyr_n = int(pass_dict['iyr'])
            eyr_n = int(pass_dict['eyr'])
            hgt = pass_dict['hgt']
            hgt_n = int(pass_dict['hgt'][:-2])
            hcl = pass_dict['hcl']
            ecl = pass_dict['ecl']
            pid = pass_dict['pid']

            if (1920 <= byr_n <= 2002) \
                    and (2010 <= iyr_n <= 2020) \
                    and (2020 <= eyr_n <= 2030) \
                    and ((hgt.endswith('cm') and (150 <= hgt_n <= 193))
                         or (hgt.endswith('in') and (59 <= hgt_n <= 76))) \
                    and re.fullmatch("#([0-9]|[a-f]){6}", hcl) \
                    and re.fullmatch("amb|blu|brn|gry|grn|hzl|oth", ecl) \
                    and re.fullmatch("[0-9]{9}", pid):

                count += 1
        except:
            continue

    return count


def main():
    passports = read_file("passport.txt")
    print(f"Part 1: {sol_1(passports)} \nPart 2: {sol_2(passports)}")


if __name__ == "__main__":
    main()
