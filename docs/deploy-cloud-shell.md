# Cloud Shell 部署 Cloud Run

在 [Google Cloud Shell](https://shell.cloud.google.com/) 中执行以下步骤。

## 一、克隆代码

```bash
git clone https://github.com/Yude-Jiang/metastellar-ppt.git
cd metastellar-ppt
```

若使用功能分支：

```bash
git fetch origin cursor/remove-st-brand-metastellar-fbd9
git checkout cursor/remove-st-brand-metastellar-fbd9
```

## 二、设置项目

```bash
export GCP_PROJECT=你的项目ID
gcloud config set project $GCP_PROJECT
```

## 三、首次：创建 API Key 密钥（只需一次）

```bash
# 启用 API
gcloud services enable run.googleapis.com cloudbuild.googleapis.com secretmanager.googleapis.com

# 写入 Cursor API Key（替换为你的真实 key）
echo -n 'sk-xxxxxxxx' | gcloud secrets create CURSOR_API_KEY \
  --data-file=- --replication-policy=automatic

# 授权 Cloud Run 默认服务账号读取密钥
PROJECT_NUMBER=$(gcloud projects describe $GCP_PROJECT --format='value(projectNumber)')
gcloud secrets add-iam-policy-binding CURSOR_API_KEY \
  --member="serviceAccount:${PROJECT_NUMBER}-compute@developer.gserviceaccount.com" \
  --role="roles/secretmanager.secretAccessor"
```

若密钥已存在，只需更新版本：

```bash
echo -n 'sk-新key' | gcloud secrets versions add CURSOR_API_KEY --data-file=-
```

## 四、部署

**方式 A — 一键脚本（推荐）**

```bash
export GCP_PROJECT=你的项目ID
export GCP_REGION=asia-east1
bash scripts/deploy-cloud-run.sh
```

**方式 B — 手动命令**

```bash
gcloud run deploy metastellar-ppt \
  --source . \
  --project $GCP_PROJECT \
  --region asia-east1 \
  --allow-unauthenticated \
  --memory 2Gi --cpu 2 --timeout 600 \
  --concurrency 4 --max-instances 1 \
  --set-secrets CURSOR_API_KEY=CURSOR_API_KEY:latest \
  --set-env-vars CURSOR_MODEL=composer-2.5
```

构建约 **5–15 分钟**（含 Playwright + LibreOffice 镜像层）。

## 五、验证

部署完成后终端会输出服务 URL，例如：

```
https://metastellar-ppt-xxxxx-asia-east1.a.run.app
```

- 应用首页：`/`
- 用户手册：`/manual`

## 六、更新部署

代码更新后，在仓库目录重新执行：

```bash
git pull
bash scripts/deploy-cloud-run.sh
```

## 常见问题

| 问题 | 处理 |
|------|------|
| `Permission denied` on secret | 执行第三节 IAM 绑定 |
| 构建超时 | Cloud Build 默认 10min，大镜像可能需重试；或先本地 `docker build` 排查 |
| Agent 报错 API key | 检查 Secret Manager 中 `CURSOR_API_KEY` 是否有效 |
| 对话模式丢上下文 | 保持 `--max-instances 1` |

## 可选环境变量

部署后可更新：

```bash
gcloud run services update metastellar-ppt \
  --region asia-east1 \
  --set-env-vars MAX_PAGES=8,RATE_LIMIT_PER_MINUTE=20
```
