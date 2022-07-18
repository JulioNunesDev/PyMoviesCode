import os
import sys

def perfunte():
    frase = input('>> ')
    teste(frase)


def teste(frase):
    try:
        platform = sys.platform
        if 'win' in platform:
            os.startfile(frase + '.exe')
        else:
            return False
    except FileNotFoundError:
        print('command invalid, try again')
        perfunte()

perfunte()

