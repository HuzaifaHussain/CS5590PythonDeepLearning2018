sentence = input("Enter a sentence:")
def middle_word(x):          #making a function
    a = sentence.split()     #spliting the given sentence then placing it in 'a'
    length = len(a)
    if length % 2 == 1:     #see if the sentence has odd number of words
         p = int(length/2)  # middle word position
         print("The middle word of the sentence is :",a[p])
    else:
        p = int((length/2)-1)  #middle two words position
        q = int(length/2)
        print("the middle letters of the sentence are:" , a[p], a[q])
middle_word(sentence)
