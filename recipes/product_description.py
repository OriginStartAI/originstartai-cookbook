from _client import chat


notes = """
OriginStartAI helps developers run OpenAI-compatible API calls, test models quickly,
and move from first call to production workflows.
"""

print(chat([
    {"role": "system", "content": "You write clear product copy for technical buyers."},
    {
        "role": "user",
        "content": f"Turn these notes into a concise product description:\n{notes}",
    },
]))
