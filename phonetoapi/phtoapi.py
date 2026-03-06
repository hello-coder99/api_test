import requests
apikey="gualck57akgtm5b0qn3sfogs8trmgs3mgrtgimqvkstgpe2eq9v8dso"
#url="https://anyapi.io/api/v1/phone/validate?phone_number=%2B12133734253&apiKey="
url="https://anyapi.io/api/v1/phone/validate?phone_number=%2B12133734253&apiKey="
url=url+apikey
"""
valid
countryCode
type
format
uri
"""
data=requests.get(url)
result=data.json()
#print(data.text)
print("validity :",result["valid"])
print("countryCode :",result["countryCode"])
print("Type of :",result["type"])
print("Format :",result["format"])
print("Uri :",result["uri"])

