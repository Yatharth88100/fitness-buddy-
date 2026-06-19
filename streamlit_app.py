
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Fitness Buddy Pro", page_icon="🏋️", layout="wide")

st.markdown("""
<style>
.stApp{
background: linear-gradient(135deg,#0F172A,#111827,#1E293B);
color:white;
}
.main-title{
text-align:center;
font-size:60px;
font-weight:800;
color:#60A5FA;
}
.subtitle{
text-align:center;
font-size:20px;
color:#CBD5E1;
margin-bottom:20px;
}
h1,h2,h3,label,p,span{
color:white !important;
}
div[data-testid="stMetric"]{
background:#1E293B;
border:1px solid #3B82F6;
border-radius:20px;
padding:15px;
}
</style>
""", unsafe_allow_html=True)

foods = {
    "Chicken Breast":{"Calories":165,"Protein":31,"Carbs":0,"Fat":3.6},
    "Egg":{"Calories":155,"Protein":13,"Carbs":1.1,"Fat":11},
    "Paneer":{"Calories":265,"Protein":18,"Carbs":1.2,"Fat":20},
    "Rice":{"Calories":130,"Protein":2.7,"Carbs":28,"Fat":0.3},
    "Oats":{"Calories":389,"Protein":17,"Carbs":66,"Fat":7},
    "Banana":{"Calories":89,"Protein":1.1,"Carbs":23,"Fat":0.3}
}

with st.sidebar:
    st.title("🏋️ Fitness Buddy Pro")
    st.success("💪 Body Analysis")
    st.info("🥗 Nutrition")
    st.warning("⚖️ Food Compare")
    st.success("🎯 Goal Tracking")

st.markdown('<div class="main-title">🏋️ Fitness Buddy Pro</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Smart Nutrition & Body Transformation Dashboard</div>', unsafe_allow_html=True)

c1,c2,c3=st.columns(3)
c1.metric("🔥 Calories Tracked","10K+")
c2.metric("🥗 Foods","500+")
c3.metric("💪 Goals","3")

st.header("👤 Your Profile")
a,b,c=st.columns(3)
with a:
    age=st.number_input("Age",10,100,20)
with b:
    height=st.number_input("Height (cm)",100,250,170)
with c:
    weight=st.number_input("Weight (kg)",30,200,70)

bmi=weight/((height/100)**2)
st.header("📈 BMI Analysis")

fig=go.Figure(go.Indicator(mode="gauge+number",value=bmi,title={"text":"BMI"},
gauge={"axis":{"range":[0,40]}}))
st.plotly_chart(fig,use_container_width=True)

st.header("🥗 Food Nutrition")
food=st.selectbox("Select Food",list(foods.keys()))
st.dataframe(pd.DataFrame(foods[food].items(),columns=["Nutrient","Value"]),use_container_width=True)

macro=pd.DataFrame({
"Macro":["Protein","Carbs","Fat"],
"Value":[foods[food]["Protein"],foods[food]["Carbs"],foods[food]["Fat"]]
})
st.plotly_chart(px.pie(macro,names="Macro",values="Value",hole=0.6),use_container_width=True)

st.header("⚖️ Food Comparison")
f1=st.selectbox("Food 1",list(foods.keys()))
f2=st.selectbox("Food 2",list(foods.keys()),index=1)

compare=pd.DataFrame({
"Nutrient":["Calories","Protein","Carbs","Fat"],
f1:[foods[f1]["Calories"],foods[f1]["Protein"],foods[f1]["Carbs"],foods[f1]["Fat"]],
f2:[foods[f2]["Calories"],foods[f2]["Protein"],foods[f2]["Carbs"],foods[f2]["Fat"]]
})
st.plotly_chart(px.bar(compare,x="Nutrient",y=[f1,f2],barmode="group"),use_container_width=True)

st.success("🚀 Fitness Buddy Pro Ready")
