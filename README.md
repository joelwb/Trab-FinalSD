# Trab-FinalSD

O trabalho da disciplina de *SD (Sistemas Distribuídos)*, do curso de graduação de Bacharelado de Sistema de Informação do IFES - Serra, pelo docente Dr. Maxwell Eduardo Monteiro.

### Informações gerais
- **Autores**: Antônio Carlos, Harã Heique, Joel Will, Nicolas Sampaio
- **Linguagem de programação**: Python (versão 3.6.8+)
- **Ferramentas de suporte**: kafka-python (versão 1.4.7)
- **Ambiente de desenvolvimento**: Visual Studio Code (versão 1.35.1+)

DynAgentX bla bla bla... Kafka bla bla bla

### Apache Kafka
*Apache Kafka* é uma biblioteca do python capaz realizar:
- x
- y
- z
- w

Além dessas features existem muitas outras, porém o importante a ressaltar é que o intuito é poupar tempo e ser mais fácil na construção de parsers. Os principais links sobre ela estão logo abaixo:
- [Documentação]()
- [Github]()

### Descrição geral
A estrutura da aplicação está definida da seguinte maneira:

```
TPA-trab2-ordenacao
    |_ README.md
    |_ relatório.pdf
    |_ codes-references.txt
    |_ src
        |_ analisys_person.py
        |_ build.py
        |_ handler_person.py
        |_ sort_collection.py
        |_ files
            |_ input
                |_ *arquivos entrada*.csv
            |_ output
                |_ *arquivos saída*.csv
            |_ analyze
                |_ *arquivos saída dos testes da análise*.csv
        |_ models
            |_ ExecutionType.py
            |_ Person.py
```

#### Descrição geral dos arquivos
Descrição geral dos principais arquivos contidos nesta aplicação:

Arquivo|Path|Descrição
---|---|---
**ExecutionType.py**|src/models/ExecutionType.py|É uma classe do tipo Enum utilizada no módulo de build.py da aplicação principal. Basicamente contém três tipos de valores que correspondem ao tipo de execução selecionada no módulo principal, os quais são: *MAIN, MAIN_WITHOUT_ARGS* e *RUN_ANALYSIS*.
**Person.py**|src/models/Person.py|Classe responsável por representar a entidade Pessoa (Person em inglês). Nesta classe além de conter os atributos voltado ao escopo do trabalho. Também contém o método de comparação entre objetos desta classe chamado *compareTo()*. Basicamente ele compara se o objeto caller, que chama o método, é menor que o objeto passado como argumento, realizando esta comparação pela chave *uid*.
**build.py**|src/build.py|É o módulo que é buildado e que contém a execução principal do programa. Além da execução principal, *main()*, também há outras formas de execução, onde um deles é voltado para testes internos do desenvolvedor sem utilização de comandos no terminal como é realizado na *main()*, o qual é chamado de *main_without_args()*. Já o outro é voltado para análise de um conjunto de dados de entrada chamado de *run_analysis()*. Ele que é responsável por realizar a chamada do script do módulo *analisys_person.py*.
**handler_person.py**|src/handler_person.py|É um módulo responsável por realizar a manipulação dos dados acerca dos objetos da classe Person. Logo todas as operações que envolvem leitura/escrita de arquivos, transformações dos dados unitários em objetos da classe Person, definições de configurações de execuções através da linha de comando, cálculos, impressões e afins. Ou seja, toda parte de lógica "hard code" está presente neste módulo, onde o *build.py* faz chamada de suas funções.
**sort_collection.py**|src/sort_collection.py|É a biblioteca/módulo responsável por realizar a ordenação de coleções/vetores, ou como é chamado em python listas. Nele está presente sete algoritmos diferentes de ordenação que pode ser escolhido para se ordenar uma coleção/lista qualquer, dado que estes elementos da coleção devem implementar o método *compareTo*, como é o caso da classe Person. Os algoritmos de ordenação presentes são: selection sort, insertion sort, quicksort, mergesort, heapsort, introsort e timsort.
**analisys_person.py**|src/analisys_person.py|Arquivo que contém toda lógica do script de análise realizada acerca da performance de todos os sete algoritmos implementados. Ele que é responsável por fazer todo o processamento dos dados de entrada através da função *analyze*, onde é passado como argumento um caminho do diretório e gerado arquivos .csv de saída que são armazenados dentro do diretório */analyze*, os quais possuem os resultados obtidos do processamento prontos para serem analizados.
**arquivos entrada.csv**|src/files/input/arquivos entrada.csv|São os arquivos do tipo CSV que alimenta a entrada de dados da aplicação. Sempre que for realizada a execução da aplicação é passado o arquivo de entrada que deve estar presente no diretório /files/input.
**arquivos saida.csv**|src/files/output/arquivos saida.csv|São os arquivos de saída do tipo CSV representando o resultado do processamento ordenação realizado dos arquivos de entrada alimentados. Sempre que for realizada a execução da aplicação também é passado o nome do arquivo de saída que será criado no diretório /files/output. 
**arquivos saida analise.csv**|src/files/analyze/arquivos saida analise.csv|São também arquivos de saída do tipo CSV, porém diferente dos presentes no /output, eles são resultados de análises feitas no módulo *analisys_person.py*. São gerados três tipos de arquivos principais: primeiro são gerados vários arquivos, onde cada arquivo contém as 10 execuções com seu tempo de execução para todas as quantidades de registros(10 à 7500000). Segundo são gerados sete arquivos, onde cada um contém um nome de um algoritmo de ordenação implementado. Neles são contidos o tempo médio de execução da cada quantidade de registros(10 à 7500000), assim como seus valores máximos e mínimos. Por fim é gerado um arquivo final com todos os algoritmos, contendo seus tempos de execuções médio em cada quantidade de registro(10 à 7500000).

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
