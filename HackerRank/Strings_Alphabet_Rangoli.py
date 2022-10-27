size=int(input())
max=(size*2-1)*2-1
center=size+1
li=[]
for i in range (max):
    li.append("-")
li[(center)]=chr(96+size)
li[(size+1)]=chr(96+size-1)
li[(size-1)]=chr(96+size-1)
li[(size+2)]=chr(96+size-2)
li[(size-2)]=chr(96+size-2)
for i in range(1,size-1):
    left=max-((i*2-1)*2-1)
    print(left)
print(li)
