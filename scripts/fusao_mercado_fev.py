from processamento_dados import Dados

# Path files
path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

#Extract
dados_empresaA = Dados.leitura_dados(path_json, 'json')
print(f"Os nomes das colunas da empresa A são:  \n{dados_empresaA.nome_colunas}")
print(f"A quantidade de linhas da empresa A é: {dados_empresaA.qtd_linhas}")

print("#####################################################################################################")

dados_empresaB = Dados.leitura_dados(path_csv, 'csv')
print(f"Os nomes das colunas da empresa B são:  \n{dados_empresaB.nome_colunas}")
print(f"A quantidade de linhas da empresa B é: {dados_empresaB.qtd_linhas}")

# Transform
key_mapping = {'Nome do Item' : 'Nome do Produto',
               'Classificação do Produto' : 'Categoria do Produto',
               'Valor em Reais (R$)' : 'Preço do Produto (R$)',
               'Quantidade em Estoque' : 'Quantidade em Estoque',
               'Nome da Loja' : 'Filial',
               'Data da Venda' : 'Data da Venda'}

dados_empresaB.rename_columns(key_mapping)
print(f"Nome de colunas da Empresa B após renomeação: \n{dados_empresaB.nome_colunas}")

print("#####################################################################################################")

dados_fusao = Dados.join(dados_empresaA, dados_empresaB)
print("Fusão de dados concluída!")
print(f"Quantidade de linhas: {dados_fusao.qtd_linhas}")

#Load
path_dados_combinados = "data_processed/dados_combinados.csv"
dados_fusao.salvando_dados(path_dados_combinados)
print(f"Dados salvos em {path_dados_combinados}")