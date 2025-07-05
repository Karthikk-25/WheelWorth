# 🚗 WheelWorth: Car Price Prediction App

**WheelWorth** is a desktop application built using **Python** and **PyQt5** that helps users estimate the selling price of a used car based on input features like mileage, fuel type, and more. The app uses a machine learning model trained on real car data and provides predictions instantly with a user-friendly interface.

---

## 📦 Features

- Beautiful and responsive **GUI** using PyQt5  
- Real-time **selling price predictions**  
- Built using a trained **Random Forest Regression model**
- Input parameters:
  - Present Price (in Lakhs)
  - Kilometers Driven
  - Year of Purchase
  - Number of Previous Owners
  - Fuel Type (Petrol, Diesel, CNG)
  - Seller Type (Dealer or Individual)
  - Transmission (Manual or Automatic)

---

## 🖥️ Tech Stack

| Component       | Library/Tool     |
|----------------|------------------|
| GUI            | PyQt5            |
| ML Model       | scikit-learn     |
| Data Handling  | pandas, joblib   |
| Packaging App  | PyInstaller      |

---

## 🚀 Getting Started

### 🔧 Requirements

- Python 3.x


- 📦 WheelWorth/
├── car_gui.py                # GUI application
├── Car model.py              # Script for training and saving the model
├── car_price_model.pkl       # Trained ML model
├── car_features.pkl          # Feature columns used in model
├── README.md                 # Project documentation

- Install dependencies:

```bash
pip install -r requirements.txt
