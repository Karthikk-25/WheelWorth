import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout,
    QComboBox, QPushButton, QFormLayout
)
from PyQt5.QtCore import Qt
import joblib
import pandas as pd

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS  # PyInstaller temp folder
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Load model and feature names with flexible path
model_path = resource_path("car_price_model.pkl")
features_path = resource_path("car_features.pkl")

model = joblib.load(model_path)
features = joblib.load(features_path)

class CarPricePredictor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🚗 Car Price Predictor")
        self.setGeometry(100, 100, 500, 550)
        self.setStyleSheet("""
            QWidget {
                background-color: #f2f2f2;
                font-family: Segoe UI;
            }
            QLineEdit, QComboBox {
                padding: 8px;
                font-size: 14px;
                border-radius: 6px;
                border: 1px solid #bbb;
            }
            QPushButton {
                padding: 10px;
                font-size: 16px;
                background-color: #0078D7;
                color: white;
                border: none;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #005A9E;
            }
            QLabel {
                font-size: 14px;
            }
        """)

        form_layout = QFormLayout()

        # Input fields
        self.present_price_input = QLineEdit()
        self.kms_driven_input = QLineEdit()
        self.owner_input = QLineEdit()
        self.year_input = QLineEdit()

        self.fuel_type = QComboBox()
        self.fuel_type.addItems(['Petrol', 'Diesel', 'CNG'])

        self.seller_type = QComboBox()
        self.seller_type.addItems(['Dealer', 'Individual'])

        self.transmission = QComboBox()
        self.transmission.addItems(['Manual', 'Automatic'])

        form_layout.addRow("💰 Price (in lakhs):", self.present_price_input)
        form_layout.addRow("🛣️ Kms Driven:", self.kms_driven_input)
        form_layout.addRow("👤 Previous Owners:", self.owner_input)
        form_layout.addRow("📆 Year of Purchase:", self.year_input)
        form_layout.addRow("⛽ Fuel Type:", self.fuel_type)
        form_layout.addRow("🏷️ Seller Type:", self.seller_type)
        form_layout.addRow("⚙️ Transmission:", self.transmission)

        self.predict_btn = QPushButton("🔍 Predict Selling Price")
        self.predict_btn.clicked.connect(self.predict_price)

        self.result_label = QLabel("")
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setStyleSheet("font-size: 16px; margin-top: 20px;")

        layout = QVBoxLayout()
        layout.addLayout(form_layout)
        layout.addWidget(self.predict_btn)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def predict_price(self):
        try:
            present_price = float(self.present_price_input.text())
            kms_driven = int(self.kms_driven_input.text())
            owner = int(self.owner_input.text())
            year = int(self.year_input.text())
            age = 2025 - year

            input_dict = dict.fromkeys(features, 0)
            input_dict['Present_Price'] = present_price
            input_dict['Kms_Driven'] = kms_driven
            input_dict['Owner'] = owner
            input_dict['Age'] = age

            # Categorical
            fuel = self.fuel_type.currentText()
            seller = self.seller_type.currentText()
            trans = self.transmission.currentText()

            if f'Fuel_Type_{fuel}' in input_dict:
                input_dict[f'Fuel_Type_{fuel}'] = 1
            if f'Seller_Type_{seller}' in input_dict:
                input_dict[f'Seller_Type_{seller}'] = 1
            if f'Transmission_{trans}' in input_dict:
                input_dict[f'Transmission_{trans}'] = 1

            final_input = pd.DataFrame([input_dict])
            predicted_price = model.predict(final_input)[0]

            self.result_label.setText(f"✅ Estimated Selling Price: ₹ {round(predicted_price, 2)} lakhs")
        except Exception as e:
            self.result_label.setText(f"⚠️ Error: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CarPricePredictor()
    window.show()
    sys.exit(app.exec_())
