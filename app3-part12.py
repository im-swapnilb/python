"""
Problem statement :
Using python dictionary, create a language dictionary.
The input to your program will be an English-French dictionary and a French-Germany dictionary.
The output will be English-Germany dictionary.
Then ask the user to enter an English word to test your program. if the word exists the program can return the
corresponding German word.

@Authors
    Karthik Thallam, id : 500188370
    Urmi Parekh, id : 500186977
    Ashish Sharma, id : 500188494
    Swapnil Bandgar, id : 500186962
"""


# This function will give you result in germany when you enter word in english
def language_dict():
    english_french = {'good': 'bonne', 'bad': 'mal', 'average': 'moyenne'}
    french_germany = {'bonne': 'gut', 'mal': 'falsch', 'moyenne': 'durchschnittlich'}
    # Enter word in english to get result in Germany.
    word = input('Enter the word : ').lower()
    if word in english_french:
        print('German word for the above English word is:', french_germany[english_french[word]])
    else:
        print('Word not found in dictionary')


if __name__ == '__main__':
    print("Language dictionary function started : ")
    language_dict()
