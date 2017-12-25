from time import gmtime, strftime
#====Initialization-of-worker-class============================================
class Worker:
    def __init__(self):
        self.fullName = "Vladyslav Zavedenski"
        self.nationality = "Poland"
        self.sex = "Male"
        self.age = 20
        self.degree = "Bachelor of computer science"
        self.experience = 1.5
        self.skills = ['Python', 'Django', 'Flask', 'C++', 'STL', 'Qt', 'SQL', 'Html', 'CSS']
        pass

    def info(self):
        print("Full Name    ==> ", self.fullName)
        print("Nationality  ==> ", self.nationality)
        print("Sex          ==> ", self.sex)
        print("Age          ==> ", self.age)
        print("Degree       ==> ", self.degree)
        print("Experience   ==> ", self.experience, "years")
        print("Technologies ==> ", self.skills)
        pass
    pass
#====Initialization-of-worker-class==END=======================================

#====Initialization-of-employer|recruiter-class================================
class Recruiter:
    def __init__(self):
        self.nameOfCompany  = "None"
        self.email          = "None"
        self.experience     = 0
        self.degree         = "None"
        self.skills         = []
        self.message        = "None"
        pass

    def putData(self):
        self.nameOfCompany  = str(input("Name of company: "))
        self.email          = str(input("Email for contact: "))
        self.experience     = float(input("Minimal professional experience (1.5 years format): "))
        self.degree         = str(input("Minimal degree: "))

        print("If you want to finish, Enter 'quit'. ")
        while True:
            skill = str(input("Enter required skill: "))
            if skill != 'quit':     self.skills.append(skill)
            else:   break

        self.message        = str(input("Enter some message (Not required): "))
        pass
    pass
#====Initialization-of-employer|recruiter-class==END===========================

#----Check-how-many-do-you-have-skills-matches---------------------------------
def matchedSkills(employer, person):
    mathes = 0
    for i in range(len(employer.skills)):
        for j in range(len(person.skills)):
            if employer.skills[i].upper() == person.skills[j].upper():
                mathes += 1
                pass
            pass
        pass
    return mathes
#----Check-how-many-do-you-have-skills-matches--END----------------------------

#----Take-a-values-from-Recruiter-class-and-put-them-into-file-----------------
def putDataIntoFile(company, email, experience, degree, matchedSkills):
    readFile = open("RegFile.txt", "a")
    readFile.write("\nDate of Registration form: {d} \n".format(d = strftime("%Y-%m-%d %H:%M:%S", gmtime())))
    readFile.write("Name of Company: {c} \n".format(c = company))
    readFile.write("Email for contant: {e} \n".format(e = email))
    readFile.write("Minimal professional experience: {ex} \n".format(ex = experience))
    readFile.write("Minimal degree: {deg} \n".format(deg = degree))
    readFile.write("Count of required skills: {m} \n".format(m = matchedSkills))
    readFile.close()
    pass
#----Take-a-values-from-Recruiter-class-and-put-them-into-file--END------------
