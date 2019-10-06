from flask import Flask, jsonify, request, render_template
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

#@app.route('/')
#def index():
#        return render_template('index.html')


@app.route('/fullstack', methods = ['GET'])
def fullStack():
#    message = {'greeting':'Hello from Flask!'}
    #return jsonify(message)
    return "<h3>Job description </h3><p>At Ocelot, full stack developers work as a team to build modern, cloud-native products with our clients. Teams are empowered to own all facets of development including frontend, backend, infrastructure, and data pipelines.An ideal candidate will enjoy being a generalist not expected to be an expert in all of these, but enthusiastic and capable of learning and contributing wherever needed.</p> "


@app.route('/cloudeng')
def cloudEng():
    return "<h3>Job description</h3><p>As a cloud engineer, you will build and automate highly available, elastic, and secure cloud-based infrastructure to support the needs of our client workloads. You will have the opportunity to work in a wide variety of areas including infrastructure automation, security, configuration management, continuous integration, continuous deployment as well as mentoring colleagues on your team and across other engineering teams.</p>"

@app.route('/bigdata')
def bigData():
    return "<h3>Job description</h3><p>As a Big Data Engineer, you will develop innovative software using distributed data processing frameworks and techniques. Ocelot Big Data Engineers define and build data pipelines that enable our clients to make faster, better, data-informed business decision. You will work in a team environment with software engineers, analysts, and data scientists with the opportunity to mentor colleagues on your team and across other engineering teams.</p>"

if __name__ == "__main__": 
     app.run(host="0.0.0.0", port=8080)

app.run()
