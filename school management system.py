import json

# file where student records are stored; keep consistent
RECORDS_FILE = "students_records.json"

# load data from disk into the global list
try:
    with open(RECORDS_FILE, "r") as f:
        students_records = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    students_records = []

class Student:
#    contructor function for attributes
    def __init__(self ,Name,Grade,ID):
        self.Name = Name
        self.Grade = Grade
        self.ID= ID


class Student_manager:
    def __init__(self):
        # always load a read latest memory from file whenever student_manager function is called
        self.load_records()
    def load_records(self):
#    Reload the global `students_records` list from disk
        global students_records
        try:
            with open(RECORDS_FILE, "r") as f:
                students_records = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            students_records = []
    def add_student(self):
        # make sure we have the latest data before appending
        self.load_records()
        #split the data provided by user
        Name=input("student_name?")
        ID=input("student_id?")
        Grade=input("student_grade?").strip().upper()
        student=Student(Name,Grade,ID)
        #appending new data in file formatted
        students_records.append({"Name":student.Name, "ID":student.ID, "Grade":student.Grade})
        print(f"The student details\n Name = {student.Name}\n ID = {student.ID}\n Grade = {student.Grade} \n are added!")
        self.save_records()

    def view_records(self):
        self.load_records()
        if len(students_records) == 0:
            print("There are no records available at the moment")
        else:
            #get whole data from file in list with for loop
            for i, student in enumerate(students_records):
                print(f"{i+1}. ID={student['ID']} ,Name={student['Name']}, Grade={student['Grade']}")

    def delete_record(self):
        self.load_records()
        #check previous data
        if not students_records:
            print("no records available")
            return
        self.view_records()
        try:
            # if data is available take delete request and fulfill it
            delete_request = int(input("which one you wanna delete? provide num "))
            # valid choices are 1..len
            if 1 > delete_request > len(students_records): 
                print("invalid num!")
            else:
                #mkae sure you go on correct index 
                delete = students_records.pop(delete_request-1)
                print(f"deleted: {delete}!")
                self.save_records()
        except ValueError:
            print("must be num!")



    def update_records(self):
        self.load_records()
        if not students_records:
            print("no records available")
            return
        self.view_records()
        try:
            updation = int(input("which one you wanna update? provide num"))
            # valid index is 1..len(students_records)
            if 1 <= updation <= len(students_records):
                # remove old entry and collect new values
                students_records.pop(updation-1)

                name = input("Enter new name: ").strip()
                grade = input("Enter new grade: ").strip().upper()
                id = input("Enter new ID: ").strip()
            #insert new data to exact old index
                students_records.insert(updation-1, {"Name":name, "ID":id, "Grade":grade})
                self.save_records()
                print("record updated!")
            else:
                print("Provide existing num ")
        except:
            print("invalid request!")
         
        
    def save_records(self):
        # write current in‑memory list back to disk
        with open(RECORDS_FILE, "w") as f:
            json.dump(students_records, f)

def records():
    while True:
        print("WELCOME TO STUDENT MANAGEMENT SYSTEM")
        print("What would you like to do?")
        try:
            preference= int(input("1. add student\n2.delete student\n3. update student\n4. view all student records\n5. exit\nchoose num "))
        except:
            print("must be a num!")
        call=Student_manager()
        if preference==1:
            call.add_student()
        elif preference==2:
            call.delete_record()
        elif preference==3:
            call.update_records()
        elif preference==4:
            call.view_records()
    

if __name__ == "__main__":
    records()









