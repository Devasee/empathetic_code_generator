import os
import requests
import json
from typing import List, Dict

GROQ_API_KEY = "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"
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

def call_groq(messages: List[Dict], model="llama3-70b-8192"):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "messages": messages,
        "temperature": 0.7
    }
    response = requests.post(GROQ_API_URL, headers=headers, json=data)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

def empathetic_review(input_json: Dict) -> str:
    code = input_json["code_snippet"]
    comments = input_json["review_comments"]
    markdown_sections = []

    # Generate per-comment analysis
    for comment in comments:
        prompt = f"""
You are an empathetic senior developer. 
Rephrase and expand the following direct review comment into a supportive, mentor-like explanation.

### Requirements:
1. Start with: --- (as a separator).
2. Heading format: ### Analysis of Comment: "{comment}"
3. Include:
   * **Positive Rephrasing:** Warm, encouraging rewrite (mentor tone).
   * **The 'Why':** Clear explanation of the software principle (performance, readability, convention).
   * **Suggested Improvement:** Show the corrected code in a fenced Python block with proper indentation (```python ... ```). Always use `user` instead of `u`.
   * **Learn More:** Provide one relevant resource link.
4. Do NOT add extra narrative paragraphs outside these bullet points.

### Code for context:
{code}
"""
        messages = [
            {"role": "system", "content": "You are a kind, experienced mentor reviewing code."},
            {"role": "user", "content": prompt}
        ]
        section = call_groq(messages)
        markdown_sections.append(section)

    # Holistic summary
    summary_prompt = f"""
Write a warm, concise conclusion for the report. 
Tone: encouraging, supportive, mentor-like. 
Remind the developer they are making great progress and learning is iterative.

Code:
{code}
Comments: {comments}
"""
    summary = call_groq([
        {"role": "system", "content": "You are a kind, experienced mentor reviewing code."},
        {"role": "user", "content": summary_prompt}
    ])
    markdown_sections.append(f"\n## Overall Feedback\n{summary}")

    return "\n".join(markdown_sections)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python empathetic_reviewer.py input.json")
        exit(1)
    with open(sys.argv[1]) as f:
        input_json = json.load(f)
    output = empathetic_review(input_json)
    with open("report.md", "w") as out_f:
        out_f.write(output)
    print("Markdown report saved to report.md")
