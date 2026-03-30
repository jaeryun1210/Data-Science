# 1
'''
def get_second_largest_number(input_nums: list[int]) -> int | None:
    nums = list(set(input_nums))
    
    if len(nums) < 2:
        return None
    
    nums.sort(reverse=True)
    return nums[1]

print(get_second_largest_number([1, 2, 3, 4, 5]))
print(get_second_largest_number([3,45,345,435,345,43,56,34,234,34]))
print(get_second_largest_number([1]))
'''
# 2
'''
def format_number_with_commas(input_num: int) -> str:
    is_negative = input_num < 0
    num_str = str(abs(input_num))
    
    result = ""
    count = 0
    
    for s in reversed(num_str):
        if count == 3:
            result = "," + result
            count = 0
        result = s + result
        count += 1
    
    if is_negative:
        result = "-" + result
    
    return result

print(format_number_with_commas(1000000))
print(format_number_with_commas(12345))
print(format_number_with_commas(-99999999))
'''
'''
내장함수 사용
def format_number_with_commas(input_num: int) -> str:
    return f"{input_num:,}"
'''
# 3
def string_to_ascii(input_str: str) -> list[int]:
    return [ord(ch) for ch in input_str]

print(string_to_ascii("Programming puzzles!"))
print(string_to_ascii(""))
print(string_to_ascii("aA"))