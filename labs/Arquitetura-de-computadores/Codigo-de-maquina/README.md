# O código de máquina

## Linguagens de alto nível

1. Facilita o desenvolvimento de software.
1. Permite uso de linguagem humana no desemvolvimento .
1. Não é entendida pelo computador, precisando ser `traduzida` por um `compilador`.

## Linguagem de máquina

1. É a linguagem entendida pelo computador.
1. É um código binário (sequências de 0 e 1, que indicam se a presença de corrente(1) ou se a ausência de corrente(0)) 
1. Cada 0 e 1 equivalem a hum bit.
1. Um bit(**binarydigit**) é a menor unidade possível para o armazenamento de informação.
1. Um grupo de 8 bits (8b) equibale a 1 byte (8B).

# Compilador

1. É o programa que traduz o código para o código de máquina.
1. O compilador interpreta o código com o um texto simples e identifica plavras chaves e gera o código novo em linguagem de máquina.
1. O processo é semelhante a tradução de um livro.
1. Normalmente programas de alta performance são escritos em linguagem compiladas. 
1. Compiladores geram arquivos que podem ser rodados em computadores com os mesmos componentes do computador que compilou o código.
1. Exemplos de linguagens compiladas: C/C++, Java, Rust, Go.

`Rust e Go, e outras linguagens modernas, apesar de serem compiladas, podem ter seus códigos rodados em Just In Time Compilation, que é uma maneira de executar o código, sem a necessidade de compilar, para realizar testes`

`Java, apesar de ser compilado, roda em uma máquina virtual, chamada de Java Virtual Machine (JVM), dessa forma seus binários podem ser rodados em qualquer computador que tenha uma versão compatível instalada`

# Interpretador

1. Similar ao compilador, porém não gera um arquivo novo.
1. O interpretador traduz o código para código de máquina e imediatamente transfere o conteúdo traduzido para ser executado pelo computador.
1. É semelhante a um interprete que traduz simultaneamente o que um estrangeiro está falando. 
1. Programas interpretados são de desenvolvimento mais rápido, porém tem execução relativamente mais lenta.
1. Códigos em liguagens interpretadas podem ser rodados em qualquer computador que tenha a mesma linguagem instalada (na mesma versão ou versão suportada).
1. Exemplos de linguagens interpretadas: Python, Ruby, JavaScript. 