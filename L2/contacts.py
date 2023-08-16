import csv

def add():
    name = input('Enter your name: ')
    number = input('Enter your number: ')
    with open('contacts.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name, number])

def show():
    with open('contacts.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)


def dele():
    print('Enter the name of the record you want to delete: ')
    name = input()
    with open('contacts.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        records = list(reader)

    with open('contacts.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in records:
            if row[0] != name:
                writer.writerow(row)
                print('The record was successfully deleted.')

def Mod():
    print('Enter the name of the record you want to modify: ')
    name = input()

    with open('contacts.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        records = list(reader)
        for row in records:
            if row[0] == name:
                number = input('Enter the new number for the user:')
                row[1] = number
                print('The record was successfully modified.')
                break
    with open('contacts.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(records)
    


'''
#Create a CSV file for first time
with open('contacts.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'Number'])
'''

a = 'add a contact'
m = 'modfiy a contact'
d = 'delet a contact'
sh = 'show the contacts '
e = 'exit'

print ( '1-' + a+' or '+'2-'+m +' or ' + '3-'+ d  +' or ' + '4-'+ sh +' or ' + '5-'+ e)
s = input('choesse : ')
if int(s) == 1:
    add()
elif int(s) == 2:
    Mod()
elif int(s) == 3:
    dele()
elif int(s) == 4:
    show()
elif int(s) == 5:
    exit
else :
    print ("that is not option")




