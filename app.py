import streamlit as st
import joblib  # For loading the saved model
import pandas as pd
# Step 1: Load the trained model and TF-IDF vectorizer
model = joblib.load('customer_query_model.pkl')
tfidf = joblib.load('tfidf_vectorizer.pkl')
# Step 2: Define categories for classification
category_mapping_reverse = {
   0: "Order Tracking",
   1: "Refunds",
   2: "Product Inquiries",
   3: "Technical Support",
   4: "Account Issues"
}
# Step 3: Streamlit App UI
st.title("Customer Query Classifier")
st.write("This app classifies customer queries into relevant categories.")
# Input text from the user
user_input = st.text_input("Enter a customer query:")
# Step 4: Classify the input query when the user submits it
if st.button("Classify"):
   if user_input:
       # Transform the input query using the TF-IDF vectorizer
       query_embedding = tfidf.transform([user_input])
       # Predict the category using the loaded model
       prediction = model.predict(query_embedding)[0]
       # Map the prediction to the category name
       predicted_category = category_mapping_reverse[prediction]
       # Display the prediction result
       st.write(f"Predicted Category: **{predicted_category}**")
   else:
       st.write("Please enter a query to classify.")