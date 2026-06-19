
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="TransformX",
    page_icon="💪",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------

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
    font-size:55px;
    font-weight:800;
    color:#4F46E5;
    margin-bottom:0px;
}

.subtitle{
    text-align:center;
    color:#64748B;
    font-size:18px;
    margin-bottom:30px;
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

h1,h2,h3{
    color:#0F172A;
}

.block-container{
    padding-top:2rem;
}

</style>
""", unsafe_allow_html=True)

# ---------------- FOOD DATABASE ----------------

foods = {
    "Chicken Breast": {"Calories":165, "Protein":31, "Carbs":0, "Fat":3.6},
    "Egg": {"Calories":155, "Protein":13, "Carbs":1.1, "Fat":11},
    "Paneer": {"Calories":265, "Protein":18, "Carbs":1.2, "Fat":20},
    "Rice": {"Calories":130, "Protein":2.7, "Carbs":28, "Fat":0.3},
    "Oats": {"Calories":389, "Protein":17, "Carbs":66, "Fat":7},
    "Milk": {"Calories":42, "Protein":3.4, "Carbs":5, "Fat":1},
    "Banana": {"Calories":89, "Protein":1.1, "Carbs":23, "Fat":0.3},
    "Apple": {"Calories":52, "Protein":0.3, "Carbs":14, "Fat":0.2},
    "Peanut Butter": {"Calories":588, "Protein":25, "Carbs":20, "Fat":50},
    "Broccoli": {"Calories":34, "Protein":2.8, "Carbs":7, "Fat":0.4}
}

# ---------------- HEADER ----------------

st.markdown('<div class="main-title">💪 TransformX</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Body Transformation & Nutrition Dashboard</div>', unsafe_allow_html=True)

# ---------------- USER PROFILE ----------------

st.header("👤 User Profile")

col1, col2, col3 = st.columns(3)

with col1:
    name = st.text_input("Name")

with col2:
    age = st.number_input("Age", 10, 100, 20)

with col3:
    gender = st.selectbox("Gender", ["Male", "Female"])

col4, col5, col6 = st.columns(3)

with col4:
    height = st.number_input("Height (cm)", 100, 250, 170)

with col5:
    weight = st.number_input("Weight (kg)", 30, 200, 70)

with col6:
    goal = st.selectbox(
        "Goal",
        ["Weight Loss", "Muscle Gain", "Maintain Weight"]
    )

# ---------------- BMI ----------------

st.header("📊 BMI Calculator")

bmi = weight / ((height / 100) ** 2)

if bmi < 18.5:
    status = "Underweight"
elif bmi < 25:
    status = "Normal"
elif bmi < 30:
    status = "Overweight"
else:
    status = "Obese"

c1, c2 = st.columns(2)

with c1:
    st.metric("BMI", round(bmi, 2))

with c2:
    st.metric("Status", status)

# ---------------- CALORIES ----------------

st.header("🔥 Daily Calories")

bmr = 10 * weight + 6.25 * height - 5 * age

if gender == "Male":
    bmr += 5
else:
    bmr -= 161

maintenance = int(bmr * 1.55)
loss = maintenance - 500
gain = maintenance + 300

c1, c2, c3 = st.columns(3)

c1.metric("Maintain", maintenance)
c2.metric("Weight Loss", loss)
c3.metric("Muscle Gain", gain)

# ---------------- WATER ----------------

st.header("💧 Water Intake")

water = round(weight * 0.04, 2)

st.metric("Recommended Water (Litres)", water)

# ---------------- FOOD SEARCH ----------------

st.header("🥗 Food Nutrition")

food = st.selectbox("Select Food", list(foods.keys()))

food_data = foods[food]

df = pd.DataFrame(
    food_data.items(),
    columns=["Nutrient", "Value"]
)

st.table(df)

# ---------------- FOOD COMPARISON ----------------

st.header("⚖️ Food Comparison")

col1, col2 = st.columns(2)

with col1:
    food1 = st.selectbox("Food 1", list(foods.keys()))

with col2:
    food2 = st.selectbox("Food 2", list(foods.keys()), index=1)

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

st.plotly_chart(fig, use_container_width=True)

# ---------------- BEST FOODS ----------------

st.header("🏆 Best Foods For Your Goal")

if goal == "Muscle Gain":
    st.success("""
    ✔ Chicken Breast

    ✔ Eggs

    ✔ Paneer

    ✔ Oats

    ✔ Peanut Butter
    """)

elif goal == "Weight Loss":
    st.success("""
    ✔ Broccoli

    ✔ Apple

    ✔ Banana

    ✔ Chicken Breast

    ✔ Oats
    """)

else:
    st.success("""
    ✔ Rice

    ✔ Milk

    ✔ Fruits

    ✔ Vegetables

    ✔ Eggs
    """)

# ---------------- MEAL PLAN ----------------

st.header("🍽 Sample Meal Plan")

if goal == "Muscle Gain":

    st.info("""
    Breakfast:
    Oats + Milk + Banana

    Lunch:
    Rice + Chicken Breast

    Dinner:
    Paneer + Roti

    Snacks:
    Peanut Butter Sandwich
    """)

elif goal == "Weight Loss":

    st.info("""
    Breakfast:
    Oats + Apple

    Lunch:
    Chicken + Salad

    Dinner:
    Paneer + Vegetables

    Snacks:
    Fruits
    """)

else:

    st.info("""
    Breakfast:
    Milk + Oats

    Lunch:
    Rice + Dal

    Dinner:
    Roti + Paneer

    Snacks:
    Fruits
    """)

# ---------------- PROGRESS TRACKER ----------------

st.header("🎯 Transformation Tracker")

target = st.number_input(
    "Target Weight (kg)",
    30,
    200,
    int(weight)
)

progress = min(weight / target, 1.0)

st.progress(progress)

st.write(
    f"Current Weight: {weight} kg | Target Weight: {target} kg"
)

# ---------------- FOOTER ----------------

st.markdown("---")
st.markdown(
    "<center>💪 TransformX | Built with Streamlit</center>",
    unsafe_allow_html=True
)
