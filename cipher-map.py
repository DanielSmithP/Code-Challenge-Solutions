""" Write a module that enables the robots to easily recall their passwords through codes when they return home.

The cipher grille and the ciphered password are represented as an array (tuple) of strings.

Input: A cipher grille and a ciphered password as a tuples of strings.

Output: The password as a string. """

def recall_password(cipher_grille, ciphered_password):
    final_answer = []
    index = 0
    
    while index <= 3:
        positions = get_positions(cipher_grille)
        for dictionary in positions:
            for key, value in dictionary.items():
                final_answer.append(ciphered_password[key][value])
        cipher_grille = rotate_grille(cipher_grille)
        index += 1
    print("".join(final_answer))
    return "".join(final_answer)
    
def get_positions(cipher_grille):
    answers = []
    for position, line in enumerate(cipher_grille):
        for index, character in enumerate(line):
            if character == 'X':
                answers.append({position : index})
    return answers
    
def rotate_grille(old_g):
    new_grille = []
    index = 0
    for line in old_g:
        new_line = "{}{}{}{}".format(old_g[3][index], old_g[2][index], old_g[1][index], old_g[0][index])
        new_grille.append(new_line)
        index += 1
    
    return new_grille

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
