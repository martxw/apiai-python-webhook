#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    print("Response:")
    print(json.dumps(r, indent=4))
    r.headers['Content-Type'] = 'application/json'
    return r


def processRequest(req):
    print ("started processing again")
    if req.get("result").get("action") != "yahooWeatherForecast":
        print ("Aint no action")
        return {}
    print ("Getting result")
    result = req.get("result")
    print ("Getting parameters")
    parameters = result.get("parameters")
    print ("Getting city")
    city = parameters.get("geo-city")
    print ("Making result")
    res = makeWebhookResult("What the hell do I care about " + city + ", huh?")
    print ("finished processing again")
    return res


def makeWebhookResult(speech):
    print (speech)
    return {
        "speech": speech,
        "displayText": speech,
        # "contextOut": [],
        "source": "apiai-weather-webhook-sample"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print ("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
