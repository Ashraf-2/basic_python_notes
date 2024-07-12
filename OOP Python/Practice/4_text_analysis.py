# we will do practice of text Mining or we can call it as Text Analysis.

# 1. Make the text lower case, count the frequency of every word and lastly count the frequency of a specific word
# givenstring="Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."

text = "amar shonar bangla ami tumay valobashi. chirodin tumar akash, tumar batash amar prane bajay bashi, amar shonar bangla ami tumay valobashi"


class TextAnalyzer:

    def __init__(self,text):

        self.fmtText = text


    def freqAll(self):
        # wordList = self.fmtText.split(' ')
        words = self.fmtText
        # print(words)
 
        wordsFormatted = words.replace('.','').replace(',','').replace('!','')
        # print("wordsFormatted: ",wordsFormatted)
        wordList = wordsFormatted.split(' ')
        # print(wordList)
        
        # create dictionary
        frequency_Map = {}
        
        for word in set(wordList): # using set to remove duplicate from the word list
            frequency_Map[word] = wordList.count(word)

        return frequency_Map

    # creating a method to find the frequency of a particular word
    def freq_of_a_word(self,dict,word):
        freqDict = self.freqAll()
        if word in freqDict:
            print("The frequecny of the word '",word,"' is: ",dict[word])
        else:
            print("This word is out of the context")
# creating instances

obj1 = TextAnalyzer(text)
string_dict = obj1.freqAll()
print(string_dict)
# print(type(string_dict))      # output: dictionary
obj1.freq_of_a_word(string_dict,"valobashi")
obj1.freq_of_a_word(string_dict,"amar")
obj1.freq_of_a_word(string_dict,"hay")