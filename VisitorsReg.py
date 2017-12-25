from additionalFile import *
#Initialization of classes objects
person = Worker()
employer = Recruiter()

print("Welcome to Visitors Registration form")
employer.putData()                              #Put some data as employer/recruiter
mathes = matchedSkills(employer, person)        #Chech mathes about required skills
putDataIntoFile(employer.nameOfCompany, employer.email,
                employer.experience, employer.degree, mathes)   #Write into file
