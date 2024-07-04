# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, input_list):
        result = []
        word_letters = [letter for letter in self.word]
        for input in input_list:
            input_letters = [letter for letter in input]
            if sorted(word_letters) == sorted(input_letters):
                result.append(input)
                    
        return result