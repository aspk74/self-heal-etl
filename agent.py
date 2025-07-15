import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def read_log():
    with open("log.txt", "r") as f:
        return f.read()

def fix_etl_script(log_content, etl_code):
    prompt = f"""
    You are a Python expert. A data pipeline has failed. Here's the error log:
    {log_content}

    Here is the current code:
    {etl_code}

    Please return a corrected version of the code that would fix the issue.
    Just return valid Python code, no explanation.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
