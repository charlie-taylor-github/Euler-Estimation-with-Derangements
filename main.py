import itertools
import math
import os

n = 9

os.system('cls' if os.name == 'nt' else 'clear')
print(f"estimating euler's number with n={str(n)}")
print("calculating...")

items = list(range(n))
permutations = list(itertools.permutations(items))
total_permutations = 0
derangements = 0

for permutation in permutations:
    is_derangement = True
    for i in range(len(permutation)):
        if permutation[i] == items[i]:
            is_derangement = False
            break
    if is_derangement:
        derangements += 1
    total_permutations += 1

estimate = total_permutations / derangements
deviation = abs(estimate - math.e)
accuracy = 100 - ((deviation/math.e) * 100)

print(f"{str(total_permutations)} permutations")
print(f"{str(derangements)} derangements")
print(f"estimated value: {str(estimate)}")
print(f"true value: {str(math.e)}")
print(f"{str(accuracy)}% accurate")
