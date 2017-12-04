import json
from flask import Flask, jsonify, request, render_template
import config
from models import db, RiskType, CustomField
from serializer import RiskTypeSerializer

app = Flask(__name__)
app.config['MONGOALCHEMY_DATABASE'] = config.DATABASE
app.config['MONGOALCHEMY_CONNECTION_STRING'] = config.URI


@app.route('/')
def index():
    return render_template("risk_types.html")
    

@app.route('/risktype', methods=['GET'])
def get_all_risks():
    all = RiskType.query.all()
    result = []
    for risk in all:
        result.append(RiskTypeSerializer.serialize(risk))
    return jsonify(result)


@app.route('/risktype', methods=['POST'])
def add_risk():
    risk = RiskTypeSerializer.deserialize(request.json)
    risk.save()

    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)