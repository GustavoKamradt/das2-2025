# Design e arquitetura de Software
Aluno: Gustavo Kamradt

# Aula 27/02/2025

## Consistência nos Trade off

É difícil fazer decições sem grandes custos, no entanto, a consistência nas decições 
para o desenvolvimento mais eficiente do programa deve ser prioridade, mesmo 
que isso implique na redução do leque de ferramentas dos seus desenvolvedores. 

## Durabilidade 
É crucial a persistência de informação, mas a persistência de dados sacrífica desempenho. 

## Escalabilidade
A facilidade da escalabilidade de um programa é essencial, para serem evitados 
gargalos logísticos e altos custos, quando forem exigidos mais recursos do programa.

## Automatização do ambiente de trabalho 
A implementação de soluções automáticas para problemas previsíveis, como, por exemplo: 
um serviço fora do ar. Isso pode ser resolvido por rotinas automátizadas, evitando 
assim custos maiores.

## Infraestrutura
A padronização e modularidade das ferramentas num projeto reduz a sua complexidade
gerando um ambiente muito mais fácil de realizar manutenções e ‘updates’.

IAC ou 'infrastructure' as code', é um conceito que gira em torno de facilitar
o acesso a funções vitais de um projeto, criando rotinas automatizadas para evitar
situações como, por exemplo, a queda de um servidor.

# Aula 06/03/2025

## Recursos são descartáveis

Uma vez que os recursos se tornam descartáveis, esses podem ser substituídos por outros,
Por exemplo: digamos que o servidor da empresa caiu, caso haja backups do banco de dados,
basta dar reboot no servidor com um backup.

Outra alternativa é a possibilidade de um bando de dados secundário, que entra em ação
assim que o banco de dados principal para de funcionar.

## Crie serviços, não servidores

Soluções serverless ou containers, como o S3, evitam a responsabilidade de cuidar diretamente de um 
servidor, uma vez que os dados estariam rodando em uma nuvem.

## NoSQL

A escalabilidade de banco de dados relacionais tradicionais é limitado quanto a
escalabilidade horizontal, pois não são feitos para serem dinâmicos. Com modelos 
de bancos de dados NoSQL, essas limitações tornam-se mais generosas, embora 
sejam mais caros de se manter.

## Otimizar gastos

Por que deveríamos sustentar uma quantidade além do necessário para manter um serviço? Na verdade, não devemos,
assim como não devemos reduzir o tamanho de um servidor ao ponto de gerar excesso de processos nas máquinas.

## Segurança

Mesmo com os melhores antivirus disponíveis no mercado, não há garantias que os nossos dados estarão 100% seguros.
Manter-se atento a pontos fracos na segurança de um serviço é critico para evitar problemas

## Local zones AWS

Local zones podem ser utilizadas para abrigar acesso a serviços AWS em lugares distantes das regiões de grande 
densidade populacional e tecnológica.

# Aula 10/03/2025

## AWS shared responsibility model

Quando conectado com o servidor EC2, a infraestrutura global é de responsabilidade da AWS, no entanto, em caso
de violação da segurança do servidor, a culpa é inteiramente da equipe que integrou o servidor à rede AWS.

## Server side Encryption

- SSE-C é uma forma de encriptação onde o usuário da AWS envia a chave de encriptação com o servidor para a rede.
- SSE-S3: é o modelo padrão para criptógrafar conteúdo da AWS, onde a AWS fornece a chave de encriptação.

## Pilares do design de segurança

- Implemente uma forte segurança de identidade
- Proteger dados em trânsito e descanso (HTTPS)
- Afastar as pessoas do banco de dados
- Mantenha a rastreabilidade dos dados
- Prepare-se para eventos de segurança (ter uma equipe de segurança 24/7)
- Automatize as melhores praticas de segurança

## Política de Permissões para o usuário

Autenticidade pode ser garantida caso o servidor saiba 3 tópicos sobre o usuário: o que sabe, o que é e o que tem.


