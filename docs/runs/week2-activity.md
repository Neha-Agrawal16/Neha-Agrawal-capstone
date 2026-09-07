# Week 2 Activity - Streaming with as_completed

Using `asyncio.as_completed` made the completion order visible: answers were printed as soon as each task finished, so the output order differed from the original question order.

I would use `asyncio.gather` when I want to wait for all tasks and keep the results aligned with the input order, and `asyncio.as_completed` when I want to process or display results immediately as individual tasks finish.