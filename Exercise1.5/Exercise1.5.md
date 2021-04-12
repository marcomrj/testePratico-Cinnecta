# Exercício 1.5

### _1. O que são os valores 112 e 835.128.600 exibidos na saída?_
##### R: Os valores exibidos no output são os tamanhos dos respectivos objetos em bytes, sendo os mesmos obtidos através da função `getsizeof()` do módulo `sys`.



### _2.Qual o conteúdo armazenado em v1_all_squares_to_100000000 (linha 2) e v2_all_squares_to_100000000 (linha 3), respectivamente?_
##### R: O conteúdo armazenado em `v1_all_squares_to_100000000` é um objeto proveniente do gerador *Ex* `<generator object <genexpr> at 0x7f78ccbf7b50>` , caso o conteúxo seja chamado com a função `next()` um "yield" retornará o primeiro valor armazenado ao quadrado, e a cada chamada do "next()" irá retornar o valor seguinte, até acabarem as ações do gerador. Já na variável `v2_all_squares_to_100000000` será retornada uma lista que contém todos os valores antigamente alocados agora elevados ao quadrado, mantendo os índices.




### _3.Considerando  que  se  deseje  fazer  a  soma  de  todos  os  números  quadrados  entre  1  e  100.000.000.000  qual das duas abordagens você escolheria?  Por quê?_
##### R: Eu escolheria a primeira abordagem, por meio de um gerador. Devido ao método que o mesmo utiliza, diferente de funções um gerador não armazena em memória todos os objetos gerados a partir da mesma, ele realiza a função e armazena apenas o valor gerado até que seja solicitado o pŕoximo `next()` poupando recursos de memória e do hardware.

