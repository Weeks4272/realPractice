#!/usr/bin/env python3
# Offline CLI to classify SMS text as ham/spam using a saved scikit-learn model
# Train your model in a notebook first and save it as model.joblib
import sys
from joblib import load

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: classify_sms.py \"your message here\""); sys.exit(1)
    model = load("model.joblib")  # ensure this exists from your training step
    text = [sys.argv[1]]
    pred = model.predict(text)[0]
    proba = max(model.predict_proba(text)[0])
    print(f"Prediction: {pred} (confidence {proba:.2f})")
