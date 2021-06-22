# RL_object_transport_single_agent
Trabalho I da disciplina de aprendizado por reforço para transporte de objetos com apenas um agente simples

Trabalho desenvolvido em python 3.8, seguir os seguintes passos para execução do mesmo:
- Ter o pipenv instalado, pip install pipenv;
- Criar um ambiente virtual na raiz do projeto com o seguinte comando: pipenv shell;
- Instalar as dependências com o comando: pipenv install;

Estados do MDP:
- Posição x e y do agente;
- Objeto está capturado;
- Posição do x e y do objeto;


Função de recompensas:
- -0.5 quando agente se deloca para um casa qualquer da grade;
- 0 quando agente se desloca para um dos lados do objeto, acabando de capturá-lo;
- 0 quando agente se desloca para a base (sem o objeto entrar na base);
- 1 quando o agente e o objeto entram na base;
- O intuito de tal política é favorecer o agente capturar o objeto e depois seguir até a base junto com o objeto;