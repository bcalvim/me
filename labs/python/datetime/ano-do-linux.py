from datetime import date
import sys
import platform


ano = date.today()
executavel = sys.executable
sistema = platform.uname()
ano_do_linux = ano.replace(year=2023)

print(f'Em {ano} inicia-se o ano do linux')

print(f'caso de tudo errado o ano do linux se iniciará em {ano_do_linux}')
print(f'Esse script de python esta sendo executado em {executavel} em um {sistema.system}')
