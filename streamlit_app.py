import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Fitness Buddy",
    page_icon="🏋️",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

.stApp{
    background: linear-gradient(
        135deg,
        #F8FAFC 0%,
        #EEF2FF 50%,
        #ECFEFF 100%
    );
}

.main-title{
    text-align:center;
    font-size:60px;
    font-weight:800;
    color:#4F46E5;
    margin-bottom:0px;
}

.subtitle{
    text-align:center;
    color:#64748B;
    font-size:20px;
    margin-bottom:25px;
}

div[data-testid="stMetric"]{
    background:white;
    padding:15px;
    border-radius:20px;
    box-shadow:0 8px 20px rgba(0,0,0,0.08);
}

section[data-testid="stSidebar"]{
    background:white;
}

.block-container{
    padding-top:2rem;
}

h1,h2,h3{
    color:#0F172A;
}

[data-testid="stMetricValue"]{
    color:#4F46E5;
}

</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================

with st.sidebar:

    st.title("🏋️ Fitness Buddy")

    st.markdown("---")

    st.success("💪 Body Analysis")
    st.info("🥗 Smart Nutrition")
    st.warning("⚖️ Compare Foods")
    st.success("🎯 Goal Tracking")

    st.markdown("---")

    st.write("Built with ❤️ using Streamlit")

# =========================
# FOOD DATABASE
# =========================

foods = {
    "Chicken Breast": {"Calories":165,"Protein":31,"Carbs":0,"Fat":3.6},
    "Egg": {"Calories":155,"Protein":13,"Carbs":1.1,"Fat":11},
    "Paneer": {"Calories":265,"Protein":18,"Carbs":1.2,"Fat":20},
    "Rice": {"Calories":130,"Protein":2.7,"Carbs":28,"Fat":0.3},
    "Oats": {"Calories":389,"Protein":17,"Carbs":66,"Fat":7},
    "Milk": {"Calories":42,"Protein":3.4,"Carbs":5,"Fat":1},
    "Banana": {"Calories":89,"Protein":1.1,"Carbs":23,"Fat":0.3},
    "Apple": {"Calories":52,"Protein":0.3,"Carbs":14,"Fat":0.2},
    "Peanut Butter": {"Calories":588,"Protein":25,"Carbs":20,"Fat":50},
    "Broccoli": {"Calories":34,"Protein":2.8,"Carbs":7,"Fat":0.4},
    "Almonds": {"Calories":579,"Protein":21,"Carbs":22,"Fat":50},
    "Fish": {"Calories":206,"Protein":22,"Carbs":0,"Fat":12}
}

# =========================
# HEADER
# =========================

st.markdown("""
<div class="main-title">
🏋️ Fitness Buddy
</div>

<div class="subtitle">
Your Personal Nutrition & Body Transformation Companion
</div>
""", unsafe_allow_html=True)

# =========================
# HERO STATS
# =========================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🔥 Calories Tracked", "10K+")

with col2:
    st.metric("🥗 Foods Available", "500+")

with col3:
    st.metric("💪 Fitness Goals", "3")

st.markdown("---")

# =========================
# PROFILE
# =========================

st.header("👤 Your Profile")

c1, c2, c3 = st.columns(3)

with c1:
    name = st.text_input("Name")

with c2:
    age = st.number_input("Age", 10, 100, 20)

with c3:
    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

c4, c5, c6 = st.columns(3)

with c4:
    height = st.number_input(
        "Height (cm)",
        100,
        250,
        170
    )

with c5:
    weight = st.number_input(
        "Weight (kg)",
        30,
        200,
        70
    )

with c6:
    goal = st.selectbox(
        "Fitness Goal",
        [
            "Weight Loss",
            "Muscle Gain",
            "Maintain Weight"
        ]
    )

st.markdown("---")

# =========================
# BMI
# =========================

st.header("📈 Body Analysis")

bmi = weight / ((height/100) ** 2)

if bmi < 18.5:
    status = "Underweight"
elif bmi < 25:
    status = "Healthy"
elif bmi < 30:
    status = "Overweight"
else:
    status = "Obese"

left, right = st.columns([1,1])

with left:

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=bmi,
        title={"text":"BMI Score"},
        gauge={
            "axis":{"range":[0,40]}
        }
    ))

    st.plotly_chart(fig, use_container_width=True)

with right:

    st.metric(
        "BMI Category",
        status
    )

    st.metric(
        "Current BMI",
        round(bmi,2)
    )

st.markdown("---")

# =========================
# CALORIES
# =========================

st.header("🔥 Daily Calorie Requirement")

bmr = 10*weight + 6.25*height - 5*age

if gender == "Male":
    bmr += 5
else:
    bmr -= 161

maintenance = int(bmr * 1.55)
loss = maintenance - 500
gain = maintenance + 300

a,b,c = st.columns(3)

a.metric("Maintain Weight", maintenance)
b.metric("Weight Loss", loss)
c.metric("Muscle Gain", gain)

st.markdown("---")

# =========================
# WATER
# =========================

st.header("💧 Hydration Tracker")

water = round(weight * 0.04, 2)

st.metric(
    "Recommended Water Intake (L/day)",
    water
)

st.markdown("---")

# =========================
# FOOD SEARCH
# =========================

st.header("🥗 Smart Nutrition")

food = st.selectbox(
    "Select Food",
    list(foods.keys())
)

food_data = foods[food]

food_df = pd.DataFrame(
    food_data.items(),
    columns=["Nutrient","Value"]
)

st.dataframe(
    food_df,
    use_container_width=True
)

# Nutrition Donut

macro_df = pd.DataFrame({
    "Macro":["Protein","Carbs","Fat"],
    "Value":[
        food_data["Protein"],
        food_data["Carbs"],
        food_data["Fat"]
    ]
})

fig = px.pie(
    macro_df,
    names="Macro",
    values="Value",
    hole=0.6,
    title=f"{food} Macro Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

# =========================
# FOOD COMPARISON
# =========================

st.header("⚖️ Compare Foods")

col1,col2 = st.columns(2)

with col1:
    food1 = st.selectbox(
        "Food 1",
        list(foods.keys())
    )

with col2:
    food2 = st.selectbox(
        "Food 2",
        list(foods.keys()),
        index=1
    )

compare_df = pd.DataFrame({
    "Nutrient":["Calories","Protein","Carbs","Fat"],
    food1:[
        foods[food1]["Calories"],
        foods[food1]["Protein"],
        foods[food1]["Carbs"],
        foods[food1]["Fat"]
    ],
    food2:[
        foods[food2]["Calories"],
        foods[food2]["Protein"],
        foods[food2]["Carbs"],
        foods[food2]["Fat"]
    ]
})

fig = px.bar(
    compare_df,
    x="Nutrient",
    y=[food1, food2],
    barmode="group",
    title="Food Nutrition Comparison"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

# =========================
# BEST FOODS
# =========================

st.header("🏆 Best Foods For Your Goal")

if goal == "Muscle Gain":

    st.success("""
✅ Chicken Breast

✅ Eggs

✅ Paneer

✅ Oats

✅ Peanut Butter

✅ Fish
""")

elif goal == "Weight Loss":

    st.success("""
✅ Broccoli

✅ Apple

✅ Banana

✅ Chicken Breast

✅ Oats

✅ Fish
""")

else:

    st.success("""
✅ Rice

✅ Fruits

✅ Milk

✅ Eggs

✅ Vegetables
""")

st.markdown("---")

# =========================
# MEAL PLAN
# =========================

st.header("🍽 Personalized Meal Plan")

if goal == "Muscle Gain":

    st.info("""
Breakfast:
🥣 Oats + Milk + Banana

Lunch:
🍚 Rice + Chicken Breast

Dinner:
🧀 Paneer + Roti

Snack:
🥜 Peanut Butter Sandwich
""")

elif goal == "Weight Loss":

    st.info("""
Breakfast:
🍎 Apple + Oats

Lunch:
🥗 Salad + Chicken

Dinner:
🥦 Vegetables + Paneer

Snack:
🍌 Banana
""")

else:

    st.info("""
Breakfast:
🥣 Oats + Milk

Lunch:
🍚 Rice + Dal

Dinner:
🧀 Paneer + Roti

Snack:
🍎 Fruits
""")

st.markdown("---")

# =========================
# GOAL TRACKER
# =========================

st.header("🎯 Goal Tracker")

target_weight = st.number_input(
    "Target Weight (kg)",
    30,
    200,
    int(weight)
)

if target_weight > 0:
    progress = min(weight / target_weight, 1.0)

    st.progress(progress)

    st.write(
        f"Current Weight: {weight} kg | Target Weight: {target_weight} kg"
    )

st.markdown("---")

# =========================
# FOOTER
# =========================

st.markdown("""
<hr>

<center>

<h3>🏋️ Fitness Buddy</h3>

<p>
Track nutrition, compare foods, calculate calories,
and achieve your dream physique.
</p>

<p>
Made with ❤️ using Streamlit
</p>

</center>
""", unsafe_allow_html=True)
