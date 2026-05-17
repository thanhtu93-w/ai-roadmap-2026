students=[]
def add_student(name,score):
    student={
        "name":name,
        "score":score
    }
    students.append(student)
while True: 
    control=input("(press e and enter to end process) " \
    "1 to add student " \
    "2 to modify student info" \
    "3 to find highest score")
    if control == "e":
        break
    elif control == "1":
        name= input("Enter student name : ")
        score= int(input("Enter student score : "))
        add_student(name,score)
    elif control == "2":
        name= input("Enter student name : ")
        for s in students:
            if s["name"]==name:
                score= int(input("Enter student new score : "))
                s["score"]=score
                print("Student modified")
                break
            else:
                print("Student not found")
    elif control == "3":
        if len(students)==0:
            print("No student found")
            continue
        highest_score=0
        for s in students:
            if s["score"]>highest_score:
                highest_score=s["score"]
                highest_score_name=s["name"]
        print("Highest score:", highest_score, "Name:", highest_score_name)