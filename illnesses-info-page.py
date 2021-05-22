#Illness information and cures page

class Illnesses:
    def __init__(self,choice,name=None,definition=None,source=None,symptoms=None,cure=None):
        self.choice=choice
        self.name=name
        self.definition=definition
        self.source="American Psychiatric Association"
        self.symptoms=symptoms
        self.cure=cure

        if self.choice=='a':
            self.depression()

        if self.choice=='b':
            self.anxiety()

        if self.choice=='c':
            self.ocd()

    def depression(self):
        self.name="Depression"
        self.definition="Depression causes feelings of sadness and/or a loss of interest in activities you once enjoyed. It can lead to a variety of emotional and physical problems and can decrease your ability to function at work and at home."
        self.symptoms="Sadness, loss of interest, change in appetite, feeling worthless or guilty, difficulty thinking, etc."
        self.cure="Medication such as antidepressants, psychotherapy, self help through things such as regular exercise and good quality sleep"


    def anxiety(self):
        self.name="Generalized Anxiety Disorder"
        self.definition="Generalized anxiety disorder involves persistent and excessive worry that interferes with daily activities."
        self.symptoms="Restlessness, feeling on edge or easily fatigued, difficulty concentrating, muscle tension, etc."
        self.cure="Psychotherapy, medications (to allieviate symptoms), joining support groups, lowering caffiene intake, etc."

    def ocd(self):
        self.name="Obsessive-compulsive disorder (OCD)"
        self.definition="Obsessive-compulsive disorder (OCD) is a disorder in which people have recurring, unwanted thoughts, ideas or sensations (obsessions) that make them feel driven to do something repetitively (compulsions)."
        self.symptoms="Obsessions (recurring and persistent thoughts, impulses, and images), Compulsions (repetitive behaviors or mental acts that a person feels driven to perform in response to an obsession) "
        self.cure="Cognitive Behavioral Therapy, medication such as SSRI's, self care, etc."


    def __str__(self):
        s=self.symptoms
        c=self.cure
        d=self.definition
        statement=(str(self.name)+"\n----------------------------------------------------\n")
        statement=statement+"\nDefinition: "+str(d)+"\n\nSymptoms: "+str(s)+"\n\nTreatment: "+str(c)+"\n\nSource: "+str(self.source)
        statement=statement+"\n\n------------------------------------------------------\n"
        return statement

print("Welcome to the Illnesses Information Page")
print("What illness would you like to know more about? (Select one)")
print("a) Depression")
print("b) Generalized Anxiety Disorder (GAD)")
print("c) Obsessive-compulsive disorder (OCD)")
while True:
    answer=""
    collect=input("Enter your choice below (a, b, or c) PRESS ENTER TO QUIT: ")

    if collect=="":
        print("\nThank you for using the Illnesses information page")
        break

    elif collect=='a' or collect=='b' or collect=='c':
        answer=Illnesses(str(collect))
        print("\n"+str(answer))

    else:
        print("Please enter a valid input")
