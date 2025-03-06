# Design e arquitetura de Software
Aluno: Gustavo Kamradt

# Aula 27/02/2025

## Consistência nos Trade off 

É dificil fazer decições sem grandes custos, no entanto a consistência nas decições 
para o desenvolvimento mais eficiente do programa deve ser prioridade, mesmo 
que isso implique na redução do lenque de ferramentas de seus desenvolvedores. 

## Durabilidade 
É crucial a persistencia de informação, mas a persistencia de dados sacrifica performance. 

## Escalabilidade
A facilidade da escalabilidade de um programa é essencial, para que sejam evitados 
gargalos logisticos e altos custos, quando forem exigidos mais recursos do programa.

## Automatização do ambiente de trabalho 
A implementação de soluções automaticas para problemas previsiveis, como por exemplo: 
uma servido fora do ar. isso pode ser resolvido por rotinas automativas, evitando 
assim custos maiores.

## Infraestrutura
A padronização e modularidade das ferramentas dentro de um projeto reduz a sua complexidade
gerando um ambiente muito mais facil de realizar manutenções e updates.

## Recursos são discartavéis

Segue abaixo uma versão ampliada do artigo, com mais conteúdo sobre o que são as leis, explicações detalhadas e uma análise comparativa que demonstra como esses conceitos podem ser aplicados na programação concorrente.

---

# Leis de Amdahl e de Gustafson: Fundamentos, Comparação e Aplicações em Programação Paralela

## Resumo

A computação paralela busca reduzir os tempos de execução de algoritmos distribuindo tarefas entre vários processadores. Entretanto, mesmo algoritmos com grande potencial de paralelização apresentam partes sequenciais que impõem limites teóricos ao ganho de desempenho. As leis de Amdahl e de Gustafson fornecem modelos matemáticos para quantificar esses limites e guiar estratégias de implementação. Este artigo explora detalhadamente os fundamentos dessas leis, confronta suas premissas e discute como aplicá-las para otimizar a programação concorrente.

## 1. Introdução

Com o avanço da tecnologia, a utilização de sistemas com múltiplos processadores ou núcleos tornou-se comum. A programação concorrente permite que diferentes partes de um algoritmo sejam executadas simultaneamente, acelerando o tempo total de execução. No entanto, nem todo o algoritmo pode ser paralelizado. Por isso, compreender os limites teóricos e as oportunidades de ganho é essencial para a criação de soluções eficientes. Nesse contexto, as leis de Amdahl e de Gustafson surgem como ferramentas fundamentais para entender e mensurar o potencial de aceleração de algoritmos paralelos.

## 2. Fundamentos das Leis

### 2.1 Lei de Amdahl

#### 2.1.1 Conceito e Fórmula

Proposta por Gene Amdahl em 1967, a Lei de Amdahl assume que um programa pode ser dividido em duas partes:
- **Parte paralelizável:** Representada pela fração \( P \) do tempo de execução que pode ser distribuída entre múltiplos processadores.
- **Parte sequencial:** Representada por \( 1-P \), que deve ser executada de forma sequencial.

O ganho máximo (speedup) ao utilizar \( N \) processadores é dado por:

\[
S(N) = \frac{1}{(1-P) + \frac{P}{N}}
\]

Esta fórmula mostra que, mesmo que \( N \) seja muito grande, o speedup é limitado pelo termo \( (1-P) \). Por exemplo, se 90% do código for paralelizável (\( P = 0{,}9 \)), o ganho máximo será:

\[
S_{\text{máx}} = \lim_{N \to \infty} \frac{1}{(1-0{,}9) + \frac{0{,}9}{N}} = \frac{1}{0{,}1} = 10
\]

#### 2.1.2 Interpretação e Implicações

A Lei de Amdahl enfatiza que, para um problema de tamanho fixo, mesmo uma pequena fração sequencial limita o ganho total obtido com a adição de mais processadores. Esse modelo é muito útil para ilustrar o impacto das partes do algoritmo que não podem ser paralelizadas e para orientar esforços de otimização, pois sugere que a redução da fração sequencial é crucial para alcançar melhorias significativas.

### 2.2 Lei de Gustafson

#### 2.2.1 Conceito e Fórmula

Apresentada por John Gustafson em 1988, a Lei de Gustafson parte de uma perspectiva diferente: ao invés de considerar um problema de tamanho fixo, ela assume que o tamanho do problema pode ser aumentado com o número de processadores disponíveis. Dessa forma, a fração paralela do trabalho cresce, enquanto a parte sequencial permanece constante ou cresce de forma muito menor.

A fórmula proposta é:

\[
S(N) = N - \alpha (N-1)
\]

onde \( \alpha \) representa a fração do tempo de execução que é sequencial. Em termos práticos, se o problema for dimensionado de forma que a fração sequencial seja reduzida em termos relativos, o ganho de desempenho pode ser quase linear com o número de processadores.

#### 2.2.2 Interpretação e Implicações

A Lei de Gustafson demonstra que, em muitas aplicações reais – como simulações científicas e processamento de grandes volumes de dados – o problema pode ser escalado para aproveitar os recursos computacionais. Assim, ao aumentar o tamanho do problema, a porção paralela domina o tempo de execução, e o speedup pode se aproximar do número de processadores utilizados, mitigando o efeito limitador da fração sequencial.

## 3. Confronto e Análise Comparativa

### 3.1 Diferenças Fundamentais

- **Tamanho do Problema:**
    - *Amdahl:* Considera um problema de tamanho fixo, onde a fração sequencial é constante, independentemente dos recursos.
    - *Gustafson:* Permite o aumento do tamanho do problema, fazendo com que a porção paralela se expanda, e a fração sequencial tenha impacto menor.

- **Limite de Speedup:**
    - *Amdahl:* O speedup máximo é limitado por \( \frac{1}{1-P} \). Mesmo com um número infinito de processadores, se \( P \) não for 100%, haverá um teto no ganho.
    - *Gustafson:* O speedup pode se aproximar de \( N \) se o problema for escalado adequadamente, indicando ganhos quase lineares com o aumento de processadores.

### 3.2 Aplicações Práticas na Programação Concorrente

Na prática, a escolha entre os modelos depende do tipo de aplicação:

- **Aplicações com Dados Limitados:** Em sistemas onde o tamanho do problema não pode ser expandido (por exemplo, processamento de um conjunto fixo de dados), a Lei de Amdahl oferece uma estimativa realista dos ganhos possíveis e ressalta a importância de minimizar a parte sequencial do código.

- **Aplicações Escaláveis:** Em cenários como simulações, renderização de imagens ou análise de grandes volumes de dados, onde o problema pode ser aumentado com a disponibilidade de mais recursos, a Lei de Gustafson é mais aplicável. Ela incentiva o desenvolvimento de algoritmos que se beneficiem do aumento da carga de trabalho paralelizável, permitindo que o ganho de desempenho seja praticamente proporcional ao número de processadores.

### 3.3 Estratégias para Otimização

Para maximizar o desempenho em sistemas paralelos, os desenvolvedores devem:
- **Reduzir a Parte Sequencial:** Investir em otimizações que permitam que mais do código seja executado em paralelo, diminuindo \( 1-P \) na fórmula de Amdahl.
- **Dimensionar o Problema:** Em aplicações onde isso é possível, aumentar o tamanho do problema para explorar melhor os recursos disponíveis, conforme sugerido pela Lei de Gustafson.
- **Gerenciar Overheads:** Minimizar os custos de comunicação, sincronização e acesso à memória que podem reduzir os ganhos teóricos previstos.

## 4. Exemplos Ilustrativos

### 4.1 Exemplo com 90% de Paralelismo (Lei de Amdahl)

Suponha um algoritmo onde 90% do trabalho pode ser paralelizado (\( P = 0{,}9 \)). Utilizando 10 processadores, o tempo paralelo seria:

\[
T(10) = (1-P) + \frac{P}{10} = 0{,}1 + \frac{0{,}9}{10} = 0{,}1 + 0{,}09 = 0{,}19
\]

O speedup seria:

\[
S(10) = \frac{1}{0{,}19} \approx 5{,}26
\]
... (42 linhas)


