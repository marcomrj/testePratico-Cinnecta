![Logo Cinnecta](https://assets.website-files.com/5b8d55652232e200a00ede43/5d03ee1b35c4e126832eb9b1_cinnecta_logo_horizontal_icone_rgb_gradiente.png)
# 1 Python 🐍
## 1.1 
### Escreva  uma  função  que  dado  um  caminho  de  diretório  irá  retornar  duas listas,  uma  lista  com  os  arquivos  deste  diretório  e  outra  lista  com  os  donos desses arquivos, ambas na mesma ordem.

## 1.2 
### Agora, tomando a lista de nomes de arquivos e a lista de donos de arquivos (do item  1.1),  escreva  uma  função  que  agrupe  os  arquivos  pelo  dono,  retornando um  dicionário  com  a  lista  de  arquivos  de  cada  dono.

## 1.3
### Um certo sistema precisa de um módulo validador de senhas, esta ao receber uma string (a senha) e uma lista com os requisitos desta, retorna a informação se  a  senha  é  válida  ou  não.   A  lista  de  requisitos é composta  pelas  seguintes entradas:
VALORES  |  PARÂMETROS
---------|-------------------------------------------------------------------------------------
Primeiro | LEN (Comprimento da senha) ,LETTERS (# de letras) , NUMBERS (# de números) ,SPECIALS (# de caracteres especiais)
Segundo  |< , > , ==
Terceiro | Um número inteiro

Escreva um script em Python3 puro para resolver esse problema e a unidade de testes para validá-lo.

## 1.4
### Escreva uma função em Python 3 para  contar o número  de  itens  em um arquivo que satisfaçam uma dada condição. O arquivo contém apenas números inteiros, separados por espaço, sem qualquer ordenação ou padronização. Então, mostre como usar sua  função para contar a quantidade de números ímpares no arquivo.]
##### Template para função
~~~Python
def count_if(file_name,condition):
  # Você consegue implementar usando apenas duas linhas de código?
~~~
## 1.5
### Dado o código Python 3 abaixo e sua respectiva saída de terminal, responda:
##### Código:
~~~Python
1. Import sys
2. v1_all_squares_to_100000000 = ( i * i for i in range(1,100000001))
3. v2_all_squares_to_100000000 = [ i * i for i in range(1,100000001)]
4. v1s = sys.getsizeof(v1_all_squares_to_100000000)
5. v2s = sys.getsizeof(v2_all_squares_to_100000000)
6. print(f'{v1s}\n{v2s}')
~~~
##### Saída:
```
112
835128600
```
##### 1. O que são os valores 112 e 835.128.600 exibidos na saída?
##### 2. Qual o conteúdo armazenado em v1_all_squares_to_100000000 (linha 2) e v2_all_squares_to_100000000(linha 3), respectivamente?
##### 3. Considerando  que  se  deseje  fazer  a  soma  de  todos  os  números  quadrados  entre  1  e  100.000.000.000  qual das duas abordagens você escolheria?  Por quê?

# 2 Banco de Dados 📥
### 2.1
#### Exiba todos os nomes de pares de empregados cujo salário do primeiro da lista é menor do que o segundo. Cada  linha  deverá  conter  dois  nomes:  nome1  e  nome2  separado  por  um  espaço  (nesse  caso  o  salário  de nome  1 é menor que o de nome  2).
##### Basicamente, para cada empregado você deve imprimir a lista de todos os outros cujo salário seja menor do que o dele, faça isso usando SQL.
###### Tabela de funcionários
  CAMPO    |    TIPO
-----------|----------------
 ID(PK)    |   int          
 Nome      |   char(20)     
 Idade     |   int          
 Endereço  |   char(40)     
 Salário   |   decimal(18,2)