from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# IBM Cloud API credentials
API_KEY = "https://private.au-syd.ml.cloud.ibm.com/ml/v4/deployments/fdfcf920-f475-42b5-a9ee-28a446a61816/predictions?version=2021-05-01"
DEPLOYMENT_URL = "https://au-syd.ml.cloud.ibm.com/ml/v4/deployments/fdfcf920-f475-42b5-a9ee-28a446a61816/predictions?version=2021-05-01"

def get_token():
    url = "https://iam.cloud.ibm.com/identity/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = f"apikey={API_KEY}&grant_type=urn:ibm:params:oauth:grant-type:apikey"
    response = requests.post(url, headers=headers, data=data)
    return response.json()["access_token"]

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        input_data = [
            float(request.form.get("road_sanctioned")),
            float(request.form.get("road_length")),
            float(request.form.get("bridges_sanctioned")),
            float(request.form.get("cost_sanctioned")),
            float(request.form.get("roads_completed")),
            float(request.form.get("length_completed")),
            float(request.form.get("bridges_completed")),
            float(request.form.get("expenditure")),
            float(request.form.get("roads_balance")),
            float(request.form.get("length_balance")),
            float(request.form.get("bridges_balance")),
            1,  # Example: Andhra Pradesh
            1   # Example: Adilabad
        ]

        payload = {
            "input_data": [
                {
                    "fields": [
                        "NO_OF_ROAD_WORK_SANCTIONED",
                        "LENGTH_OF_ROAD_WORK_SANCTIONED",
                        "NO_OF_BRIDGES_SANCTIONED",
                        "COST_OF_WORKS_SANCTIONED",
                        "NO_OF_ROAD_WORKS_COMPLETED",
                        "LENGTH_OF_ROAD_WORK_COMPLETED",
                        "NO_OF_BRIDGES_COMPLETED",
                        "EXPENDITURE_OCCURED",
                        "NO_OF_ROAD_WORKS_BALANCE",
                        "LENGTH_OF_ROAD_WORK_BALANCE",
                        "NO_OF_BRIDGES_BALANCE",
                        "STATE_NAME_Andhra Pradesh",
                        "DISTRICT_NAME_Adilabad"
                    ],
                    "values": [input_data]
                }
            ]
        }

        token = get_token()
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        response = requests.post(DEPLOYMENT_URL, headers=headers, json=payload)
        result = response.json()

        try:
            prediction = result["predictions"][0]["values"][0][0]
        except:
            prediction = "Error in prediction"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
