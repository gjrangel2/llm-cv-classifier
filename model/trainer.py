from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments, IntervalStrategy
from sklearn.model_selection import train_test_split # type: ignore
from datasets import load_dataset

# Cargar datos
dataset = load_dataset('csv', data_files='data/train.csv', split='train')
tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')

def tokenize(batch):
    return tokenizer(batch['text'], padding=True, truncation=True)

dataset = dataset.map(tokenize, batched=True)
dataset = dataset.rename_column("label", "labels")

# Modelo
model = BertForSequenceClassification.from_pretrained('bert-base-multilingual-cased', num_labels=6)

# Entrenamiento
training_args = TrainingArguments(
    output_dir="./model_output",
    eval_strategy=IntervalStrategy.EPOCH,  # ✅ enum en lugar de string
    per_device_train_batch_size=8,
    num_train_epochs=5,
    save_steps=500,
    logging_dir="./logs"
)

train_dataset, eval_dataset = dataset.train_test_split(test_size=0.2).values()

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset   # ✅ ahora sí hay validación
)

# Entrenar
trainer.train()

# Guardar modelo y tokenizer
output_dir = "./model"
trainer.save_model(output_dir)
tokenizer.save_pretrained(output_dir)