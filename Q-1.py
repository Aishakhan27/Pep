s="a mouse is smaller than a dog but  dog is stronger"
# output=["a", "is", "dog"],have to print the words only one time
k=2
string=[]
words=s.split()
for i in range(len(words)):
    if words.count(words[i])>=k:
        string.append(words[i])
x=[]
for word in string:
    if word not in x:
        x.append(word)
print(x)

