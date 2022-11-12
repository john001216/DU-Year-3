import os
import sys
import CBFtfidf

print('+---------------------------------------------------+')
print('|                                                   |')
print('| Hi! Welcome to \'Durham Movie Recommender System\'! |')
print('|                                                   |')
print('+---------------------------------------------------+\n')

usersPool = ['1','2','3','4','5','6','7','8','9']

def r_u_new_user():
    QnewUser = input('Are you new to this system? ([y]/[n]): ')

    if QnewUser == 'n':
        exsisting_user()
    elif QnewUser == 'y':
        new_user()
    else:
        print('  --> if \'yes\' type \'y\', if \'no\' type \'n\'')
        r_u_new_user()

def exsisting_user():
    user_id = input('  --> userID: ')
    print('+---------------------------------------------------+')
    print('                Welcome back [', user_id, ']!')
    print('+---------------------------------------------------+')
    print('\n')
    print('        +-----------------------------------+')
    print('        |              MENU                 |')
    print('        |    1. Make a move recommendation  |')
    print('        |    2. Update my profile           |')
    print('        +-----------------------------------+\n')
    menu_choice = input('[1]/[2]: ')
    if menu_choice == '1':
        print('Finding movies for you...') ## call RS functions
        CBFtfidf.to_CBF('2001: A Space Odyssey (1968)')
    elif menu_choice == '2':
        print('        +-----------------------------------+')
        print('        |           User Profile            |')
        print('        |        1. Seen Movie              |')
        print('        |        2. My Ratings              |')
        print('        |        3. My Tags                 |')
        print('        +-----------------------------------+\n')
        profile_choice = input('[1]/[2]/[3]: ') ## call profile page
        print(type(profile_choice))

def new_user():
    new_id = input('  --> set new ID: ')
    if new_id in usersPool:
        print('Exsisting user ID! Set again...')
        new_user()
    else:
        print('+---------------------------------------------------+')
        print('Thank you for registering [', new_id,']!')
        print('+---------------------------------------------------+')
        usersPool.append(new_id)
        QsetProfile = input('Set user profile! ([y]/[later]): ')
        if QsetProfile == 'y':
            print('user profile page') ## call profile page
        elif QsetProfile == 'later':
            print('Set user profile asap to get accurate recommendation')
        # else:
        #     print('  --> if \'yes\' type \'y\', if \'later\' type \'later\'')

# def user_profile(k):
#     if k == 'profile setting':


r_u_new_user()