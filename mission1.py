# 1
'''def sum_even(input_nums: list[int]) -> int:
    total = 0
    
    for num in input_nums:
        if num % 2 == 0:
            total += num
    return total

print(sum_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(sum_even([10, 20, 30, 40, 50]))
print(sum_even([9, 7, 5, 3, 1]))'''

'''def sum_even(input_nums: list[int]) -> int:
    return sum([num for num in input_nums if num % 2 == 0])

print(sum_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(sum_even([10, 20, 30, 40, 50]))
print(sum_even([9, 7, 5, 3, 1]))'''

# 2
'''def remove_vowels(input_str: str) -> str:
    result = ""
    
    for ch in input_str:
        if ch not in "aeiouAEIOU":
            result += ch
            
    return result


print(remove_vowels("Hello, World!"))
print(remove_vowels("aeiouAEIOU"))
print(remove_vowels("zzxxxccvvbbnnmmmLLKKUHH"))'''

'''def remove_vowels(input_str: str) -> str:
    return "".join([ch for ch in input_str if ch not in "aeiouAEIOU"])

print(remove_vowels("Hello, World!"))
print(remove_vowels("aeiouAEIOU"))
print(remove_vowels("zzxxxccvvbbnnmmmLLKKUHH"))'''
# 3
'''def get_longest_string(input_strs: list[str]) -> str:
    longest = input_strs[0]

    for s in input_strs:
        if len(s) > len(longest):
            longest = s

    return longest


print(get_longest_string(["cat", "dog", "bird", "lizard"]))
print(get_longest_string(["cat", "dog", "bird", "wolf"]))
print(get_longest_string(["a", "b", "c", "d"]))'''

def get_longest_string(input_strs: list[str]) -> str:
    return max(input_strs, key=len)

print(get_longest_string(["cat", "dog", "bird", "lizard"]))
print(get_longest_string(["cat", "dog", "bird", "wolf"]))
print(get_longest_string(["a", "b", "c", "d"]))
