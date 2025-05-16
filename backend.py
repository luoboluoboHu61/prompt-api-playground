import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")  # 使用系统环境变量

def get_gpt_response(prompt, system_instruction="You are a helpful assistant.", temperature=0.7):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Error: {e}"
