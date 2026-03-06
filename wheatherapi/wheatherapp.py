from flask import Flask,render_template,request
import requests
import json
import getcred

app=Flask(__name__)
def data_gen(location):
    #url=f"https://www.meteosource.com/api/v1/free/point?place_id={location}&sections=all&timezone=UTC&language=en&units=metric&key="
    #key="03387mh2qcbpvzgs4kio70udiqlf4y5pp0hbjxuy"
    url=getcred.get_url(location)
    key=getcred.get_api_key()
    print(url)
    print(key)

    url=url+key

    data=requests.get(url)

    result=data.content

    f=result.decode()
    parser=json.loads(f)
    return parser

@app.route("/")
def current_wheather():
    location=request.args.get("location")
    if not location:
        return "/location=?? not provided"
    parser=data_gen(location)
    icon=parser["current"]["icon"]
    wtype=parser["current"]["summary"]
    temperature=parser["current"]["temperature"]
    speed=parser["current"]["wind"]["speed"]
    angle=parser["current"]["wind"]["angle"]
    direction=parser["current"]["wind"]["dir"]
    pre=parser["current"]["precipitation"]
    return render_template("wheather2.html",
                            location=location,
                            icon=icon,
                            wtype=wtype,
                            temperature=temperature,
                            speed=speed,
                            angle=angle,
                            direction=direction,
                            pre=pre)
app.run()
