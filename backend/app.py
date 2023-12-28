# Libraries and frameworks
import uvicorn
from fastapi import FastAPI
import csv
import whoisdomain
import pycountry
from tortoise.contrib.fastapi import register_tortoise
from fastapi.middleware.cors import CORSMiddleware


# Local files
from helpers import get_domain_name, reviewTester, phish_model_ls
from models import PhishingReportSchema, reviewDetectionSchema, PhishingReport, newsDetectionSchema, mistakePhishingReport
from news_predictor import PredictionModel

# Initialize FastAPI
app = FastAPI()

# Connect to database
register_tortoise(
    app,
    db_url="sqlite://db\db.sqlite3",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],
)
# API root
@app.get('/')
async def index():
	return {
		"GET": {
			"/phishing": "Takes a URL as a parameter and returns True if the website is phishing, False if it is not.",
			"/reports": "Returns all the reports the users have reported.",
			"/details": "Takes a URL as a parameter and returns details about the domain such as name, registrar, registrant country, creation date, expiration date, last updated, dnssec, registrant, emails, and country name."
		},
		"POST": {
			"/report": {
				"description": "Takes a URL and a reason as parameters and reports a website. Returns 'already reported' if the website has already been reported, 'invalid url' if the URL is invalid, and 'success' if the report was successful.",
				"format": {
					"url": "www.example.com",
					"Reason": "very bad example."
				}
			},
			"/review": {
				"description": "Takes a URL and a review as parameters and checks if the review is fake. Returns True if the review is fake, False if it is legit.",
				"format": {
					"url": "www.example.com",
					"review": "very bad example."
				}
			},
			"/news": {
				"description": "Takes a news text as a parameter and checks if the news is fake. Returns True if the news is fake, False if it is legit.",
				"format": {
					"news": "This might be a real or fake news"
				}
			}
		},
		"PUT": {
			"/reports/{id}": {
				"description": "Takes an id and a boolean value as parameters and sets the validity of the report. Returns 'success' if the operation was successful, 'failed' if it was not.",
				"format": "/reports/{id}?real={true || false}"
			}
		}
	}

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


# report mistake phishing and save to database
@app.post('/report_mistake')
async def report_mistake(report: PhishingReportSchema):
	domain = get_domain_name(report.url)
	reports = await mistakePhishingReport.all()
	urls = [report.url for report in reports]
	if domain in urls:
		return {'result': 'already reported'}
	elif not domain:
		return {'result': 'invalid url'}
	report = mistakePhishingReport(url=domain, reason=report.reason, real=True)
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
	try:
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
		try:
			country_name = pycountry.countries.get(alpha_2=registrant_country).name
		except:
			country_name = 'Unknown'
		
	except:
		name = 'Unknown'
		registrar = 'Unknown'
		registrant_country = 'Unknown'
		creation_date = 'Unknown'
		expiration_date = 'Unknown'
		last_updated = 'Unknown'
		dnssec = 'Unknown'
		registrant = 'Unknown'
		emails = 'Unknown'
		country_name = 'Unknown'
	print(name, registrar, registrant_country, creation_date, expiration_date, last_updated, dnssec, registrant, emails, country_name)	
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
		"country_name": country_name,
		"domain" : domain
		}

#check if a given review is real or fake on a post request that also needs a url
@app.post('/review')
async def check(review: reviewDetectionSchema):
	prediction = reviewTester(review.review)
	print(prediction)
	return {'prediction': f'{prediction}'}

#check if a given news is real or fake on a post request that only needs a news
@app.post('/news')
async def check(news: newsDetectionSchema):
	if len(news.news) > 30:
		model = PredictionModel(news.news)
		prediction = model.predict()['prediction']
	else:
		prediction = 'not enough news to check'
	return {'prediction': f'{prediction}' }

# Run API with uvicorn
if __name__ == '__main__':
	uvicorn.run(app,host="127.0.0.1",port=8000)
