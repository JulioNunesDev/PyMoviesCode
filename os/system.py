import os

## TRAS OS CAMINHOS
#sistema = os.environ
#print(sistema['USERNAME'])
#print(os.getcwd())

#Trabalhando com pastas

#novo_caminho = r'C:\Users\Julio Nunes\Documents'
### PARA MUDAR  O CAMINHO ATUAL
#os.chdir(novo_caminho)

### PARA LISTAR TODOS OS ARQUIVOS DENTRO DA PASTA OU DIRETORIO
##print(os.listdir())

## PARA CRIAR UMA PASTA
#os.mkdir('teste')

#########################################


### ABRINDO ARQUIVOS
#caminho = r'C:\Users\Julio Nunes\Documents'
#os.startfile(caminho)

### RENOMEIA UM ARQUIVO MAIS TEM QUE TER O CAMINHO EXATO
#os.rename()

### REMOVENDO ARQUIVOS
#os.remove()

### walk
#os.walk(os.getcwd())
### dirname
#os.path.dirname(os.getcwd())
### join
drive = 'C:'
usuario = 'Julio Nunes'
pasta_base = 'Documents'
caminho = os.path.join(drive,r'\Users', usuario, pasta_base)
os.chdir(caminho)
print(os.getcwd())