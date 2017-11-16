from Palindrome import is_palindrome
from Pyramid import make_pyramid
from Frequency import count_letters

def getInputFile(target):
    if target == "palindrome":
        return "Palindrome.in"
    if target == "countletters":
        return "CountLetters.in"
    if target == "pyramid":
        return "Pyramid.in"

def callTarget(target, line):
    if target == "palindrome":
        is_palindrome(line)
    if target == "countletters":
        count_letters(line)
    if target == "pyramid":
        make_pyramid(line)

def testProgram(target):
    print("Testing target : " + target)
    #print("-------------------------------------------------------------------------------------------")
    with open(getInputFile(target)) as f:
        line = f.readline()
        while line:
            print("---------------------------------------------")
            print("Input line: " + line);
            print("Output: ")
            callTarget(target, line.strip())
            line = f.readline()
    print("\n\n")

testProgram("palindrome")
testProgram("countletters")
testProgram("pyramid")