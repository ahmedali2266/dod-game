print('The Game will take several number and print the summ and Average og them')

count=int(input('how many numbers would you like to sum '))

cornt_count=0
summ=0
while cornt_count < count:
    number=float(input('Enter the number: '))
    summ +=number
    cornt_count +=1

print('Summ of all numbers = ',summ)
print('Avarage of all numbers = ',summ/count)
