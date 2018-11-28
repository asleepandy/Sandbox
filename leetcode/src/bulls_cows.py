"""
for example:

Secret number:  "1123"
Friend's guess: "0111"
In this case, the 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow,
and your function should return "1A1B".
1122, 2211
1122, 1222
011, 110
"""


def getHint(secret, guess):
    """
    :type secret: str
    :type guess: str
    :rtype: str
    """
    secret = list(secret)
    guess = list(guess)
    bulls = 0
    cows = 0
    is_cows = []
    for n in range(len(guess)):
        if guess[n] == secret[n]:
            secret[n] = '-'
            guess[n] = '-'
            bulls += 1

    for n in range(len(guess)):
        if guess[n] != '-' and guess[n] in secret and secret.count(guess[n]) > is_cows.count(guess[n]):
            cows += 1
            is_cows.append(guess[n])

    return '{0}A{1}B'.format(bulls, cows)
