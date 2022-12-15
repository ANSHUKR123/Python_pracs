def lis(num,list1=[]):
    total=sum(list1)
    comission=(0.05*total) if(total>50000) else 0
    if(total>=80000):
        return (num,total,comission,"Excellent Sales")
    elif(total>=60000):
        return (num,total,comission,"Good Sales")
    elif(total>=40000):
        return (num,total,comission,"Average Sales")
    else:
        return (num,total,comission,"Work Hard")
    
def main():
    n=int(input("Enter no of worker - "))
    fin=[]
    y=0
    while(0<n):
        y=y+1;
        print("Worker no ",(y))
        u_input=input("enter sales of four week seprated by comma no spaces of worker -")
        list2=[]
        for i in u_input.split(','): # type casting
            list2.append(int(i))
        fin.append(lis(y,list2))
        n=n-1
    print("Final list : ")    
    print(fin)
main()