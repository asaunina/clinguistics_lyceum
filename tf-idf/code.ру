import collections

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
    tf_new1 = collections.Counter(new1)
    for i in tf_new1:
        tf_new1[i] = tf_new1[i]/(float(len(new1)))
    return tf_new1
        
k = len(open("new1.txt","r").read().split())
print(compute_tf(new1), sep='\n')
print("Количество словоупотреблений в тексте -" ,k)



import math
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
