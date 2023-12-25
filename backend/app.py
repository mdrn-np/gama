import uvicorn
from fastapi import FastAPI
import joblib
from helpers import get_domain_name
from models import PhishingReport
from tortoise.contrib.fastapi import register_tortoise
from models import PhishingReportSchema


app = FastAPI()

# Connect to database
register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True
)
# Load Model
phish_model = open('phishing.pkl','rb')
phish_model_ls = joblib.load(phish_model)

# API with prediction
@app.get('/phishing')
async def predict(url: str):
	X_predict = []
	domain = get_domain_name(url)
	X_predict.append(str(domain))
	y_Predict = phish_model_ls.predict(X_predict)
	reports = await PhishingReport.filter(real=True).all()
	urls = [report.url for report in reports]
	if domain in urls:
		result = True
	if y_Predict == 'bad':
		result = True
	else:
		result = False
	return (result)

# report phishing and save to database
@app.post('/report')
async def report(report: PhishingReportSchema):
	domain = get_domain_name(report.url)
	reports = await PhishingReport.all()
	urls = [report.url for report in reports]
	if domain in urls:
		return {'result': 'already reported'}
	elif not domain:
		return {'result': 'invalid url'}
	report = PhishingReport(url=domain, reason=report.reason)
	await report.save()
	return {'result': 'success'}

#get all reports
@app.get('/reports')
async def reports():
	reports = await PhishingReport.all()
	return reports

#update report
@app.put('/reports/{id}')
async def update(id: int, real: bool):
	await PhishingReport.filter(id=id).update(real=real)
	return {'result': 'success'}

# Run API with uvicorn
if __name__ == '__main__':
	uvicorn.run(app,host="127.0.0.1",port=8000)
