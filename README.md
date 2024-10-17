This project demonstrates how to classify customer queries into categories like Order Tracking, Refunds, Product Inquiries, Technical Support and Account Issues using a combination of Generative AI (GenAI) and Lazy Predict.
Lazy Predict is used to automatically select the best-performing machine learning model, while GenAI (BERT embeddings) is used for feature extraction from customer queries. The result is an efficient, scalable solution for automating customer support workflows.

**Table of Contents**
• Overview
• Features
• Installation
• Usage
• Model Training and Evaluation
• Streamlit App
• Future Enhancements
• Contributing
• License

**Overview**

In today’s fast-paced business world, customer support teams often receive thousands of queries daily. Automating the classification of these queries can significantly improve response times and reduce operational costs. This project uses
GenAI and Lazy Predict to automate the process of categorizing customer queries and routing them to the appropriate team.
This solution can be used in various industries such as e-commerce, banking, and SaaS, where fast and accurate query handling is essential.

**Features**

• Automated Model Selection
: Uses Lazy Predict to compare multiple machine learning models and automatically select the best one.

• Generative AI for Text Embeddings
: Uses BERT-based embeddings to transform customer queries into numerical representations.

• Real-time Query Classification
: A Streamlit app that allows for real-time classification of customer queries into predefined categories.

•Accurate Query Routing
: Automatically routes customer queries to the correct department based on the predicted category.

**Installation**

To get started, follow these steps to set up the project locally:
1. Clone the Repository
:
git clone
https://github.com/shrina81/Implementation.git

cd customer-query-classifier

2.Set Up a Virtual Environment
(optional but recommended):
python3 -m venv env
source env/bin/activate  # For Windows use: env\Scripts\activate

3.Install Dependencies
:
Install the necessary Python libraries using pip:
pip install -r requirements.txt


**Usage**

Model Training and Saving

To train the model and save it for use in the Streamlit app, run the following Python script:
python app.py
This script will:
• Load and preprocess the dataset of customer queries.
• Train the machine learning model using Lazy Predict to select the best model.
• Save the trained model and the TF-IDF vectorizer to .pkl files for use in the Streamlit app.

**Streamlit App**

To launch the Streamlit app and classify queries in real-time:
streamlit run app.py
Once the app is running, you can enter customer queries and see which category they are classified into.

Model Training and Evaluation

The model is trained on a dataset of customer queries across the following categories:
•Order Tracking
•Refunds
•Product Inquiries
•Technical Support
•Account Issues

After the model is trained,
Lazy Predict
is used to compare multiple classifiers such as:
• DecisionTreeClassifier
• LogisticRegression
• RandomForestClassifier
• GradientBoostingClassifier
Lazy Predict automatically ranks the models based on accuracy, balanced accuracy, and F1 score.

**Streamlit App**

The app uses the saved model to classify customer queries in real-time. You can try it out by entering sample queries, such as:
• “Where is my order?”
• “How do I get a refund?”
• “I need help logging into my account.”
The model will predict one of the predefined categories based on the input query.

Future Enhancements

In the future, the following enhancements are planned:
•More Categories
: Expand the query categories to cover more specific customer support topics.
•Model Tuning
: Implement hyperparameter tuning to further improve model accuracy.
•Data Augmentation
: Use Generative AI to generate more diverse training data and improve model robustness.



**Contact**

If you have any questions or need further information, feel free to contact me via email or through my GitHub profile.
**shrinaneema81@gmail.com**

