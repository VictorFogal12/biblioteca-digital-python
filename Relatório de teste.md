Relatório de Testes e Feedback do Projeto Biblioteca Digital
1. Objetivo dos Testes

Validar o correto funcionamento das funcionalidades principais do sistema:
Listar arquivos organizados por tipo e ano.
Adicionar arquivos novos.
Renomear arquivos existentes.
Remover arquivos indesejados.

2. Metodologia
Testes realizados localmente em ambiente de desenvolvimento.
Foram testados arquivos fictícios com nomes seguindo o padrão nome_ano.extensão.
Foi usada a interface de linha de comando para execução.
Testes manuais para verificar respostas e mensagens no console.

3. Resultados dos Testes
Listar arquivos: arquivos foram organizados corretamente por tipo e ano.
Adicionar arquivos: arquivos vazios foram criados com sucesso na pasta.
Renomear arquivos: nomes alterados corretamente, inclusive lidando com arquivos inexistentes.
Remover arquivos: arquivos removidos, com mensagens para casos de arquivo não encontrado.

4. Feedback Recebido
Funcionalidade simples e direta, fácil de usar por usuários sem conhecimento técnico.
Sugestão para permitir adicionar arquivos existentes através de cópia, e não criar arquivos vazios.
Sugestão para guardar metadados mais detalhados dos documentos.
Solicitação para incluir opção de busca por nome ou filtro específico.
Pedido para melhorar mensagens de erro para torná-las mais amigáveis.

5. Ações de Melhoria Incorporadas
Implementação futura planejada para permitir upload/cópia de arquivos reais.
Preparação do projeto para inclusão de banco de dados para metadados.
Inclusão no roadmap de busca e filtros.
Revisão das mensagens de erro para serem mais descritivas e úteis.

6. Complementado com logs de testes e screenshots.

a. Código
=== Teste de Adição de Arquivos ===
Arquivo 'artigo_2022.pdf' adicionado com sucesso.
Arquivo 'tese_2023.epub' adicionado com sucesso.
Arquivo 'relatorio-2021.txt' adicionado com sucesso.
Arquivo 'imagem_1998.jpg' adicionado com sucesso.

=== Arquivos Iniciais ===

Tipo: pdf
 Ano: 2022
  - artigo_2022.pdf

Tipo: jpg
 Ano: 1998
  - imagem_1998.jpg

Tipo: txt
 Ano: 2021
  - relatorio-2021.txt

Tipo: epub
 Ano: 2023
  - tese_2023.epub

=== Teste de Renomeação ===
Arquivo renomeado de 'artigo_2022.pdf' para 'artigo_final_2022.pdf'.

=== Teste de Remoção ===
Arquivo 'tese_2023.epub' removido com sucesso.

=== Estado Final dos Arquivos ===

Tipo: pdf
 Ano: 2022
  - artigo_final_2022.pdf

Tipo: jpg
 Ano: 1998
  - imagem_1998.jpg

Tipo: txt
 Ano: 2021
  - relatorio-2021.txt

b. Código para Interface de Linha de Comando (CLI)

========================================
   SISTEMA DE BIBLIOTECA DIGITAL
========================================

Escolha uma opção:
1 - Listar arquivos
2 - Adicionar arquivo
3 - Renomear arquivo
4 - Remover arquivo
0 - Sair

========================================

Opção escolhida: 
1

=== ARQUIVOS NA BIBLIOTECA ===


Tipo: pdf
 Ano: 2022
  - artigo_final_2022.pdf

Tipo: jpg
 Ano: 1998
  - imagem_1998.jpg

Tipo: txt
 Ano: 2021
  - relatorio-2021.txt

Pressione Enter para continuar...

Opção escolhida: 
2

=== ADICIONAR NOVO ARQUIVO ===

O nome do arquivo deve conter um ano (YYYY) e uma extensão.
Exemplo: artigo_2023.pdf

Digite o nome do arquivo: 
Brasil_2025.txt

Arquivo 'Brasil_2025.txt' adicionado com sucesso.

Pressione Enter para continuar...

Opção escolhida: 
3

=== RENOMEAR ARQUIVO ===

Arquivos disponíveis:

Tipo: pdf
 Ano: 2022
  - artigo_final_2022.pdf

Tipo: txt
 Ano: 2025
  - Brasil_2025.txt
 Ano: 2021
  - relatorio-2021.txt

Tipo: jpg
 Ano: 1998
  - imagem_1998.jpg

O novo nome deve conter um ano (YYYY) e a mesma extensão.

Digite o nome do arquivo atual: Brasil_2025.txt
Digite o novo nome: Portugal_1500.txt
Arquivo renomeado de 'Brasil_2025.txt' para 'Portugal_1500.txt'.

Pressione Enter para continuar...

Opção escolhida: 
4

=== REMOVER ARQUIVO ===

Arquivos disponíveis:

Tipo: pdf
 Ano: 2022
  - artigo_final_2022.pdf

Tipo: jpg
 Ano: 1998
  - imagem_1998.jpg

Tipo: txt
 Ano: 1500
  - Portugal_1500.txt
 Ano: 2021
  - relatorio-2021.txt

Digite o nome do arquivo a ser removido: Portugal_1500.txt
Tem certeza que deseja remover 'Portugal_1500.txt'? (s/N): S
Arquivo 'Portugal_1500.txt' removido com sucesso.

Pressione Enter para continuar...

Opção escolhida: 
0

Obrigado por usar o Sistema de Biblioteca Digital!
Até logo!