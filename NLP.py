import nltk
nltk.download('wordnet') ##lemmatize
nltk.download('punkt')  ##tokenize

from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize

lem=WordNetLemmatizer()

sentence="Hi!, This is Shivam Pahariya. I am studying at SRMIST."
token=word_tokenize(sentence)
token

for i in token:
    l=lem.lemmatize(i,"v")
    print(l)
