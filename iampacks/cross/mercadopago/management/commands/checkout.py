import iampacks.cross.mercadopago
import json

CLIENT_ID="1495799923023357"
CLIENT_SECRET="Jxlm7QqG3y7fUtnfwsPcwTAzxCtzhBUI"

mp = mercadopago.MP(CLIENT_ID, CLIENT_SECRET)

print mp

preference = {
  "items": [
    {
      "title": "Test",
      "quantity": 1,
      "currency_id": "USD",
      "unit_price": 10.4
    }
  ]
}

preferenceResult = mp.create_preference(preference)

print preferenceResult 
