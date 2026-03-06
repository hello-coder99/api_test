from flask import Flask,request,render_template
import requests
app=Flask(__name__)
def get_data(ip):
    url=f"http://ip-api.com/json/{ip}"
    data=requests.get(url).json()
    return data
"""
status : success
country : Japan
countryCode : JP
region : 13
regionName : Tokyo
city : Chiyoda City
zip : 100-0001
lat : 35.694
lon : 139.754
timezone : Asia/Tokyo
isp : Akamai International B.V.
org : Akamai Technologies, Inc.
as : AS20940 Akamai International B.V.
query : 23.48.0.1
data = requests.get(url).json()
"""
@app.route("/")
def about_location():
    ip=request.args.get("ip")
    if not ip:
        return "go to the argument /?ip=??"
    data=get_data(ip)
    status=data["status"]
    country=data["country"]
    countryCode=data["countryCode"]
    region=data["region"]
    regionName=data["regionName"]
    city=data["city"]
    zipcode=data["zip"]
    lat=data["lat"]
    lon=data["lon"]
    timezone=data["timezone"]
    isp=data["isp"]
    org=data["org"]
    assure=data["as"]
    query=data["query"]
    return render_template("iploc2.html",
                           status=status,
                           country=country,
                           countryCode=countryCode,
                           region=region,
                           regionName=regionName,
                           city=city,
                           zipcode=zipcode,
                           lat=lat,
                           lon=lon,
                           timezone=timezone,
                           isp=isp,
                           org=org,
                           assure=assure,
                           query=query)



app.run()
