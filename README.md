# 🏥 Medical Insurance Predictor System

## 🚀 Project Purpose

The Medical Insurance Predictor project is a sophisticated application utilizing data science and machine learning to deliver personalized insights into medical insurance charges. Employing a Decision Tree Regressor model, the system analyzes diverse health factors—such as age, BMI, number of children, smoking habits, and gender—to provide accurate predictions tailored to individual profiles.

## 🔍 Problem Statement

The project addresses the need for transparent and personalized predictions of medical insurance charges. By leveraging machine learning, it empowers users to make informed decisions about insurance coverage based on their unique health profiles.

## 📊 Key Aspects and Features

### 🔄 Decision Tree Regressor Model:
Utilizes an advanced machine learning model to analyze health parameters and predict accurate medical insurance charges.

### 🌐 User-Friendly Streamlit Web App:
Interactive web app developed with Streamlit, enabling users to navigate and explore medical insurance charges effortlessly.

### 🤖 Predictive Analytics:
Transparent and informed decision-making through precise predictions, providing insights into potential insurance costs.

### 📊 Data Visualization:
Visual representations of the impact of different health factors on insurance charges for a better understanding.

### 📈 Exploratory Data Analysis (EDA):
In-depth analysis of the medical insurance dataset to uncover patterns, trends, and correlations.

### 📉 Model Evaluation Metrics:
Utilizes key metrics such as Mean Absolute Error (MAE) and R-squared for assessing the accuracy of predictions.

### 🚀 Continuous Integration/Continuous Deployment (CI/CD):
Ensures code quality and deployment readiness with GitHub Actions for seamless integration.


## 🛠️ Technologies and Techniques Used

### 🐍 Python:
Implemented in Python, a versatile language widely used in data science.

### 📊 Pandas, NumPy, Matplotlib, Seaborn:
Data processing and visualization libraries to organize and analyze health data.

### 🤖 Scikit-Learn:
Machine learning library used for implementing the Decision Tree Regressor model.

### 🌐 Streamlit:
Web app development with Streamlit for an intuitive user experience.

### 📈 GitHub Actions:
Continuous integration for code quality assurance.

Certainly! Below is a template inspired by the provided reference, tailored for showcasing the process of the Medical Insurance Predictor project:

## 📊 Data Exploration and Analysis (Jupyter Notebook)
- Explore the dataset by opening the Jupyter Notebook (`Medical Insurance Predictor.ipynb`).
- Follow the step-by-step instructions to load and analyze the medical insurance dataset.
- Screenshots:
  - Loading and exploring the medical insurance dataset.
 
  ![image](https://github.com/Bidishabiswas1704/insurance_predictor/assets/140384850/c0396704-c117-4611-b0ec-2d512f133d9a)

  - Steps involved in cleaning the data.

  ![image](https://github.com/Bidishabiswas1704/insurance_predictor/assets/140384850/384aa8a7-5b9b-4837-850d-00acbfcef565)

  ![image](https://github.com/Bidishabiswas1704/insurance_predictor/assets/140384850/e2a4046c-b919-4369-bec4-4646b558bc7d)


## ⚙️ Model Training and Prediction
- The notebook provides a detailed walkthrough of training the Decision Tree Regressor model for predicting insurance charges.
- Screenshots:
  - Key model parameters influencing predictions.

  ![image](https://github.com/Bidishabiswas1704/insurance_predictor/assets/140384850/400c268d-8eae-411c-8008-1e2de8333f25)

  ![image](https://github.com/Bidishabiswas1704/insurance_predictor/assets/140384850/08dc2b88-078f-4add-b94e-1e5b86c69853)

  ![image](https://github.com/Bidishabiswas1704/insurance_predictor/assets/140384850/9b92a95f-2476-4722-8cde-39f31671284f)

  ![image](https://github.com/Bidishabiswas1704/insurance_predictor/assets/140384850/1717e86e-1051-4fa4-929d-ddf1819bc384)

  ![image](https://github.com/Bidishabiswas1704/insurance_predictor/assets/140384850/1139ea5c-4464-45f5-a5ce-8d24ab16e90b)


  - Model evaluation metrics, by finding co-relation between dependent and independent variables using Pearson's co-relation method.
 
  ![image](https://github.com/Bidishabiswas1704/insurance_predictor/assets/140384850/d35d419e-4ba0-4861-bb92-0146fa48e503)

  ![image](https://github.com/Bidishabiswas1704/insurance_predictor/assets/140384850/7f26736d-afcd-47b5-aa78-c5360ab4a597)

  ![image](https://github.com/Bidishabiswas1704/insurance_predictor/assets/140384850/972e9305-0c76-412a-8b49-0f4d44b0ae3b)

  ![image](https://github.com/Bidishabiswas1704/insurance_predictor/assets/140384850/14aaa8c9-63af-4846-a70b-9f08066ca760)

  ![image](https://github.com/Bidishabiswas1704/insurance_predictor/assets/140384850/46d09f43-2112-4232-b6bf-0ea16efbfc63)

 
  - Visualizations capturing crucial aspects during the model training phase (finding co-realtion between various variables using Heatmap).

![image](https://github.com/Bidishabiswas1704/insurance_predictor/assets/140384850/25e165f3-2d24-40df-b374-28fe009549a7)

## 📊 Model Evaluation Metrics

**R-squared (R2):**
- **Definition:** R2 quantifies the proportion of the variance in the dependent variable that the model explains. It ranges from 0 to 1, with higher values indicating a better fit.
- **Interpretation:** An R2 score of 1 denotes a perfect fit, while 0 suggests the model does not explain any variability. A higher R2 signifies that the model captures a larger proportion of the target variable's variance.

**Mean Absolute Error (MAE):**
- **Definition:** MAE calculates the average absolute differences between predicted and actual values, providing a straightforward measure of prediction accuracy.
- **Interpretation:** Lower MAE values indicate better model performance, as they represent smaller average errors. MAE is less sensitive to outliers compared to MSE, making it particularly useful when extreme values may impact the overall performance assessment.

Both R2 and MAE complement MSE and RMSE in offering comprehensive insights into different aspects of a model's accuracy, providing a more holistic understanding of its predictive capabilities.
- Included  screenshots of these metrics in the notebook.

![image](https://github.com/Bidishabiswas1704/insurance_predictor/assets/140384850/48613bac-7eeb-48bf-a120-1af052522d32)

![image](https://github.com/Bidishabiswas1704/insurance_predictor/assets/140384850/a71d7a61-b40d-436b-8f17-6a2e4dd2c068)

## 📊 Visualization and Interpretation
- Display screenshots of key visualizations aiding in the interpretation of both historical and predicted data.

![image](https://github.com/Bidishabiswas1704/insurance_predictor/assets/140384850/2847eec5-3ffa-45bd-8f7e-767631d9365d)

## 📈 Automated Prediction and Results
- Explain how the notebook automates the prediction process, making it accessible for users with varying levels of statistical knowledge.
- Screenshots:
  - Forecasted results compared with actual data using graphical method.

  ![image](https://github.com/Bidishabiswas1704/insurance_predictor/assets/140384850/62b79a7c-01b7-4268-a707-05232b2ea54d)

  ![image](https://github.com/Bidishabiswas1704/insurance_predictor/assets/140384850/34fb8271-cedc-47ec-8313-2bd712e18884)


  - Highlighted insights or patterns revealed through the prediction results.
 
  ![image](https://github.com/Bidishabiswas1704/insurance_predictor/assets/140384850/fda977fc-96a9-4dca-a986-406495d75f1e)


## 📄 Usage Instructions
**Get Started:**
1. 📥**Clone the repository:**
  ```bash
  git clone https://github.com/Bidishabiswas1704/insurance_predictor/tree/main 
  ```
  - Follow the instructions in the README.md for setting up and running the Medical Insurance Predictor web app.

Feel free to customize the sections based on the specifics of your Medical Insurance Predictor project.


2. 🚀**Install dependencies:**

```bash
pip install -r requirements.txt
```

3. 🌐**Deployment:**
```bash
streamlit run medical_insurance.py
```

Open the web browser and go to http://localhost:8501 to explore the medical insurance predictor application.

## 📊 Example Screenshots and User Guidance

### Step 1: Opening the Web App

![image](https://github.com/Bidishabiswas1704/HR_Insights_Dashboard/assets/140384850/a654b156-5389-48c3-9a8d-757b0d115c50)

- Navigate to the web app by running the provided command in the terminal.
- The initial screen presents a clean and user-friendly interface.

### Step 2: Adjusting Health Parameters

- Use the sliders to set your age, BMI, and the number of children.

![image](https://github.com/Bidishabiswas1704/insurance_predictor/assets/140384850/b9400833-bc07-4303-992a-c54dd1b38ea5)

- Select 'Yes' or 'No' to indicate whether you are a smoker.

![image](https://github.com/Bidishabiswas1704/insurance_predictor/assets/140384850/efa14cb0-4477-48a9-a13b-a5f20124378e)

- Choose your gender by clicking on 'Male' or 'Female'.

![image](https://github.com/Bidishabiswas1704/insurance_predictor/assets/140384850/18856fd3-f0db-4884-bbf6-3696e4ee1be0)

### Step 3: Predicting Insurance Charges

- After setting your health parameters, click the "Predict Insurance Charges" button.

![image](https://github.com/Bidishabiswas1704/insurance_predictor/assets/140384850/0697af35-6059-4847-931b-bf7bda46865d)

- The app processes your inputs using the advanced Decision Tree Regressor model.

### Step 4: Viewing Predictions

- The predicted insurance charges are displayed on the screen.

![image](https://github.com/Bidishabiswas1704/insurance_predictor/assets/140384850/27c88af7-5de0-4721-9a3d-b7a1c106aad5)

- The result provides transparency into the estimated cost based on your health profile.

### Special Feature: Currency Conversion

- The app goes beyond predictions with a special feature.
- The predicted values are automatically converted into the top five exchangeable currencies at the current rates.

![image](https://github.com/Bidishabiswas1704/insurance_predictor/assets/140384850/ee4bb597-d75d-4fb4-b8ca-1cb459317bfe)


### Recruiters and Users Note:
- As a recruiter or user, this intuitive interface allows for easy navigation and a seamless experience.
- Explore the power of predictive analytics and currency conversion all in one place!



## 📂 Directory Structure

```
.
├── data/
│   └── Medical_insurance.csv
├── notebooks/
│   └── Medical Insurance Predictor.ipynb
├── screenshots/
│   ├── ![Screenshot 1](https://github.com/Bidishabiswas1704/insurance_predictor/assets/140384850/c51a52f9-99c8-4dae-aa47-8347dae96f0d)

│   └── ![Screenshot 1]https://github.com/Bidishabiswas1704/insurance_predictor/assets/140384850/007542d2-3bc4-46aa-906e-46078d3028cf)

├── medical_insurance.py
├── insurane_predictor_dtr.pkl
├── requirements.txt
├── README.md
└── .github/https://github.com/Bidishabiswas1704/insurance_predictor
    └── workflows/
        └── ci_cd.yml
```

## 🤝 Contribution

Contributions are welcome! Feel free to open issues, propose new features, or submit pull requests.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Feel free to modify and adapt this template to suit the specifics of your Medical Insurance Predictor project.
