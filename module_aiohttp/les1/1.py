def isValidSubsequence(array: list, sequence):
    for item in sequence:
        if item in array:
            return False
    return True


l1 = [5, 1, 22, 25, 6, -1, 8, 10]
l2 = [1, 6, -1, 10, 100]

print(isValidSubsequence(l1, l2))
