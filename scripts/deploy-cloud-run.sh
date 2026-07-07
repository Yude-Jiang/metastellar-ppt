#!/usr/bin/env bash
# Deploy Metastellar PPT to Google Cloud Run (run from Cloud Shell).
#
# Usage:
#   export GCP_PROJECT=your-project-id
#   export GCP_REGION=asia-east1          # optional, default asia-east1
#   export SERVICE_NAME=metastellar-ppt   # optional
#   bash scripts/deploy-cloud-run.sh
#
# First-time setup (once per project):
#   gcloud services enable run.googleapis.com cloudbuild.googleapis.com secretmanager.googleapis.com
#   echo -n 'YOUR_CURSOR_API_KEY' | gcloud secrets create CURSOR_API_KEY --data-file=- --replication-policy=automatic
#   PROJECT_NUMBER=$(gcloud projects describe $GCP_PROJECT --format='value(projectNumber)')
#   gcloud secrets add-iam-policy-binding CURSOR_API_KEY \
#     --member="serviceAccount:${PROJECT_NUMBER}-compute@developer.gserviceaccount.com" \
#     --role="roles/secretmanager.secretAccessor"

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

PROJECT="${GCP_PROJECT:-$(gcloud config get-value project 2>/dev/null || true)}"
REGION="${GCP_REGION:-asia-east1}"
SERVICE="${SERVICE_NAME:-metastellar-ppt}"
MODEL="${CURSOR_MODEL:-composer-2.5}"

if [[ -z "$PROJECT" || "$PROJECT" == "(unset)" ]]; then
  echo "Error: set GCP_PROJECT or run: gcloud config set project YOUR_PROJECT_ID"
  exit 1
fi

echo "==> Project:  $PROJECT"
echo "==> Region:   $REGION"
echo "==> Service:  $SERVICE"
echo "==> Source:   $ROOT"

echo "==> Enabling required APIs (safe to re-run)..."
gcloud services enable run.googleapis.com cloudbuild.googleapis.com secretmanager.googleapis.com \
  --project="$PROJECT" --quiet

if ! gcloud secrets describe CURSOR_API_KEY --project="$PROJECT" &>/dev/null; then
  echo ""
  echo "WARNING: Secret CURSOR_API_KEY not found in project $PROJECT."
  echo "Create it first:"
  echo "  echo -n 'YOUR_KEY' | gcloud secrets create CURSOR_API_KEY --data-file=- --project=$PROJECT --replication-policy=automatic"
  echo ""
  read -r -p "Continue deploy without secret? (y/N) " ans
  [[ "${ans:-}" =~ ^[Yy]$ ]] || exit 1
  SECRET_ARGS=()
else
  SECRET_ARGS=(--set-secrets "CURSOR_API_KEY=CURSOR_API_KEY:latest")
fi

echo "==> Deploying to Cloud Run (source build, may take 5–15 min)..."
gcloud run deploy "$SERVICE" \
  --source . \
  --project="$PROJECT" \
  --region="$REGION" \
  --allow-unauthenticated \
  --memory 2Gi \
  --cpu 2 \
  --timeout 600 \
  --concurrency 4 \
  --max-instances 1 \
  --port 8080 \
  "${SECRET_ARGS[@]}" \
  --set-env-vars "CURSOR_MODEL=${MODEL},SESSIONS_DIR=/tmp/sessions" \
  --quiet

URL="$(gcloud run services describe "$SERVICE" --project="$PROJECT" --region="$REGION" --format='value(status.url)')"
echo ""
echo "Deployed successfully."
echo "  App:    ${URL}"
echo "  Manual: ${URL}/manual"
echo ""
