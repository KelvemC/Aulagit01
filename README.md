# GIT  E GITHUB

Guia prático para iniciantes.

### INSTALAÇÃO 

https://git-scm.com/download

# SCENES

- [x] Você deseja criar pontos na história da produção do seu projeto.

# Para iniciar o git no projeto use

- git init

# Vamos fizer que tenho um projeto de uma landingpage.html

- touch landingpage.html

# Escreva dentro dela "landingpage finalizada"

# Eu quero criar um ponto na história na minha produção a onde eu iniciei a landingpage

- git add landingpage.html

# Agora posso passar uma mensagem usando esse comando:

- git commit -m "mensagem"

# Agora eu quero olhar o ponto da história:

- [x] Você deseja verificar mudanças feitas no seu projeto.

- git log 

# Agora eu quero fazer uma alteração na minha landingpage.

# Faça as alterações no arquivo

# Existe um comando para ver o estado do meu desenvolvimento:

- git status

# No git precisamos informar qual arquivo deve ser colocado no ponto da história (qual arquivo devo enviar para meu repositório), o comando do commit vai sempre enviar arquivos para lá, mas qual arquivos? é os arquivo que adicionamos com o git add

# Para adicionar no novo ponto use o mesmo comando:

- git add landingpage.html

# E depois um git commit para criar o ponto na história

- git commit -m "texto"

# Agora posso verificar as mudanças feita no meu projeto 

- git log

# Apartir desses pontos criados na história, eu posso visitar eles e ver o que foi feitos neles.

# Copie o codigo do commit e use:

- git show número do commit

# Use git show sem número nenhum para visualizar o último ponto na história

- git show

# ------------------------------------------------------------------------------------------------------------


- [x] Você começa uma nova funcionalidade no seu projeto, sem estragar o que já foi feito.

# Podemo usar o poder da branch no git (o branch significa ramificação ) enquanto estou na ramificação master, eu posso criar uma linha alternativa apartir da branch:

# Podemos colocar um nome para branch do tipo cart git branch feature/cart

- git branch 

# Para eu mudar para essa branch use:

- git checkout nome da branch

# Agora que estou nessa linha alternativa eu posso criar meu arquivo:

- touch cart.html

# Podemos voltar para linha do tempo principal

- git checkout master 

# E podemos ver nossa linhas do tempo usando o :

- git branch

# ls -al serve para vilualizar algumas coisas 

- ls -al


- [x] Você adiciona as novas funcionalidades ao seu projeto em produção.

# Podemos unir a linha paralela que foi criada a essa principal, use:

- git merge nome da branch


- [x] Você quer deletar a branch da nova funcionalidade, depois de aplicar em seu projeto. 

# Para deletar uma branch use o comando:

- git branch -D nome da branch

resumo  
* `git init` // inicia a linha do tempo
* `git add` // adiciona ou atualiza mudanças para irem para linha do tempo.
* `git commit` // adiciona um ponto na linha do tempo.
* `git log` // visualiza os pontos na linha do tempo / commit.
* `git status` // informa o estado das alterações do nosso projeto.
* `git show` // apresenta determinado ponto na história.
* `git branch` // gerenciar novas linhas do tempo.
* `git checkout` // manipular as linhas do tempo.
* `git merge` // unir as linhas do tempo.
* `git push` // envia as alterações locais para o repositório remoto.
* `git clone` // clonar um projeto.
* `git pull` // puxar do repositório remoto uma atualização.
* ``
# COMO COLOCAR MEU PROJETO NA NUVEM (GITHUB)

- [x] Você quer colocar seu projeto na nuvem.

o git que foi criado aqui é um repositório local e o do github é um repositório remoto.

# Depois de criar o repositório use:

-  git remote add origin https://github.com/KelvemC/Aulagit01.git

# Para visualizar meu repositório remotos 

- git remot -v

# Agora podemos usar o gitpush ele é o que vai colocar meu repositório local no remoto, mas como
# é minha primeira vez use o comando:

- git push -u origin master

# Seu eu quero adicionar todas as coisas que estiverem em minha página uso o comando:

- git add .

# Como eu já criei minha linha do tempo nem preciso usar o push como o da primeira vez agora é só:

- git push


- [x] Você vai pegar um projeto já iniciado, para trabalhar com o time.

# Vá em algum repositório criado pegue o link e use:

- git clone link

# Posso criar um branch nova com um comando curto:

- git checkout -b nome da branch


# Posso usar um comando curto para adiconar ou atualizar comentando algo:

- git commit -am "texto"


- [x] Você precisa resolver um conflito.

# Em caso de tentar unir duas branch criadas, poderá ocorrer algum conflito e para a solução é só ir até o local que está ocorrendo o conflito e escolher uma das opções que o vscode ajuda para a solução.

- vim nome do projeto para alterar 

- [x] Antes de enviar a resolução, precisamos atualizar o projeto local.

# O comando git pull é um comando que vai puxar atualizações na nuvem

- git pull

# em seguida é só dar um git push


- [x] Você precisa voltar um arquivo para um determinado momento na linha do tempo.

# use o comando git log para saber o ponto  e use:

- git checkout ponto da linha do tempo -- arquivo que desja que volte para um determinado ponto


- [] Você precisa recuperar algo deletado.