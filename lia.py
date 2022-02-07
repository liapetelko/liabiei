import streamlit as st 
#First Questions
st.title("Eilat")
start = int(st.selectbox("Enter the start", [10,11,12,13,14,15,16,17,18,19,20]))
end = int(st.selectbox("Enter the end", [10,11,12,13,14,15,16,17,18,19,20]))
adults = int(st.selectbox("Adults?",[1,2,3,4]))

kidsBool = st.button("Press if wanna add Kids / Babies")
if (kidsBool):
    kids = int(st.selectbox("Kids?",[0,1,2,3,4]))
    babies = int(st.selectbox("Babies?",[0,1,2,3,4]))

hotel = st.selectbox("Hotel?", ["RB","KS","SP","LAG","RIV","ROG"])

#Some upgrades..
