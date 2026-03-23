from utils.config import client

def ask_llm(prompt):
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": "You are an expert AI decision-making agent."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content