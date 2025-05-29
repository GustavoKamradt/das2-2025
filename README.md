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
Por exemplo: digamos que o servidor da empresa caiu, caso haja 'backups' do banco de dados,
basta dar 'reboot' no servidor com um 'backup'.

Outra alternativa é a possibilidade de um bando de dados secundário, que entra em ação
assim que o banco de dados principal para de funcionar.

## Crie serviços, não servidores

Soluções serverless ou containers, como o S3, evitam a responsabilidade de cuidar diretamente de um
servidor, uma vez que os dados estariam a rodar numa nuvem.

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

## Pilares do 'design' de segurança

- Implemente uma forte segurança de identidade
- Proteger dados em trânsito e descanso (HTTPS)
- Afastar as pessoas do banco de dados
- Mantenha a rastreabilidade dos dados
- Prepare-se para eventos de segurança (ter uma equipe de segurança 24/7)
- Automatize as melhores praticas de segurança

## Política de Permissões para o usuário

Autenticidade pode ser garantida caso o servidor saiba 3 tópicos sobre o usuário: o que sabe, o que é e o que tem.

# Aula 13/03/25

## AWS configure

#### PowerShell

- ~aws configure
- Access key
- Secret access key
- us-east-1
- json

- cd .aws
- cat ./aws/credential
- aws ec2 describe-instances

## Grupos de usuários

Quando temos um servidor com poucos membros, é possível delimitar as permissões para cada usuário individualmente,
mas quando há um quantidade muito elevada, é necessário a utilização de grupos de usuários, possibilitando
definir permissões para cada grupo.

## Notas

- Princípio de privilégio mínimo: conceda ao usuário apenas o necessário para fazer a sua função, nada a mais, nada a
  menos.
  Habilitar MFA

## IMA roles

As 'roles' definem quais usuários podem assumir uma função determinada via uma credencial temporária.

# Aula 17/03

## Role-Based Access Control (RBAC)

Sistema que permite a utilização de 'roles' para simplificar a segurança e
facilitar a gestão de permissões.

## Identity based policies

Política de segurança linkada a um usuário,

## Resource based policies

Política de segurança linkada a recursos, ou seja, e3 sq, etc. pode ser usada para criar recursos como buckets,
tornando o acesso mais granular.

## Determining permissions at time of request

Quando o ocorre uma requisição da API na aws por um usuário, o IMA é responsável por identificar as permissões daquele
usuário, impedindo o acesso do usuário caso o mesmo não tenha as permissões necessárias. As permissões também podem ser negadas,
mesmo o usuário tem permissão para executar uma função, caso os parameter estabelecidos para que a permissão seja
efetiva
sejam violados

## Tipos de armazenamento

- Block storage (EBS): Os dados são armazenados num dispositivo por meio de blocos com tamanho fixo.
- File storage (EFS): Os dados são armazenados numa estrutura hierárquica
- Object storage (s3): Os dados são armazenadas como objetos baseados em atributos e metadados.

## AMAZON s3

- O Amazon s3 possui um armazenamento de até 5TB para cada objeto.
- Armazena documentos como objetos em bucket que você define.
- todo o objeto armazenado no s3 tem uma URL, o que não quer dizer que terá acesso a eles.
- Chance minima de perder objetos, devido à criação de 'backups' automáticos.
- armazena dados que podem ser usados para análises.
- Dá suporte com 'backups' e recuperação de desastres.
- é possível separar um objeto em objetos menores e dar 'upload' para o servidor de forma fragmentada.
- Provem segurança na transferência de arquivos, mesmo por longas distâncias.
- Não é possível alterar objetos na S3, caso seja necessário, deve-se baixar o arquivo, alterá-lo e então dar reupload
  no arquivo

# Aula 20/03/25

## AWS Transfer Family

O transfer Family é um serviço que serve para facilitar a transferencia de dados ao S3, podendo usar
protocolos FTP, FTPS e SFTP. Essa função é principalmente utilizada para evitar mudanças na
infraestrutura do servidor.

## Classes de armazenamento de objetos

- S3 Standard: Tem 'uploads' mais baratos, porém o preço de armazenamento é caro.
- S3 Intelligent-Tiering: Move os arquivos entre os modelos disponíveis conforme a frequência de acessos.
- S3 Standard-IA: ideal para objetos que não serão utilizados com tanta frequência.
- S3 One-zone-IA: ainda mais barato que o Standard-IA, porém mais devagar.
- S3 glacier Deep Arquive: armazenamento mais barato, porém é extremamente lento para movimentar os dados salvos aqui.
- S3 glacier Instant Retrieval: pouco mais caro que o Deep Archive, porém o 'download' de objetos é instantâneo.
- S3 outpost: gera uma nuvem privada ao cliente, porém perda a elasticidade da rede AWS.

# Aula 24/03/25

## S3 lifecycle

O S3 lifecycle refere-se a ações que Amazon AWS aplica para um grupo de objeto. Ações como a transitar um objeto entre
classes de armazenamento ou definição de data de expiração, dificilmente podem ser alteradas no futuro ou custarão
caríssimo.

## Versioning

É uma função que lhe permite salvar várias versões de um mesmo objeto, facilitando a realização de recuperação de dados
ou reverter ações, uma vez que desabilitando essa função, o objeto pode ser perdido para sempre.

## Cors

É recurso de segurança suportado pelo Amazon AWS, que permite definir restrições para operações HTTPs vindas de outros
sítes.

# Aula 27/03/25

## Cuidados

- cautela ao expor seus buckets na internet.
- usar pelo menos o servidor side encryption com o S3
- considerar qual região faz mais sentido a ser usada, considerando o custo e agilidade do acesso aos dados.

## S3 Inventory

O S3 Inventory auxilia a administração de espaço nos seus armazementos de dados, acelerando o 'workflow' da sua equipe.

# Aula 03/04/25

## categorias diferentes de Compute Service

Existem vários serviços oferecido pela AWS, como a possibilidade de criar maquinas virtuais, containers, funções
serverless, etc. por exemplo, o ec2 instance é uma máquina virtual que pode ser criada com o sistema operacional desejado, enquanto o ECS
é um serviço de container que pode ser utilizado para criar containers com a linguagem de programação desejada.

## Amazon AMI

A amazon AMI(Amazon machine image) é uma imagem de máquina virtual que pode ser utilizada para criar instâncias EC2, com
o sistema operacional desejado. A AMI pode ser criada com o sistema operacional desejado, além de outras configurações como o tipo
de armazenamento, etc. Não só isso, mas também tem a capacidade ser criada a partir de uma instância EC2 existente ou de
uma imagem de máquina virtual. A partir da imagem, o usuário é capaz de compartilhar a AMI com outros usuários, permitindo que eles
criem instâncias EC2 com a mesma configuração.

## Amazon EC2 instance

O Amazon EC2 é um serviço que simplifica a criação, o gerenciamento e a escalabilidade de AMIs. Esse automatiza o
processo de atualização das AMIs, tornando o processo mais rápido e eficiente. Além disso, o EC2 também permite a criação de
instâncias EC2 com diversas configurações de tipo de armazenamento.

## Amazon EBS

O Amazon EBS é um serviço de armazenamento em bloco que pode ser utilizado para armazenar dados de instâncias EC2. O EBS
é altamente escalável e pode ser utilizado para armazenar dados de forma persistente. Além disso, esse também permite a
criação de snapshots, que são cópias de segurança dos dados armazenados no próprio EBS, podendo serem utilizadas para restaurar os
dados armazenados em caso de falha ou perda de dados.

## Amazon EFS

O Amazon EFS é um serviço de armazenamento em arquivos que pode ser utilizado para armazenar dados de instâncias EC2. O
EFS é altamente escalável e pode ser utilizado para armazenar dados de forma persistente, podem comportar até petabytes de
dados.

# AULA 07/04/25

## Amazon EBS

O Amazon EBS é um serviço de armazenamento em bloco que pode ser utilizado para armazenar dados de instâncias EC2. Essa
forma de
armazenamento não perde os dados do EC2, mesmo que a instância seja parada ou encerrada, sendo ideal para armazenar
dados que
devem se manter persistentes.

## Amazon user data best practices

- Instanciar scripts manualmente, ao invés de automatizar o processo.
- Quando iniciado uma EC2 é possível escolher qual usuários vai executar o ‘script’, o que pode servir para evitar
  que o ‘script’ seja executado por um usuário não autorizado.

## Placement Strategies

- Cluster placement group: Coloca as instâncias num grupo de ‘cluster’, o que pode melhorar a latência entre as
  instâncias, mas pode ser mais prejudicial caso aconteça acidentes.
- Spread placement group: Coloca as instâncias em diferentes racks, o que pode melhorar a disponibilidade, caso seja
  necessário para programa que não devem cair.
- Partition placement group: Coloca as instâncias em diferentes partições, o que pode melhorar a disponibilidade.

## EC2 pricing

- On-demand: paga-se por hora, o que pode ser mais caro, mas é ideal para aplicações que não são utilizadas com
  frequência, como aplicações experimentais.
- Reserved: paga-se por um ano ou 3 anos, o que pode ser mais barato do que o On-demand, dependendo da aplicação que for
  ser usada.
- Savings plan: Paga-se por hora, é eficiente para aplicação com taxa de acessos bastante volátil, mas serve bem para
  qualquer tipo de aplicação.
- Spot: Paga-se por hora, e é o melhor custo beneficio para executar containers, devido aos generosos descontos.

# Aula 10/04/25

## Database

pontos a se considerar na hora de escolher um banco de dados:

- escalabilidade
- tamanho do armazenamento
- caraterísticas do banco de dados (latência, disponibilidade, etc.)
- durabilidade

### Banco de dados relacional x não relacional

- Relacional: mais fácil de trabalhar, mas menos escalável e possui a sua estrutura de dados restrita a tabelas.
- Não relacional: mais difícil de trabalhar, porém muito mais escalável, mais rapido e tem uma grande variedade de
  estruturas de dados.

## AMAZON Database options

- Amazon RDS: banco de dados relacional mais utilizado na AWS.
- Amazon Aurora: banco de dados relacional mais rápido da AWS. Aurora serveless é uma versão do Aurora que pode ser
  escalada automaticamente.
- Amazon DynamoDB: banco de dados não relacional mais escalável da AWS.
- Amazon ElastiCache: banco de dados não relacional mais barato da AWS.

# AULA 17/04/25

## Backup e recuperação de dados com o Amazon RDS

- Chaves de criptografia: são utilizadas para criptógrafar os dados armazenados no banco de dados, garantindo a
  segurança dos dados.
  podendo encriptar dados via AWS KMS ou AWS CloudHSM, dependendo do tipo de banco de dados utilizado.

## AMAZON dynamoDB

O Amazon DynamoDB é um banco de dados não relacional que pode ser utilizado para armazenar dados de forma escalável e
rápida. Esse também possui o Amazon DynamoDB streams, que é um serviço que permite a captura de alterações em tempo real nos
dados armazenados no DynamoDB.
A segurança aplicada nesse serviço é feita por meio de chaves de criptografia, utilizadas para criptógrafar os dados
armazenados no banco de dados, garantindo a segurança dos dados.

A estrutura de dados do DynamoDB é baseada em tabelas, onde cada tabela possui uma Sort key e uma Partition key. A Sort
key é utilizada para ordenar os dados armazenados na tabela,
enquanto a Partition key é utilizada para particionar os dados armazenados na tabela.

### Casos de Usos

- Aplicações ‘web’: O DynamoDB pode ser utilizado para armazenar dados de aplicações ‘web’, como dados de usuários,
  produtos, etc.
- Aplicações móveis: O DynamoDB pode ser utilizado para armazenar dados de aplicações móveis, como dados de usuários,
  produtos, etc.
- Aplicações IoT: O DynamoDB pode ser utilizado para armazenar dados de aplicações IoT, como dados de sensores,
  dispositivos, etc.

## AMAZON Redshift

O Amazon Redshift é um banco de dados relacional feito para warehousing de dados, que pode ser utilizado para armazenar
dados de forma escalável e rápida.
Esse serviço também possui o Amazon Redshift Spectrum, que é um serviço que permite a consulta de dados armazenados no Amazon
S3, utilizando o Amazon Redshift.

## Purpose-built databases

- Amazon KeySpaces: banco de dados para uso de Cassandra.
- Amazon MemoryDB: banco de dados para uso de cache.
- Amazon Neptune: banco de dados para uso de grafos.
- Amazon Timestream: banco de dados para uso temporal.
- Amazon QLDB: banco de dados para uso de ledger, possui characteristics de blockchain como a imutabilidade dos dados.

# Aula 05/05/25

## VPC

VPC ou Virtual private cloud é um serviço que permite a criação de uma rede privada na AWS, onde é possível criar
sub-redes, definir regras de segurança e conectar-se a outras redes. A VPC é utilizada para isolar os recursos da AWS, garantindo a
segurança e a privacidade dos dados armazenados na nuvem, considerando que dentro dessas sub-redes, é possível criar
instâncias EC2, bancos de dados e outras serviços de forma interna a VPC.

A VPC permite a criação de subnets, onde é possível segregar uma rede maior em várias redes, tornando-as mais seguras e
facilitando a gestão de recursos. Sendo essas sub-redes representadas por CIDR, que é uma forma de representar endereços
IP e as suas respetivas máscaras de sub-rede.

Existem Duas categorias de sub-redes: as públicas e as privadas:

- Publicas: podem ser acessadas pela internet, ou seja, possuem um gateway de internet associado a elas.
- Privadas: não podem ser acessadas pela internet, ou seja, não possuem um gateway de internet associado a elas.

# Aula 08/07/25

Existem dois tipos de ip associados a uma instância EC2: o ip privado e o ip público. O ip privado é utilizado para
comunicação entre as instâncias dentro da VPC, enquanto o ip público é utilizado para comunicação com a internet.
O ip privado é atribuído automaticamente pela AWS, enquanto o ip público pode ser atribuído manualmente ou
automaticamente.

A conexão entre a VPC e a internet é feita por meio de um gateway de internet, que é um ponto de entrada e saída para a
VPC.
Utilizando o NAT gateway, é possível permitir que instâncias privadas acessem a internet, enquanto o NAT gateway não
pode ser acessado pela internet.

## VPC security layers

- Security groups: é um firewall utilizado para controlar o tráfego de entrada e saída das instâncias EC2, permitindo ou
  negando o acesso a elas.
  sendo um firewall stateful, não é necessário definir regras de saída para o tráfego de entrada.

- Network ACL: é um firewall utilizado para controlar o tráfego de entrada e saída das sub-redes. Sendo um firewall
  stateless, ou seja,
  é necessário definir regras de saída para o tráfego de entrada.

- Bastion hosts: é uma instância EC2 utilizada para acessar outras instâncias EC2 dentro da VPC.

- Interface VPC endpoints: é um ponto de entrada para acessar serviços da AWS dentro da VPC, sem precisar passar pela
  internet.

- Gateway load balancer: é um balanceador de carga utilizado para distribuir o tráfego entre as instâncias EC2 dentro da
  VPC.
- 
- VPC flow logs: é um serviço utilizado para registrar o tráfego de entrada e saída das instâncias EC2 dentro da VPC.
  Esses logs podem ser utilizados para auditoria e análise de segurança.

# AULA 19/05/25

## Design de redes com multiplos VPCs

- Full mesh architecture: é uma arquitetura de rede onde todas as VPCs estão conectadas entre si, permitindo a comunicação entre
todas as VPCs.
- Hub and spoke architecture: é uma arquitetura de rede onde uma VPC central (hub) está conectada a várias VPCs (spokes), interligando-as
entre si. Essa arquitetura é mais escalável e fácil de gerir do que a full mesh architecture, pois permite a comunicação entre as VPCs
sem a necessidade de criar conexões diretas entre todas as VPCs.

## AWS Transit Gateway

O AWS Transit Gateway é um serviço que permite a conexão de várias VPCs e redes locais, facilitando a
comunicação entre elas. Esse serviço é muito versátil para todo o tipo de aplicação, pois o seu custo está relacionado ao 
tráfego de dados, o que pode ser vantajoso para aplicações com tráfego de dados variável.

## VPC Peering

O VPC Peering é um serviço que permite a conexão de duas VPCs, permitindo a comunicação entre elas. Serviço muito útil para
aplicações que precisam de comunicação entre VPCs, mas não é tão escalável quanto o AWS Transit Gateway, pois não permite a
conexão de várias VPCs numa única rede.

## AWS site-to-site VPN

O AWS site-to-site VPN é um serviço que cria uma conexão segura entre a VPC e a rede local, permitindo a comunicação entre elas. 
é possível ligar diversas redes 'on-premises' a uma VPC, mas o custo é elevado, pois o tráfego de dados é cobrado por hora.

## AWS Direct Connect

O AWs Direct Connect gera uma VLAN que inclui redes 'on-premises' a fim de incluir recursos AWS dentro da rede. Esse serviço gera uma
conexão segura e previsível em termos de latência, o que pode ser vantajoso para aplicações que precisam de comunicação consistentes
entre VPCs e redes locais.

# Aula 26/05/25

## Gerindo Permissões de rede

Associar permissões a usuários diretamente é uma prática cabível, pelo menos quando o número de usuários é baixo.





