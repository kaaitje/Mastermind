def auto_feedback(guess_list, code):
    """
    This function gives automated feedback, its used to check the given feedback.
    :param guess_list: list
    :param code: string
    :return: tuple
    """
    correct_color = 0
    correct_place = 0
    temp_guess_list = []
    temp_code = []
    # Check for black pins
    for i in range(0, len(guess_list)):
        if guess_list[i] == code[i]:
            correct_place += 1
            tmp = code[i]
            temp_guess_list.append(tmp)
            temp_code.append(tmp)

    guess_list_2 = [x for x in guess_list if x not in temp_guess_list]
    code_2 = [x for x in code if x not in temp_code]
    # Check for white pins
    for i in range(0, len(guess_list_2)):
        if guess_list_2[i] in code_2:
            correct_color += 1
    return correct_color, correct_place


def manual_feedback(guess_list, code):
    """
    This function asks the player for feedback and checks it using the feedback function
    :param guess_list: list
    :param code: string
    :return: tuple
    """
    while True:
        try:
            print(guess_list[0], guess_list[1], guess_list[2], guess_list[3])
            right_color = int(input("How many are colors are in the code but on the wrong spot? "))
            right_place = int(input("How many colors were guessed spot on? "))
            if auto_feedback(guess_list, code) != (right_color, right_place):
                print("The feedback you gave is incorrect. ", auto_feedback(guess_list, code))
            else:
                return right_color, right_place
        except ValueError:
            print("Sorry, you gave the wrong input try again.")

