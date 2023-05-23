import streamlit as st

st.set_page_config(page_title="Invoice System", layout="wide")
st.title("Invoice System")

col1, col2 = st.columns(2)
invoice_no = col1.text_input("Invoice Number", key="invoice_no")
invoice_date = col1.text_input("Invoice Date", key="invoice_date")
sold_to = col1.text_input("Sold To", key="sold_to")
ship_to = col1.text_input("Ship To", key="ship_to")
po_no = col1.text_input("PO Number", key="po_no")
payment_terms = col1.radio("Payment Terms", ("30 Days Net", "45 Days Net", "60 Days Net", "Others"), key="payment_terms")
due_date = col1.text_input("Due Date", key="due_date")
total_amt = col1.number_input("Total Amount", key="total_amt")

if st.button("Submit"):
    st.write("Invoice record submitted")