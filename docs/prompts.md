Prompts Used to Generate Technical Documentation

Purpose
These prompts were used to structure and generate the technical architecture documentation for the codebase.

Prompts
1) High-level architecture
- "Draft a concise technical architecture for a Python Flask e-commerce prototype supporting product listing with filters, product details, and a session-based shopping cart. Include routing, data model, session handling, and extensibility."

2) Data model and session
- "Describe dataclasses for Product, CartItem, and Cart including methods for add/update/remove and serialization to/from the session."

3) Filtering and listing
- "Explain how to implement filtering by gender, age group, size, price range, and text search on the server side, returning results to a Jinja2 template."

4) Security and performance
- "List minimal security considerations (SECRET_KEY, input validation) and performance considerations (O(n) filtering, when to move to DB, caching, pagination)."

5) Build and run
- "Provide simple steps to run locally, including dependencies and commands."

Usage Notes
- These prompts are reference-only and can be reused when evolving the system.


