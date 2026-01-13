# 🏠 Bengaluru House Price Prediction

A complete **end-to-end Machine Learning project** that predicts house prices in **Bengaluru, India**, using real estate data. This project covers **data cleaning, feature engineering, outlier detection, model selection, deployment**, and a **Streamlit-based web application**.

---

## 🚀 Project Highlights

* Extensive **data cleaning & domain-driven outlier removal**
* Strong **feature engineering** (price per sqft, BHK logic, location grouping)
* Compared multiple ML models using **GridSearchCV**
* Selected **Linear Regression** with ~84% R² score
* Deployed using **Streamlit** for real-time predictions
* Model exported using **Pickle & JSON** for production use

---

## 🖥️ Web Application Preview (Streamlit)

### 📸 App Screenshot

![Bengaluru House Price Prediction App](./app_screenshot.png)
<img width="1314" height="841" alt="app_screenshot png" src="https://github.com/user-attachments/assets/e37b963e-bc49-4a02-b232-bfec38746368" />


---

## 📂 Dataset Overview

* **Dataset**: Bengaluru House Prices (CSV)
* **Target Variable**: `price` (in Lakhs)
* **Key Features Used**:

  * `total_sqft` – Total area of the property
  * `bhk` – Number of bedrooms
  * `bath` – Number of bathrooms
  * `location` – Property locality

Unused and noisy columns like `availability`, `society`, `balcony`, and `area_type` were removed.

---

## 🔄 Machine Learning Workflow

### 1️⃣ Data Cleaning

* Removed null values
* Converted `size` → numeric `bhk`
* Standardized `total_sqft` (handled ranges like `2100-2850`)

### 2️⃣ Feature Engineering

* Created **price per square feet** feature
* Cleaned `location` names and reduced dimensionality
* Grouped rare locations (<10 entries) into `other`

### 3️⃣ Outlier Detection & Removal

Outliers were removed using **real-estate domain knowledge**:

* Properties with `< 300 sqft per BHK`
* Extreme `price_per_sqft` values using **mean ± std (per location)**
* Invalid pricing where **2 BHK price > 3 BHK price** in the same area
* Bathroom outliers (`bath > bhk + 2`)

---

## 🧠 Model Building & Evaluation

### Models Tested

* Linear Regression
* Lasso Regression
* Decision Tree Regressor

### Evaluation Strategy

* Train/Test Split (80/20)
* K-Fold Cross Validation (ShuffleSplit)
* Hyperparameter tuning using **GridSearchCV**

### 📊 Model Performance (R² Score)

| Model                 | Cross-Val R² |
| --------------------- | ------------ |
| **Linear Regression** | **~0.84**    |
| Lasso Regression      | ~0.81        |
| Decision Tree         | ~0.72        |

✅ **Linear Regression selected as the final model** due to stability, interpretability, and best performance.

---

## 🧪 Sample Prediction Logic

The model predicts prices realistically:

* Premium locations (e.g., *Indira Nagar*) have higher prices
* Increasing BHK or bathrooms increases predicted value
* Same configuration shows variation across locations

---

## 📦 Deployment Artifacts

The following files are generated for deployment:

* `Bangaluru_house_price_pred.pickle` → Trained ML model
* `columns.json` → Feature column metadata

These are used directly in the **Streamlit application**.

---

## ▶️ How to Run This Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<kiranpukale-222>/<house-price-prediction-bangaluru>.git
cd <house-price-prediction-bengaluru>
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Streamlit App

```bash
streamlit run app.py
```

---

## 📈 Future Enhancements

* Add advanced models (Random Forest, XGBoost)
* Improve UI with charts & confidence intervals
* Deploy on **Streamlit Cloud / AWS / Azure**
* Add real-time data updates

---

## 👤 Author

**Kiran Pukale**
Aspiring Data Scientist | Machine Learning Enthusiast

---

⭐ If you found this project useful, please **star ⭐ the repository** and feel free to fork or contribute!
