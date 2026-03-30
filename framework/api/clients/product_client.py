from framework.common.config.config import Config
import requests

API_BASE_URL = Config.API_BASE_URL
HEADERS = {"Content-Type": "application/x-www-form-urlencoded"}

class ProductClient:

    #get all the products list client method 
    def get_all_products(self):
        response  =  requests.get(url=f"{API_BASE_URL}/productsList" )
        return response 
    
    #post to all products list client method 
    def post_to_all_prdocut_list(self):
        response  = requests.post(url=f"{API_BASE_URL}/productsList" )
        return response 

    #get all brands list client method
    def get_all_brands(self):
        response = requests.get(url=f"{API_BASE_URL}/brandsList")
        return response

    #update to brand list client method
    def update_to_all_brands(self):
        response  = requests.put(url=f"{API_BASE_URL}/brandsList")
        return response
    
    #search a product
    def search_product(self, payload:dict):

        response =  requests.post(url=f"{API_BASE_URL}/searchProduct", headers=HEADERS, data=payload)
        return response
    
    #search a product without paylooad
    def search_product_without_payload(self):
        response = requests.post(url=f"{API_BASE_URL}/searchProduct", headers=HEADERS)
        return response