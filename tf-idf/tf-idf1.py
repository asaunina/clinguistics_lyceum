
import math
from collections import Counter

def words(stringIterable):
    lineStream = iter(stringIterable)
    for line in lineStream:
        for word in line.split():
            yield word
            
new1 = []
with open('new1.txt', 'r') as myself:
    for word in words (myself):
        new1.append (word)
        
def compute_tf(new1):
    tf_new1 = Counter(new1)
    for i in tf_new1:
        tf_new1[i] = tf_new1[i]/(float(len(new1)))
    return tf_new1
        
k = len(open("new1.txt","r").read().split())
print(compute_tf(new1), sep='\n')
print("количество словоупотреблений в тексте -" ,k)




def words(stringIterable):
    lineStream = iter(stringIterable)
    for line in lineStream:
        for word in line.split():
            yield word
            
new1 = []
new2 = []
new3 = []

with open('new1.txt', 'r') as myself:
    for word in words (myself):
        new1.append (word)
with open('new2.txt', 'r') as myself:
    for word in words (myself):
        new2.append (word)
with open('new3.txt', 'r') as myself:
    for word in words (myself):
        new3.append (word)        
                               
corpus = [new1, new2, new3]

def compute_idf(word, corpus):             
    return math.log10(len(corpus)/sum([1.0 for i in corpus if word in i])) 

print (compute_idf('chapter', corpus))




def compute_tfidf(corpus):
    def compute_tf(text):
        tf_text = Counter(text)
        for i in tf_text:
            tf_text[i] = tf_text[i]/float(len(text))
        return tf_text

    def compute_idf(word, corpus):
       return math.log10(len(corpus)/sum([1.0 for i in corpus if word in i]))
 

    documents_list = []
    for text in corpus:
        tf_idf_dictionary = {}
        computed_tf = compute_tf(text)
        for word in computed_tf:
            tf_idf_dictionary[word] = computed_tf[word] * compute_idf(word, corpus)
        documents_list.append(tf_idf_dictionary)

    return documents_list

print(compute_tfidf(corpus))

