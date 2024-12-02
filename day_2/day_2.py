def remove_i(arr, i):
    return arr[:i] + arr[i + 1:]


def check_diff(diff, diff_before):
    if diff > 0 > diff_before:
        return False
    elif diff < 0 < diff_before:
        return False
    elif diff > 3 or diff < -3 or diff == 0:
        return False
    return True


def check_safe(arr):
    diff_before = arr[1] - arr[0]
    if diff_before > 3 or diff_before < -3 or diff_before == 0:
        return False
    for i in range(1, len(arr) - 1):
        diff = arr[i + 1] - arr[i]
        if not check_diff(diff, diff_before):
            return False
        diff_before = diff
    return True


def is_safe_with_dampener(arr):
    if check_safe(arr):
        return True
    for i in range(len(arr)):
        new_arr = remove_i(arr, i)
        if check_safe(new_arr):
            return True
    return False


input_file = open('input.txt', 'r')
lines = input_file.readlines()
res = 0

for line in lines:
    arr = line.split()
    arr = [int(i) for i in arr]
    if is_safe_with_dampener(arr):
        res += 1

print(res)
