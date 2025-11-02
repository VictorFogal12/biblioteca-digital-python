# 1. Criação do Repositório no GitHub
Passos para criar o repositório
Acesse o site do GitHub (github.com) e faça login.
Clique no botão "New repository" ou "Novo repositório".
Defina um nome para o repositório, por exemplo: biblioteca-digital-python.
(Opcional) Escreva uma descrição clara do projeto.
Escolha se o repositório será público (qualquer um pode ver) ou privado (apenas você e colaboradores autorizados).
Inicialize o repositório com um arquivo README (descritivo do projeto).
Clique em "Create repository" para criar.
Fazer o primeiro commit
No README.md, você pode colocar uma breve descrição do projeto.
Faça commit com a mensagem: "Inicialização do projeto com README".

# 2. Manipulação de arquivos e diretórios em Python
Explicação
O principal objetivo dessa etapa é permitir que o sistema gerencie os documentos digitais armazenados na biblioteca, que estarão numa pasta específica do computador. Precisamos:
Listar os arquivos organizando-os por extensão (PDF, ePUB, etc.) e por ano (extraído do nome do arquivo).
Adicionar novos arquivos à biblioteca.
Renomear arquivos já existentes.
Remover arquivos que não são mais necessários.
Tudo isso será feito com funções simples em Python usando o módulo os.
O que esse código faz na prática:
Cria uma pasta biblioteca_digital (se não existir).

Funções para:
Listar os documentos organizados por tipo e ano.
Adicionar um arquivo novo (aqui cria um arquivo vazio simulando a adição).
Renomear um arquivo existente.
Remover um arquivo.
Na parte final (if __name__ == "__main__":) há um teste básico que demonstra essas funções.
# Resultado esperado dessa simulação
Inicialmente adiciona dois arquivos: artigo_2022.pdf e tese_2023.epub.
Lista e organiza os arquivos por tipo e ano.
Renomeia "artigo_2022.pdf" para "artigo_final_2022.pdf".
Remove "tese_2023.epub".
Lista novamente mostrando o arquivo renomeado e a remoção do outro
Com essa simulação, você pode ver claramente o funcionamento básico de cada operação solicitada para o sistema
# Código para Interface de Linha de Comando (CLI)
Como funciona
Ao executar o script, aparece um menu no console com opções numeradas.
O usuário escolhe a ação digitando o número correspondente.
Todas as operações chamam as funções que manipulam os arquivos na pasta biblioteca_digital.
O programa só termina quando o usuário escolher a opção 0.

# 3. Integração com Git e GitHub:
Configuração para Pull Requests
No GitHub, por padrão, os repositórios públicos aceitam pull requests.
Para permitir colaboração, nas configurações do repositório (Settings):
Vá em "Branches".
Configure uma Branch Protection Rule para a branch principal (main ou master) para exigir revisões de pull request antes do merge, se desejar maior controle.
Isso obriga os colaboradores a submeterem mudanças via pull requests, que você pode revisar antes de mesclar.

Exemplo de Guia de Contribuição (CONTRIBUTING.md)
Crie um arquivo chamado CONTRIBUTING.md na raiz do projeto com o seguinte conteúdo:

text
# Guia de Contribuição para o Projeto Biblioteca Digital em Python

Obrigado por seu interesse em contribuir!

## Como contribuir

### Passo 1: Fork do repositório

- Clique no botão "Fork" no GitHub e crie uma cópia do repositório para sua conta.

### Passo 2: Clonar o repositório forkado

git clone https://github.com/seuusuario/biblioteca-digital-python.git
cd biblioteca-digital-python

text

### Passo 3: Criar uma branch para suas mudanças

git checkout -b minha-feature

text

### Passo 4: Fazer suas alterações

- Faça as modificações necessárias no código.

### Passo 5: Commit e push das mudanças

git add .
git commit -m "Descrição clara e objetiva do que foi alterado"
git push origin minha-feature

text

### Passo 6: Abrir um Pull Request

- No GitHub, vá para seu repositório forkado.
- Clique em "Compare & pull request".
- Descreva suas mudanças e envie o pull request.

### Boas práticas de commits

- Mensagens curtas e claras, no presente do indicativo.
- Faça commits pequenos e consistentes.
- Use o comando `git status` para monitorar alterações.

---

Agradecemos pela sua colaboração!
Com isso, seu repositório estará preparado para colaboração organizada, facilitando a manutenção e crescimento do sistema.

