# Habilitando rastreamento de dependência

1. Go gerencia as dependências através do módulo do seu código.
1. Esse módulo é definido pelo arquivo go.mod.
1. go.mod permanece em seu código, incluindo o código fonte.
1. Para habilitar o rastreamento de dependência em seu código rode `go
   mod init` dando um nome para o módulo. Esse nome será o path do
   módulo.
1. Nesse exemplo usaremos `go mod init example/hello`
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
