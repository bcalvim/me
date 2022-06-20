# Habilitando rastreamento de dependência

1. Go gerencia as dependências através do módulo do seu código.
1. Esse módulo é definido pelo arquivo go.mod.
1. go.mod permanece em seu código, incluindo o código fonte.
1. Para habilitar o rastreamento de dependência em seu código rode `go
   mod init` dando um nome para o módulo. Esse nome será o path do
   módulo.
1. Nesse exemplo usaremos `go mod init example/hello`
1. Em uma situação de desenvolvimento real o path para o módulo seria,
   tipicamente, o repositório onde o código fonte estaria armazenado,
   como por exemplo `github.com/meumodulo`
1. Crie um arquivo chamado `hello.go`
1. Copie o código abaixo:
```go
package main

import "fmt"

func main() {
  fmt.Println("Hello, World!")
}
```
1. Rode o código com `go run .`
1. Nesse código declaramos o pacote main, que agrupa funções 
1. Importamos o pacote fmt que contém funções de formatação de texto,
   incluindo impressão no console(terminal). Esse pacote faz parte da
   biblioteca padrão do Go
1. A função main imprime no terminal a mensagem.
1. Podemos importar código feito por outra pessoa 
1. Nesse exemplo importamos o pacote `rsc.io/quote` da seguinte forma:
```go
pacage main

import "fmt"

import "rsc.io/quote"

func main() {
  fmt.Println(quote.Go())
}
```
1. Depois de adicionar as linhas ao código original rode o comando `go
   mod tidy` para que os requisitos do módulo possam ser atendidos. Esse
   comando irá adicionar o módulo e criará um arquivo chamado `go.sum`
   que servirá para autenticar o módulo importado. 
1. Após podemos rodar novamente o programa com `go run .` obtendo uma
   mensagem diferente da anterior.
1. Outras funções que podem ser chamadas no lugar de `quote.Go()` são:
   `quote.Glass()`, `quote.Hello()` e `quote.Opt`. 

Referências:  
https://go.dev/doc/tutorial/getting-started  
https://pkg.go.dev/rsc.io/quote  

Tags:  
    #go
