from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer() # Need to feed it some strings

#creating some feeding data
string1 = 'Hii Katie the self driving car will be late'
string2 = 'Hi Sebastian the machine learning class will be great great great'
string3 = 'Hi Katie, the machine learning class will be most excellent'

email_list = [string1, string2, string3]

# Fiting the model to the data
bag_of_words = vectorizer.fit(email_list)
bag_of_words = vectorizer.transform(email_list)

print(bag_of_words)
#if you run print(bag_of_words) it will give you a tuples followed by integers e.g. (1, 5) 3. This is interpreted as: In document number one, word number 5 was spotted 3 times.

#To decipher which number is a word are which, you can use:
print(vectorizer.vocabulary_.get("great"))

#for the other direction (what is a word associated with a number)

## Stopwords are words like "the" "and" with high frequency and low information value. A list of these stopwords can be found on
from nltk.corpus import stopwords
sw = stopwords.words("english")
