import streamlit
import json
import requests

# Título da aplicação
streamlit.title('Modelo de predição de salário')

# Inputs do usuário
streamlit.write('Quantos meses o profissional está na empresa?')
tempo_na_empresa = streamlit.slider('Meses', min_value=1, max_value=120, value=60, step=1)

streamlit.write('Qual o nível do profissional na empresa?')
nivel_na_empresa = streamlit.slider('Nível', min_value=1, max_value=10, value=5, step=1)

# Preparar dados para a API
input_features = {
    'tempo_na_empresa': tempo_na_empresa,
    'nivel_na_empresa': nivel_na_empresa
}

# Criar um botão e capturar um evento deste botão para disparar para a API
if streamlit.button('Estimar salário'):
    response = requests.post(url="http://localhost:8000/predict", data=json.dumps(input_features))
    response_json = json.loads(response.text)
    salario_em_reais = round(response_json['salario_em_reais'], 2)
    streamlit.subheader(f'O salário estimado é de R$ {salario_em_reais}')