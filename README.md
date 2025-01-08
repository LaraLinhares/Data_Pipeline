# Data_Pipeline

## Descrição

Este projeto é uma implementação para leitura, transformação, fusão e salvamento de dados provenientes de dois arquivos: um JSON e um CSV. O código organiza esses dados, renomeia colunas e os combina em um único conjunto, que é então exportado para um novo arquivo CSV.

## Funcionalidades

O código possui uma classe `Dados` com os seguintes métodos e funcionalidades principais:

1. **Leitura de Dados**:
   - Leitura de arquivos JSON e CSV.
   - A função `leitura_dados` seleciona automaticamente o tipo de arquivo e lê os dados de acordo com o formato fornecido.

2. **Transformação de Dados**:
   - Renomeação das colunas de dados usando um mapeamento definido.
   - Combinação de dados de duas fontes em um único conjunto de dados.

3. **Fusão de Dados**:
   - A fusão é feita através do método `join`, que concatena os dados das duas fontes (empresa A e empresa B) em uma lista única.

4. **Salvamento de Dados**:
   - O método `salvando_dados` exporta os dados combinados para um novo arquivo CSV.

## Dependências

- Python 3.12.7
- Módulos padrão:
  - `json`
  - `csv`

## Estrutura de Código
```sh
.
├── data_raw/
│   ├── dados_empresaA.json
│   └── dados_empresaB.csv
├── data_processed/
│   └── dados_combinados.csv
├── notebooks/
│   └── explorer.py
├── scripts/
│   ├── fusao_mercado_fev.py
│   └── processamento_dados.py
```

## Mais Informações
  Código desenvolvido durante o curso "Pipeline de dados: combinando Python e orientação a objeto" da Alura.




