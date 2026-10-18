# Baidu Unlimited-OCR Integration

Use Baidu's `baidu/Unlimited-OCR` model for OCR in this suite. “Unlimited” is the model name and long-horizon design, not a promise of unlimited cloud quota.

Official sources:

- Repository: https://github.com/baidu/Unlimited-OCR
- Model card: https://huggingface.co/baidu/Unlimited-OCR
- vLLM recipe: https://recipes.vllm.ai/baidu/Unlimited-OCR
- Managed API: https://cloud.baidu.com/doc/OCR/s/fmr1p39gb

The integration was checked against Baidu repository revision `d49ff64afffc1f47ab563dc1c589bc2f78808fa4`. Recheck the official instructions before changing model-serving dependencies because this project is recent and its runtime requirements may change.

## Preferred Path: Local Endpoint

Use a local or organization-controlled deployment for unpublished or confidential material. Baidu documents Transformers, vLLM, and SGLang inference. The bundled client follows the OpenAI-compatible SGLang chat-completions request shape shown in Baidu's repository.

One documented server shape is:

```bash
python -m sglang.launch_server \
  --model baidu/Unlimited-OCR \
  --served-model-name Unlimited-OCR \
  --attention-backend fa3 \
  --page-size 1 \
  --mem-fraction-static 0.8 \
  --context-length 32768 \
  --enable-custom-logit-processor \
  --disable-overlap-schedule \
  --skip-server-warmup \
  --host 127.0.0.1 \
  --port 10000
```

Then run:

```bash
python scripts/unlimited_ocr_client.py \
  --pdf paper.pdf \
  --output-dir paper-ocr \
  --server-url http://127.0.0.1:10000
```

The official model is large and GPU-oriented. Do not automatically download model weights, install CUDA packages, launch containers, or alter a user's environment without authorization.

## Remote Self-Hosted Endpoint

The client rejects non-loopback endpoints unless `--allow-remote` is supplied. Use that flag only after confirming authorization, transport security, retention rules, and the destination host. The flag does not make a remote service safe; it records an explicit choice.

## Managed Baidu API

Baidu's managed document-parsing API is asynchronous: submit a task, receive a `task_id`, then poll the query endpoint. It accepts document data or a document URL and can return structured JSON/Markdown. It requires Baidu credentials and is subject to documented file, page, QPS, pricing, and trial limits.

Do not place API keys in a skill file, command history, manuscript, or output. Use environment-backed credentials. Do not upload confidential material unless the user explicitly authorizes the managed service and applicable policy permits it.

The bundled client intentionally targets a local OpenAI-compatible endpoint and does not submit to Baidu Cloud. Add a cloud adapter only for a user who has chosen that deployment route.

## OCR Settings and Tradeoffs

- Use 300 DPI as the default for PDF pages; increase only when small text requires it.
- Use `gundam` image mode for independent pages. Use `base` only when following Baidu's documented multi-image path.
- Use deterministic decoding (`temperature: 0`).
- Preserve one output file per source page before merging.
- Never treat OCR output as sufficient verification for a consequential number, equation, or citation when the rendered page can be checked.
