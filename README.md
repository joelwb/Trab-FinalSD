# Trab-FinalSD

O trabalho da disciplina de *SD (Sistemas Distribuídos)*, do curso de graduação de Bacharelado de Sistema de Informação do IFES - Serra, pelo docente Dr. Maxwell Eduardo Monteiro.

### Informações gerais
- **Autores**: Antônio Carlos, Harã Heique, Joel Will, Nicolas Sampaio
- **Linguagem de programação**: Python (versão 3.6.8+)
- **Ferramentas de suporte**: kafka-python (versão 1.4.7)
- **Ambiente de desenvolvimento**: Visual Studio Code (versão 1.35.1+)

o *DynagentX* é uma adaptação padrão do [AgentX](http://www.networksorcery.com/enp/protocol/agentx.htm) com intuito de atender aos requisitos de uma [SD-WAN](https://www.cisco.com/c/pt_br/solutions/enterprise-networks/sd-wan/what-is-sd-wan.html). É um framework adaptável e flexível, onde seus principais componentes são:
- A plataforma principal *DynagentX*;
- OSGiSnmpMasterAgentX (função de mestre);
- OSGiSnmpSubAgentX (consome serviços do mestre);
- DynagentX remoto.

O trabalho consiste na implementação de um simples sistema *DynagentX* com a utilização e apoio da tecnologia [*Apache Kafka*](https://kafka.apache.org/) implementada na linguagem de programação *Python*. 

### Apache Kafka
[*Apache Kafka*](https://kafka.apache.org/intro) é uma plataforma distribuída, logo um sistema distribuído, de mensagens e streaming. Basicamente seu funcionamento é:
1. O chamado *producer* é responsável por produzir o recurso chamado *message*;
2. A *mensagem* é armazenada/anexada em uma estrutura chamada *topic*, o qual este agrupa as mensagens;
3. O chamado *consumer* é reponsável por consumir as mensagens produzidas presentes nos *topics*.

Logo caso necessite mover e transformar um considerável volume de dados em tempo real entre diferentes sistemas, o *Apache Kafka* pode atender essa demanda.

<figure>
    <img src="https://github.com/joelwb/Trab-FinalSD/blob/master/images/Esquema_kafka_funcionamento-2.png?raw=true" alt="Funcionamento do kafka" title="Workflow básico de funcionamento do Kafka" />
</figure>

Alguns links sobre a tecnologia estão logo abaixo:
- [Documentação](https://kafka.apache.org/documentation/)
- [Post sobre](https://medium.com/@gabrielqueiroz/o-que-%C3%A9-esse-tal-de-apache-kafka-a8f447cac028)

### Descrição geral
A estrutura da aplicação está definida da seguinte maneira:

```
Trab-FinalSD
    |_ README.md
    |_ images
    |_ diagrams
    |_ src
        |_ handler_master.py
        |_ handler_slaves.py
        |_ simple_main.py
        |_ models
            |_ Master.py
            |_ Slave.py
```

#### Descrição geral dos arquivos
Descrição geral dos principais arquivos contidos nesta aplicação:

Arquivo|Path|Descrição
---|---|---
**Master.py**|src/models/Master.py|É uma classe resposável por agir como o coordenador da aplicação tendo o conhecimento de todos os slaves instanciados na aplicação.
**Slave.py**|src/models/Slave.py|Classe responsável por representar o coordenado pelo mestre da aplicação. Possui um identificador e um dado status definindo se está em funcionamento ou não, o qual fornece essa informação ao Master, quando este requer.
**handler_master.py**|src/handler_master.py|É o módulo que é buildado e executa a instancia do objeto da classe Master. Nele há um método responsável por perguntar ao operador (usuário) se deseja saber sobre o funcionamento de um determinado slave da aplicação.
**handler_slaves.py**|src/handler_slaves.py|É um módulo responsável por realizar inicializar os slaves baseado nas propriedades passado como argumento via terminal no momento de ser buildade, no caso seu ID e nome respectivamente. No momento que o slave é criado é mostrado suas principais informações, assim como o horário de sua instância e quando ele foi requisitado pelo seu mestre.

#### Modelagem estrutural (Diagrama de Classes)

#### Modelagem comportamental (Diagrama de Sequências)

### Como executar?
Para executar a aplicação o app no ambiente Linux basta seguir os seguintes passos:

1. Primeiramente é necessário realizar o download do server *Kafka* e iniciá-lo manualmente. Para fazer o download basta clica neste [link](https://kafka.apache.org/quickstart) e seguir o *step 1*;
2. Após isso basta abrir o terminal bash no local em que foi baixao o arquivo e descompactá-lo e entrar no diretório do arquivo descompactado:

        $ tar -xzf kafka_2.12-2.3.0.tgz
        $ cd kafka_2.12-2.3.0

3. No diretório execute o comando abaixo para startar o servidor *ZooKeeper*:

        $ bin/zookeeper-server-start.sh config/zookeeper.properties

4. No mesmo diretório abra outro terminal bash e execute o seguinte comando abaixo para startar o servidor *Kafka*:

        $ bin/kafka-server-start.sh config/server.properties

5. Antes de inicializar a aplicação deve checar se contém *kafka-python*, que permite manipular o *Kafka* através da linguagem Python. Execute os seguintes comandos:

        $ sudo apt install python3-pip
        $ pip3 install kafka-python

6. Para buildar/executar o app no ambiente Linux, onde a linguagem é Python, que geralmente já vem instalado nativamente, basta abrir o CLI (Command Line Interface) no diretório __/src__ da aplicação e executar o seguinte comando para inicializar o server:

        $ python3 handler_server.py
        
7. Para cada slave que se deseja criar é nessário abrir um novo terminal, sendo necessário passar como argumento o ID e o nome do slave respectivamente, como é mostrado abaixo. Lembrando que o nome do slave é opcional.

        $ python3 handler_slaves.py id_do_slave [nome_do_slave]
    
__OBS.:__ Importante ressaltar que também pode se criar um ambiente virtual e instalar as dependências definidas no passo 5 e seguir os mesmos passos adiantes.

### Informações adicionais
Todo o código fonte está hospedado no [GitHub](https://github.com/joelwb/Trab-FinalSD).
