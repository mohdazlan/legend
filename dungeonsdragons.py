print('''

                                        _                                    
 ____                                 _| |_    ____                          
|    \ _ _ ___ ___ ___ ___ ___ ___   |   __|  |    \ ___ ___ ___ ___ ___ ___ 
|  |  | | |   | . | -_| . |   |_ -|  |   __|  |  |  |  _| .'| . | . |   |_ -|
|____/|___|_|_|_  |___|___|_|_|___|  |_   _|  |____/|_| |__,|_  |___|_|_|___|
              |___|                    |_|                  |___|            

''')
print('Welcome to Dungeons & Dragons')

player_name = input('What is your name, adventurer\n')

health = 100
damage = 20

print('\nwelcome, ' + player_name + ' !you have ' + str(health) + ' health and can do damage ' + str(damage))
print('You came acress a dragon!! What will you do??')
print('1. Fight')
print('2. Run')
choice = int(input('Enter either 1 or 2: '))
if choice == 1:
    print("You attack the dragon and do " + str(damage) + ' damage')
    print('the dragon back off, spit some acid and does 10 damage')
    health -= 10
    print('Your current health is ' + str(health))
elif choice== 2:
    print('You run away from the dragon')
    print('live today for tomorrow')
    #dragon manage to throw rocks at you deals with twice the damage you inflict
    #print your current health
else:
    print('\nInvalid choice, the dragon get to eat you alive!!!')
print("Thanks for playing!")