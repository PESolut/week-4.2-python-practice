from capitals import states


# init var to track guessed capitals
guessedCapitals = []

print('You need to guess all the capitals my guyza')

# flow of the app
# 1) check guessedCapitals to see if theres a need for a repsonse
    # if not; tell the user he won
# 2) prompt user to guess
# 3) check if theres any match between guess to each state within our DS
    # if so, remove that state from our list, add that capital to guessed capitals and keep the loop going
    # if not, tell the user hes wrong and restart the loop

#guard clause, check if guessedCapitals is full...
while 1:
    guessedCapitalsLen = len(guessedCapitals)

    if guessedCapitalsLen == 50:
    # tell the user he won.
        print('you won')
    # otherwise move on

    print('you guessed '+ str(guessedCapitalsLen) + ' capitals correct so far')
    guess = input("Please enter your Guess:")

    # we need to mutate the states dictionary so it does not include any object to which the capital key == currentElCap
    
    # for capital in states:
    #     currentElCap = (capital)
    #     print(currentElCap)
    #     if currentElCap in states:
    #         print('FLAG')
            # states = {key: val for key,
            #           val in states.items() if key != 'currentElCap'}
            
    # print(states)



