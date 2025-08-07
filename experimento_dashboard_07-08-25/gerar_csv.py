import pandas as pd

# Dados contábeis de exemplo
dados = {
    "Data": [
        "2025-01-01", "2025-01-02", "2025-01-03", "2025-01-04", "2025-01-05",
        "2025-01-06", "2025-01-07", "2025-01-08", "2025-01-09", "2025-01-10",
        "2025-01-11", "2025-01-12", "2025-01-13", "2025-01-14", "2025-01-15"
    ],
    "Conta": [
        "Receitas de Vendas", "Salários", "Aluguel", "Receitas de Serviços", "Impostos",
        "Receitas de Vendas", "Manutenção", "Receitas de Serviços", "Salários", "Aluguel",
        "Receitas de Vendas", "Marketing", "Impostos", "Receitas de Serviços", "Manutenção"
    ],
    "Tipo": [
        "Receita", "Despesa", "Despesa", "Receita", "Despesa",
        "Receita", "Despesa", "Receita", "Despesa", "Despesa",
        "Receita", "Despesa", "Despesa", "Receita", "Despesa"
    ],
    "Valor": [
        5000.00, 2000.00, 1500.00, 3000.00, 800.00,
        4500.00, 600.00, 3500.00, 2000.00, 1500.00,
        5200.00, 900.00, 1000.00, 3700.00, 700.00
    ]
}

df = pd.DataFrame(dados)

# Salvar o CSV
df.to_csv("contabilidade.csv", index=False)

print("Arquivo 'contabilidade.csv' criado com sucesso.")
