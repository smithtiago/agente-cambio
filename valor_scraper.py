import requests
import json
from datetime import datetime

def get_exchange_rate():
    """
    Usa uma API pública estável (Open Exchange Rates ou similar via RapidAPI ou fonte direta).
    Para turismo no Brasil, as fontes mais estáveis sem bloqueio são APIs de bancos ou 
    indexadores que não bloqueiam User-Agents simples.
    """
    # Vamos usar a cotação comercial e adicionar um spread médio (turismo é aprox 4% acima)
    # Ou buscar de um indexador que permita acesso.
    
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            usd_brl = data['rates']['BRL']
            eur_brl = usd_brl / data['rates']['EUR']
            
            # Spread médio turismo (4%)
            spread = 1.04
            
            return {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "source": "ExchangeRate-API (Calculado Turismo)",
                "currencies": {
                    "dolar_turismo": round(usd_brl * spread, 4),
                    "euro_turismo": round(eur_brl * spread, 4)
                }
            }
    except Exception as e:
        return {"error": str(e)}
    return {"error": "unknown"}

if __name__ == "__main__":
    res = get_exchange_rate()
    print(json.dumps(res, indent=4))
