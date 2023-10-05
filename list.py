l1=[10,20,30,40,50,60,60]                                           #making a list l1
l2=[70,80,90,100]                                                   #making a list l2
l3=l1+l2                                                            #concatinating l1 and l2 using l3

print(l1,"\n")                                                      #printing l1
print("Checking Data Type:",type(l1),"\n")                          #printing data type of l1
print("The Current Lenght Of The List Is",len(l1),"\n")             #printing lenght of l1

print("The item At Oth position is",l1[0],"\n")                     #printing item at 0th position(forward indexing)
print("Item at 4th position:",l1[4],"\n")                           #printing item at 4th position(forward indexing)
'''print(l1[7])'''                                                  #error statement
print("item at -1th position",l1[-1],"\n")                          #printing item at -1th position(reverse indexing)
print("item at -5th position",l1[-5],"\n")                          #printing item at -5th position(reverse indexing)

print("printing full l1 using slicing: \n",l1[::],"\n")             #printing full l1 using slicing
print("printing l1 till 40 using slicing: \n",l1[:4],"\n")          #printing l1 till 40 using slicing
print("printing l1 from 50 using slicing: \n",l1[4:],"\n")          #printing l1 from 50 using slicing
print("printing l1 with step value 2 in slicing: \n",l1[::2],"\n")  #printing alternate elements of l1 by setting step value 2 in slicing
print(l1[::-1],"\n")                                                #printing l1 in reverse manner using slicing

print(30 in (l1),"\n")                                              #using membership operator
print(70 in (l1))                                                   #using membership operator

print(l3,"\n")                                                      #printing concatination of l1 and l2 as l3

print((l1)*3,"\n")                                                  #printing l1 three times using multiplication

l1.append(99)                                                       #appending 99 in l1
print("Appending l1",l1,"\n")

l1.insert(3,35)                                                     #inserting 35 in 3rd position
print("Inserting l1",l1,"\n")

l1.extend([101,105,107,110])                                        #extending l1
print("Extending l1",l1,"\n")

l1.pop()                                                            #using pop: last element (100) is deleted from l1
print("poping l1",l1,"\n")

l1.pop(3)                                                           #using pop(index) to remove 3rd element(40) from l1
print("Poping element at index number 3:",l1,"\n")

l1.remove(60)                                                       #removing 60 from l3 from l1
print("Removing 60 from l1: \n",l1,"\n")

l1.append(60)
print("no of occurence of 60: \n",l1.count(60),"\n")                #using count to know the occurence of 60 in l1


print("The Index number of 101 is :",l1.index(101),"\n")            #using index to know the position of 101 i l1

print("largest elemement in l1 is",max(l1),"\n")                    #printing largest elemement in l1

print("smallest elemement in l1 is",min(l1),"\n")                   #printing smallest elemement in l1

print("The Sum Of all the elements in l1 is ",sum(l1),"\n")         #printing sum of all the elements of l1

l1.sort()                                                           #sorting l1 in ascending order
print("The Sorted Form Of L1 is: \n",l1,"\n")

l1.reverse()                                                        #finding the reverse of l1
print("The reverse Form Of L1 is: \n",l1,"\n")

c=l1.copy()                                                         #copying l1 into variable c
print("l1 is copied as variable c which is: \n c=",c,"\n")

c.clear()                                                           #clearing variable c
print("If we clear variable c then the output is: \n c=",c,"\n")


l5= list(input("enter list: "))
print(l5)
