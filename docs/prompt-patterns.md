# Prompt Patterns

## Role + Task + Constraints

```text
You are a practical developer support assistant.
Draft a reply to this ticket.
Keep it under 120 words and include two debugging steps.
```

## JSON-Only Extraction

```text
Return only valid JSON with keys: name, intent, urgency, next_action.
```

## SEO Outline

```text
Create an SEO outline for developers searching for OpenAI-compatible API examples.
Include H2 sections, search intent, and a short call to action.
```

## Production Guardrails

- Keep prompts short.
- Specify output format.
- Validate structured output.
- Retry transient failures.
- Log errors without logging secrets.
