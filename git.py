import csv
import schedule
import time

# def record(name, age):
#     with open('catalog.csv', 'a+') as f:
#         writer = csv.writer(f, delimiter='/')
#     writer.writerow((name, age))
# con = input('con?  ')
# while con == 'yes':
#     record(input(), int(input()))



def write_csv():
    name = input('Enter name: ')
    age = input('Enter age: ')
    with open('users.csv', 'a') as f:
        writer = csv.writer(f, delimiter='/')
        writer.writerow(
            (name, age)
        )
    answ = input('Continue? y or n : ')
    if answ == 'y':
        write_csv()
    else:
        print('stop!')

write_csv()

def mailing():
    with open('users.csv', 'r') as f:
        data = f.readlines()
        names = [i.replace('\n','') for i in data]
        for i in names:
            name = i.split('/')
            if int(name[-1]) >= 18:
                print(f'Скидки сегодня! {name[0]}')

schedule.every(3).second.do(mailing)

while True:
    schedule.run_pending()
    time.sleep(1)

