# -*- coding: utf-8 -*-
"""nlp.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MU8UCwQA1UrsJM6wWrXw0_4dxDXpYyc4
"""

!pip install spacy
!pip install scispacy
!pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.4.0/en_ner_bc5cdr_md-0.4.0.tar.gz

import spacy

# Load the pre-trained biomedical model from SciSpacy
# This model is trained on diseases and chemicals
nlp = spacy.load("en_ner_bc5cdr_md")

# Sample biomedical text
biomedical_text = """
Chronic Diseases and Their Management

Chronic diseases like diabetes and high blood pressure (hypertension) are major health issues worldwide.

Diabetes is a condition where the blood sugar level is too high. There are two main types:

Type 1 diabetes: The body does not produce insulin because the immune system attacks the cells in the pancreas.
Type 2 diabetes: The body does not use insulin properly, often due to obesity and lifestyle choices.
To manage diabetes:

Eat a healthy diet with whole grains, fruits, and vegetables.
Exercise regularly.
Take medications like metformin, which helps control blood sugar. Some people may need insulin injections.
High Blood Pressure (Hypertension) means that the force of the blood against the artery walls is too high. It often has no symptoms but can lead to heart problems if not controlled.

To manage high blood pressure:

Reduce salt intake and eat more foods rich in potassium.
Get regular exercise.
Take medications like ACE inhibitors or beta-blockers to help lower blood pressure
"""

# Process the text using the NLP model
doc = nlp(biomedical_text)

# Extract and display biomedical entities (diseases and chemicals)
print("Extracted Biomedical Entities:")
for entity in doc.ents:
    print(f"{entity.text} ({entity.label_})")