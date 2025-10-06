import joblib

# Carregar o modelo
model = joblib.load('../model/sorvete_model.pkl')

# Exemplo de temperatura do dia
temperatura_do_dia = float(input("Digite a temperatura do dia: "))

# Prever vendas
vendas_previstas = model.predict([[temperatura_do_dia]])

print(f"Vendas previstas: {vendas_previstas[0]:.0f} sorvetes")