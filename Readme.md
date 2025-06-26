# Streamlit Demo App  
**Software Design Lecture Project**  

A simple Streamlit web application demonstrating two machine learning models, built for educational purposes in a Software Design course.

## 🎯 Features  
- **Two Model Demo**: Interactive interface to compare predictions from two different ML models.  
- **User-Friendly UI**: Simple sliders/inputs to adjust model parameters.  
- **Real-Time Predictions**: Instant visualization of model outputs.  

## 🧠 Models Included  
1. **Model 1**: A simple deeplearning model on Fashion-MNIST dataset  
2. **Model 2**: A simple machine learning model for comments sentiment analysis  

## 🛠️ Tech Stack  
- **Framework**: [Streamlit](https://streamlit.io/)  
- **Language**: Python
- **Libraries**: NumPy, Pandas, Scikit-learn, Matplotlib/Plotly, Seras  
- **Deployment**: Local run & Streamlit Cloud  

## 🚀 Quick Start  

### Prerequisites  
- Python 3.7+  
- pip  

### Installation  
1. Clone the repository:  
   ```bash
   git clone https://github.com/EliyaKaheni/StreamlitDemo.git
   cd StreamlitDemo
   ```
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  

### Run the App  
```bash
streamlit run main.py
```

## 📂 Project Structure  
```
StreamlitDemo/
├── main.py                          # Main Streamlit application script
├── models/                          # Trained models or model-building code
│   ├── fashion_mnist_model.keras    # Model 1 
│   └── sentiment_model.joblib       # Model 2
├── images/                          # Images used in code
│   ├── negative_feedback.jpg        # Image 1 
│   └── positive_feedback.jpg        # Image 2 
├── requirements.txt                 # Dependencies
└── README.md                        # This file
```

## 📚 Lecture Context  
This project was created as part of a **Software Design** lecture to demonstrate:  
- Modern web app development with Streamlit  
- Model deployment basics  
- UI/UX design for ML applications  

## 🌟 How to Contribute  
1. Fork the repository.  
2. Create a new branch (`git checkout -b feature/your-feature`).  
3. Commit changes (`git commit -m 'Add some feature'`).  
4. Push to the branch (`git push origin feature/your-feature`).  
5. Open a Pull Request.  

## 📜 License  
MIT License.
---
