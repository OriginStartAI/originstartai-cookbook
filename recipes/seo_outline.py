from _client import chat


topic = "OpenAI-compatible API examples for Python and Node.js developers"

print(chat([
    {"role": "system", "content": "You create concise SEO outlines for developer audiences."},
    {
        "role": "user",
        "content": (
            "Create an SEO outline with search intent, H2 sections, and a short call to action "
            f"for this topic:\n{topic}"
        ),
    },
]))
