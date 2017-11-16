#************************************************************************           
    # letter_freq -- program to calculate and print letter frequencies.            
    #                                                         
    # Author:  Saad Qazi                            
    #                                                         
    # Purpose:  Calculate letter frequencies of words.            
    #                                                         
    # Usage:                                                 
    #      Runs the program and the output is printed in string format.          
#************************************************************************



def count_letters(word):
	if not word:
		return ''
	word = word.replace(' ', '').lower()
	freq_dict = {}
	for letter in word:
		freq_dict[letter] = freq_dict.get(letter,0) + 1
	ret = ''
	for letter in word:
		if letter in freq_dict:
			ret += letter + str(freq_dict[letter]) + ' '
			del freq_dict[letter]
	print(ret[:-1])



alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']

def count_of_letter(alpha,word):
    count = 0
    for i in range(len(word)):
        if (word[i]) == (alpha):
            count = count + 1
    return count


def letter_freq_v1(word):
    for i in range(len(alphabets)):
        count = count_of_letter(alphabets[i],word)

        if count > 0:
            print (alphabets[i]+str(count)+ '   ',end='')


