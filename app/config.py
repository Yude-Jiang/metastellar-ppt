"""Central configuration from environment variables."""
from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "workspace_template"
SESSIONS = Path(os.environ.get("SESSIONS_DIR", "/tmp/sessions"))

MAX_PAGES = int(os.environ.get("MAX_PAGES", "6"))
RATE_LIMIT_PER_MINUTE = int(os.environ.get("RATE_LIMIT_PER_MINUTE", "10"))
MAX_UPLOAD_FILE_BYTES = int(
    os.environ.get("MAX_UPLOAD_FILE_BYTES", str(10 * 1024 * 1024))
)
MAX_UPLOAD_TOTAL_BYTES = int(
    os.environ.get("MAX_UPLOAD_TOTAL_BYTES", str(30 * 1024 * 1024))
)
MAX_UPLOAD_FILES = int(os.environ.get("MAX_UPLOAD_FILES", "5"))
SESSION_TTL_HOURS = float(os.environ.get("SESSION_TTL_HOURS", "24"))
SESSION_CLEANUP_INTERVAL_SEC = int(
    os.environ.get("SESSION_CLEANUP_INTERVAL_SEC", "3600")
)
RUN_TIMEOUT_SEC = float(os.environ.get("RUN_TIMEOUT_SEC", "540"))
GCS_BUCKET = os.environ.get("GCS_BUCKET")
CURSOR_MODEL = os.environ.get("CURSOR_MODEL", "composer-2.5")
