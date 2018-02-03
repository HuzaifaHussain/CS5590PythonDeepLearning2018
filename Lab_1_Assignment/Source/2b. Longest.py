sentence = input('Enter the sentence: ')
words = sentence.split()  #splitting the given sentence and placing it in words
length = 0                #initial length is zero
long_word = ''            #empty string at first
for x in words:
    if(len(x)>length):
        length = len(x)
        long_word = x
print('Longest word in the sentence: ',long_word)
