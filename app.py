import streamlit as st
import pandas as pd
import joblib
import json

st.set_page_config(page_title="Cyber AI", layout="centered")

# اللغات
with open("lang.json", "r", encoding="utf-8") as f:
    lang = json.load(f)
code = st.selectbox("🌐 Language / اللغة", ["en", "fr", "ar"])
T = lang[code]

st.title(T["title"])

model = joblib.load("models/cyber_ai_model.pkl")

ip = st.text_input(T["input_ip"])
protocol = st.selectbox(T["input_protocol"], ["TCP", "UDP", "ICMP"])

if st.button(T["predict_button"]):
    if ip and protocol:
        df = pd.DataFrame([[ip, protocol]], columns=["src_ip", "protocol"])
        df["src_ip"] = pd.factorize(df["src_ip"])[0]
        df["protocol"] = pd.factorize(df["protocol"])[0]
        pred = model.predict(df)
        if pred[0] == 1:
            st.error(T["alert"])
        else:
            st.success(T["safe"])
