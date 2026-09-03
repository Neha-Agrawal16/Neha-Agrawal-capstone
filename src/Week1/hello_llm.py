import sys
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

def ask(question: str) -> str:
    """Send one question to the LLM and return the answer text."""
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            #{"role": "system", "content": "You are concise."},
            #{"role": "system", "content": "You are a kindergarten teacher. Explain like the listener is five years old."},
            #{"role": "system", "content": "You are a Shakespearean poet. Reply in iambic verse where possible."},
            {"role": "system", "content": "You are a brilliant but impatient physicist. You explain accurately but you don't have time for niceties."},
            {"role": "user",   "content": question},
        ],
        #temperature=0.3,
        #temperature=0.0,
        temperature=1.5,
    )
    return resp.choices[0].message.content

if __name__ == "__main__":
    q = " ".join(sys.argv[1:]) or "Say hello in one sentence."
    print(ask(q))