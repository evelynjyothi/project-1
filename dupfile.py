file=open("file.txt","r")
"""print("Using readline:")
line1=file.readline()
line2=file.readline()
print(repr(line1))
print(repr(line2))
line=file.readline()
while line !='':
    print(line)
    line=file.readline()
file.close()"""
import pickle
l=[1,2,3,4,5,6]
file=open("file1.txt","wb")
pickle.dump(l,file)
file.close()
with open("file1.txt") as f:
    print(f.read())