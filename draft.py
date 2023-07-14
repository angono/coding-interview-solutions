# Q. 2
def solution(array, toMove):
    n = len(array)
    i = 0
    j = n - 1
    while i < j:
        if array[i] == toMove:
            array[i], array[j] = array[j], array[i]
            j -= 1
        else:
            i += 1
    return array

# Q. 3 
def solution(characters, document):
    # Create a dictionary to store the count of each character in the available characters
    char_count = {}
    for char in characters:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Iterate through the document and check if each character is available in the sufficient quantity
    for char in document:
        if char not in char_count or char_count[char] < 1:
            # If a character is not available or there are not enough of that character, return False
            return False
        char_count[char] -= 1
    
    # If all characters in the document are available, return True
    return True



# https://app.codility.com/c/run/XBZ5EW-K32/
# https://app.codility.com/c/feedback/XBZ5EW-K32/


# Q. 4

def is_same_bst(arr1, arr2):
    if not arr1 and not arr2:
        return True
    elif not arr1 or not arr2:
        return False
    elif arr1[0] != arr2[0]:
        return False

    left1 = [x for x in arr1 if x < arr1[0]]
    right1 = [x for x in arr1 if x > arr1[0]]
    left2 = [x for x in arr2 if x < arr2[0]]
    right2 = [x for x in arr2 if x > arr2[0]]
    return is_same_bst(left1, left2) and is_same_bst(right1, right2)


def solution(arrayOne, arrayTwo):
    return is_same_bst(arrayOne, arrayTwo)


