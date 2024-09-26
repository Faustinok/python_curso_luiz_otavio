import os
# o os oferece funcionalidades para trabalhar como  o sistema operacional
print('a' * 80)
print('a' * 80)
os.system('powershell.exe clear')
print('a' * 80)
print('a' * 80)
os.system('powershell.exe clear')
caminho = os.path.join('D:\\', 'cursos', 'teste.txt')
print(caminho)
diretorio, arquivo = os.path.split(caminho)
caminho_arquivo, extensao_arquivo = os.path.splitext(arquivo)
print(caminho_arquivo, extensao_arquivo)
print(os.path.exists('D:/cursos'))
print(os.path.abspath('.'))
# caminho2 = os.system('powershell.exe pwd')

# os list dir
os.system('powershell.exe clear')
caminho2 = os.path.join('C:/', 'Users', 'Administrador', 'Downloads')
# print(caminho2)
# C:\Users\Administrador\Downloads\doc
for item in os.listdir(caminho2):
    # vou mostrar so oq e pasta com excessao da pasta doc
    if not os.path.isdir(os.path.join(caminho2, item)):
        continue
    print(item)
    if item == 'doc':
        print('#'*80)
        for iten in os.listdir(os.path.join(caminho2, item)):
            print(iten)
        print('#'*80)

os.system('powershell.exe clear')
caminho3 = os.path.join('C:/', 'Users', 'Administrador', 'Downloads', 'doc')
for root, dirs, files in os.walk(caminho3):
    print('pasta atual', root)
    for dir_ in dirs:
        print(' ', 'dir: ', dir_)
    for files_ in files:
        print(' ', 'file: ', files_)
        # deleta os arquivos
        if root == 'C:/Users/Administrador/Downloads/doc/raissa 2':
            caminho4 = 'C:/Users/Administrador/Downloads/doc/raissa 2'
            os.unlink(os.path.join(caminho4, files_))
