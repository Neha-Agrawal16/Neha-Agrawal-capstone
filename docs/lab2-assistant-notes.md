# Lab 2 — Coding-assistant verification note

## The change

I added total-cost reporting to `src/pipeline/pipeline.py`. The pipeline now calculates the total cost of the completed answers using `sum(a.cost_usd for a in answers)`, logs the total cost using the existing logger, and prints the total cost at the end of the pipeline. I chose this improvement because it is a small, focused change that can be verified without changing the existing retry logic, batch processing, or SQLite persistence.

## The ask

I asked ChatGPT to add total-cost reporting to `src/pipeline/pipeline.py`.

The prompt was:

"Add total-cost reporting to `src/pipeline/pipeline.py`. After the batch completes, calculate the total cost using `sum(a.cost_usd for a in answers)`. Then log the total cost using the existing `log` logger and print the total cost at the end of the pipeline. Do not modify the existing retry logic, batch processing, SQLite persistence, or other functionality."

## What it produced

The assistant suggested adding the total-cost calculation after the batch completed:

`total_cost = sum(a.cost_usd for a in answers)`

It also added logging and printing of the total cost:

`log.info(f"total cost: {total_cost}")`

`print(f"total cost: ${total_cost:.6f}")`

No unrelated pipeline functionality was intentionally changed.

## What I verified before accepting

* Diff read: I reviewed the committed diff and confirmed that the change was limited to total-cost reporting in `src/pipeline/pipeline.py` and the verification note.

* Test run: I ran `python -m src.pipeline.pipeline`. The pipeline successfully processed 20 questions, with 20 successful answers, 0 retries, and a reported total cost of `$0.002000`. SQLite persistence also completed successfully with Run ID 6 and 20 answers persisted. I checked the log using `Get-Content logs/pipeline.log -Tail 5`, which confirmed the total cost and persistence.

* Security check: No new dependencies were introduced. There were no changes to API-key or secret handling, SQL logic, retry logic, or unsanitised input processing. The change only reads existing `cost_usd` values and reports their total.

## What I changed before committing

Nothing. I reviewed the suggested change and accepted it without additional code modifications.
