# Given a singly linked list, determine if it is a palindrome.

# Example 1:

# Input: 1->2
# Output: false
# Example 2:

# Input: 1->2->2->1
# Output: true



def isPalindrome(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    current = head
    word_list = []
    while current is not None:
        word_list.append(current.val)
        current = current.next
    return self.check(word_list)
            
    
def check(self, word_list):
    for i in range(len(word_list)/2):
        if word_list[i] == word_list[-(i+1)]:
            continue
        else:
            return False
    return True