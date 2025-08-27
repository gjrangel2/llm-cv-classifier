import csv
import random

categories = {
    0: ["Java", "Spring Boot", "MySQL", "REST APIs", "PostgreSQL"],
    1: ["React", "Angular", "CSS", "TypeScript", "Responsive design"],
    2: ["Selenium", "Cypress", "Jest", "QA", "Automated testing"],
    3: ["RETILAP", "iluminación pública", "instalaciones eléctricas", "normativa técnica", "supervisión"],
    4: ["Python", "Power BI", "Excel", "SQL", "Data analysis"],
    5: ["Ley 18 de 1990", "normativas urbanas", "consultoría legal", "seguridad pública", "compliance"]
}

def generate_text(label):
    skills = random.sample(categories[label], 3)
    return f"Profesional con experiencia en {', '.join(skills)}"

with open("data/train.csv", "w", newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["text", "label"])
    for label in categories:
        for _ in range(100):  # 100 ejemplos por clase
            writer.writerow([generate_text(label), label])
