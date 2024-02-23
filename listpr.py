l = ["hello","world",'a',16]
true = True
while true == True:
    num=int(input("1_Add at end \n 2_Delete from end \n 3_ Insert at specific point \n 4_Delete from specific point \n 5_ Clear feature1 list \n 6_Print \n7_Stop\n"))
    while not(num>0 and num<8):
        num=int(input("again:"))
    if num==1:
        val=input("Enter something to insert : ")
        while val == None:
            val=input("Please enter correctly : ")
        l.append(val)
    elif num==2:
        l.pop()
    elif num==3:
        ind = int(input("Enter index value : "))
        while (ind>len(l)):
            ind = int(input("Enter correct index value : "))
        val=input("Enter something to insert : ")
        l.insert(ind,val)
    elif num==4:
        ind = int(input("Enter index value to delete: "))
        while (ind>len(l)):
            ind = int(input("Enter correct index value : "))
        l.pop(ind)
    elif num==5:
        l.clear()
    elif num==6:
        print(f"The list is : {l}")
    if num==7:
        true=False