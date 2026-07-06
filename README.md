# Metastellar PPT

AI-powered presentation generator that builds polished PowerPoint decks via the Cursor SDK.
Uses the Metastellar blue design system — **not** STMicroelectronics brand.

## Quick start (local)

```bash
export CURSOR_API_KEY=your_key
pip install -r requirements.txt
playwright install chromium
uvicorn app.main:app --reload --port 8080
```

Open http://localhost:8080

## Deploy (Cloud Run)

```bash
gcloud run deploy metastellar-ppt \
  --source . \
  --project YOUR_PROJECT \
  --region asia-east1 \
  --allow-unauthenticated \
  --memory 2Gi --cpu 2 --timeout 600 \
  --concurrency 4 --max-instances 1 \
  --set-secrets CURSOR_API_KEY=CURSOR_API_KEY:latest \
  --set-env-vars CURSOR_MODEL=composer-2.5
```

## Environment variables

| Variable | Default | Description |
|----------|---------|-------------|
| `CURSOR_API_KEY` | — | Required. Cursor API key (use Secret Manager in prod). |
| `CURSOR_MODEL` | `composer-2.5` | Model for the agent. |
| `RATE_LIMIT_PER_MINUTE` | `10` | Per-IP rate limit for API routes. |
| `MAX_PAGES` | `6` | Maximum slides per request. |
| `MAX_UPLOAD_FILES` | `5` | Max reference files per request. |
| `MAX_UPLOAD_FILE_BYTES` | `10485760` (10 MB) | Per-file upload limit. |
| `MAX_UPLOAD_TOTAL_BYTES` | `31457280` (30 MB) | Total upload limit per request. |
| `SESSION_TTL_HOURS` | `24` | Auto-delete session workspaces after this age. |
| `SESSION_CLEANUP_INTERVAL_SEC` | `3600` | How often to sweep expired sessions. |
| `RUN_TIMEOUT_SEC` | `540` | Max seconds per agent run. |
| `GCS_BUCKET` | *(empty)* | Optional. Persist session tarballs for restore after instance restart. |
| `SESSIONS_DIR` | `/tmp/sessions` | Workspace root (tmpfs on Cloud Run). |

## Modes

- **One-shot (default):** `POST /generate` → deck + previews in one unattended run.
- **Edit:** `POST /edit` with `{session, instruction}` after a one-shot run.
- **对话模式（Beta）**：首轮只出大纲与追问，用户确认后才 BUILD。

## Density

- **Speaker-led** (`density=speaker`): fewer words per slide, presentation pacing.
- **Reading-first** (`density=reading`): denser slides for async review.

## Design system

Agent rules: `workspace_template/AGENTS.md` and `workspace_template/skills/metastellar-slides/`.  
Python helpers: `workspace_template/slide_theme.py` (blue Tailwind palette, layout builders).

## Outputs

Each session produces:

- `output/deck.pptx` — downloadable presentation
- `output/preview-*.png` — rendered slide previews for self-check
- `build.py` — reproducible build script for edits

## Security notes

- Upload limits and rate limiting are enabled by default.
- Session IDs are 12 hex chars — use network controls if you need stronger access control.
