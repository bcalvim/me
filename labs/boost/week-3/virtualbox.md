# Como executar uma máquina virtual pelo terminal no windows

1. Configure seu path para que o executável esteja visível. Para isso
   basta acessar `settings>System>About>Advanced Settings>Environment
   Variables>Path>Edit>New and add C:\Program Files\Oracle\VirtualBox` 
1. Após adicionado abra um novo terminal e os commandos serão
   reconhecidos.

1. `vboxmanage startvm vmname --type headless` inicia uma máquina
   virtual em headless(sem interface gráfica no host)
