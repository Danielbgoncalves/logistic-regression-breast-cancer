import pandas as pd
import matplotlib
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay


# Aqui vamos criar uma tabela (dase de dados) com os dados médios da tabela (ela tem as variações e piores casos também)

mean_features = [
    'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean',
    'smoothness_mean', 'compactness_mean', 'concavity_mean',
    'concave_points_mean', 'symmetry_mean', 'fractal_dimension_mean'
]

usecols = list(range(12)) # [0,1,...,11]
col_names = ['id', 'diagnosis'] + mean_features # só define os nomes das colunas

df = pd.read_csv("wdbc.data", header=None, usecols=usecols, names=col_names)

print(df.head())

# Separar em treino e validação 

 ## não da pra fazer conta com 'maligno' e 'benígno' então transformamos em números
 ## via função anônima (me parece)
df['diagnosis'] = df['diagnosis'].map({'B':0, 'M':1})

X = df[mean_features]
Y = df['diagnosis']

 ## 20% do df vai ser para teste e 80% para treinamento 
 ## 42 é pra o embaralhamento entre quais saõ de teste e quais são de validação serem sempre as mesmas
 ## 42 especificamente pq essa é a resposta pra vida, universo e tudo ! (o motivo deve ser esse eu acho)
x_train, x_valid, y_train, y_valid = train_test_split(X,Y, test_size=0.2, random_state=42)

 ## mostra o tamanho dos sets
print("Tamanhos de treino e validaçao\nx é uma matriz de amostrs x propriedades y é so amostras")
print("x_train:", x_train.shape)
print("x_valid:", x_valid.shape)
print("y_train:", y_train.shape)
print("y_valid:", y_valid.shape)

# Agora precisamos normalizar

 ## é uma classe responsável por deixar todos os dados, principalemnte os muitos diferentes entre sí próximos
 ## se temos idades que vao de 1 a 100 e alturas de 1 a 2 mesmo que a altura importe muito para ela vai ser 
 ## completamente apagada pela informação da idade que vai acabar importante muito mais nas contas (e talvez 
 ## isso nem sej ao caso na realidade então precisamos deixar todos os números próximos)
scaler = StandardScaler()

 ## esse método calcula o z-score e o aplica aos dados para normaliza-los z = (valor - media)/ desvio padrão da população
x_train_scaled = scaler.fit_transform(x_train)
x_valid_scaled = scaler.fit_transform(x_valid)

 ## mostra os as 5 primeiras linhas desse novo dataset
x_train_scaled[:5]

# Agora vamos aplicar a regressão logística

 ## essa é a classe que de fato faz a regressão logística
model = LogisticRegression()
 
 ## chama o metodo de treinamento
model.fit(x_train_scaled, y_train)

# Temos que verificar se o modelo realmente aprendeu algo

 ## o modelo faz a predição (diz, com base no que aprendeu qual seria o resultado)
 ## o retorno aqui é um lista delas
y_pred = model.predict(x_valid_scaled)

 ## quero ver as predições vs. o gabarito de alguns Y
print("Valores reais (y_valid):", y_valid[:10].values)
print("Valores previstos (y_pred):", y_pred[:10])

 ## cálculo da acurácia
acuracia = accuracy_score(y_valid, y_pred)
print(f'Acurácia: {acuracia:.4f}')

 ## cálculo da matriz de confusão com um método específico 
matrix_confusion = confusion_matrix(y_valid, y_pred)

 ## serve para plotar (tornar visível) a matriz
ConfusionMatrixDisplay(matrix_confusion).plot()

# Acho que vale a pena salvar o modelo

joblib.dump(model, 'modelo_pred_cancer.pkl')
