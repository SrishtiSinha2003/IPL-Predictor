# 🏏 IPL Win Predictor

![Streamlit App](https://img.shields.io/badge/Made%20With-Streamlit-blue?style=for-the-badge&logo=streamlit)

This is a **Machine Learning-powered IPL Win Predictor** web app built with Python and Streamlit.

📍 **Live App:**  
🔗 [Click here to try it out!](https://ipl-predictor-cricklytics.streamlit.app/)

---

## 🚀 Features

- Predicts the winning probability of an IPL team in a live match scenario.
- Takes into account:
  - Batting & Bowling teams
  - Target score
  - Current score, overs completed, and wickets
  - Match location
- Clean and interactive UI with Streamlit

---

## 💡 How It Works

- A classification model is trained on historical IPL data.
- The model learns patterns from features like:
  - Runs left
  - Balls left
  - Current run rate
  - Required run rate
  - Wickets in hand
- Outputs probabilities for both teams

---

## 🛠️ Tech Stack

| Technology     | Role                    |
|----------------|-------------------------|
| Python         | Core language           |
| Pandas         | Data handling            |
| scikit-learn   | ML pipeline & modeling  |
| Streamlit      | Web app framework       |
| Pickle         | Model serialization     |

---

## 📦 Installation

```bash
git clone https://github.com/SrishtiSinha2003/IPL-Predictor.git
```
```bash
cd IPL-Predictor
```
```bash
pip install -r requirements.txt
```
```bash
streamlit run webapp.py
```

### 📸 Preview
### 📄 License
This project is licensed under the MIT License.
### 🌟 Show Some Love
If you like the project, give it a ⭐ on GitHub and share it with your friends!
