### DOD GAME Developed by AHMED ALI ###
class games:
    ###constructor code
    def __init__(self):
        print('welcome IN dod game Developed by AHMED ALI ')
        print('choose your game from our collection')
        print('press[1] : play Even_Odd Game')
        print('press[2] : play Sum_Average Game')
        print('press[3] : play Multipication Game')

        self.choices()



###########################################3
   ## available choices
    def choices(self):
        while True:
            user_choice=input('Enter your choice to play next game ... If you want to exit, enter C : ')
           # C capitall and c small to close the game 
            if user_choice == 'c':
               print('Thanks for trying, I hope you come back again  ( ˘ ³˘)♥')
               break
            elif user_choice == 'C':
                print('Thanks for trying, I hope you come back again  ( ˘ ³˘)♥')
                break
            
            try:
                user_choice=int(user_choice)
                if user_choice ==1:
                   self.Even_Odd_Game()
                elif user_choice ==2:
                     self.Sum_Average_game()
                elif user_choice==3:
                    self.Multipication_game()
                else:
                    print('please choice between 1 , 2, or 3 ')

            except ValueError:
                print('please Enter A valid number')

###########################################
   ## Even_Odd_Game code
    def Even_Odd_Game(self):
        print('welcome in the Even-odd Game  ')
        print('please Enter A Number...And I will tell you if it Even or odd')
        print('If YOU Wanna close the Game Enter X  ')

        while True:
            num=input('Enter A number:  ')
            if num == 'x':
               print('close the game ')
               print('Thanks ....')
               break

            try:
                num =int(num)

                if num % 2 ==0:
                    print('Even number ')

                else:
                    print('Odd number')

            except ValueError:
                print('place Enter A Valid Nnmber')

            print('-----------------------------------')

######################################################
    ##Sum_Average_gamen code
    def Sum_Average_game(self):
        
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



##########################################################
##Multipication_game code    
    def Multipication_game(self):
        print('welcome to Multipication APP')
        print ('Please Enter THE  First Number and last Number of Multipicaion table')
        start=int(input('Enter The frist number of table : '))
        end=int(input('Enter The last number of table : '))

        for r in range(start,end+1):
            for t in range(1,13):
                print(r, 'X' ,t,'=',r*t)
            print('___________________________')


#object from class
game1=games()  


# creat class
# methods - pass
# creat object from class
# bilud projects games
# add code constructor
# create choices method
# handling exception (!= charachter ,1 2 3)
# connect methods ---- choices
