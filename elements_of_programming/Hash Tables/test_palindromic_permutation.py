#write a program to test whether a string can be permuted to form a palindrome
#ignore spaces, punctuations


#Time: O(n)
#Space: O(n)
def palindrome_permutation(string):
    dict_ = {}

    lower_case_string = string.lower()
    for char in lower_case_string:
        if char.isalpha() or char.isdigit():
            if char in dict_:
                dict_[char] += 1
            else:
                dict_[char] = 1

    odd_count = 0

    for dict_letter in dict_:
        if dict_[dict_letter] % 2 != 0:
            odd_count +=1

    if odd_count > 1:
        return False
    return True


print palindrome_permutation('Eva, Can &@!)I St44ab Bats In A Cave?') #----> True
print palindrome_permutation('A Man, A Plan, A Canal-^#@*!Panama!') #----> True
print palindrome_permutation('Madam In)@)@) Eden, Im Adam') #----> True
print palindrome_permutation('ahsdkasjldkjalskdjklaja') #----> False