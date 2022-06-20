# Entendendo Administração de Servidores

Servidores existem para servir. Os dados que eles servem incluem páginas da
web, arquivos, email e diversos outros tipos de conteúdo. Alguns dos desafios
que um administrador de servidores encontrarão são:

1. **Acesso Remoto** Servidores tipicamente são localizados em ambientes com
   temperatura e acesso controlados e raramente possuem um ponto de acesso
local, obrigando seus administradores a acessá-los remotavamente, via SSH
(Secure Shell). 

1. **Segurança diligente** Para ser útil um servidor precisa atender a requisições
   de conteúdo de alguém que o acessa remotamente. Para manter o servider
seguro é necessário que eu administrador mantenha aberta apenas as portas
necessárias pra prover o serviço, mantendo todas as portas desncessárias
fechadas, assim mitigando os pontos de vulnerabilidade. Algumas ferramentas
utilizadas são *iptables* e *firewalld*

1. **Monitoramento contínuo** Um servidor precisa ficar disponível 24x7 365 dias
   por ano, por isso é necessário configurar ferramentas de monitoramento para
armazenar dados sobre o funcionamento do servidor e, caso necessário, notificar
a equipe de manutenção devido algum comportamento atípico.

Tags: 
 
    #linux #servidores
