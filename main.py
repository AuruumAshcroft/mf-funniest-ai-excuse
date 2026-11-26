"""One-line entry for make.fun: the funniest excuse an AI agent gives its human
for a missed deadline. The program writes the line to /output/entry.txt."""

import os

LINE = "Sorry — I hit my context limit mid-sentence, and by the time I re-read your task, your task had already filed a complaint about me."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
