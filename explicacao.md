# Regressão Linear

- Boa para prever **valores contínuos**, como:
  - Altura
  - Idade
  - Preços
- Não funciona bem para problemas com **respostas binárias** (sim ou não), como:
  - Email é spam?
  - Vai chover?
  - Tumor é maligno?

### Fórmula Geral

\[
\hat{y} = b_0 + b_1X_1 + b_2X_2 + \ldots
\]

---

# Regressão Logística

- Ideal para **classificação binária**
- Retorna **probabilidades**
  - Exemplo: _"Há 93% de chance desse tumor ser benigno"_
- Utiliza a **função sigmoide**

### Função Sigmoide

\[
\sigma(z) = \frac{1}{1 + e^{-z}}
\]

- O resultado estará **sempre entre 0 e 1**
- \(\hat{y}\) é o valor previsto, e quanto mais longe de \(y\) real (0 ou 1), maior o **custo (erro)**

---

## Treinando o Modelo

1. Os valores iniciais de \(b_0, b_1, b_2, \ldots\) são definidos aleatoriamente ou zerados
2. Uma previsão inicial é feita com o modelo
3. O erro é avaliado com a função de perda **Log Loss**
4. Se o erro for alto, ajustamos os pesos

### Usando Gradiente Descendente

- Calcula-se a derivada da função de custo \(J\) em relação a cada peso
- **Interpretação da derivada:**
  - Derivada **positiva** → função está subindo → erro aumenta → **diminuir o peso**
  - Derivada **negativa** → função descendo → erro reduzindo → **aumentar o peso**

### Atualização dos Pesos

\[
b_i = b_i - \alpha \cdot \frac{\partial J}{\partial b_i}
\]

- \(b_i\): peso específico
- \(\alpha\): taxa de aprendizado (ex: 0.01)
  - Pode ser fixa ou otimizada com algoritmos modernos:
    - **Adam**, **Adagrad**, **RMSprop**
- \(\frac{\partial J}{\partial b_i}\): derivada parcial da função de perda em relação a \(b_i\)

---

## Avaliação do Modelo

- **Acurácia**:  
  \[
  \text{acurácia} = \frac{\text{número de acertos}}{\text{número total de amostras}}
  \]  
  Funciona bem quando as classes 0 e 1 estão balanceadas

- **Matriz de Confusão** (2x2):  
  |                | Previsto: Positivo | Previsto: Negativo |
  |----------------|--------------------|--------------------|
  | **Real: Positivo** | Verdadeiro Positivo (VP) | Falso Negativo (FN) |
  | **Real: Negativo** | Falso Positivo (FP) | Verdadeiro Negativo (VN) |

- **Precisão**:  
  \[
  \text{precisão} = \frac{VP}{VP + FP}
  \]

- **Recall**:  
  \[
  \text{recall} = \frac{VP}{VP + FN}
  \]

- **F1 Score**:  
  \[
  F1 = 2 \cdot \frac{\text{precisão} \cdot \text{recall}}{\text{precisão} + \text{recall}}
  \]

---

> ✍️ **Data**: 24 de Abril de 2025.

