import sys
import os


lista = [0,1,2,3,4]
nome = sys.argv[1::]
def ola():
    print('ola')
print(sys.argv)
if nome[0] == '--help':
      ola()
elif nome[0] == 'adm':
        os.startfile('notepad.exe')