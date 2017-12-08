

def start(nice=0, mean=0, name=""):
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)


def describe_game(name):
    """
checks to see if its a new gamer or not
if its new, get user info
if not new, thank them for playing and continue"""
    if name != "": #if we dont already have player info, get it and start new game
        print('\nThank you for playing again, {}!'.format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input('\nWhat is your name? ').title()
                if name != "":
                    print ('\nWelcome {}!'.format(name))
                    print ('\nIn this game, you will be greeted by several different people, \nYou can choose to be nice or mean.')
                    print ('\nAt the end of the game, your fate will be influenced from your actions.')
                    stop = False
    return name

def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input('\nA stranger approaches you for a conversation.\nWill you be nice or mean? n/m:').lower()
        if pick == 'n':
            print ('\nThey smile, wave, and walk away...')
            nice = (nice + 1)
            stop = False
        if pick == 'm':
            print ('\nThe stranger glares at you, raises a fist and storms away...')
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) #passes variables to score

def show_score(nice,mean,name):
    print ("\n{}, you currently have ({}, Nice) and ({}, Mean) points.".format(name,nice,mean))


def score(nice,mean,name):
    #score function is passed the values stored in the next variables
    if nice > 5:
        win(nice,mean,name)
    if mean > 5:
        lose(nice,mean,name)
    else:
        nice_mean(nice,mean,name)

def win(nice,mean,name):
    print ("\nNice Job {}! you won! \nEveryone loves you and you live in peace!".format(name))
    again(nice,mean,name)

def lose(nice,mean,name):
    print ("\nOh no {}! You got stoned by the town...".format(name))
    again(nice,mean,name)

def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nLet's Play again? y/n: ".lower())
        if choice =='y':
            stop = False
            reset(nice,mean,name)
        if choice =="n":
            print("\nCome Back Soon!")
            stop = False
            exit()
        else:
            print("\nPlease enter 'y' for 'YES', 'n' for 'NO'...")

def reset(nice,mean,name):
    nice = 0
    mean = 0
    start(nice,mean,name)                   
                       

start()    
                       
                       
