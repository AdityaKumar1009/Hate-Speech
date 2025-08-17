# 🛡️ Hate Speech Detection Web App  

This project is a **Hate Speech Detection system** trained on **Kaggle's Jigsaw Toxic Comment Challenge dataset**.  
The model is fine-tuned using Transformers and then integrated into a **Flask web application** to provide real-time predictions.  

---

## 📖 Project Workflow
1. **Training**  
   - The model is trained in [`Toxic_Comments.ipynb`](./Toxic_Comments.ipynb)  
   - Dataset: [Jigsaw Toxic Comment Classification Challenge](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge)  
   - Labels:  
     - Toxic  
     - Severe Toxic  
     - Obscene  
     - Threat  
     - Insult  
     - Identity Hate  

2. **Model Saving**  
   - After training, the model and tokenizer are saved inside the `final_model/` folder.  

3. **Web Application**  
   - The trained model is loaded into [`app.py`](./app.py)  
   - A **Flask backend** powers the classification API  
   - A simple **HTML frontend** (`templates/index.html`) provides an interactive interface  
