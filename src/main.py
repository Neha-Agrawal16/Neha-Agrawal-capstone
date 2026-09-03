from openai import OpenAI
from src.config import OPENAI_MODEL

client = OpenAI()


def ask_llm(prompt: str) -> str:
    response = client.responses.create(
        model=OPENAI_MODEL,
        input=prompt,
    )
    return response.output_text


if __name__ == "__main__":
    answer = ask_llm(
        "Explain retrieval-augmented generation in three sentences."
    )
    print(answer)