# os + shtil - mover copiar e apagar arquivos
# mover/ renomear -> shutil.move
# mover / renomear -> os.rename
# copiar -> shutil.copy
# apagar -> os.unlink
# apagar diretorio recursivamente -> shutil.rmtree
import os
import shutil
HOME = 'C:/Users/Administrador/Downloads'
doc = os.path.join(HOME, 'doc')
pasta_from = os.path.join(doc, 'raissa')
pasta_to = os.path.join(doc, 'raissa2')
# print(pasta_from)
os.makedirs(pasta_to, exist_ok=True)
for root, dirs, files in os.walk(pasta_from):
    for dir_ in dirs:
        caminho_dest_dir = os.path.join(root.replace(
            pasta_from, pasta_to), dir_)
        os.makedirs(caminho_dest_dir, exist_ok=True)
    for file in files:
        caminho_orig = os.path.join(root, file)
        caminho_dest = os.path.join(root.replace(pasta_from, pasta_to), file)
        shutil.copy(caminho_orig, caminho_dest)
# para copiar a pasta inteira no lugar de ir arquivo por arquivo
shutil.copytree(pasta_from, pasta_to)
# apagar pasta recursivamente
shutil.rmtree(pasta_to, ignore_errors=True)
# renomear arquivo ou pasta
shutil.move(pasta_from, pasta_from + 'novo')
