# convert txt file integers into number arrays
with open("input.txt", "r") as f:
    arr = []
    for line in f:
        l = line.strip()
        arr.append(int(l))

# Part 1 

# Using hash tables
def twoSumHash(num_arr, pair_sum):
    hashTable = {}

    for i, num in enumerate(arr):
        complement = pair_sum - num
        if complement in hashTable:
            multiple = num * complement
            print(f"The product of {num} and {complement}: {multiple}")
        hashTable[num] = i

# Part 2

# combination of hash and i,j loops (alternative is two pointers)
def threeSum(num_arr, target):
    for i in range(len(num_arr) - 1):
        s = set()
        new_sum = target - num_arr[i]

        for j in range(i + 1, len(num_arr)):
            if (new_sum - num_arr[j]) in s:
                product = num_arr[i] * num_arr[j] * (new_sum - num_arr[j])
                print(f"The product of {num_arr[i]}, {num_arr[j]} and {new_sum - num_arr[j]}: {product}")

            s.add(num_arr[j])


if __name__ == "__main__":
    twoSumHash(arr, 2020)
    # The product of 548 and 1472 = 806656
    threeSum(arr, 2020)
    # The product of 807, 893 and 320 = 230608320
