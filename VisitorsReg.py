
fullName = 'Vladyslav Zavedenski'
Age = 20
Sex = 'Male'
myTechnologies = ['Python', 'C++', 'STL', 'Qt', 'SQL', 'Html', 'CSS', 'Django', 'Flask']
#опыт

print("Welcome to Visitors Registration form")
print("If you are looking for workers, please fill this field.")

date = str(input("Please enter date (dd/mm/yy): "))
company = str(input("Name of company: "))
email = str(input("Email for contact: "))
experience = float(input("Minimal professional experience (1.5 years format): "))
degree = str(input("Minimal degree: "))
mathes = 0
skills = []
while True:
    print("If you want to finish, Enter 'quit'. ")
    skill = str(input("Enter necessary skill: "))
    if skill != 'quit':
        skills.append(skill)
    else:
        break

for i in range(len(skills)):
    for j in range(len(myTechnologies)):
        if skills[i] == myTechnologies[j]:
            mathes += 1


openFile = open("RegFile.txt", "a")
openFile.write("Date of Registration form: {d} \n".format(d = date))
openFile.write("Name of Company: {c} \n".format(c = company))
openFile.write("Email for contant: {e} \n".format(e = email))
openFile.write("Minimal professional experience: {ex} \n".format(ex = experience))
openFile.write("Minimal degree: {deg} \n".format(deg = degree))
openFile.write("Count of required skills: {m} \n".format(m = mathes))
openFile.close()
