#this code asks the user for symptoms and gives a diagnosis
def stress():
    print("\nAre you experiencing aches and pains, headaches, and/or exhaustion? (Y/N)\n")
    s1=input("")
    if s1=="Y":
        print("\nYou may be experiencing stress")
        print("Symptoms also may include: Racing heart, weak immune systems, muscle tension, etc.")
    if s1=="N":
        depression()

def depression():
    print("\nAre you experiencing anger, emptiness, loss of interest and/or reduced concentration? (Y/N)")
    d1=input("")
    if d1=="Y":
        print("\nYou may be experiencing depression")
        print("Symptoms also may include: irritability, anxiousness, loss of appetite, feeling tired easily, etc.")
    if d1=="N":
        anxiety()

def anxiety():
    print("\nAre you experiencing difficulty concentrating, fatigue and exhaustion, sweaty palms, and/or shaking? (Y/N)")
    a1=input("")
    if a1=="Y":
        print("\nYou may be experiencing Generalized Anxiety Disorder")
        print("Symptoms also may include: irritability, muscle tension, difficulty sleeping, etc.")

print("Welcome to Symptom quiz\nPlease answer the questions below:")
stress()
print("You have reached the end of the quiz")
