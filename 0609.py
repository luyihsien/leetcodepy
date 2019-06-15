text = "alice is a good girl she is a good student"
first = "a"
second = "good"
print(text.split())
a=text.split()
b=[]
for i in range(len(a)-2):
    if a[i]==first and a[i+1]==second:
        b.append(a[i+2])
print(b)
a="cdadabcc"
d=set(a)
print(d)
b=''
for i in d:
    b=b+i
print(b)