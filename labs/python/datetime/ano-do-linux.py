from datetime import date


ano = date.today()

ano_do_linux = ano.replace(year=2023)

print(f'Em {ano} inicia-se o ano do linux')

print(f'caso de tudo errado o ano do linux se iniciará em {ano_do_linux}')
