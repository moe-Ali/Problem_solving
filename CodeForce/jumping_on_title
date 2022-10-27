test_num=int(input())
final=[]
for i in range(test_num):
    char=input()
    list_chr=list(char)
    last=len(list_chr)-1
    first_char=list_chr[0]
    last_char=list_chr[last]
    if ord(first_char)>ord(last_char):
        list_chr.sort(reverse=True)
    else:
        list_chr.sort()
    first_index=list_chr.index(first_char)
    last_index="".join(list_chr).rindex(last_char)
    cost=0
    if first_index>last_index:
        tail_list=list_chr[first_index:last_index:-1]
        tail_list.append(last_char)
    else:
        tail_list=list_chr[first_index:last_index]
        tail_list.append(last_char)
    for i in range(len(tail_list)-1):
        cost+=abs((ord(tail_list[i])-96)-(ord(tail_list[i+1])-96))
    main_list=list(char)
    order=""
    used_index=[]
    for i in tail_list:
        for j in range(len(main_list)):
            if main_list[j]==i and j not in used_index:
                order+=str(j+1)+" "
                used_index.append(j)
                break
    m=len(tail_list)
    final.append(str(cost)+" "+str(m))
    final.append(order)
for i in final:
    print(i)
