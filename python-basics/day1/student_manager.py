students=[]
while True :
    name = input("Enter Student name(Press e and Enter to exit) : ")
    
    if name == "e":
        break
    students.append(name)
print("Students : ")
for s in students:
    print(s)