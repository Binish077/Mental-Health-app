#this code is for keeping a diary for the userw

Diary = []

class DiaryEntry:
    def __init__(self, month, day, year, action, sensation):
        super().__init__()
        self.month = month
        self.day = day
        self.year = year
        self.action = action
        self.sensation = sensation

def write_in_diary():
    print("Enter todays date")

    print("Month (ex May):")
    month = input('')
    print("Day (ex 21):")
    day = input('')
    print('Year (ex 2021):')
    year = input('')

    running = True
    while running:
        print('What did you do today? (ex I mowed the lawn)')
        action = input('')
        print('How did you feel? (ex Happy)')
        sensation = input('')

        Diary.append( DiaryEntry(month, day, year, action, sensation))

        while True:
            print('Did you do anything else today? Yes (y) No (n)')
            res = input('')
            if res == 'n':
                running = False
                break
            elif res == 'y':
                break
            else:
                print('Please enter a valid response')

def print_entry(entry):
    print(entry.month + " " + entry.day + ", " + entry.year + ':')
    print('What I did: ' + entry.action)
    print('I felt: ' + entry.sensation)

def view_diary():
    running = True
    while running:
        print('Please choose a day (ex May 21 2021), or a month (ex May 2021), or a year (ex 2021), or exit (done)')
        view_date = input("").split(" ")
        if view_date[0].isdigit() == True and len(view_date) == 1:
            for entry in Diary:
                if entry.year == view_date[0]:
                    print_entry(entry)

        elif  view_date[0].isalnum() == True and len(view_date) == 2:
            for entry in Diary:
                if entry.month == view_date[0] and entry.year == view_date[1]:
                    print_entry(entry)

        elif len(view_date) == 3:
            for entry in Diary:
                if entry.month == view_date[0] and entry.day == view_date[1] and entry.year == view_date[2]:
                    print_entry(entry)

        elif view_date[0] == 'done':
            running = False

def execute_diary():
    runnning = True
    while runnning:
        print("What would you like to do?")
        print("Write in diary (w), view diary (v), or exit diary (bye)")

        res = input('')

        if(res == 'w'):
            write_in_diary()
        elif(res == 'v'):
            view_diary()
        elif(res == 'bye'):
            runnning = False
