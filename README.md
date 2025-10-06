# Previsão de Vendas de Sorvete - Projeto Gelato Mágico

Este projeto utiliza **Machine Learning** para prever a quantidade de sorvetes vendidos com base na **temperatura do dia**. O objetivo é ajudar sorveterias a planejarem melhor a produção, evitando desperdícios e otimizando vendas.

projeto-gelato-ml/
├─ data/
│ └─ vendas.csv # Dados históricos de temperatura e vendas
├─ model/
│ └─ sorvete_model.pkl # Modelo treinado salvo após executar train.py
├─ train.py # Script para treinar o modelo de regressão linear
├─ predict.py # Script para fazer previsões interativas
├─ requirements.txt # Dependências do Python
└─ README.md # Este arquivo


---

## Descrição de cada parte

### 1. `data/vendas.csv`
Arquivo que contém os **dados históricos** das vendas de sorvete e a temperatura correspondente.  
- **temperatura**: temperatura do dia  
- **vendas**: quantidade de sorvetes vendidos  

Exemplo:

| temperatura | vendas |
|------------|--------|
| 20         | 60     |
| 25         | 90     |
| 30         | 120    |

---

### 2. `train.py`
Script responsável por:  
- Ler os dados do CSV  
- Treinar um modelo de **regressão linear** usando `scikit-learn`  
- Salvar o modelo treinado em `model/sorvete_model.pkl` para ser usado posteriormente em previsões  

---

### 3. `predict.py`
Script interativo que permite:  
- Carregar o modelo treinado  
- Receber a temperatura do dia como entrada  
- Retornar a quantidade prevista de sorvetes a serem vendidos  

---

### 4. `model/sorvete_model.pkl`
Arquivo gerado após executar `train.py`. Contém o **modelo treinado**, que pode ser reutilizado sem precisar treinar novamente.

---

### 5. `requirements.txt`
Lista de dependências necessárias para rodar os scripts do projeto:

pandas
scikit-learn
joblib


Instalação:

```bash
pip install -r requirements.txt

Como usar

Instale as dependências do Python.

Treine o modelo com:

python train.py


Faça previsões interativas com:

python predict.py


Digite a temperatura do dia e o script mostrará a quantidade de sorvetes prevista.

Observações

Todo o projeto pode ser executado localmente, sem necessidade de nuvem.

---

