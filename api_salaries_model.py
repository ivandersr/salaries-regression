from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import joblib
import pandas as pd

# Criar uma instância do FastAPI
app = FastAPI()

# Criar uma classe de validação dos dados de entrada (request body)
class RequestBody(BaseModel):
    tempo_na_empresa: int
    nivel_na_empresa: int

# Carregar o modelo para a prediçaõ
poly_model = joblib.load('./salaries_model.pkl')

@app.post('/predict')
def predict(data: RequestBody):
    input_features = {
        'tempo_na_empresa': data.tempo_na_empresa,
        'nivel_na_empresa': data.nivel_na_empresa
    }

    pred_df = pd.DataFrame(input_features, index=[1])

    predicted_salary = poly_model.predict(pred_df).item(0)

    return {
        'salario_em_reais': predicted_salary
    }

