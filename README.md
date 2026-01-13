💉 Multiple Disease Prediction System
A Python-based ML web application that predicts Diabetes and Heart Disease using patient data and displays results in real-time.
🚀 Features
⚡ Real-time predictions for Diabetes and Heart Disease
🎨 Interactive UI built with Streamlit
📊 Data visualization using Matplotlib & Seaborn
🔄 Feature scaling with StandardScaler for robust predictions
🧩 Modular design: separate models for each disease
🛠 Technologies Used
Tool	Purpose
Python 🐍	Core language
Scikit-learn	Logistic Regression & SVM models, StandardScaler
Streamlit 🌐	Web app interface
Matplotlib & Seaborn 📈	Visualization of correlations and feature distributions
Pickle 💾	Saving and loading trained ML models
📋 Dataset & Inputs
Diabetes Prediction Inputs
Feature	Description
👶 Pregnancies	Number of pregnancies
🍬 Glucose	Plasma glucose level
💓 BloodPressure	Diastolic blood pressure (mm Hg)
💪 SkinThickness	Triceps skin fold thickness (mm)
💉 Insulin	Serum insulin (IU/mL)
⚖️ BMI	Body Mass Index
🧬 DiabetesPedigreeFunction	Genetic likelihood of diabetes
🎂 Age	Age of patient
Heart Disease Prediction Inputs
Feature	Description
🎂 Age	Patient’s age
♂️/♀️ Sex	Male = 1, Female = 0
💓 CP	Chest pain type (0–3)
🩺 Trestbps	Resting blood pressure (mm Hg)
🧪 Chol	Serum cholesterol (mg/dL)
🍬 FBS	Fasting blood sugar >120 mg/dL (1=yes, 0=no)
📈 RestECG	Resting ECG results (0–2)
❤️ Thalach	Max heart rate achieved
🏃 Exang	Exercise induced angina (1=yes, 0=no)
📉 Oldpeak	ST depression induced by exercise
🗻 Slope	Slope of peak exercise ST segment
🩸 CA	Number of major vessels colored by fluoroscopy
🧪 Thal	Thalassemia type (3,6,7)
⚙️ Installation
# Clone the repo
git clone https://github.com/<your-username>/multiple-disease-prediction.git
cd multiple-disease-prediction

# Install dependencies
pip install -r requirements.txt
🖥 Usage
# Run the web app
streamlit run app.py
Open the URL (usually http://localhost:8501)
Select Diabetes Prediction or Heart Disease Prediction
Enter the patient details
Click Get Test Result to see the prediction ✅
📊 Project Workflow
Raw Medical Data
        ↓
Data Preprocessing (Scaling, Train-Test Split)
        ↓
Model Training (Logistic Regression / SVM)
        ↓
Evaluation (Accuracy ~85–90%)
        ↓
Model Serialization (.sav using Pickle)
        ↓
Streamlit Web App
(User Input → Prediction)
📈 Visualization
Correlation heatmaps: Understand which features influence disease
Feature distributions: Detect outliers and data patterns
Helps drive actionable health insights
💡 Why LR & SVM?
Logistic Regression: Interpretable, outputs probability, fast training
SVM: Handles small datasets well, robust, can separate non-linear patterns
Other algorithms like Random Forest or Neural Networks were avoided for simplicity and interpretability
