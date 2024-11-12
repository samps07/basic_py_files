d1={'student1':43,'student2':23}
print(d1)
n=int(input("enter number of students to be added: "))
for i in range(n):
    x=input("enter student name to be added:")
    y=int(input("enter student marks: "))
    d1.update({x:y})
for x,y in d1.items():
    if (y<33):
        print(f"{x} has failed")
print(d1)



