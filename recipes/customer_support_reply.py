from _client import chat


ticket = """
I tried the API example but received a 401 error. I am not sure whether my API key is wrong.
"""

print(chat([
    {"role": "system", "content": "You write calm and practical support replies."},
    {"role": "user", "content": f"Draft a support reply for this ticket:\n{ticket}"},
]))

