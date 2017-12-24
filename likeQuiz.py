print("It looks strange, but ...")

myName = ['Vladyslav', 'Vlad']
mySex = 'Male'
myTechnologies = ['Python', 'C++', 'STL', 'Qt', 'SQL', 'Html', 'CSS', 'Django', 'Flask']


print("So, maybe you can tell something about yourself =) ")
name = str(input("What's your name: "))
sex = str(input("Who are you? Boy|Girl: "))
technologies = str(input("What's your favorite technology: "))

for a in range(len(myName)):
    if name == myName[a]:
        print("Cool, we have a same names!")
        pass
    pass
for a in range(len(myTechnologies)):
    if technologies == myTechnologies[a]:
        print("Hmm, {tech} good choise ".format(tech = myTechnologies[a]))
        pass
    pass
