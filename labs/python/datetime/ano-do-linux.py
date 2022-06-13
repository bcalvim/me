from datetime import date
import sys
import platform


ano = date.today()
executavel = sys.executable
sistema = platform.uname()
ano_do_linux = ano.replace(year=2023)

if sistema.system == 'Windows':
    print('Estranho, estamos rodando num Windows')
elif sistema.system == 'Linux':
    print('Eba, estamos em um Linux')
else:
    print(f'Estamos rodando em um {sistema.system}')

print(f'Em {ano} inicia-se o ano do linux')

print(f'caso de tudo errado o ano do linux se iniciará em {ano_do_linux}')
