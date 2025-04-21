import pandas as pd

# Lê o arquivo CSV
df = pd.read_csv('exemplo.csv')

# Mostra as 5 primeiras linhas
print("📋 Primeiras linhas:")
print(df.head())

# Total de vendas por produto
print("\n💰 Vendas por produto:")
vendas_produto = df.groupby('nome_produto')['quantidade'].sum()
print(vendas_produto)

# Receita total por loja
print("\n🏬 Receita total por loja:")
df['receita'] = df['quantidade'] * df['preco']
receita_loja = df.groupby('loja')['receita'].sum()
print(receita_loja)

# Produto mais vendido
produto_mais_vendido = vendas_produto.idxmax()
print(f"\n🏆 Produto mais vendido: {produto_mais_vendido}")

# Receita total
total = df['receita'].sum()
print(f"\n📈 Receita total: R$ {total}")
