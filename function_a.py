def most_common_value(number_list):
    """ returns the most common element of the list
    """
    numbers = {}
    for number in number_list:
        if number not in numbers:
            numbers[number] = 1
        else:
            numbers[number] += 1
    max_number = None
    max_occurrences = 0
    for k, v in numbers.items():
        if max_number is None or v > max_occurrences:
            max_occurrences = v
            max_number = k
        elif v == max_occurrences:
            if type(max_number) == int:
                max_number = [max_number]
            max_number.append(k)
    return max_number


if __name__ == "__main__":
    nums = [1, 1, 3, 3, 3, 7, 8, 2, 1, 3]
    print(f"Most common value = {most_common_value(nums)}")

nums1 = [1, 1, 3, 3, 3, 7, 8, 2, 1, 3] # 3
nums2 = [1, 1, 2, 2, 6, 7, 11] # [1, 2]
nums3 = [1, 1, 2, 2, 6, 6, 7, 7, 11, 11] # [1, 2, 6, 7, 11]
assert most_common_value(nums1) == 3
assert most_common_value(nums2) == [1, 2]
assert most_common_value(nums3) == [1, 2, 6, 7, 11]

