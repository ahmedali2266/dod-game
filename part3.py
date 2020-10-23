print('welcome to Multipication APP')
print ('Please Enter THE  First Number and last Number of Multipicaion table')
start=int(input('Enter The frist number of table : '))
end=int(input('Enter The last number of table : '))

for r in range(start,end+1):
    for t in range(1,13):
        print(r, 'X' ,t,'=',r*t)
    print('___________________________')
