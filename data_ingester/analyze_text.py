from transformers import pipeline

model = pipeline("text2text-generation", model="google/flan-t5-base")

def extract_financial_info(text):

    prompt = f"""
    Extract financial commitments, risks and obligations from this document:

    {text}
    """

    result = model(prompt, max_length=200)

    return result[0]['generated_text']