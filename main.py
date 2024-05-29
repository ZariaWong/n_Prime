N=int(input())
list1=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
A=0
if N==2:
    A=0
else:
    for i in list1:
        if i<N:
            if N%i!=0 :
                A=A+1
print(A)
