# import streamlit as st

# st.set_page_config(page_title="Birthday Celebration", page_icon="🎂")

# st.title("🎉 Celebrate Your Birthday! 🎉")

# name = st.text_input("Enter your name:")
# birth_date = st.date_input("Your Birth Date")

# cake_flavor = st.selectbox("Choose a cake flavor:", ["Chocolate", "Vanilla", "Strawberry"])
# toppings = st.multiselect("Pick your toppings:", ["Cherries", "Fruits", "Nuts", "Whipped Cream"])
# sprinkles = st.radio("Add sprinkles?", ["Yes", "No"])

# if st.button("🎂 Celebrate Now!"):
#     st.success(f"Happy Birthday, {name or 'Friend'}! Here's your {cake_flavor} cake!")
    
#     st.image("assets/cake.gif", caption="Your cake is ready!", use_column_width=True)
    
#     audio_file = open('assets/birthday_song.mp3', 'rb')
#     audio_bytes = audio_file.read()
#     st.audio(audio_bytes, format='audio/mp3')
import streamlit as st
import os
import random
from datetime import date, timedelta

st.set_page_config(page_title="🎉 Birthday Celebration 🎂", layout="centered")

st.title("🎉 Let's Celebrate Your Birthday!")

name = st.text_input("Enter your name:")

start_date = date.today() - timedelta(days=365*100)
end_date = date.today()

birth_date = st.date_input("Your Birth Date", value=date.today(), min_value=start_date, max_value=end_date)

cake_flavors = ["chocolate", "vanilla", "strawberry"]
topping_options = ["cherries", "fruits", "nuts", "whipped cream"]
sprinkle_options = ["yes", "no"]

cake_flavor = st.selectbox("Choose your cake flavor:", cake_flavors)
toppings = st.multiselect("Select your toppings:", topping_options)
sprinkles = st.radio("Add sprinkles?", sprinkle_options)

def surprise_me():
    random_flavor = random.choice(cake_flavors)
    random_toppings = random.sample(topping_options, random.randint(0, len(topping_options)))
    random_sprinkles = random.choice(sprinkle_options)
    return random_flavor, random_toppings, random_sprinkles

if st.button("🎉 Surprise Me!"):
    # Randomize cake options only
    cake_flavor, toppings, sprinkles = surprise_me()
    
    st.markdown(f"### Happy Birthday, {name if name else 'Friend'}! 🎈🎉")
    st.write(f"**Your birth date:** {birth_date.strftime('%B %d, %Y')}")
    st.write(f"**Cake Flavor:** {cake_flavor}")
    st.write(f"**Toppings:** {', '.join(toppings) if toppings else 'none'}")
    st.write(f"**Sprinkles:** {sprinkles}")

    topping_str = "+".join(toppings) if toppings else "none"
    filename = f"{cake_flavor}_{topping_str}_{sprinkles}.gif"
    filepath = os.path.join("assets", filename)

    if os.path.exists(filepath):
        st.image(filepath, caption="Here's your birthday cake!", use_container_width=True)
    else:
        st.warning("🎂 This cake combo isn't available yet. Try a different combination!")

    try:
        audio_file = open('assets/birthday_song.mp3', 'rb')
        st.audio(audio_file.read(), format='audio/mp3')
    except FileNotFoundError:
        st.info("🎵 Birthday song coming soon!")

elif st.button("🎂 Celebrate Now!"):
    st.markdown(f"### Happy Birthday, {name if name else 'Friend'}! 🎈🎉")
    
    topping_str = "+".join(toppings) if toppings else "none"
    filename = f"{cake_flavor}_{topping_str}_{sprinkles}.gif"
    filepath = os.path.join("assets", filename)

    if os.path.exists(filepath):
        st.image(filepath, caption="Here's your birthday cake!", use_container_width=True)
    else:
        st.warning("🎂 This cake combo isn't available yet. Try a different combination!")
    
    # Only play music if the image was successfully shown
    try:
        with open('assets/birthday_song.mp3', 'rb') as audio_file:
            st.audio(audio_file.read(), format='audio/mp3')
    except FileNotFoundError:
        st.info("🎵 Birthday song coming soon!")
