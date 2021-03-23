import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pywhatkit as kit

#URL Apija
url = "https://api.nomics.com/v1/markets?key=ca8d50c8ba35a730557fb6b03d4b7a48"

#parametar pretrage podataka
parameters = {
   
   'base':"BTC",
   'quote':'USD',
   'start':'1',
   'limit':'2'

}

headers = {
    'Accepts':'application/json'
}

class Worker:

    def getBTCdaily(): #Kaci se na API i uzima vrijednost BitCoina
        session = Session()
        session.headers.update(headers)

        try:
            response = session.get(url, params=parameters)
            global data
            data = json.loads(response.text)
            print(json.dumps(data, indent=4))

        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)


    def sendBTCtoWP(getBTCDaily): #salje @data koju je uzeo sa API na broj telefona
        kit.sendwhatmsg("+38761156814", "Vrijednost tvog BitCoina je: " + data, 23, 23)


        

        
 



