import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path

BASE_DIR=Path(__file__).resolve().parent.parent

app=FastAPI()
MODEL_PATH = BASE_DIR / "models" / "random_forest_model.pkl"
model = joblib.load(MODEL_PATH)
SCALER_PATH = BASE_DIR / "models" / "scaler.pkl"
scaler = joblib.load(SCALER_PATH)

class MachineData(BaseModel):
    Type:int
    air_temperature:float
    process_temperature:float
    rotational_speed:float
    torque:float
    tool_wear:float
@app.get("/")
def home():
    return {"message":"Pred Maintenance API"}

@app.post("/prediction")
def predict(data:MachineData):
    temperature_difference=(
        data.process_temperature-data.air_temperature
    )
    wear_torque_ration=(
        data.tool_wear/(data.torque+1)
    )
    machanical_stress=(
        data.torque*data.rotational_speed
    )
    thermal_stress=(
        data.process_temperature*data.air_temperature
    )
    input_data=pd.DataFrame(
        [[
            data.Type,
            data.air_temperature,
            data.process_temperature,
            data.rotational_speed,
            data.torque,
            data.tool_wear,
            temperature_difference,
            wear_torque_ration,
            machanical_stress,
            thermal_stress
        ]],
        columns=[
            "Type",
            "Air temperature [k]",
            "Process temperature [K]",
            "Rotational speed [rpm]",
            "Torque [Nm]",
            "Tool wear [min]",
            "temperature difference",
            "Wear Torque Ratio",
            "Machanical Stress",
            "thermal Stress"
        ]
    )
    input_scaled=scaler.transform(input_data)
    prediction=model.predict(input_scaled)
    probability=model.predict_proba(input_scaled)[0][1]
    return{
        "machine_failure":int(prediction),
        "failure_probability":float(probability)
    }
