exam1 = int(input("Enter Total number of working days: "))
exam = int(input("Enter Total number of days absent: "))
total_working_days= exam1-exam
percentage= (total_working_days/exam1)*100
print("Attendance Percentage: ",percentage,"%")
if percentage<75:
     print("You are not elibible to write the exam")
     
else:
        print("You are eligible to write the exam")             