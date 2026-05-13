# gitblame-iq

ever join a codebase and have absolutely no idea who to ask about anything at all?

`git blame` tells you who wrote a line but it doesn't tell you who *owns* auth, 
who writes the cleanest code, or who's been here long enough to know where 
the bodies are buried.

this tool chews through a repo's commit history and spits out a profile for 
each contributor — what they own, how they write, when they work, and a plain 
english summary.

## what you get

- which files/folders each dev dominates
- commit size and frequency patterns
- comment density and rough complexity stats
- a short AI-generated blurb per developer
- one self-contained HTML report you can share or open in a browser

## usage

```bash
pip install -r requirements.txt
python -m gitblame_iq.cli --repo /path/to/repo
```

opens `report.html` when done.

## stack

- gitpython — walks the commit history
- radon — measures code complexity
- anthropic — writes the plain english summaries
- jinja2 — builds the HTML report
- click + rich — CLI

## why

i got tired of spending the first two weeks on a new repo doing archaeology.