name=input()
numb=int(input())
dic={}
for i in range(numb):
    inp=input()
    f_name=inp.split(" ")[0]
    opration=inp.split(" ")[1]
    if opration=="likes":
        s_name=inp.split(" ")[2].split("'")[0]
    else:
        s_name=inp.split(" ")[3].split("'")[0]
    if name ==f_name:
        pass
    else:
        if opration=="posted":
            if f_name in dic.keys():
                dic[f_name]+=15
            else:
                dic[f_name]=15
        elif opration=="commented":
            if f_name in dic.keys():
                dic[f_name]+=10
            else:
                dic[f_name]=10
        else:
            if f_name in dic.keys():
                dic[f_name]+=5
            else:
                dic[f_name]=5
    if name ==s_name:
        pass
    else:
        if opration=="posted":
            if s_name in dic.keys():
                dic[s_name]+=15
            else:
                dic[s_name]=15
        elif opration=="commented":
            if s_name in dic.keys():
                dic[s_name]+=10
            else:
                dic[s_name]=10
        else:
            if s_name in dic.keys():
                dic[s_name]+=5
            else:
                dic[s_name]=5
newlist = sorted(dic, key=lambda x: (-dic[x],x))
print("Output:")
for i in newlist:
    print(i)
