d1={'t1':'watering plants','t2':'sun bath'}
print("welcome to planner\n")
for i in range(1,100):
    y=input("what do you want to do : \n1.know about my tasks\n2.add a task\n3.mark task completed\n4.update task\n\n : ")
    if (y=='1'):
        x=input("enter task to be known:")
        if x in d1.keys():
            print(f"your task {x} is : {d1.get(x)}")
        else:
            a=input(f"there is no {x} task in your planner, to know available tasks in planner input \"yes\" else input \"no\" to go back to main menu : ")
            if a=='yes':
                print("available tasks in your planner are : \n")
                print(i for i in d1.keys())

    elif (y=='2'):
        x=input("enter the new task:")
        d1.update({'t3':x})
        print(d1.items())
