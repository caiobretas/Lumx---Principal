import csv
from json import loads
from requests import get, post

class ControllerHTTPBase:
    
    def runAPI_GET(self, endpoint) -> list:
        result = get(endpoint)
        list_: list = loads(result.text)[f'Data'][f'Data']
        return list_
    
    def get(self, endpoint: str, headers: str | None = None, type = 'JSON') -> list:
        if type.upper() == 'JSON':
            try:
                return loads(get(endpoint, headers=headers).text)
            
            except Exception as e:
                print(f'\nErr: {e}\n')
                raise e
            
        elif type.upper() == 'CSV':
            try:
                response = get(endpoint, headers=headers)
                data =  response.content.decode('utf-8').splitlines()
                return csv.DictReader(data, delimiter=';')

            except Exception as e:
                print(f'\nErr: {e}\n')
                raise e

    def post(self, obj, endpoint: str, headers: str | None) -> None:
        response = post(url=endpoint,data=obj,headers=headers)
        print(response.status_code)
        print(response.json())
        
        return response
