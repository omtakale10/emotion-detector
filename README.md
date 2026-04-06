# Emotion Detector Web Application

## 📌 Project Overview

The Emotion Detector is an AI-based web application that analyzes user input text and identifies emotions such as **anger, disgust, fear, joy, and sadness** using the IBM Watson NLP API.

This project demonstrates the integration of **natural language processing, API handling, Flask web development, unit testing, and static code analysis**.

---

## 🚀 Features

* Detects emotions from user input text
* Displays emotion scores and dominant emotion
* Web interface using Flask
* Unit testing for validation
* Error handling for invalid inputs
* Static code analysis using pylint

---

## 🛠️ Technologies Used

* Python
* Flask
* IBM Watson NLP API
* Requests Library
* unittest (for testing)
* pylint (for code analysis)

---

## 📂 Project Structure

emotion-detector/
│
├── EmotionDetection/
│   ├── **init**.py
│   └── emotion_detection.py
│
├── server.py
├── test_emotion_detection.py
├── README.md

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

git clone https://github.com/yourusername/emotion-detector.git

cd emotion-detector

---

### 2. Install Dependencies

pip install flask requests pylint

---

### 3. Run the Application

python server.py

Open in browser:
http://127.0.0.1:5000

---

## 🧪 Running Unit Tests

python test_emotion_detection.py

---

## ⚠️ Error Handling

* Handles blank input from user
* Handles API failure (status code 400)
* Displays appropriate error messages

---

## 🔍 Static Code Analysis

Run:
pylint server.py

---

## 📊 Example Output

Input:
"I am very happy today"

Output:

* Anger: 0.01
* Disgust: 0.02
* Fear: 0.03
* Joy: 0.90
* Sadness: 0.01
* Dominant Emotion: joy

---

## 🌐 Deployment

The application is deployed locally using Flask and can be accessed via a web browser.

---

## 👨‍💻 Author

Om Takale

---

## 📜 License

This project is for educational purposes.

