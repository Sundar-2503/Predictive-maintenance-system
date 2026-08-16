import joblib
import pandas as pd
import streamlit as st

model=joblib.load("E:/New folder/predictive-maintenance-system/models/random_forest_model.pkl")
scaler=joblib.load("E:/New folder/predictive-maintenance-system/models/scaler.pkl")

st.title("AI Powered Predictive Maintenance System")
machine_type=st.selectbox(
    "Machine Type",
    ["L","M","H"]
)
machine_mapping={
    "L":0,
    "M":1,
    "H":2
}
air_temperature=st.number_input(
    "Air Temperature (K)",
    value=300.0
)
process_temperature=st.number_input(
    "Process Temperature (K)",
    value=310.0
)
rotational_speed=st.number_input(
    "Rotational speed (rpm)",
    value=1500.0
)
torque=st.number_input(
    "Torque (Nm)",
    value=40.0
)
tool_wear=st.number_input(
    "Tool Wear (min)",
    value=100.0
)
if st.button("Predict"):
    temperature_difference=(process_temperature-air_temperature)
    wear_torque_ratio=(tool_wear/(torque+1))
    machanical_stress=(torque*rotational_speed)
    thermal_stress=(process_temperature*air_temperature)
    input_data=pd.DataFrame(
        [[
            machine_mapping[machine_type],
            air_temperature,
            process_temperature,
            rotational_speed,
            torque,
            tool_wear,
            temperature_difference,
            wear_torque_ratio,
            machanical_stress,
            thermal_stress
        ]],
        columns=[
            "Type",
            "Air temperature [K]",
            "Process temperature [K]",
            "Rotational speed [rpm]",
            "Torque [Nm]",
            "Tool wear [min]",
            "Temperature Difference",
            "Wear Torque Ratio",
            "Machanical Stress",
            "Thermal Stress"
        ]
    )
    input_scaled=scaler.transform(input_data)
    prediction=model.predict(input_scaled)[0]
    probability=(model.predict_proba(input_scaled)[0][1])
    if prediction==1:
        st.error(f"Failure detected ({probability:.2f})")
    else:
        st.success(f"Machine Healthy ({1-probability:.2f})")
