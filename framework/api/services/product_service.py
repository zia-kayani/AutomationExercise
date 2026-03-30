from framework.api.clients.product_client import ProductClient

class ProductService:

    def __init__(self):
        self.product_client = ProductClient()

    #get all the products list service method
    def get_all_products(self):
        response =  self.product_client.get_all_products()
        data = response.json()

        if data.get("responseCode") != 200:
            raise Exception(f"Failed to get products list. Response: {data}")
        return data

    #post to all products list service method
    def post_to_all_product_list(self):
        response = self.product_client.post_to_all_prdocut_list()
        data = response.json()

        if data.get("responseCode") != 405:
            raise Exception(f"Expected failure when using POST on products list. Response: {data}")
        return data
    
    #get all brands list service method
    def get_all_brands(self):
        response = self.product_client.get_all_brands()
        data = response.json()

        if data.get("responseCode") != 200:
            raise Exception(f"Failed to get brands list. Response: {data}")
        return data

    #update to all brand list service method 
    def put_to_all_brands(self):
        response = self.product_client.update_to_all_brands()
        data = response.json()
        if data.get("responseCode") != 405:
            raise Exception(f"failed to get 405 response code, expeceted 405 response code ")
        return data
    
    #search a product 
    def search_a_product(self, payload:dict):
        response = self.product_client.search_product(payload)
        data  = response.json()
        if data.get("responseCode") != 200:
            raise Exception(f"Failed to search product. Response: {data}")
        return data
        
    #search a product without payload
    def search_a_product_without_payload(self):
        response = self.product_client.search_product_without_payload()
        data = response.json()
        if data.get("responseCode") != 400:
            raise Exception(f"Expected failure when searching product without payload. Response: {data}")
        return data
    