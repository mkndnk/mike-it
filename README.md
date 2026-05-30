# flow-local

A free, **100% local** push-to-talk dictation app for macOS — a self-hosted alternative to Wispr Flow. Hold a hotkey, speak, release; your speech is transcribed locally, optionally cleaned up by a local LLM, and pasted into whatever app is focused. No cloud, no subscription, nothing leaves your machine.

## How it works

1. **Hold Right-Option**, speak, release.
2. Audio is transcribed locally with [mlx-whisper](https://github.com/ml-explore/mlx-examples) (`whisper-large-v3-turbo`).
3. Optionally, a local LLM ([mlx-lm](https://github.com/ml-explore/mlx-lm), `Qwen2.5-3B-Instruct-4bit`) cleans up filler words, punctuation, and grammar — without answering or following the dictated text.
4. The result is pasted into the focused app via the clipboard (Cmd+V), then the clipboard is restored.

A menu-bar icon shows status (🎤 idle · 🔴 recording · ✍️ transcribing) and lets you toggle AI cleanup or quit.

> Requires Apple Silicon (MLX). Models download from Hugging Face on first run.

## Setup

```bash
git clone <this-repo> flow-local
cd flow-local
python3.12 -m venv .venv          # or: uv venv --python 3.12
.venv/bin/pip install -r requirements.txt
```

Run it:

```bash
.venv/bin/python flow.py            # menu-bar app
.venv/bin/python flow.py --selftest # test the LLM cleanup step only
```

## Package as a .app (optional)

Building a standalone `FlowLocal.app` gives the app a stable identity so macOS permissions (Microphone, Accessibility, Input Monitoring) attach to it once:

```bash
.venv/bin/python setup.py py2app -A   # ALIAS mode → dist/FlowLocal.app
```

ALIAS mode references the venv and source, so edits to `flow.py` are picked up with **no rebuild**. Rebuild only when `setup.py` changes.

### Permissions

Grant **FlowLocal** (or your terminal, when running from source) access under
System Settings → Privacy & Security:

- **Microphone** — to record speech
- **Accessibility** + **Input Monitoring** — to capture the global hotkey and paste

## Configuration

Tune the config block at the top of [`flow.py`](flow.py):

| Setting | Default | Notes |
| --- | --- | --- |
| `WHISPER_MODEL` | `whisper-large-v3-turbo` | transcription model |
| `CLEANUP_MODEL` | `Qwen2.5-3B-Instruct-4bit` | LLM cleanup model |
| `RECORD_KEY` | Right-Option | hold-to-talk key |
| `LANGUAGE` | `en` | `None` to auto-detect |
| `CLEANUP_ENABLED` | `True` | toggle AI cleanup (also in the menu) |
| `RESTORE_CLIPBOARD` | `True` | restore clipboard after paste |
