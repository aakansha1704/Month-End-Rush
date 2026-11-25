import streamlit as st
import pandas as pd

st.title("Month-End-Rush")

if "score" not in st.session_state:
    st.session_state.score= 0
    st.session_state.health=100
    st.session_state.audited=False

col1, col2, col3 = st.columns(3)
col1.metric("Period", "Q1-Jan")
col2.metric("Compliance Health",f"{st.session_state.health}%")
col3.metric("Audit Score",f"{st.session_state.score} pts")

st.divider()

lsb1 = [{'ID':101, 'Market':'Germany', 'Cost_Center':'CC123','Currency':'EUR','Amt':12344.15},{'ID':102, 'Market':'France', 'Cost_Center':'CC127','Currency':'USD','Amt':12944.15}, {'ID':103, 'Market':'Spain', 'Cost_Center':'CC133','Currency':'EUR','Amt':14344.35},{'ID':104, 'Market':'India', 'Cost_Center':'CC143','Currency':'INR','Amt':17344.65}, {'ID':105, 'Market':'Italy', 'Cost_Center':None,'Currency':'EUR','Amt':19344.15}]

df=pd.DataFrame(lsb1)
st.subheader("Incoming Subsidiary Batch")
st.dataframe(df,use_container_width=True)
if st.button("Inspect Batch"):
    st.write("Welcome to your monthly closing!")
    st.session_state.score+=50
    st.session_state.audited=True
    st.rerun()
if  st.session_state.audited:
    missing_cc=df["Cost_Center"].isna()
    wrong_currency = (df["Market"].isin(["Germany","France","Spain","Italy"])) & (df["Currency"]!="EUR")
    quarantine_df = df[missing_cc|wrong_currency]
    st.error("Quarantined Postings Detected")
    st.dataframe(quarantine_df,use_container_width=True)
