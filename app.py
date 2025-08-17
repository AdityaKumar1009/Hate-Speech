from flask import Flask, request, render_template
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

# Path to your saved model
MODEL_PATH = "/Users/crazeformarvel/Downloads/LLMs-for-Text-Classification-main/final_model"

# Define your label mapping
id2label = {
    0: "Toxic",
    1: "Severe Toxic",
    2: "Obscene",
    3: "Threat",
    4: "Insult",
    5: "Identity Hate"
}
label2id = {v: k for k, v in id2label.items()}

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_PATH,
    num_labels=len(id2label),
    id2label=id2label,
    label2id=label2id
)

# Create pipeline
hate_speech_clf = pipeline(
    "text-classification", 
    model=model, 
    tokenizer=tokenizer, 
    return_all_scores=True
)

# Initialize Flask app
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    predictions = None
    final_prediction = None

    if request.method == "POST":
        text = request.form.get("text")

        if text:
            preds = hate_speech_clf(text)[0]  # get list of scores
            # Sort by score descending
            preds = sorted(preds, key=lambda x: x["score"], reverse=True)

            predictions = preds
            final_prediction = preds[0]["label"]  # top prediction

    return render_template("index.html", predictions=predictions, final_prediction=final_prediction)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
