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
    <img src="" alt="Funcionamento do kafka" title="Workflow básico de funcionamento do Kafka" />
    <figcaption>Workflow básico de funcionamento do Apache Kafka.</figcaption>
</figure>

Os principais links sobre a tecnologia estão logo abaixo:
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
**Master.py**|src/models/ExecutionType.py|É uma classe do tipo Enum utilizada no módulo de build.py da aplicação principal. Basicamente contém três tipos de valores que correspondem ao tipo de execução selecionada no módulo principal, os quais são: *MAIN, MAIN_WITHOUT_ARGS* e *RUN_ANALYSIS*.
**Slave.py**|src/models/Person.py|Classe responsável por representar a entidade Pessoa (Person em inglês). Nesta classe além de conter os atributos voltado ao escopo do trabalho. Também contém o método de comparação entre objetos desta classe chamado *compareTo()*. Basicamente ele compara se o objeto caller, que chama o método, é menor que o objeto passado como argumento, realizando esta comparação pela chave *uid*.
**handler_master.py**|src/build.py|É o módulo que é buildado e que contém a execução principal do programa. Além da execução principal, *main()*, também há outras formas de execução, onde um deles é voltado para testes internos do desenvolvedor sem utilização de comandos no terminal como é realizado na *main()*, o qual é chamado de *main_without_args()*. Já o outro é voltado para análise de um conjunto de dados de entrada chamado de *run_analysis()*. Ele que é responsável por realizar a chamada do script do módulo *analisys_person.py*.
**handler_slaves.py**|src/handler_person.py|É um módulo responsável por realizar a manipulação dos dados acerca dos objetos da classe Person. Logo todas as operações que envolvem leitura/escrita de arquivos, transformações dos dados unitários em objetos da classe Person, definições de configurações de execuções através da linha de comando, cálculos, impressões e afins. Ou seja, toda parte de lógica "hard code" está presente neste módulo, onde o *build.py* faz chamada de suas funções.

### Como executar?
Para buildar/executar o app no ambiente Linux, onde a linguagem Python geralmente já vem instalado nativamente, basta abrir o CLI(Command Line Interface) no diretório __/src__ e digitar o seguinte comando:

    $ python3 build.py --input arquivo_entrada.csv --output arquivo_saida.csv --algorithm identificador_algoritmo
    Ou
    $ python3 build.py --input arquivo_entrada.csv --output arquivo_saida.csv -a identificador_algoritmo
    Ou
    $ python3 build.py --input arquivo_entrada.csv --output arquivo_saida.csv

__OBS.:__ Importante ressaltar que o arquivo de entrada deve estar presente no diretório __/src/files/input__ e o arquivo de saída será gerado no diretório __/src/files/output__

Note que o nome dos arquivos tanto de entrada, precedidos de *--input*, quanto de saída, precedidos de *--output*, são **obrigatórios**. Caso não sejam passados será lançada uma exceção explicando formas de ser executada de maneira correta. Também há a possibilidade de utilização do comando abaixo que também fornecerá informações para o correto comando de execução do app.

    $ python3 build.py --help
    Ou
    $ python3 build.py -h

Já o identificador do algoritmo é um argumento **opcional** precedido de *-a*, quando abreviado, ou *--algorithm*, sem abreviação. Logo quando este parâmetro não é fornecido o **algoritmo de ordenação default é o Quicksort**. Quanto aos identificadores de algoritmo (*identificador_algoritmo*) podem ser utilizados os seguintes:


### Informações adicionais
Todo o código fonte está hospedado no [GitHub](https://github.com/joelwb/Trab-FinalSD).
