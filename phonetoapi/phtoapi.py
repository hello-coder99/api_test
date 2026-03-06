#issue : generally it working perfectly on us based phone number
from flask import Flask,request,render_template
import requests
import getcred

app=Flask(__name__)
def get_data(phone):
    url=getcred.get_url(phone)
    url=url+getcred.apikey
    """
    valid
    countryCode
    type
    format
    uri
    """
    data=requests.get(url)
    result=data.json()
    return result
@app.route("/",methods=["GET"])
def phone_validity_check():
    phone=request.args.get("phone")
    if not phone:
        return "/phone=???"
    result=get_data(phone)
    return render_template("validity2.html",
                           valid=result["valid"],
                           countrycode=result["countryCode"],
                           phtype=result["type"],
                           Informat=result["format"]["international"],
                           Nformat=result["format"]["national"],
                           uri=result["uri"])



app.run()
