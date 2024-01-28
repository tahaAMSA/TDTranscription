import os
import dotenv
from langchain.chains import create_extraction_chain
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

# Schema
schema = {
    "properties": {
        "doctor_name": {"type": "string"},
        "patient_name": {"type": "string"},
        "patient_age": {"type": "integer"},
        "consultation_date": {"type": "string"},
        "symptoms": {"type": "array", "items": {"type": "string"}},
        "physical_examination_findings": {"type": "array", "items": {"type": "string"}},
        "diagnostic_hypotheses": {"type": "array", "items": {"type": "string"}},
        "additional_tests": {"type": "array", "items": {"type": "string"}},
        "treatment_plan": {"type": "array", "items": {"type": "string"}},
        "follow_up_recommendations": {"type": "array", "items": {"type": "string"}},
        "conclusion": {"type": "string"}
    },
    "required": ["doctor_name", "patient_name", "patient_age", "consultation_date"]
}

# Input
inp = "result.txt"

# Run chain
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
chain = create_extraction_chain(schema, llm)
result = chain.run(inp)

# Afficher le résultat
print(result)
