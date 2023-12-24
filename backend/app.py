import uvicorn
from fastapi import FastAPI, Query
import joblib

app = FastAPI()

# Load Model
phish_model = open('phishing.pkl','rb')
phish_model_ls = joblib.load(phish_model)

# API with prediction
@app.get('/phishing')
async def predict(url: str = Query(...,min_length=1,max_length=2083)):
	X_predict = []
	X_predict.append(str(url))
	y_Predict = phish_model_ls.predict(X_predict)
	if y_Predict == 'bad':
		result = True
	else:
		result = False

	return (result)

# Run API with uvicorn
if __name__ == '__main__':
	uvicorn.run(app,host="127.0.0.1",port=8000)
    