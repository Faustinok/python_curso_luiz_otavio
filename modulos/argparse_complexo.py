from argparse import ArgumentParser

parser = ArgumentParser()
# quando vc passar um argumento na execucao, devera passar o valor tipo -b 123
parser.add_argument('-a', '--nome_longo',
                    help='descricao do argumento',
                    # type=str tipo do argumento ,
                    # metavar='SRTINGS',
                    # default='qualquer coisa',
                    required=True,
                    # action='append', # recebe o argumento mais de uma vez
                    # nargs= '+' # recebe mais de um valor
                    )
parser.add_argument('-v', '--verbose',
                    help='mostra logs', action='store_true'
                    # store_true vai dizer falso ou verdadeiro se informado
                    )
args = parser.parse_args()

if args.nome_longo is None:
    print('Argument -a is necessary')
    print(f'default argument : {args.nome_longo}')
else:
    print(f'muito bom seu merdinha, valor de a: {args.nome_longo}')
