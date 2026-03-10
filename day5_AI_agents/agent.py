import os
from dotenv import load_dotenv
from google import genai
from tools import calculator

load_dotenv()

RESULTS_FILE = "results.txt"
QUERIES_FILE = "queries.txt"
GEMINI_MODEL = "gemini-2.5-flash"

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def ask_gemini(prompt: str) -> str:
    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
    )
    return response.text.strip()


def decide_tool(user_question: str) -> str:
    """
    Ask Gemini whether a calculator tool is needed for this question.

    Returns:
        'calculator' or 'none'
    """
    routing_prompt = f"""User question: {user_question}

Available tools:
- calculator → performs mathematical calculations

If the question requires math calculation, respond with exactly:
TOOL: calculator

Otherwise respond with exactly:
TOOL: none

Respond with only one line."""

    response_text = ask_gemini(routing_prompt)

    if "calculator" in response_text.lower():
        return "calculator"
    return "none"


def extract_math_expression(user_question: str) -> str:
    """
    Ask Gemini to extract the math expression from the user question.

    Returns:
        A clean math expression string e.g. '25 * 8'
    """
    extraction_prompt = f"""Extract only the mathematical expression from this question as plain text.
Return only the expression with no words, no punctuation, no explanation.

Question: {user_question}

Expression:"""

    return ask_gemini(extraction_prompt)


def generate_final_answer(user_question: str, tool_result: str) -> str:
    """
    Ask Gemini to write a helpful final answer given the tool result.
    """
    answer_prompt = f"""User question: {user_question}
Tool result: {tool_result}

Write a single, concise, helpful response."""

    return ask_gemini(answer_prompt)


def answer_directly(user_question: str) -> str:
    """
    Ask Gemini to answer the question directly without any tools.
    """
    return ask_gemini(user_question)


def run_agent(user_question: str) -> dict:
    """
    Run the full REACT-style agent loop for a single question.

    Returns:
        A dict with keys: question, thought, tool, observation, final_answer
    """
    tool_decision = decide_tool(user_question)

    if tool_decision == "calculator":
        thought = "The user asked a math question. I should use the calculator tool."
        math_expression = extract_math_expression(user_question)
        observation = str(calculator(math_expression))
        final_answer = generate_final_answer(user_question, observation)
    else:
        thought = "This is a conceptual question. I can answer directly without tools."
        observation = "N/A"
        final_answer = answer_directly(user_question)

    return {
        "question": user_question,
        "thought": thought,
        "tool": tool_decision,
        "observation": observation,
        "final_answer": final_answer,
    }


def format_result(result: dict) -> str:
    lines = [
        f"Query: {result['question']}",
        f"Thought: {result['thought']}",
        f"Action: Use {result['tool']}",
        f"Observation: {result['observation']}",
        f"Final Answer: {result['final_answer']}",
        "-" * 60,
    ]
    return "\n".join(lines)


def main() -> None:
    with open(QUERIES_FILE, "r") as f:
        queries = [line.strip() for line in f if line.strip()]

    all_results = []

    for query in queries:
        print(f"\nProcessing: {query}")
        result = run_agent(query)
        formatted = format_result(result)
        print(formatted)
        all_results.append(formatted)

    with open(RESULTS_FILE, "w") as f:
        f.write("\n".join(all_results))

    print(f"\nResults saved to {RESULTS_FILE}")


if __name__ == "__main__":
    main()