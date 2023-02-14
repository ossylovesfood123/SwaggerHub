from flask import Flask, render_template 
import subprocess

app = Flask(__name__)

@app.route("/")

def index ():
    username = "swaggerhub"
    password = "ViptelaWan2023"


    #use curl to log into the website and get information 
    curl_command = 'curl -c cookie.txt -b cookie.txt -d "username={}&password={}" http://swaggerhub.cisco.com/apiproxy/auth/login -L -s'.format(username,password)
    output = subprocess.check_output(curl_command, shell=True)

    curl_command = 'curl -b cookie.txt http://swaggerhub.cisco.com/gw/accounts/reports/audit?orgNames=SDWan_Org -L -s'
    website_data = subprocess.check_output(curl_command, shell=True)

    return render_template("index.html", website_data=website_data.decode("utf-8"))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)


