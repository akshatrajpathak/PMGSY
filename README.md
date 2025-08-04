# PMGSY
# **PMGSY Intelligent Classification System**

## 📌 Overview
The **Pradhan Mantri Gram Sadak Yojana (PMGSY)** is a flagship rural development program in India aimed at providing all-weather road connectivity to unconnected rural habitations.  
Over the years, PMGSY has evolved into multiple schemes (**PMGSY-I, PMGSY-II, RCPLWEA**, etc.), each having distinct objectives, funding patterns, and specifications.  

Manual classification of projects into their respective schemes is **time-consuming, error-prone, and inefficient**.  
This project uses **IBM Cloud Lite Services** to **automatically classify road and bridge projects** into the correct PMGSY scheme based on **physical and financial attributes**.

---

## 🚀 Features
- Automated classification of PMGSY projects with **high accuracy**.
- **User-friendly web interface** built using Flask.
- **Deployed on IBM Cloud** with an accessible API endpoint.
- Eliminates manual classification errors.
- Reduces time taken for scheme identification.

---

## 🛠️ Technology Stack
- **IBM Cloud Lite Services**
  - Watson Studio
  - Watson Machine Learning
  - Cloud Object Storage
  - AutoAI
- **Python** (Pandas, NumPy, Scikit-learn)
- **Flask** (for web UI)
- **HTML, CSS** (for frontend styling)

---

## 📂 Dataset
Dataset: **[PMGSY AI Kosh Dataset](https://aikosh.indiaai.gov.in/web/datasets/details/pradhan_mantri_gram_sadak_yojna_pmgsy.html)**  
Contains:
- Physical attributes (length of roads, number of bridges, etc.)
- Financial attributes (cost sanctioned, expenditure, etc.)
- Target variable: **PMGSY_SCHEME**

---

## ⚙️ Project Workflow
1. **Data Collection & Exploration**  
   Download and inspect the PMGSY dataset from AI Kosh.

2. **Data Preprocessing**  
   - Handle missing values.
   - Encode categorical variables.
   - Scale numeric features.
   - Split into training and testing sets.

3. **Model Building using IBM AutoAI**  
   - Upload cleaned dataset to IBM Watson Studio.
   - Select `PMGSY_SCHEME` as target.
   - Run AutoAI to generate and evaluate models.
   - Save and deploy the best model.

4. **Model Deployment**  
   - Deploy to Watson Machine Learning.
   - Generate public API endpoint.

5. **Web Interface Development**  
   - Flask app for user inputs.
   - Form sends data to IBM Cloud API.
   - Displays predicted scheme.

---

## 📊 Results
- **Accuracy:** ~0.909 (Holdout)
- Fully deployed and functional on IBM Cloud.
- Significantly reduces manual classification time.

---

## 🌟 Future Scope
- Integrate **Geospatial Data (GIS)** for improved accuracy.
- Build a **mobile app** for on-site classification.
- Automate integration with **Government dashboards**.

---

## 📜 License
This project is licensed under the **MIT License** - see the LICENSE file for details.

---

## 📎 GitHub Link
*(Replace with your actual repository link)*
