# Production Notes

Before moving a cookbook recipe into production, check:

- API key is stored in a secret manager.
- Base URL and model are environment-specific.
- Errors are logged without exposing user secrets.
- Outputs are validated before being used downstream.
- Long prompts have size limits.
- Costs and credit usage are monitored.

## Common Production Flows

```text
User input -> validation -> OriginStartAI call -> output validation -> product action
```

```text
Batch input -> chunking -> OriginStartAI call -> retry queue -> final export
```

## Recharge Planning

Start with a small budget. New users can recharge `$5` and get `$5` extra API credits.
