from _client import chat


text = """
OriginStartAI helps developers run OpenAI-compatible API calls and test practical AI workflows.
The goal of this cookbook is to make common integration tasks easy to copy and adapt.
"""

print(chat([
    {"role": "system", "content": "You summarize text into concise bullet points."},
    {"role": "user", "content": f"Summarize this text:\n{text}"},
]))

