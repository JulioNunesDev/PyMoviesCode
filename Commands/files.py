import os

drive = 'C:'
users = '\\Users\Julio Nunes'
dir = 'Desktop\\'
caminho = os.path.join(drive, users, dir)
print(caminho)
os.chdir(caminho)
print(os.getcwd())
# Read 'r'
# Write 'w'
# Append 'a'
#with open(caminho + 'teste.txt', 'w', encoding='utf-8') as arq:
# arq.write('testa')
print(os.listdir(caminho))
def init():
        nome_pasta  = input('Digite nome pasta:>> ')
        texto = input('Digite mensagem:>> ')
        ext = input('Digite extensao:>> ')
        modo = input("Digite modo> 'a, r, w' :>> ")
        criando_files(nome_pasta, texto, ext, modo)

def criando_files(nome_pasta, texto, ext, modo):

    with open(caminho + str(f'{nome_pasta}.') + ext, modo, encoding='utf-8') as arq:
                   arq.write(f'\n{texto}')

init()


