# Create your own API 
# Tutorial from John Watson Rooney YouTube channel

from fastapi import FastAPI
from Scraper import Scraper

app = FastAPI()
quotes = Scraper()

@app.get('/{category}')
async def read_item(category):
    return quotes.scrape_data(category)

# In Terminal, type: uvicorn FastAPI-Uvicorn:app --reload
# 'FastAPI-Uvicorn' is whatever you called the file. Usually it will be called 'main'
# 'app' is whatever you called the object 

# http://127.0.0.1:8000/docs 
# That will show you all the endpoints your API has