# ST Deck Agent

Internal Cloud Run tool that generates ST-brand-compliant PowerPoint decks via the Cursor SDK.

## Quick start (local)

```bash
export CURSOR_API_KEY=your_key
pip install -r requirements.txt
playwright install chromium
uvicorn app.main:app --reload --port 8080
```

Open http://localhost:8080

## Modes

- **One-shot (default):** `POST /generate` → deck + previews in one unattended run.
- **Edit:** `POST /edit` with `{session, instruction}` after a one-shot run.
- **对话模式（Beta）**：首轮只出大纲与追问，用户**明确确认后**才 BUILD；后续可继续对话修改。需 `--max-instances 1`；重启后对话上下文丢失。

## Outputs

Each session produces:

- `output/deck.pptx` — download served with a friendly name from `deck_meta.json` or the request subject.
- `output/preview-*.png` — rendered slide previews for self-check.
- `build.py` — reproducible build script for edits.

## Brand compliance

Agent rules live in `workspace_template/AGENTS.md` and `workspace_template/skills/st-ppt-brand/`.  
Python helpers in `workspace_template/st_brand.py` include `text_on()` for contrast and `closing_slide()` for external decks.

## Preview fonts

The Docker image uses Liberation Sans as an Arial metric substitute for LibreOffice preview rendering. Generated `.pptx` files still declare Arial; final rendering on machines with real Arial may differ slightly.

## Security notes

- Upload limits and rate limiting are enabled by default.
- Session IDs are 12 hex chars — not a secret; use Cloud Run IAP or network controls if you need stronger access control.
