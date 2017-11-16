#************************************************************************           
    # pyramid -- program to print odd lettered words in a pyramid.            
    #                                                         
    # Author:  Saad Qazi                            
    #                                                         
    # Purpose:  Calculate letter frequencies of words.            
    #                                                         
    # Usage:                                                 
    #      Runs the program and the output is printed in string format.          
#************************************************************************

def make_pyramid(word):
# This function is for odd lettered words
    num_rows = int((len(word))/2)
    word_len = len(word)
    for i in range(num_rows+1):
        for j in range(0,word_len):
            if j < num_rows - i or j > num_rows + i:
                print (' ',end="")
            else:
                print (word[j],end="")
        print ('\n')
    return



