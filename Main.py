from Mastermind.functies_simple_strategy import *
from Mastermind.functies_feedback import *
from Mastermind.Knuth import *

play_again = 'yes'
# Simple interface using prints, explains the rules and shows the options.
while play_again == 'yes':
    ''' interface gedeelte'''
    print('rules:'
          '\n======================================================================='
          '\nThe rules of mastermind are simple'
          '\nYou can choose from six different colors to make your combination thats four long'
          '\nThe computer tries to guess your code, your job is to provide the correct feedback'
          '\nA white peg is placed if the code contains the color but is in the wrong position'
          '\nA black peg is placed for each code peg from the guess which is correct in both color and position.'
          '\nColors to chose from are Red (r), Blue (b), Yellow (y), Orange (o), Green (g), Purple (p).'
          '\nExample code looks like: rryo'
          '\n======================================================================='
          '\nOptions:'
          '\n======================================================================='
          '\nOption 1: Choose a code and the computer guesses using my own strategy 1, worst case strategy '
          '\nOption 2: Choose a code and the computer guesses using implementation 2, The simple strategy algorithm'
          '\nOption 3  Choose a code and the computer guesses using implementation 3 eigen implementatie'
          '\n======================================================================='
          '\nChoose: 1, 2 or 3')

    option = input('Make a choice:')
    colors = ['r', 'b', 'y', 'o', 'g', 'p']

    # Deze optie zou gebruik moeten maken van de worst case strategie maag ik kom er niet uit. Wel een opzetje gemaakt
    # maar moet nog de functie die er bij hoort maken.
    if option == '1':
        code = input('input your code')
        combos = combinations(colors, 4)
        possible_combos = combinations(colors, 4)
        unused_combos = combinations(colors, 4)
        first_guess = ('r', 'r', 'b', 'b')
        feedback = (0, 1)
        for turn in range(11):
            if feedback != (0, 4):
                if turn < 10:
                    print(turn)
                    if turn <= 0:
                        feedback = manual_feedback(first_guess, code)
                        possible_combos = simple_algorithm(possible_combos, feedback, first_guess)
                        unused_combos.remove(first_guess)

                    else:
                        guess = worst_case(possible_combos, unused_combos)
                        feedback = manual_feedback(guess, code)
                        unused_combos.remove(guess)
            else:
                print('The computer did not guess the code,'
                      '\nWant to play again?\n')
                play_again = input('Type yes else reply with no: ')

    # option 2 makes use of the simple strategy algorithm.
    elif option == '2':
        code = input('input your code')
        combos = combinations(colors, 4)
        possible_combos = combos
        feedback = (0, 1)
        for turn in range(11):
            print(len(possible_combos))
            if turn < 10:
                guess = possible_combos[0]
                manual_feedback(guess, code)
                feedback = auto_feedback(guess, code)
                possible_combos = simple_algorithm(possible_combos, feedback, guess)
                if feedback == (0, 4):
                    print('The computer guessed the code,'
                          '\nWant to play again?\n')
                    play_again = input('Type yes else reply with no: ')
                    break

            else:
                print('The computer did not guess the code,'
                      '\nWant to play again?\n')
                play_again = input('Type yes else reply with no: ')

    # Option 3 this is a combination of the simple and worst case strategy, it makes the best first gues
    # then it goes over to simple strategy
    elif option == '3':
        code = input('input your code')
        combos = combinations(colors, 4)
        possible_combos = combinations(colors, 4)
        unused_combos = combinations(colors, 4)
        first_guess = ('r', 'r', 'b', 'b')
        feedback = (0, 1)
        for turn in range(11):
            if feedback != (0, 4):
                if turn < 10:
                    print(turn)
                    if turn <= 0:
                        feedback = manual_feedback(first_guess, code)
                        possible_combos = simple_algorithm(possible_combos, feedback, first_guess)
                    else:
                        guess = possible_combos[0]
                        feedback = manual_feedback(guess, code)
                        possible_combos = simple_algorithm(possible_combos, feedback, guess)
            else:
                print('The computer guessed the code,'
                      '\nWant to play again?\n')
                play_again = input('Type yes else reply with no: ')
                break
    else:
        print('This is not the correct input')
