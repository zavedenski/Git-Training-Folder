print ("Hello, it's my third commit with git!")

myName = ['Vladyslav', 'Vlad']
mySex = 'Male'
myTechnologies = ['Python', 'C++', 'SQL']


print("So, maybe you can tell something about yourself =) ")
name = str(input("What's your name: "))
sex = str(input("Who are you? Boy|Girl: "))
technologies = str(input("What's your favorite technology: "))

for a in range(myName):
    if name == myName[a]:
        print("Cool, we have a same names!")
        pass
    pass
for a in range(myTechnologies):
    if technologies == myTechnologies[a]:
        print("I like {tech} too".format(tech == myTechnologies[a]))
        pass
    pass
