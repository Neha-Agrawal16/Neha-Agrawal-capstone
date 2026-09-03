0001-capstone-framing.md` · 💻 Self-paced · 5 min

**1. What we're doing & why.** Create the empty ADR file with the right structure. The shape comes from the Solution Framing Canvas (Day 2, slide 38) — six boxes that capture *what the system is for, what it takes in, what it puts out, what tools it uses, what it remembers, and what it's allowed to decide for itself*. Filling these six boxes is your design.

**2. Where we are now.** `docs/adr/` exists but only has a `.gitkeep`. No ADR yet.

**3. What we're about to do.** Create `docs/adr/0001-capstone-framing.md` with the template structure. We'll fill it in 3b.

**4. Make the change.** Create `docs/adr/0001-capstone-framing.md` with this content:

```markdown
# ADR-0001: Capstone Framing — <Your Capstone Name>

- **Status:** Draft v1
- **Date:** <today's date in YYYY-MM-DD>
- **Author:** <your name>

## Context

<2–3 sentences: what problem is this capstone trying to solve, for whom, and why now?>

## Decision — Solution Framing Canvas

| Box | Your answer |
|-----|-------------|
| **Inputs** | <what the user / caller sends — text, file uploads, parameters> |
| **Outputs** | <what the system produces — a text answer, a citation list, a structured result> |
| **Tools** | <what external services it uses — OpenAI, your retriever, a database, …> |
| **Memory** | <what the system remembers between calls — nothing, last N turns, durable history> |
| **Autonomy level** | <on the spectrum from chatbot to agentic system, where this sits and why> |
| **Decision boundaries** | <what it's allowed to decide on its own, vs. what needs a human> |

## Consequences

- **Positive:** <2–3 bullet points: what this design unlocks>
- **Negative / risks:** <2–3 bullet points: what's harder / costlier / riskier because of this choice>
- **Things we'll re-visit:** <1–2 specific things we'll come back to in later ADRs>
```

**Reading this template:**

- **Status** — `Draft v1` for now. Later ADRs might be `Accepted`, `Superseded`, or `Deprecated`.
- **Six Canvas boxes** — these are the Solution Framing Canvas you saw on Day 2. Each box is *one* sentence; if you can't say it in one sentence, you don't understand the choice well enough yet.
- **Consequences** — positive, negative, things to revisit. Negative consequences matter as much as positive ones; we want learners to be honest about trade-offs from W1.