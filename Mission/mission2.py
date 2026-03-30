# 1
'''
def filter_even_length_strings(input_strs: list[str]) -> list[str]:
    return [s for s in input_strs if len(s) % 2 == 0]


print(filter_even_length_strings(["cat", "dog", "fish", "elephant"]))
print(filter_even_length_strings(["q", "w", "e", "r","t","y"]))
print(filter_even_length_strings(["qq", "ww", "ee", "rr","tt","yy"]))
'''
#2
'''
def reverse_elements(input_nums: list[int]) -> list[int]:
    return input_nums[::-1]

print(reverse_elements([1,2,3,4,5]))
print(reverse_elements([]))
print(reverse_elements([20,15,25,10,30,5,0]))
'''
# 3
def filter_type_str(input_list: list[str | int]) -> list[str]:
    return [item for item in input_list if isinstance(item,str)]

print(filter_type_str(["hello",1,2,"www"]))
print(filter_type_str([]))
print(filter_type_str([1,2,3,4,5]))