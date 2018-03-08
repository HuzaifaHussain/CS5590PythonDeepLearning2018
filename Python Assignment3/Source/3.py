from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tag import pos_tag
import nltk
p = open('rough.txt',"r", encoding="UTF8")
sentence_reading = p.read()
NewTokenWords = word_tokenize(sentence_reading)
OldWords = stopwords.words('english')
NewFilterWords = [w for w in NewTokenWords if w not in OldWords]
NewFilterWords = [w for w in NewFilterWords if len(w)>2]
LemmatizingWords = list()
for x in NewFilterWords:
    LemmatizingWords.append(WordNetLemmatizer().lemmatize(x))
print("The output of Lemmatizing words obtained are :\n",LemmatizingWords)
Result = list()
for y in pos_tag(LemmatizingWords):
    if y[1][:2] == 'VB':
        continue
    else:
        Result.append(y[0])
MostOccuring = nltk.FreqDist(Result)
WordsChosen = dict()
for word, most in MostOccuring.most_common(5):          #As mentioned in the question, we are using top five words
    WordsChosen[word] = most
FiveTopWords = WordsChosen.keys()
print('\nFive words which are most common are:', WordsChosen)
ObtainedResult = list()
for word in sentence_reading.split('\n'):
    for choose in WordsChosen:
        if choose in word.lower():
            ObtainedResult.append(word)
            break
print('\nThe Text Summary is as follows :\n', "\n".join(ObtainedResult))