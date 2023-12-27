# Libraries and frameworks
import uvicorn
from fastapi import FastAPI
import csv
import whoisdomain
import pycountry
import joblib
from tortoise.contrib.fastapi import register_tortoise

# Local files
from helpers import get_domain_name, reviewTester
from models import PhishingReportSchema, reviewDetectionSchema, PhishingReport
from news_predictor import PredictionModel

# Initialize FastAPI
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
@app.put('/report/{id}')
async def update(id: int, real: bool):
	try:
		await PhishingReport.filter(id=id).update(real=real)
		if real:
			with open('Datasets\phishing_site_urls.csv', 'a', newline='') as f:
				writer = csv.writer(f)
				writer.writerow(str(PhishingReport.get(id=id).url),"bad")
		return {'result': 'success'}
	except:
		return {'result': 'failed'}


# Get website details from whois
@app.get('/details')
async def whois(url: str):
	domain = get_domain_name(url)
	whois_data = whoisdomain.query(domain)
	name = whois_data.name
	registrar = whois_data.registrar
	registrant_country = whois_data.registrant_country
	creation_date = whois_data.creation_date.strftime('%Y/%m/%d')
	expiration_date = whois_data.expiration_date.strftime('%Y/%m/%d')
	last_updated = whois_data.last_updated.strftime('%Y/%m/%d')
	dnssec = whois_data.dnssec
	registrant = whois_data.registrant
	emails = whois_data.emails
	country_name = pycountry.countries.get(alpha_2=registrant_country).name
	
	return { 
		"name": name,
		"registrar": registrar, 
		"registrant_country": registrant_country, 
		"creation_date": creation_date,
		"expiration_date": expiration_date,
		"last_updated": last_updated,
		"dnssec": dnssec,
		"registrant": registrant, 
		"emails": emails,
		"country_name": country_name
		}

#check if a given review is real or fake on a post request that also needs a url
@app.post('/review')
async def check(review: reviewDetectionSchema):
	prediction = reviewTester(review.review)
	return {'prediction': f'{prediction}'}

#check if a given news is real or fake on a post request that only needs a news
@app.post('/news')
async def check(news: str):
	if len(news) > 30:
		model = PredictionModel(news)
		prediction = model.predict()
	else:
		prediction = 'not enough news to check'
	return {'prediction': f'{prediction}' }

# Run API with uvicorn
if __name__ == '__main__':
	uvicorn.run(app,host="127.0.0.1",port=8000)
