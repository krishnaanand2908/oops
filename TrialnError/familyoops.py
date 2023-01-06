import os
import fontstyle as fnt

class family:
    def __init__(self, name, age, sex, qualification, agepost):
        self.name = name
        self.age = age
        self.sex = sex
        self.quali = qualification
        self.gen = agepost

    def details(self):
        return f"NAME: {self.name}\nAGE: {self.age}\nSEX: {self.sex}\nQUALIFICATIONS: {self.quali}\nGENERATION: {self.gen}"


krishna = family("Krishna Anand", 14, "Male", "School Student", "Generation 3")
shivraj = family("Shivraj Anand", 20, "Male",
                 "College Student", "Generation 3")
rknani = family("Rajkumari Devi", 72, "Female", None, "Generation 1")
vk = family("Bandana Kumari", 45, "Female", "Office Assistant", "Generation 2")
pnc = family("Parmanand Choudhary", 72, "Male", "Owner of 'Choudhary General Store'", 'Generation 1')

members = {1: krishna,
           2: shivraj,
           3: rknani,
           4: vk,
           5: pnc,}

if __name__ == '__main__':
    os.system('cls')
    while 1:
        name = int(input(fnt.apply(
            "Enter:\n1 for Krishna\n2 for Shivraj\n3 for Rajkumari Devi\n4 for Bandana Kumari\n---> ", 'blue/bold')))
        print()
        try:
            member = members.get(name)
            print(fnt.apply(member.details(), 'green/bold'))
        except:
            print(fnt.apply('Some Error Occured! Please try again!', 'red.bold'))
        print()
