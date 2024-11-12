import random
for i in range(1,100):
    user1=input("\nenter your choice\nstone/paper/scissors : ")
    if(user1==''):
        print("please provide input!\n")
    else:
        comp=random.choice(['stone','paper','scissors'])
        print(f"computer chose : {comp}")
        if(user==comp):
            print("its a draw!")
        elif((user=='stone')and(comp=='scissors'))or((user=='paper')and(comp=='stone'))or((user=='scissors')and(comp=='paper')):
            print("you win")
        else:
            print("you lose")