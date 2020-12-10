## Day 7: Handy Haversacks 
You land at the regional airport in time for your next flight. In fact, it looks like you'll even have time to grab some food: all flights are currently delayed due to *issues in luggage processing*.

Due to recent aviation regulations, many rules (your puzzle input) are being enforced about bags and their contents; bags must be color-coded and must contain specific quantities of other color-coded bags. Apparently, nobody responsible for these regulations considered how long they would take to enforce!

For example, consider the following rules:

```
`light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
`
```

These rules specify the required contents for 9 bag types. In this example, every `faded blue` bag is empty, every `vibrant plum` bag contains 11 bags (5 `faded blue` and 6 `dotted black`), and so on.

You have a `*shiny gold*` bag. If you wanted to carry it in at least one other bag, how many different bag colors would be valid for the outermost bag? (In other words: how many colors can, eventually, contain at least one `shiny gold` bag?)

In the above rules, the following options would be available to you:


 - A `bright white` bag, which can hold your `shiny gold` bag directly.
 - A `muted yellow` bag, which can hold your `shiny gold` bag directly, plus some other bags.
 - A `dark orange` bag, which can hold `bright white` and `muted yellow` bags, either of which could then hold your `shiny gold` bag.
 - A `light red` bag, which can hold `bright white` and `muted yellow` bags, either of which could then hold your `shiny gold` bag.

So, in this example, the number of bag colors that can eventually contain at least one `shiny gold` bag is `*4*`.

*How many bag colors can eventually contain at least one `shiny gold` bag?* (The list of rules is quite long; make sure you get all of it.)


## --- Part Two ---
It's getting pretty expensive to fly these days - not because of ticket prices, but because of the ridiculous number of bags you need to buy!

Consider again your `shiny gold` bag and the rules from the above example:


 - `faded blue` bags contain `0` other bags.
 - `dotted black` bags contain `0` other bags.
 - `vibrant plum` bags contain `11` other bags: 5 `faded blue` bags and 6 `dotted black` bags.
 - `dark olive` bags contain `7` other bags: 3 `faded blue` bags and 4 `dotted black` bags.

So, a single `shiny gold` bag must contain 1 `dark olive` bag (and the 7 bags within it) plus 2 `vibrant plum` bags (and the 11 bags within *each* of those): `1 + 1*7 + 2 + 2*11` = `*32*` bags!

Of course, the actual rules have a small chance of going several levels deeper than this example; be sure to count all of the bags, even if the nesting becomes topologically impractical!

Here's another example:

```
`shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
`
```

In this example, a single `shiny gold` bag must contain `*126*` other bags.

*How many individual bags are required inside your single `shiny gold` bag?*

---

## Solution

``` py
import re
import collections


def read_file(file):
    with open(file) as f:
        file = f.read().splitlines()
    return file


def sol_1(inv_rules, color='shiny gold'):
    queue, reachable = collections.deque([color]), set()

    while queue:
        color = queue.pop()
        for c in inv_rules.get(color, []):
            if c not in reachable:
                reachable.add(c)
                queue.appendleft(c)

    return len(reachable)


def sol_2(rules, color="shiny gold"):
    return sum(number + number * sol_2(rules, c) for c, number in rules[color].items())


def main():
    rules_file = read_file("input.txt")

    rules, inv_rules = {}, {}

    for rule in rules_file:
        color, cl_rule = rule.split(' bags contain ')
        rules[color] = {color: int(number) for number, color in re.findall(
            '(\d+) (\w+ \w+)', cl_rule)}
        for c in rules[color]:
            inv_rules[c] = inv_rules.get(c, []) + [color]

    print(f'Part 1: {sol_1(inv_rules)}\nPart 2: {sol_2(rules)}')
```

### Explanation
#### main() 
* First of all, to make the code for solution 1 and 2 shorter, we first deal with the input by creating two dictionaries (rules and inv_rules), which is used to store information we need later on. 
* For rules dict: Color, and the color rules are split into two based on the string "bags contain", which then allows us to add the main color, and the color rules and it's given amount. Rules dict then becomes a dict like this -> `{'shiny gold': {'pale aqua': 1, 'dark cyan': 3, 'vibrant purple': 5, 'drab blue': 2}, ...}` (the form of {main color: {color rules:int, }})
* As for the inv rules dict, we take each color in the nest dicts (color rules) and turn them into the keys instead. This takes the form of -> `{'shiny gold': ['plaid gold', 'bright violet', 'clear brown', 'clear blue', 'faded gold', 'drab purple'], ...}`. 

#### sol_1()
* we use deque here because we're able to append to the left of a list, which is useful if you want to iterate over all possible values by popping and appending (to the left). 
* the main idea of this function is we go through the dictionary in inv_rules, when we find shiny gold, we take it's parent, and add it into a set called queue. By appending and popping, we go through each possible parent for "shiny gold", and we get the total number of parents (colors) using the len function on our set 

#### sol_2()
* sol_2 gets a bit complicated, but all it's doing is we take the rules dictionary, which contains {color : {color rule : int}} and get the color and number. Now we're trying to find the total amount of bags in a 'shiny bag', so all we have to do is take the parent color 'shiny gold', we iterate over all the color rules, and in each of those color rules, get their color rules, and so on. 
* To achieve something like this, the concept of recursion is incredibly useful, although the time complexity is not efficient, it does the job.z

## References / Resources
* [Python get method](https://www.programiz.com/python-programming/methods/dictionary/get)
* [Python Recursion](https://www.programiz.com/python-programming/recursion)
* [re.search vs re.findall](https://www.geeksforgeeks.org/python-regex-re-search-vs-re-findall/)
* [collections.deque()](https://www.educative.io/edpresso/how-to-use-a-deque-in-python)

