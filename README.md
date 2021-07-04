# GIT  E GIT HUB

Guia prático para iniciantes.

### INSTALAÇÃO 

https://git-scm.com/download

# SCENES

- [x] Você deseja criar pontos na história da produção do seu projeto

# para iniciar o git no projeto use

- git init

# Vamos fizer que tenho um projeto de uma landingpage.html

- touch landingpage.html

# escreva dentro dela "landingpage finalizada"

# eu quero criar um ponto na história na minha produção a onde eu iniciei a landingpage

- git add landingpage.html

# agora posso passar uma mensagem usando esse comando:

- git commit -m "mensagem"

# agora eu quero olhar o ponto da história:

- [x] Você deseja verificar mudanças feitas no seu projeto

- git log 

# agora eu quero fazer uma alteração na minha landingpage.

# faça as alterações no arquivo

# existe um comando para ver o estado do meu desenvolvimento:

- git status

# no git precisamos informar qual arquivo deve ser colocado no ponto da história (qual arquivo devo enviar para meu repositório), o comando do commit vai sempre enviar arquivos para lá, mas qual arquivos? é os arquivo que adicionamos com o git add

# para adicionar no novo ponto use o mesmo comando:

- git add landingpage.html

# e depois um git commit para criar o ponto na história

- git commit -m "texto"

# agora posso verificar as mudanças feita no meu projeto 

- git log

# apartir desses pontos criados na história, eu posso visitar eles e ver o que foi feitos neles.

# copie o codigo do commit e use:

- git show número do commit

# use git show sem número nenhum para visualizar o último ponto na história

- git show

# ------------------------------------------------------------------------------------------------------------


- [x] Você começa uma nova funcionalidade no seu projeto, sem estragar o que já foi feito.

# podemo usar o poder da branch no git (o branch significa ramificação ) enquanto estou na ramificação master, eu posso criar uma linha alternativa apartir da branch:

# podemos colocar um nome para branch do tipo cart git branch feature/cart

- git branch 

# para eu mudar para essa branch use:

- git checkout nome da branch

# agora que estou nessa linha alternativa eu posso criar meu arquivo:

- touch cart.html

# podemos voltar para linha do tempo principal

- git checkout master 

# e podemos ver nossa linhas do tempo usando o :

- git branch

# ls -al serve para vilualizar algumas coisas 

- ls -al


- [x] Você adiciona as novas funcionalidades ao seu projeto em produção.

# podemos unir a linha paralela que foi criada a essa principal, use:

- git merge nome da branch


- [x] Você quer deletar a branch da nova funcionalidade, depois de aplicar em seu projeto. 

# para deletar uma branch use o comando:

- git branch -D nome da branch

resumo  
* `git init` // inicia a linha do tempo
* `git add` // adiciona ou atualiza mudanças para irem para linha do tempo
* `git commit` // adiciona um ponto na linha do tempo
* `git log` // visualiza os pontos na linha do tempo / commit
* `git status` // informa o estado das alterações do nosso projeto 
* `git show` // apresenta determinado ponto na história

# COMO COLOCAR MEU PROJETO NA NUVEM (GITHUB)

- [x] Você quer colocar seu projeto na nuvem

o git que foi criado aqui é um repositório local e o do github é um repositório remoto.

# depois de criar o repositório use:

-  git remote add origin https://github.com/KelvemC/Aulagit01.git

# para visualizar meu repositório remotos 

- git remot -v

# agora podemos usar o gitpush ele é o que vai colocar meu repositório local no remoto, mas como
# é minha primeira vez use o comando:

- git push -u origin master

# seu eu quero adicionar todas as coisas que estiverem em minha página uso o comando:

- git add .