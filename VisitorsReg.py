from additionalFile import *

person = Worker()

print("Welcome to Visitors Registration form")
employer = Recruiter()
employer.putData()

mathes = matchedSkills(employer, person)

putDataIntoFile(employer.nameOfCompany, employer.email, employer.experience, employer.degree, mathes)
