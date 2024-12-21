#   Author: Dayan Abdulla
#   Date: 09/18/2024
#   Homework #2 Program #6
#####################################
def main():
    #input
    letter = input("Enter a letter: ")

    #input
    sentence = input("Enter a sentence: ")

    #length of sentence
    length = len(sentence)

    #without spaces
    noSpaces = sentence.replace(" ", "")
    lengthNoSpaces = len(noSpaces)

    #counting word
    words = sentence.split()
    word_count = len(words)

    #reverse sentence
    reverseSentence = sentence[::-1]

    #counting letter
    countE = sentence.lower().count('e')

    #vowels
    vowels = 'aeiou'
    vowel1 = sum(1 for char in sentence.lower() if char in vowels)


    #outputs in same sequence
    print(f"This sentence has {length} characters")
    print(f'The length of the sentence without spaces is {lengthNoSpaces} letters')
    print(f"This sentence has {word_count} words")
    print(f"The sentence in complete rever is {reverseSentence}")
    print(f"There is {countE} occurrence of e in sentence.")
    print(f"The number of vowels in the sentence is {vowel1} ")

if __name__ == "__main__":
    main()
