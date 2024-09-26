import os
import math
# os.path.getsize e os.stat para dados dos arquivos


def formata_tamanho(tamanho_em_bytes: int, base: int = 1024) -> str:
    """ formata um tamanho, de bytes para o tamanho aprorpiado """
    if tamanho_em_bytes <= 0:
        return '0B'
    abreviacao_tamanhos = 'B', 'KB', 'MB', 'GB', "TB", "PB"
    # math.log vai retornar o logaritmo do tamanho_em_bytees
    # com a base (1024 por padrao) isso deve bater
    # com o nosso indice na abreviacao dos tamanhos
    indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base))
    # por quanto nosso tamanho deve ser dividido para
    # gerar o tamanho correto
    potencia = base ** indice_abreviacao_tamanhos
    # nosso tamanho final
    tamanho_final = round(tamanho_em_bytes / potencia, 2)
    # a abreviacao que queremos
    abreviacao_tamanho = abreviacao_tamanhos[indice_abreviacao_tamanhos]
    return f'{tamanho_final} {abreviacao_tamanho}'


# print(formata_tamanho(4353545354))
caminho3 = os.path.join('C:/', 'Users', 'Administrador', 'Downloads', 'doc')
for root, dirs, files in os.walk(caminho3):
    for files_ in files:
        caminho_completo = os.path.join(root, files_)
        tamanho = os.path.getsize(caminho_completo)
        print(f'arquivo: {files_} Tamanho: {formata_tamanho(tamanho)}')
