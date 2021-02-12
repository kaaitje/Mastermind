def combinations(elementenlijst, lengte):
    """
    This function creates a list with all the posible combinations using a list with elements
    and the lenght a combination has to be
    :param elementenlijst: list with strings
    :param lengte: int
    :return: list with strings (sorted alphabeticaly)
    """
    # bron https://www.hackerrank.com/challenges/itertools-product/problem
    import itertools as it
    allecombinaties = []

    for j in it.product(elementenlijst, repeat=lengte):
        allecombinaties.append(j)

    return sorted(allecombinaties)


def simple_algorithm(possible_combos, feedback, guess):
    """
    Simple function that checks what combinations match the feedback
    :param possible_combos: list
    :param feedback: string
    :param guess: string
    :return: list
    """

    from Mastermind.functies_feedback import auto_feedback
    possible_combos_new = []
    for possibility in possible_combos:
        if auto_feedback(guess, possibility) == feedback:
            possible_combos_new.append(possibility)
    return possible_combos_new
