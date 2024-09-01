# Loan Approval Prediction

This project is a machine learning-based loan approval prediction system. It predicts whether a loan application will be approved based on various input features using a pre-trained model.

## Project Structure

- `LoanApproval.ipynb`: Jupyter notebook containing data analysis, preprocessing, model training, and evaluation.
- `app.py`: Flask web application for serving the loan approval model.
- `loan_approval_dataset.csv`: Dataset used for training the model.
- `model.pkl` & `scaler.pkl`: Serialized model and scaler used by the Flask app.
- `requirements.txt`: Python dependencies for the project.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Jupyter Notebook
- Required Python libraries listed in `requirements.txt`

### Installation

# Clone the repository
git clone https://github.com/Krishna2win/Loan_Approval.git && cd Loan_Approval

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py

# Open the app in your browser
# Visit http://127.0.0.1:5000/

### Usage

# Start the Flask app
python app.py

# Access the app
# Open your web browser and go to http://127.0.0.1:5000/

# Explore the Jupyter notebook (optional)
jupyter notebook LoanApproval.ipynb

### Model

The loan approval model is created using scikit-learn and is integrated into a Streamlit application. The process includes:

1. **Data Preprocessing**: Handling missing values, encoding categorical features, and scaling numerical features.
2. **Model Training**: Trained using algorithms like logistic regression.
3. **Deployment**: The trained model (`model.pkl`) and scaler (`scaler.pkl`) are loaded in the Streamlit app for real-time predictions.

Use the Streamlit interface to input data and get predictions.


### Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request for review.

Feel free to open issues for bugs, suggestions, or questions.

