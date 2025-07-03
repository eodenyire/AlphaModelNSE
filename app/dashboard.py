# Streamlit interactive UI
import streamlit as st  
import plotly.graph_objects as go  

def create_dashboard(model):  
    st.title("NSE Alpha Model Dashboard")  
    
    # Input widgets  
    rsi = st.slider("RSI (14-day)", 0, 100, 50)  
    macd = st.number_input("MACD", value=0.0)  
    pe_ratio = st.number_input("P/E Ratio", value=15.0)  
    sentiment = st.text_area("News Headline")  
    
    # Prediction  
    features = preprocess_inputs(rsi, macd, pe_ratio, sentiment)  
    prob_up = model.predict(features)[0]  
    
    # Visualize  
    fig = go.Figure(go.Indicator(  
        mode="gauge+number",  
        value=prob_up * 100,  
        title="Probability of 3-Day Gain",  
        gauge={'axis': {'range': [0, 100]}}  
    ))  
    st.plotly_chart(fig)  
    
    if prob_up > 0.7:  
        st.success("STRONG BUY SIGNAL")  
    elif prob_up < 0.3:  
        st.error("STRONG SELL SIGNAL")  
