total_classes=int(input("Enter total number of classes : "))
attented_classes=int(input("Enter number of attended classes : "))

attendance=(attented_classes/total_classes)*100

if attendance>=75:
    print(f"Attendance is {attendance}% You're allowed for Semister Exam")
else:
    print(f"Attendance is {attendance}% You're not allowed for Semister Exam")