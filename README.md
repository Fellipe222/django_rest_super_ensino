# RESUMO
Este projeto visa oferecer APIs REST efetuar operações básicas de uma instituiçao de ensino, através do DRF (Django Rest Framework).

# Instalação
- <a href="https://hub.docker.com/layers/fellipe222/teste-super-ensino/1.0/images/sha256:7352bc41a78c69b24dd3c133d3b9c66a7d66d6e9fdb5b1b1fec2ed7f7fe1e150" target="_blank">Container do projeto!</a>
![image](https://user-images.githubusercontent.com/56563965/182082309-536fc006-d617-4eaf-85d7-76f097765b57.png)

- Caso não possua o Docker na sua máquina, download: <a href="https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe?utm_source=docker&utm_medium=webreferral&utm_campaign=dd-smartbutton&utm_location=header" target="_blank">Windows</a> | <a href="https://desktop.docker.com/mac/main/amd64/Docker.dmg?utm_source=docker&utm_medium=webreferral&utm_campaign=dd-smartbutton&utm_location=module" target="_blank">MAC (chip Intel)</a> | <a href="https://desktop.docker.com/mac/main/arm64/Docker.dmg?utm_source=docker&utm_medium=webreferral&utm_campaign=dd-smartbutton&utm_location=module" target="_blank">MAC (chip Apple)</a> | <a href="https://docs.docker.com/desktop/linux/install/" target="_blank">Linux</a>

# Funcionalidades
Através do django admin, professores podem:
- Cadastrar, editar, remover e visualizar disciplinas (e.g.: 'Matemática','Português')
![image](https://user-images.githubusercontent.com/56563965/182060980-433f2e57-0111-459b-8c3e-1b411690126e.png)

- Cadastrar, editar, remover e visualizar séries (e.g.: '1ª série fundamental')
![image](https://user-images.githubusercontent.com/56563965/182061060-6eae33d1-8503-4a22-9b23-c98d917e1a96.png)

- Cadastrar, editar, remover e visualizar novos alunos (vinculando: série)
![image](https://user-images.githubusercontent.com/56563965/182061171-cdbcba25-74f2-4abb-9049-95112d166645.png)

- Cadastrar, editar, remover e visualizar questionários (vinculando: disciplina e série)
![image](https://user-images.githubusercontent.com/56563965/182061319-ddc9aeca-68c4-41f7-bcd8-d1209cb537d8.png)

- Cadastrar, editar, remover e visualizar perguntas (viculando: questionário)
![image](https://user-images.githubusercontent.com/56563965/182061366-e1d88846-e4c5-4c02-b7f2-eed060314ec1.png)

- Cadastrar, editar, remover e visualizar alternativas (vinculando: perguntas)
![image](https://user-images.githubusercontent.com/56563965/182061431-7f81ecf1-04f3-42fb-a96d-99b9b22f1869.png)

Alunos podem:
- Cadastrar respostas (vinculando: id_aluno e pergunta), através do método POST

# Diagrama de relações entre modelos
![image](https://user-images.githubusercontent.com/56563965/182056316-81e38b99-b60b-467d-a1ee-435d35ed79e8.png)

# Endpoints
Através de <i>localhost/api/</i>, podemos visualizar os endpoints no padrão: <i>[ MÉTODO ] /endpoint/</i>:
![image](https://user-images.githubusercontent.com/56563965/182056757-3e4728c8-5bd1-42b3-b7db-7a73994da401.png)

# Na prática
Para visualizar a relação completa de perguntas, podemos:
- GET <i>localhost/api/admin/perguntas/</i> para visualizar as perguntas e resposta correta:
![image](https://user-images.githubusercontent.com/56563965/182057614-6d9317be-48f4-4fa9-a039-c18f298822f2.png)

- GET <i>localhost/api/aluno/perguntas/</i> para visualizar apenas perguntas:
![image](https://user-images.githubusercontent.com/56563965/182057704-62066b76-37e7-4aa3-970d-aa113d4247d8.png)

- GET <i>localhost/api/admin/perguntas/<id_pergunta></i> para visualizar apenas uma pergunta específica e sua resposta correta:
![image](https://user-images.githubusercontent.com/56563965/182057954-bbf434db-6fdf-4f6b-98d1-1f29519bfdf5.png)

- GET <i>localhost/api/aluno/perguntas/<id_pergunta></i> para visualizar apenas uma pergunta específica:
![image](https://user-images.githubusercontent.com/56563965/182058040-7cc197c2-7e76-4222-907d-3357189f6119.png)
  
- POST <i>localhost/api/resposta/<id_aluno></i> para enviar respostas ao servidor, a partir de um dicionário contendo as chaves: <b>id_pergunta</b> e <b>valor</b>. Retorna um dicionário com a chave <b>acertou</b>:bool:
![image](https://user-images.githubusercontent.com/56563965/182057105-d9fd311d-3d71-4d53-9045-891a7bcc74cd.png)
  
- GET <i>localhost/api/desempenho/<id_aluno>/<id_questionario></i> para visualizar o desemprenho de um aluno no questionário especificado:
![image](https://user-images.githubusercontent.com/56563965/182059340-4f0cc30e-6aca-403b-ac14-e54937986d5b.png)

  

