olá!! 

Este projeto foi desenvolvido para criar uma interface web interativa para o treinamento de redes neurais,
com o objetivo específico de prever condições meteorológicas, mais precisamente se haverá chuva na Austrália no dia seguinte.
O projeto utiliza a biblioteca TensorFlow/Keras para construir e treinar modelos de aprendizado de máquina que analisam dados meteorológicos e
fazem previsões baseadas nas configurações fornecidas pelos usuários.


# Motivação do Projeto:

O projeto surgiu da necessidade de avaliar a possibilidade de chuva na Austrália no dia seguinte, utilizando redes neurais para analisar 
dados históricos e fazer previsões. O objetivo é permitir que os usuários ajustem e experimentem com diferentes configurações de modelos de
aprendizado de máquina para entender melhor o comportamento dos dados e otimizar a performance das previsões. Esta abordagem interativa facilita a 
experimentação e o ajuste fino dos modelos para obter insights precisos sobre as condições meteorológicas futuras

![image](https://github.com/user-attachments/assets/e83709f1-3705-40c0-b4a2-b4ec5c4cc2b0)


# Arquitetura do Projeto:

# Front-end (HTML/JavaScript): 
Proporciona uma interface de usuário intuitiva onde os usuários podem
configurar a arquitetura da rede neural, incluindo camadas, unidades, funções de ativação, otimizadores e funções de perda. 
Além disso, é possível definir métricas de avaliação e parâmetros de treinamento, como o número de épocas e a divisão de validação. 
Essas configurações são enviadas ao backend através de solicitações HTTP POST.

# Back-end (Flask): 
Recebe as configurações do modelo do front-end e utiliza o TensorFlow/Keras para construir, 
compilar e treinar a rede neural com base em dados meteorológicos fornecidos. A função train_model é responsável por 
todas as etapas de construção e treinamento do modelo, e também realiza a avaliação do desempenho. Os resultados, que incluem a perda e as métricas especificadas,
são retornados ao front-end para visualização.

# Dados (CSV):
O backend carrega dados meteorológicos de um arquivo CSV, realiza o pré-processamento necessário e utiliza
esses dados para treinar o modelo. As variáveis de entrada incluem informações como precipitação, umidade e pressão, 
enquanto a variável alvo é a previsão de chuva para o dia seguinte.
