# hobby-project

Agentic AI built with PydanticAI that converts natural language infrastructure requirements into validated, cost-compliant Cloud Infrastructure plans.

## Features

**Requirement Gathering**: It listens to what you want (e.g., "I need a database that won't crash if 10,000 people visit at once").

**Market Research** (Tool Call): It doesn't guess prices. It uses a "Tool" to check the live market (like an Amazon AWS pricing API) to see how much a database actually costs today.

**Technical Design** (Tool Call): It picks the specific "Cloud Parts" (servers, firewalls, storage) needed to make your app work safely.

**The Budget Inspector** (Tool Call): If the agent picks parts that cost $150 but you only have $100, the "Inspector" (Pydantic) blocks the result and tells the AI: "Too expensive. Redesign it using cheaper parts."

**The Delivery** (Tool Call): It hands you a clean, error-free Markdown file.

**Self-Critique** (Prompt): Each agent self criticises its own output to reduce hallucination
