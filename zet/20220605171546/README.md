# Beginner Boost Week 4

* Console é o que usamos para acessar fisicamente a máquina
* Terminal é o que usamos para acessar remotamente uma máquina (ex. ssh)

1. File System

* o diretório home é o diretório onde ficam armazenadas as pastas dos
  usuários do sistema. 
* Um usuário, normalmente, não possui as mesmas permissões que o usuário
  root. Para realizar certas ações o usuário precisa elevar suas
  permissões utilizando o comando sudo (caso tenha acesso a este comando
  pertença ao grupo dos `sudoers`.
* `<permissões usuário><permissões grupo><permissões outros>`
* `r(4)` - Leitura
* `w(2)` - Escrita
* `x(1)` - Execução 
* `[permissões] [usuario] [grupo]` 

# Comandos

* `ip -c a` - Endereço IP
* `mv <foo> <other>` - Move um arquivo ou pasta. Também é utilizado para
  renomear um arquivo ou pasta.
* `cp <foo> <other>` - Copia um arquivo ou pasta para outro diretório. O
  novo arquivo terá uma timestamp diferente da do arquivo original.
* `cp -ar <foo> <other>` - Faz uma cópia dos aquivos e mantém a timestamp do arquivo original.
* `scp <foot> <target>:` - Copia um arquivo ou pasta de forma remota para outro sistema.
* `pwd` - exibe o caminho.
* `cd` - muda de diretório.
* `ls` - lista arquivos.
* `ls -lha` - lista aquivos incluindo arquivos ocultos.
* `ls -ld` - lista as permissões do diretório atual.
* `stat <foo>` - Lista os detalhes de um inode.
* `chmod` - Comando para alterar as permissões de um arquivo.
* `sudo passwd <user>` - Muda a senha de um usuário.
* `passwd` - Mudar a própria senha.
* `sudo adduser <user>` - Adiciona um novo usuário.
* `sudo deluser <user>` - Remove um usuário.
* `sudo rmdir <foo>` - Remove um diretório se estiver vazio.
* `sudo rm -rf <foo>` - Remove um arquivo ou diretório, mesmo que
  contenha arquivos.
* `grep <foo>` - Busca em um arquivo pelo conteúdo especificado.
* `file <foo>` - 

## Relacionado

* https://picoctf.org
* `man 5 passwd`

Tags:  

    #linux #sistemadearquivos #filesystem
