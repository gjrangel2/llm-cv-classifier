from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import BertTokenizer, BertForSequenceClassification
import torch

app = FastAPI()

tokenizer = BertTokenizer.from_pretrained("model/")
model = BertForSequenceClassification.from_pretrained("model/")
model.eval()

class InputText(BaseModel):
    text: str

@app.post("/predict")
def predict(input: InputText):
    inputs = tokenizer(input.text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.nn.functional.softmax(outputs.logits, dim=1)
        label = torch.argmax(probs).item()
        confidence = probs[0][label].item()
    return {"label": label, "confidence": round(confidence, 2)}
