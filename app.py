{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "de35683d-83e9-4490-98a9-cb6025b63b37",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n",
      " * Restarting with watchdog (windowsapi)\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "1",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\renus\\anaconda3\\Lib\\site-packages\\IPython\\core\\interactiveshell.py:3585: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, request, render_template\n",
    "import joblib\n",
    "import numpy as np\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "# Load your trained model\n",
    "model = joblib.load('C:\\\\Users\\\\renus\\\\OneDrive\\\\Desktop\\\\Portfolio Website\\\\Churn Analysis Finance\\\\churn_best_rf_model.pkl')\n",
    "\n",
    "# Home Page\n",
    "@app.route('/')\n",
    "def home():\n",
    "    return render_template('index.html')\n",
    "\n",
    "# Predict route\n",
    "@app.route('/predict', methods=['POST'])\n",
    "def predict():\n",
    "    if request.method == 'POST':\n",
    "        gender = request.form['gender']\n",
    "        marital_status = request.form['marital_status']\n",
    "        income = float(request.form['income'])\n",
    "        age = int(request.form['age'])\n",
    "        customer_segment = request.form['customer_segment']\n",
    "        account_balance = float(request.form['account_balance'])\n",
    "\n",
    "        # Encode categorical variables (same way you trained)\n",
    "        gender = 1 if gender.lower() == 'male' else 0\n",
    "        marital_status = 1 if marital_status.lower() == 'married' else 0\n",
    "        customer_segment = 0 if customer_segment.lower() == 'basic' else (1 if customer_segment.lower() == 'plus' else 2)\n",
    "\n",
    "        features = np.array([[gender, marital_status, income, age, customer_segment, account_balance]])\n",
    "\n",
    "        prediction = model.predict(features)[0]\n",
    "\n",
    "        if prediction == 1:\n",
    "            result = \"Customer is likely to CHURN ❌\"\n",
    "        else:\n",
    "            result = \"Customer is NOT likely to churn ✅\"\n",
    "\n",
    "        return render_template('index.html', prediction_text=result)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0b2fb7ae-3043-4f97-a347-9d395e995aaa",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
