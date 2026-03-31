print("Enter marks obtained in 5 different subjects: ")
math=int(input("Enter the marks for math: "))
english=int(input("Enter the marks for english: "))
science=int(input("Enter the marks for science: "))
history=int(input("Enter the marks for history: "))
music=int(input("Enter the marks for music: "))
total= math + english + science + history + music
avg=total/5

if avg >= 95 and avg <= 100:
    print("Your grade is A+")
elif avg >= 90 and avg < 95:
    print("Your grade is A-")
elif avg >= 85 and avg < 90:
    print("Your grade is B+")
elif avg >= 80 and avg < 85:
    print("Your grade is B")
elif avg >= 75 and avg < 80:
    print("Your grade is B-")
elif avg >= 70 and avg < 75:
    print("Your grade is C+")
elif avg >= 65 and avg < 70:
    print("Your grade is C")
elif avg >= 60 and avg < 65:
    print("Your grade is C-")
elif avg >= 55 and avg < 60:
    print("Your grade is D+")
elif avg >= 50 and avg < 55:
    print("Your grade is D")
elif avg >= 45:
    print("You failed!")
else:
    print("Invaild input!!!")