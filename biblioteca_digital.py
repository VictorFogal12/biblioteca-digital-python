"""
Módulo de gerenciamento de biblioteca digital.
Fornece funcionalidades para gerenciar arquivos digitais, organizando-os por tipo e ano.
"""

import os
import re
from pathlib import Path
import string

# Configuração do caminho da biblioteca
biblioteca_path = './biblioteca_digital'

def validar_nome_arquivo(nome_arquivo):
    """
    Valida se o nome do arquivo é válido.
    
    Args:
        nome_arquivo (str): Nome do arquivo a ser validado
        
    Returns:
        bool: True se o nome é válido, False caso contrário
        str: Mensagem de erro em caso de nome inválido
    """
    # Verifica caracteres válidos
    caracteres_validos = set(string.ascii_letters + string.digits + '.-_')
    if not all(c in caracteres_validos for c in nome_arquivo.replace('/', '').replace('\\', '')):
        return False, "Nome do arquivo contém caracteres inválidos"
    
    # Verifica se tem extensão
    if '.' not in nome_arquivo:
        return False, "Nome do arquivo deve ter uma extensão"
    
    # Verifica se tem ano no formato correto
    if not re.search(r'\d{4}', nome_arquivo):
        return False, "Nome do arquivo deve conter um ano no formato YYYY"
    
    return True, ""

def listar_arquivos():
    """
    Lista todos os arquivos da biblioteca organizados por tipo e ano.
    
    Returns:
        dict: Dicionário com arquivos organizados por tipo e ano
    """
    try:
        arquivos = os.listdir(biblioteca_path)
        organizados = {}
        
        for arquivo in arquivos:
            tipo = arquivo.split('.')[-1].lower()
            ano = "Desconhecido"
            match = re.search(r'\d{4}', arquivo)
            if match:
                ano = match.group(0)

            if tipo not in organizados:
                organizados[tipo] = {}
            if ano not in organizados[tipo]:
                organizados[tipo][ano] = []
            organizados[tipo][ano].append(arquivo)
        
        return organizados
    except Exception as e:
        print(f"Erro ao listar arquivos: {str(e)}")
        return {}

def adicionar_arquivo(nome_arquivo):
    """
    Adiciona um novo arquivo vazio à biblioteca.
    
    Args:
        nome_arquivo (str): Nome do arquivo a ser adicionado
    """
    try:
        # Validar nome do arquivo
        valido, mensagem = validar_nome_arquivo(nome_arquivo)
        if not valido:
            print(f"Erro: {mensagem}")
            return

        caminho = os.path.join(biblioteca_path, nome_arquivo)
        if os.path.exists(caminho):
            print("Arquivo já existe.")
            return
            
        with open(caminho, 'w', encoding='utf-8') as f:
            f.write("")
        print(f"Arquivo '{nome_arquivo}' adicionado com sucesso.")
    except Exception as e:
        print(f"Erro ao adicionar arquivo: {str(e)}")

def renomear_arquivo(nome_atual, novo_nome):
    """
    Renomeia um arquivo existente na biblioteca.
    
    Args:
        nome_atual (str): Nome atual do arquivo
        novo_nome (str): Novo nome para o arquivo
    """
    try:
        # Validar novo nome
        valido, mensagem = validar_nome_arquivo(novo_nome)
        if not valido:
            print(f"Erro: {mensagem}")
            return

        caminho_atual = os.path.join(biblioteca_path, nome_atual)
        novo_caminho = os.path.join(biblioteca_path, novo_nome)
        
        if not os.path.exists(caminho_atual):
            print("Arquivo original não encontrado.")
            return
            
        if os.path.exists(novo_caminho):
            print("Já existe um arquivo com o novo nome.")
            return
            
        os.rename(caminho_atual, novo_caminho)
        print(f"Arquivo renomeado de '{nome_atual}' para '{novo_nome}'.")
    except Exception as e:
        print(f"Erro ao renomear arquivo: {str(e)}")

def remover_arquivo(nome_arquivo):
    """
    Remove um arquivo da biblioteca.
    
    Args:
        nome_arquivo (str): Nome do arquivo a ser removido
    """
    try:
        caminho = os.path.join(biblioteca_path, nome_arquivo)
        if not os.path.exists(caminho):
            print("Arquivo não encontrado.")
            return
            
        os.remove(caminho)
        print(f"Arquivo '{nome_arquivo}' removido com sucesso.")
    except Exception as e:
        print(f"Erro ao remover arquivo: {str(e)}")

def inicializar_biblioteca():
    """
    Inicializa a estrutura da biblioteca, criando o diretório se necessário.
    """
    try:
        if not os.path.exists(biblioteca_path):
            os.makedirs(biblioteca_path)
            print(f"Diretório '{biblioteca_path}' criado com sucesso.")
    except Exception as e:
        print(f"Erro ao criar diretório da biblioteca: {str(e)}")

def imprimir_estrutura(organizacao):
    """
    Imprime a estrutura organizada dos arquivos.
    
    Args:
        organizacao (dict): Dicionário com a organização dos arquivos
    """
    for tipo, anos in organizacao.items():
        print(f"\nTipo: {tipo}")
        for ano, arquivos in anos.items():
            print(f" Ano: {ano}")
            for arquivo in arquivos:
                print(f"  - {arquivo}")

if __name__ == "__main__":
    # Inicialização
    inicializar_biblioteca()
    
    # Testes das funcionalidades
    print("\n=== Teste de Adição de Arquivos ===")
    adicionar_arquivo("artigo_2022.pdf")
    adicionar_arquivo("tese_2023.epub")
    adicionar_arquivo("relatorio-2021.txt")
    adicionar_arquivo("imagem_1998.jpg")
    
    print("\n=== Arquivos Iniciais ===")
    organizacao = listar_arquivos()
    imprimir_estrutura(organizacao)
    
    print("\n=== Teste de Renomeação ===")
    renomear_arquivo("artigo_2022.pdf", "artigo_final_2022.pdf")
    
    print("\n=== Teste de Remoção ===")
    remover_arquivo("tese_2023.epub")
    
    print("\n=== Estado Final dos Arquivos ===")
    organizacao = listar_arquivos()
    imprimir_estrutura(organizacao)










