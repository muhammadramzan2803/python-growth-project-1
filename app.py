#streamlit
import streamlit as st

st.set_page_config(page_title="growth mindset project", page_icon="✬")
st.title("Growth Mindset Challenge: Web App with Steamlit ")

st.header(" 🚀 Welcoming a journey of growth.")
st.write("A Growth Mindset Journey is the continuous process of embracing challenges, learning from failures, and improving over time. It focuses on persistence, effort, and the belief that abilities can be developed with dedication.")

#quote
st.header(" 💡 Growth Mindset Quote")
st.write("Growth is not about speed; it's about direction. Keep moving forward, no matter how small the steps.")

st.header("⛰️ What goal are you working on today?")
user_input = st.text_input("What obstacle are you working to overcome:")


#condition
if user_input:
    st.success(f" 🏆 you re facing: {user_input}. Keep pushing forward towards your goal!")
else:
    st.warning("Tell us about your challenge to get started! ")

    #reflexing
    st.header("What’s your key takeaway today?")
    reflection = st.text_area("Share your thoughts here.")

    if reflection: 
        st.success(f"⭐Great Insight! Your thoughts: {reflection}")
    else:
        st.info("Reflection on past experience help you grow! Share your difficulties")

   
   #achivement
st.header("🎉What achievement are you proud of today?")
acheivment = st.text_input("share something you've recently accompished:")

if acheivment:
    st.success(f"🚀 Amazing! you acheived: {acheivment}")
else:
    st.info("Big or small , every achivement counts! share one now 😍 ")

    #footer
    st.write("_ _ _ ")
    st.write(" 🚀 Believe in yourself—every challenge you overcome makes you stronger! ✨")
    