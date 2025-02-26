import requests
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
import random
from keybert import KeyBERT
from transformers import pipeline

PATENT_COUNT_PER_ROW = 25

def get_base_patents(query_terms):
    df = pd.DataFrame()
    
    for query_term in query_terms:
        sart = 0
        
        query_term = '%22' + query_term + '%22'
        query_term.replace(' ', '%20')
        
        bulk_data_api_url = f"https://developer.uspto.gov/ibd-api/v1/application/publications?searchText={query_term}&start={start}&largeTextSearchFlag=Y"
        