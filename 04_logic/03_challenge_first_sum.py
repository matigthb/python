"""
Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y devuelve sus índices. 
Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""

def find_first_sum(nums, goal) -> list:
    indexes = []
    #for key1, num1 in enumerate(nums):
    #    for key2, num2 in  enumerate(nums):
    #        if key1 >= key2:
    #            continue
    #        if num1 + num2 == goal:
    #            indexes = [key1 ,key2] 
    #            break

    #for i in range(len(nums)):
    #    for j in range(i+1, len(nums)):
    #        if nums[i] + nums[j] == goal:
    #            return [i, j]
    #            break

    seen = {}

    for index, value in enumerate(nums):
        missing = goal - value
        if missing in seen: return [seen[missing], index]

        seen[value] = index

    return indexes


print(find_first_sum([4, 5, 6, 2],8))