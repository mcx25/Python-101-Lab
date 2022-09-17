print('Welcome to Flarsheim Guesser!')
decision='y'
while decision == 'Y' or decision =='y':
#while statement for the users decision to continue or not

    remainder_1=1
    remainder_2=1
    remainder_3=1
#This line of code is asking user for input of a number
    print('Please think of a number between and including 1 and 100.\n')

#While and if statements for the remainder divided by 3
    remainder_1=int(input('What is the remainder when your number is divided by 3 ?'))
    while remainder_1 < 0 or remainder_1 >=3:
        if remainder_1 < 0:
            print('The value you entered must be greater that or equal to 0')
        elif remainder_1 >= 3:
            print('The value entered must be less than 3')

        remainder_1 = int(input('What is the remainder when your number is divided by 3 ? '))
#While and if elif statements for the remainder divided by 5
        remainder_2 = int(input('What is the remainder when your number is divided by 5 ? '))
    while remainder_2 < 0 or remainder_2 >= 5:
        if remainder_2 < 0 :
            print('The value entered must be 0 or greater')
        elif remainder_2 >= 5 :
            print('The value entered must be less than 5')
        remainder_2 = int(input('What is the remainder when your number is divided by 5 ?'))
#While and if elif statements for the remainder divided by 3  
    remainder_3 = int(input('What is the remainder when your number is divided by 7 ? '))
    while remainder_3 < 0 or remainder_3 >= 7:
        if remainder_3 < 0 :
            print('The value entered must be 0 or greater')
        elif remainder_3 >= 7 :
            print('The value entered must be less than 7')
        remainder_3 = int(input('What is the remainder when your number is divided by 7 ?'))

    for i in range(1,101):
        if i%3 == remainder_1 and i%5 == remainder_2 and i%7 == remainder_3:
            print('Your number was',i)
            print('How amazing is that? \n')
#User decision to continue or not
    decision= input('Do you want to play again? Y to continue or N to quit')
    while decision != 'Y' and decision != 'N' and decision != 'y' and decision != 'n':
        decision=input('Do you want to play again? Y to continue or N to quit')
                        
        
