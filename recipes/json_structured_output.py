from _client import chat


prompt = """
Extract a task list from this sentence:
Create a GitHub organization, publish starter examples, and verify the first API call.
"""

print(chat([
    {"role": "system", "content": "Return only valid JSON."},
    {"role": "user", "content": prompt},
]))

