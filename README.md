# ♻️ KHUL JA SIM SIM
### Smart Waste Management System (SWMS)

<p align="center">
  <img src="assets/banner.png" alt="Smart Waste Banner" width="800"/>
</p>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python&logoColor=yellow"></a>
  <a href="https://streamlit.io/"><img src="https://img.shields.io/badge/Streamlit-App-red?logo=streamlit"></a>
  <a href="https://ultralytics.com/yolov8"><img src="https://img.shields.io/badge/YOLOv8-AI_Model-green?logo=github"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
  <a href="#"><img src="https://img.shields.io/badge/Status-Active-success"></a>
</p>

---

## 🌍 Project Overview

The **Smart Waste Management System (SWMS)** is an intelligent **Reverse Vending Machine (RVM)** simulation that uses AI and computer vision to identify **plastic bottles**, reward users for recycling, and automatically send **transaction summaries** via **Email** and **SMS**.

This project demonstrates how **IoT + AI + Automation** can encourage sustainable waste management and reward eco-friendly behavior. 🌱

---

## 🧩 Features at a Glance

| Feature | Description |
|----------|--------------|
| 👤 **User Registration** | Simple form for user info (Name, Email, Phone) |
| 🧴 **Plastic Bottle Detection** | Uses YOLOv8 for real-time detection via webcam |
| ⚖️ **Weight Estimation** | Predicts approximate bottle weight |
| 💰 **Reward Calculation** | Reward generated per bottle scanned |
| ⏳ **Auto-Stop** | Stops detection after 30s of inactivity |
| 📩 **Email Notification** | Sends transaction summary to user’s Gmail |
| 📱 **SMS Confirmation** | Sends transaction message to user’s mobile |
| 🧾 **Reward Summary** | Shows total bottles, weight, and cumulative balance |
| 💬 **Scalable AI Integration** | Can integrate ML-based prediction and chat assistants |

---

## 🧠 System Architecture

```text
[User Registration]
        ↓
[Real-time Detection (YOLOv8)]
        ↓
[Weight & Reward Calculation]
        ↓
[Transaction: Email + SMS]
        ↓
[Reward Summary Dashboard]
```

---

## 🖥️ Tech Stack

| Category | Technology |
|-----------|-------------|
| Frontend | Streamlit |
| Backend | Python 3.10+ |
| AI Model | YOLOv8 (Ultralytics) |
| Notifications | Twilio (SMS), Gmail SMTP (Email) |
| Libraries | OpenCV, NumPy, Streamlit |
| Deployment | GitHub / Local Machine |

---

## ⚙️ Setup Instructions

### 🪄 Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/Smart-Waste-Management-System.git
cd Smart-Waste-Management-System
```

### 🪄 Step 2: Create a Virtual Environment
```bash
python -m venv venv
.env\Scriptsctivate       # Windows
source venv/bin/activate      # Linux/Mac
```

### 🪄 Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### 🪄 Step 4: Run the Application
```bash
streamlit run app.py
```

Open your browser → [http://localhost:8501](http://localhost:8501)

---

## 📁 Project Structure

```bash
Smart-Waste-Management-System/
│
├── app.py                  # Streamlit main app
├── detector.py             # YOLO-based detection logic
├── utils.py                # Reward & weight estimation functions
├── notify.py               # Email & SMS sending logic
├── models/
│   └── plastic_detector.pt # YOLO model (auto-downloaded)
├── assets/
│   ├── banner.png          # Banner image
│   ├── register.png        # Registration screenshot
│   ├── scanning.png        # Scanning screenshot
│   └── summary.png         # Reward summary screenshot
├── requirements.txt
└── README.md
```

---

## 💰 Reward Calculation Logic

| Weight Range (g) | Reward (₹) |
|------------------:|-----------:|
| 0 – 10 | ₹5 |
| 11 – 20 | ₹10 |
| 21 – 30 | ₹15 |
| >30 | ₹20 |

> Total reward is calculated per bottle and added to the user’s cumulative balance.

---

## 📩 Email Example

**Subject:** Smart Waste Management - Transaction Summary  
```
Hello Akshay,

Your recycling transaction was successful! ♻

📦 Bottles Scanned: 5
⚖️ Total Weight: 125g
💵 Reward Credited: ₹45

Thank you for helping keep our planet clean! 🌍
-- Smart Waste Management System
```

---

## 📱 SMS Example
```
Hi Akshay, your recycling was successful!
₹45 credited for 5 bottles. ♻
```

---

## 🔐 API Setup (notify.py)

In your `notify.py`, replace these placeholders with your real credentials:

```python
EMAIL_SENDER = "yourmail@gmail.com"
EMAIL_PASSWORD = "your_google_app_password"

TWILIO_SID = "your_twilio_account_sid"
TWILIO_AUTH = "your_twilio_auth_token"
TWILIO_NUMBER = "+1XXXXXXXXXX"
```

> ⚠️ You must create a **Google App Password** (for Gmail SMTP)  
> and verify your **Twilio phone number** before sending messages.

---

## 🧠 Future Enhancements

| Feature | Description |
|----------|--------------|
| 🧠 AI Plastic Classifier | Identify plastic type (PET, HDPE, PVC) |
| ⚖️ Smart Weight Predictor | Estimate actual bottle weight using ML |
| 🧾 PDF Receipts | Generate user recycling reports |
| 💳 Digital Wallet | Maintain reward transaction history |
| 🤖 Chatbot | AI Assistant for guidance and support |

---

## 🧰 Requirements File
```text
streamlit
opencv-python
ultralytics
numpy
twilio
```

---
## How to Run
- Get-ExecutionPolicy
- Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
- .\venv\Scripts\activate
- python -m streamlit run app.py
---
> “Recycling turns things into other things —  
> which is like magic for the planet.” 🌎✨

---

## 🪪 License

This project is licensed under the **MIT License** —  
you are free to use and modify it with attribution.

---

## 💫 Badges Summary

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python&logoColor=yellow">
  <img src="https://img.shields.io/badge/Streamlit-Frontend-red?logo=streamlit">
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-green">
  <img src="https://img.shields.io/badge/Twilio-SMS-orange?logo=twilio">
  <img src="https://img.shields.io/badge/Gmail-Email%20Notification-red?logo=gmail">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg">
</p>

---

## 🏆 Acknowledgments
- [Streamlit](https://streamlit.io) – for interactive frontend  
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) – for object detection  
- [Twilio](https://www.twilio.com/) – for instant SMS service  
- [OpenCV](https://opencv.org) – for live camera integration  

---

