email_list = ['test@email.com', 'test@yandex.ru', 'test@gmail.com']

if 'test@yandex.' in email_list:
    print ('Exist')
else:
    print ('Not exist')

#print all
numbers_list = [1,2,3,4,5]

for number in numbers_list:
    print number

#print just greater than 2
print('\n')


for number in numbers_list:
    if number > 2:
        print number
