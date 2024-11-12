import math
print("this is the combiantion tool:")
x=input("enter the question :")
if 'select'or'combination' in x:
    n=int(input("enter n : "))
    r=int(input("enter r : "))
    result=math.factorial(n)/(math.factorial(n-r)*math.factorial(r))
    print("the combinations is :",result)
elif 'arrangements'or'permutation' in x:
    print("this is a perm pb")
    printf("is it a string problem?")
    z=input()
    if z=='yes':
        s=input("enter the string:")
        perm=math.factorial(len(s))
        for i in s:
            perm=perm/math.factorial(s.count(i))
        else:
            print('haha')


else:
    print("this is not a related pb")