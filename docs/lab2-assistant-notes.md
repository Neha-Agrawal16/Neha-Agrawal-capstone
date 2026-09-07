# Lab 2 — Coding Assistant Verification

## Step 5a — Chosen Improvement

Add total-cost reporting to the pipeline.

The pipeline should calculate the total cost using:

`sum(a.cost_usd for a in answers)`

The total cost should be both printed and logged.

## Why I chose this improvement

This is a small change that is easy to verify without changing the existing batch processing, retry, or database functionality.

## Step 5b — Coding Assistant Prompt

Add total-cost reporting to `src/pipeline/pipeline.py`.

After the batch completes, calculate the total cost using:

`sum(a.cost_usd for a in answers)`

Then:

1. Log the total cost using the existing `log` logger.
2. Print the total cost at the end of the pipeline.

Do not modify the existing retry logic, batch processing, SQLite persistence, or other functionality.
## Step 5c — Implementation and Verification

### Change made

Added total-cost reporting to `src/pipeline/pipeline.py`:

`total_cost = sum(a.cost_usd for a in answers)`

The total cost is both logged and printed after the pipeline completes.

### Verification

I ran:

`python -m src.pipeline.pipeline`

The pipeline successfully processed 20 questions.

Results:

* Questions processed: 20
* Successful answers: 20
* Retries: 0
* Total cost: $0.002000
* SQLite persistence: successful
* Run ID: 6
* Answers persisted: 20

I also checked the log using:

`Get-Content logs/pipeline.log -Tail 5`

The log confirmed that the total cost was recorded and that the run was persisted to `results.db`.

### Verification conclusion

The change was verified successfully. The new total-cost reporting works without affecting the existing batch processing, logging, or SQLite persistence functionality.
