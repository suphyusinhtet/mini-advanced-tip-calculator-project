import streamlit as st

st.header('Advanced Tip Calculator')
st.caption('This is an advanced tip calculator to share bill based on number of people who eat together.')
st.subheader('_This_ _mini_ _app_ is :blue[cool] :sunglasses:')

bill = st.number_input("Bill", value=None, placeholder="$0")
tip = st.number_input("Tip", value=None, placeholder="%0")
person = st.number_input("Number of person", value=1, placeholder="1")
if bill and tip and person:
    tip_percentage = tip / 100
    tip_amount = bill * tip_percentage
    total_bill = (bill + tip_amount) / person
    st.write("Total Bill",total_bill)
