# (Level: Easy)
# Given an array of numbers, replace each even number with two of the same number.
# e.g, [1,2,5,6,8] -> [1,2,2,5,6,6,8,8]. Assume that the array has enough space to accommodate the result.
#ESTCV

#brute force
def replace_even_numbers(lst):
    seen = set()

    for indx, num in enumerate(lst):
        if num in seen:
            continue;

        if type(num) != int:
            lst[indx] = -1
        elif num % 2 == 0:
            lst.insert(indx, num)
            seen.add(num)
    return lst

def get_last_val_index(lst):
    indx= 0
    for num in lst:
        if num != -1:
            indx+=1
    return indx -1
            
def replace_even_numbers(lst):
    if lst == None or len(lst) == 0:
        return lst
    end = -1
    original_length = get_last_val_index(lst)
    for i in range(original_length, -1, -1):
        num = lst[i]
        if num == None:
            lst[end] = -1
            end -= 1
            continue;
        if num % 2 == 0:
            lst[end] = num
            end -= 1
        lst[end] = num
        end -= 1
    return lst
# time: O(n)
#spce: O(1)
print(replace_even_numbers([1,2,5,6,8, -1, -1, -1]))
print(replace_even_numbers([]))
print(replace_even_numbers(None))
print(replace_even_numbers([1,3,5]))
print(replace_even_numbers([2,None, 4,6,None, 8, -1, -1, -1, -1]))


# Given a sentence, reverse the words of the sentence. For example, "i live in a house" becomes "house a in live i".

#What if I have a null value
#What if the string is empty
#Am I guaranteed just letters or can it be periods

#Test Cases
# "i live in a house"
# "i live in a blue house"
#Null
#"empty"

def reverse_words(words):
    if words == None or len(words) == 0:
        return words
    array_words = words.split(" ")

    indx = len(array_words) / 2
    indx_end = -1
    for indx in range(indx):
        temp = array_words[indx]
        array_words[indx] = array_words[indx_end]
        array_words[indx_end] = temp
        indx_end -=1
    return array_words

def reverse_words(words):
    if words == None or len(words) == 0:
        return words

    return_string = ""
    last_space = None
    for indx in range(len(words) -1, -1, -1):
        char = words[indx]
        if char == " ":
            return_string += words[indx+1: last_space]
            return_string += " "
            last_space = indx

    return_string += words[0: last_space]
    return return_string

#space: O(N)
#time: O(N)
print(reverse_words("i live in a house"))
print(reverse_words("i live in a blue house"))
print(reverse_words(None))
print(reverse_words(""))
# "house live in a blue i"
#"house blue a in live i "