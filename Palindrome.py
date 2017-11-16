#**************************************************************************           
    # isPalindrome -- program to print an input string if it is palindrome.            
    #                                                         
    # Author:  Saad Qazi                            
    #                                                         
    # Purpose:  Determines if a word is a palindrome.            
    #                                                         
    # Usage:                                                 
    #      Runs the program and input is printed if it is a palindrome.          
#***************************************************************************
def is_palindrome_v1(word):
    reversedWord = word[::-1]
    if word.lower() == reversedWord.lower():
        print(word + " is a palindrome!")
    else:
        print(word + " is not a palindrome!")
    return

def is_palindrome(word):
    for i in range (0, len(word) // 2):
        if word[i] != word[(i * -1) - 1]:
            print(word + " is not a Palindrome")
            return
    print (word + " is a Palindrome")
    return

    