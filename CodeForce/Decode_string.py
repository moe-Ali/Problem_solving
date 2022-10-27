test_num=int(input())
final=[]
for i in range(test_num):
    word=""
    char_max_num=int(input())-1
    char_num=char_max_num
    code=input()
    for i in range(len(code)):
        if  code[len(code)-i-1]=="0" and code[len(code)-i-2]!="0":
            char_num-=2
        else:
            pass
    position=0
    for j in range(char_num+1):
        if code[(char_max_num-position)]!="0":
            word+=chr(int(code[(char_max_num-position)])+96)
            position+=1
        else:
            word+=chr(int(code[(char_max_num-position-2):(char_max_num-position)])+96)
            position+=3
    final.append(word[::-1])
for i in final:
    print(i)
