test_num=int(input())
final_list=[]
for i in range(test_num):
    line=input()
    a=int(line.split(" ")[0])
    b=int(line.split(" ")[1])
    c=int(line.split(" ")[2])
    f_elev=abs(a-1)
    s_elev=abs(b-c)+abs(c-1)
    if f_elev < s_elev:
        final_list.append(1)
    elif s_elev < f_elev:
        final_list.append(2)
    else:
        final_list.append(3)
for i in final_list:
    print(i)
