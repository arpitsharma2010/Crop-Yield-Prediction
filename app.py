from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/check")
def check():
    # Input numeric fields
    rain = float(request.args.get("rain"))
    temp = float(request.args.get("temp"))
    harvest = float(request.args.get("harvest"))
    
    # Define mapping for categorical fields
    crops = ["rice", "wheat", "soyabean", "cotton", "maize", "barley"]
    soils = ["clay", "chalky", "loam", "silt", "sandy", "peaty"]
    regions = ["north", "south", "east", "west"]
    weather = ["rainy", "cloudy", "sunny"]
    irrigation = ["yes", "no"]
    fertilizer = ["yes", "no"]
    
    # Generate one-hot encoded values
    crop_values = [1.0 if request.args.get("c1") == crop else 0.0 for crop in crops]
    soil_values = [1.0 if request.args.get("s1") == soil else 0.0 for soil in soils]
    region_values = [1.0 if request.args.get("r1") == region else 0.0 for region in regions]
    weather_values = [1.0 if request.args.get("w1") == condition else 0.0 for condition in weather]
    irri_values = [1.0 if request.args.get("ir1") == option else 0.0 for option in irrigation]
    fert_values = [1.0 if request.args.get("fe1") == option else 0.0 for option in fertilizer]
    
    # Combine all inputs into a single data list
    data = [[
        rain, temp, harvest, 
        *region_values, 
        *soil_values, 
        *crop_values, 
        *weather_values, 
        *irri_values, 
        *fert_values
    ]]
    
    # Load the model and predict
    with open("db.model", "rb") as f:
        model = pickle.load(f)
    res = model.predict(data)
    msg = f'The predicted yield of the crop per hectare is: {res[0]} tons.'
    
    # Return a pop-up script with the message
    return f"""
    <script>
        alert("{msg}");
        window.location.href = "/";
    </script>
    """

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
