from frontend_preeti import render_header, render_bust_alert, render_interval
import streamlit as st, pandas as pd
st.title("SIH26079 - Forecast Bust Detection")
c1,c2 = st.columns(2)
with c1:
    st.subheader("Step 6 Error DB")
    df=pd.read_csv("error_database.csv")
    st.metric("Samples", len(df)); st.dataframe(df.head())
with c2:
    st.subheader("Step 13: C(x)=[f(x)-q, f(x)+q]")
    st.metric("Predicted Error", "4.2 mm")
    st.metric("90% Interval", "[3.1, 5.3] mm")
    st.progress(84); st.error("BUST ALERT Delhi")
st.map(pd.DataFrame({"lat":[28.6,19.07],"lon":[77.2,72.87]}))