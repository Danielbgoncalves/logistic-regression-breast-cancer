# Regressão Logistica para identificação de Câncer de Mama

Este projeto utiliza **regressão logística** para classificar tumores de mama como **malignos** ou **benignos**, com base em características extraídas de imagens de exames.
Há, além dos códigos do modelo um arquivo com explicações teóricas. No código também há comentários que tentam explicar cada parte do código. 

## Dataset

Utilizei o [Breast Cancer Wisconsin Diagnostic Dataset](https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic), que contém 569 amostras, cada uma com 30 características numéricas derivadas de imagens digitais de biópsias de mama.

### Colunas utilizadas:
Foram selecionadas as **10 médias** principais:

- `radius_mean`
- `texture_mean`
- `perimeter_mean`
- `area_mean`
- `smoothness_mean`
- `compactness_mean`
- `concavity_mean`
- `concave_points_mean`
- `symmetry_mean`
- `fractal_dimension_mean`

A coluna `diagnosis` foi usada como rótulo (`M` para maligno, `B` para benigno). Converti para `1` e `0` respectivamente.

---

## Modelo

- Algoritmo: `LogisticRegression` (da scikit-learn)
- Dados normalizados com `StandardScaler`
- Avaliação com `accuracy_score` e `ConfusionMatrixDisplay`
- Acurácia obtida: **~96.5%**

---
## Resultados

Um modelo simples como o produzirdo aqui (menos de 100 linhas) foi capaz de atingir acurácia de 96.49% Isso demonstra o poder desse tipo de modelo.
A matriz de confusão a seguir demonstra:

![matriz de confusão do modelo: uma matriz 2x2, 71 no canto esquerdo acima, 0 no direito acima, 4 no esquerdo de baixo e 39 no direito de baixo ](matriz_confusao.png)

---

## Como executar

1. Clone o repositório:
```bash
git clone https://github.com/Danielbgoncalves/logistic-regression-breast-cancer.git
cd logistic-regression-breast-cancer
```
2. Instale as dependências:
```bash 
pip install -r requirements.txt
```
3. Baixe também o arquivo `wdbc.data` no site da archive.ics.uci.edu

4. Execute o scrip principal:
```bash 
 python main.py
 ```

5. Ou ainda, use o jupiter notebook. O arquivo também está aqui no repositório

## Observações
Este projeto é didático e foi desenvolvido como prática de aprendizado de machine learning com dados reais.

Sinta-se à vontade para adaptar, melhorar e contribuir! 