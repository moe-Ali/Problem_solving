def first_input():
    intial_input=input("Please Enter the number_of_candy (n>=1) and the starting_jump_power (x<=2000) as => n x\n")
    n=int(intial_input.split(" ")[0])
    x=int(intial_input.split(" ")[1])

    # Error in n , x handling
    if n>=1 :
        pass
    else:
        print(" !!ERROR in number_of_candy!! Please Re-Enter the values")
        first_input()
    if x<=2000:
        pass
    else:
        print(" !!ERROR starting_jump_power!! Please Re-Enter the values")
        first_input()
    return n,x

def second_input(n):
    dic={}
    print("Please Enter every candy as => type_of_candy jump_hight_to_reach candy_mass")
    for i in range(n):
        candy_input=input()
        t=int(candy_input.split(" ")[0])
        h=int(candy_input.split(" ")[1])
        m=int(candy_input.split(" ")[2])
        dic[i]=[t,h,m]

        # Error in dictionary items handling
        if t>=0 and t<=1:
            pass
        else:
            print(" !!ERROR in type_of_candy!! Please Re-Enter the values")
            second_input(n)
        if h >= 1:
            pass
        else:
            print(" !!ERROR in Jump_hight_to_reach!! Please Re-Enter the values")
            second_input(n)
        if m<=2000:
            pass
        else:
            print(" !!ERROR in candy_mass!! Please Re-Enter the values")
            second_input(n)
    return dic

# checking which type is there more of fruit drops or caramel drops
def bigger(dic):
    zero_counter=0
    one_counter=1
    for i in range(len(dic)):
        if dic[i][0]==0:
            zero_counter+=1
        else:
            one_counter+=1
        if zero_counter>=one_counter:
            bigger_num=0    
        else:
            bigger_num=1
    return bigger_num

def logic(n,x,dic):
    bigger_num=bigger(dic)
    candy_num=0
    dic_used_index=[]
    for j in range(n):
        # for the first candy to eat
        if j==0:
            for i in dic.keys():
                if x>=dic[i][1] and bigger_num==dic[i][0]:
                    x+=dic[i][2]
                    candy_num+=1
                    prev=dic[i][0]
                    dic_used_index.append(i)
                    break
                else:
                    pass
            if candy_num==0:
                for i in dic.keys():
                    if x>=dic[i][1]:
                        x+=dic[i][2]
                        candy_num+=1
                        prev=dic[i][0]
                        dic_used_index.append(i)
                        break
                    else:
                        pass
        # after the first candy where we have a previous candy value
        else:
            for i in dic.keys():
                if i in dic_used_index:
                    pass
                else:    
                    if (dic[i][0])==prev:
                        pass
                    else:
                        if x>=dic[i][1]:
                            x+=dic[i][2]
                            candy_num+=1
                            prev=dic[i][0]
                            dic_used_index.append(i)
                        else:
                            pass
    return candy_num

# using the functions   
n,x=first_input()
dic=second_input(n)
print("The out put is: "+str(logic(n,x,dic)))
