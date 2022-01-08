Você pode baixar o projeto clicando em CODE e Download ZIP

Como rodar a aplicação:

VSCODE

1 - baixar vscode https://code.visualstudio.com/download

PYTHON

1 - baixar python https://www.python.org/downloads/ (marcar a caixinha add python 3.10 to path na instalação)

XAMPP

1 - baixar xampp https://www.apachefriends.org/pt_br/download.html

2 - abrir xampp e rodar apache e mysql

3 - abrir no navegador http://localhost/phpmyadmin/

4 - dentro do site acima, clicar em "novo" no canto superior esquerdo

5 - criar a base de dados com o nome "projetopub"

DJANGO

1 - abrir cmd ou terminal do vscode e digitar "pip install django" (caso o pip peça para atualizar a versão, copie o código que o pip pede e atualize)

2 - geralmente o código do pip é o seguinte "python -m pip install --upgrade pip". Rode apenas se o pip não estiver atualizado

3 - dentro do vscode, aperte em "file" no canto superior esquerdo, depois "open folder" e abra a pasta "projetoPub" que é o projeto

4 - com o terminal do vscode aberto, certifique-se que você está dentro da pasta "projetoPub" que contém o arquivo manage.py e pastas do projeto

5 - dentro da pasta do projeto que contém o arquivo "manage.py", digite no terminal os seguintes códigos:

6 - python manage.py makemigrations

7 - python manage.py migrate

8 - python manage.py runserver

9 - com o server rodando sem erros, clique no link da penúltima linha que é o server, dê um ctrl + click em cima do link que no meu caso é "http://127.0.0.1:8000/". Clique no seu link que apareceu no terminal após a linha 8 (python manage.py runserver)

10 - se tudo deu certo, o link te levou para a página inicial do meu projeto em que contém um cabeçalho com as opções Início, Receitas, Despesas, Contas e minhas redes sociais na parte da direita. No corpo tem informações sobre mim e no rodapé tem meu nome com um link para meu linkedin no nome.

Espero que você tenha conseguido abrir meu projeto na sua máquina. Obrigado!
