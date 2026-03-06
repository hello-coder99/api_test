from flask import Flask,render_template,request
import requests
import json
import getcred

app=Flask(__name__)
def data_gen(location):
    url=getcred.get_url(location)
    key=getcred.get_api_key()

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
    return render_template("wheather.html",
                            location=location,
                            icon=icon,
                            wtype=wtype,
                            temperature=temperature,
                            speed=speed,
                            angle=angle,
                            direction=direction,
                            pre=pre)

@app.errorhandler(404)
def info_not_found(error):
    return render_template("404.html"),404

@app.errorhandler(500)
def server_error(error):
    return render_template("500.html"),500

app.run()
