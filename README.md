# RESUMO
Este projeto visa oferecer APIs REST efetuar operações básicas de uma instituiçao de ensino, através do DRF (Django Rest Framework).

Professores podem:
- Cadastrar disciplinas (e.g.: 'Matemática','Português')
- Cadastrar séries (e.g.: '1ª série fundamental')
- Cadastrar novos alunos (vinculando: série)
- Cadastrar questionários (vinculando: disciplina e série). 
- Cadastrar perguntas (viculando: questionário)
- Cadastrar alternativas (vinculando: perguntas)

Alunos podem:
- Cadastrar respostas (vinculando: pergunta)

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

  

