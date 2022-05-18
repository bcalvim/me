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
