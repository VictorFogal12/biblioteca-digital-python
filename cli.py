"""
Interface de linha de comando interativa para o sistema de biblioteca digital.
Fornece um menu numérico para gerenciar os arquivos da biblioteca.
"""

import os
from biblioteca_digital import (
    listar_arquivos,
    adicionar_arquivo,
    renomear_arquivo,
    remover_arquivo,
    imprimir_estrutura,
    inicializar_biblioteca
)

def limpar_tela():
    """Limpa a tela do terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_menu():
    """Exibe o menu principal do sistema."""
    limpar_tela()
    print("=" * 40)
    print("   SISTEMA DE BIBLIOTECA DIGITAL")
    print("=" * 40)
    print("\nEscolha uma opção:")
    print("1 - Listar arquivos")
    print("2 - Adicionar arquivo")
    print("3 - Renomear arquivo")
    print("4 - Remover arquivo")
    print("0 - Sair")
    print("\n" + "=" * 40)

def pausar():
    """Pausa a execução até o usuário pressionar Enter."""
    input("\nPressione Enter para continuar...")

def listar():
    """Lista todos os arquivos da biblioteca."""
    limpar_tela()
    print("=== ARQUIVOS NA BIBLIOTECA ===\n")
    organizacao = listar_arquivos()
    imprimir_estrutura(organizacao)
    pausar()

def adicionar():
    """Adiciona um novo arquivo à biblioteca."""
    limpar_tela()
    print("=== ADICIONAR NOVO ARQUIVO ===\n")
    print("O nome do arquivo deve conter um ano (YYYY) e uma extensão.")
    print("Exemplo: artigo_2023.pdf")
    
    nome = input("\nDigite o nome do arquivo: ").strip()
    if nome:
        adicionar_arquivo(nome)
    else:
        print("\nNome de arquivo inválido!")
    pausar()

def renomear():
    """Renomeia um arquivo existente."""
    limpar_tela()
    print("=== RENOMEAR ARQUIVO ===\n")
    
    # Mostra os arquivos disponíveis
    print("Arquivos disponíveis:")
    organizacao = listar_arquivos()
    imprimir_estrutura(organizacao)
    
    print("\nO novo nome deve conter um ano (YYYY) e a mesma extensão.")
    nome_atual = input("\nDigite o nome do arquivo atual: ").strip()
    if nome_atual:
        novo_nome = input("Digite o novo nome: ").strip()
        if novo_nome:
            renomear_arquivo(nome_atual, novo_nome)
        else:
            print("\nNovo nome inválido!")
    else:
        print("\nNome atual inválido!")
    pausar()

def remover():
    """Remove um arquivo da biblioteca."""
    limpar_tela()
    print("=== REMOVER ARQUIVO ===\n")
    
    # Mostra os arquivos disponíveis
    print("Arquivos disponíveis:")
    organizacao = listar_arquivos()
    imprimir_estrutura(organizacao)
    
    nome = input("\nDigite o nome do arquivo a ser removido: ").strip()
    if nome:
        confirmacao = input(f"Tem certeza que deseja remover '{nome}'? (s/N): ").strip().lower()
        if confirmacao == 's':
            remover_arquivo(nome)
        else:
            print("\nOperação cancelada!")
    else:
        print("\nNome de arquivo inválido!")
    pausar()

def main():
    """Função principal do programa."""
    inicializar_biblioteca()
    
    while True:
        exibir_menu()
        opcao = input("\nOpção escolhida: ").strip()
        
        if opcao == "1":
            listar()
        elif opcao == "2":
            adicionar()
        elif opcao == "3":
            renomear()
        elif opcao == "4":
            remover()
        elif opcao == "0":
            limpar_tela()
            print("Obrigado por usar o Sistema de Biblioteca Digital!")
            print("Até logo!\n")
            break
        else:
            print("\nOpção inválida!")
            pausar()

if __name__ == '__main__':
    main()