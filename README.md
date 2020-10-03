# DF-Bus

**Número da Lista**: 2<br>
**Conteúdo da Disciplina**: Grafos 2<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 16/0133505  |  Lucas Gomes Silva |
| 19/0134623  |  Marcos Diego da Silva Gomes |

## Sobre 
O projeto tem como objetivo utilizar o conceito de grafos no ambiente de transporte coletivo na região do Distrito Federal. Através de dados coletados, com relação ao valor das passagens de ônibus no DF, será apresentado ao usuário o caminho com o menor custo para se chegar ao destino desejado, dado o lugar de origem. O caminho é definido através da utilização do algoritmo de Dijkstra.

## Screenshots
#### Tela inicial
![start_screen](images/start_screen.png)
#### Opções
![options](images/options.png)
#### Resultado
![result](images/result.png)

## Instalação 
**Linguagem**: Python<br>
É necessário ter instalado o **Python** e o **pip** para executar o projeto (é recomendado utilizar um ambiente virtual para instalar e executar o projeto).

- Para instalar o gerenciador de pacotes pip:<br>
    ``` sudo apt-get install python3-pip ```
    
- Clone o repositório:<br>
    ``` git clone https://github.com/projeto-de-algoritmos/Grafos2_DF-Bus ```

- Instale as bibliotecas necessárias:<br>
    ``` pip install -r requirements.txt ```

## Uso 
### Para executar o projeto
Após estar dentro da pasta do projeto e com todas as bibliotecas instaladas, existe os seguintes passos para visualização do projeto: <br>
1. Entre na pasta do projeto pelo terminal e rode o seguinte comando no terminal: <br>
    ``` python main.py ```

### Como usar
1. Na lateral direita selecione a origem e destino.
2. Clique no botão "Buscar".
3. Será apresentado no mapa as cidades da origem até o destino.




