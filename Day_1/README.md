# Day 1: Report Repair

After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

## Part 1

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

```
1721
979
366
299
675
1456
```

In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?

## Part Two 

The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?

---

## Solution

### Part 1: Two Sums

First step is to read the txt file and put the integers into array form 
```python
with open("input.txt", "r") as f:
    arr = []
    for line in f:
        l = line.strip()
        arr.append(int(l))
```

An inefficient solution to this problem is using i and j loops, this has a time complexity of O(n^2). 

```python
def twoSum(num_arr, pair_sum):
    # search first element
    for i in range(len(num_arr) - 1):
        # search other element
        for j in range(i + 1, len(num_arr)):
            # if i and j sum to pair_sum, multiply pair
            if num_arr[i] + num_arr[j] == pair_sum:
                multiple = num_arr[i] * num_arr[j]
                return multiple
```

A more efficient solution is usign hashtables, where you first find the complements of each number with the target 2020, and stores it in a dictionary. This eliminates the need to loop over all the numbers twice as before.

```python
def twoSumHash(num_arr, pair_sum):
    hashTable = {}

    for i, num in enumerate(arr):
        complement = pair_sum - num
        if complement in hashTable:
            multiple = num * complement
            return multiple

        hashTable[num] = i

# twoSumHash(arr, 2020)
# 806656
```

### Part 2: Three Sums

The solution to the three sums problem require a combination of a hash-based approach and the i, j loops, which means it is O(n^2).  

```python
def threeSum(num_arr, target):

    for i in range(len(num_arr) - 1):
        s = set()
        new_sum = target - num_arr[i]

        for j in range(i + 1, len(num_arr)):
            if (new_sum - num_arr[j]) in s:
                product = num_arr[i] * num_arr[j] * (new_sum - num_arr[j])
                return product

            s.add(num_arr[j])

# print(threeSum(arr, 2020))
# 230608320
```

Run the solution at [repl](https://repl.it/@benthecoder/day1aoc)

## Resources

This problem is the famous two sums problem in coding interviews. Part two takes it up a notch and introduces the three sums problem.

Helpful references for this coding challenge

* [Two Sums](https://www.codementor.io/@info658/classic-python-interview-question-the-two-sum-problem-1aajub9joq)
* [Three Sums](https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/)
