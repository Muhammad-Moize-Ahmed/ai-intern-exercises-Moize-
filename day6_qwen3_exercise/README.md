# Qwen3.5-0.8B — Local LLM Exercise

## System Specs

| | |
|---|---|
| **CPU** | Intel(R) Core(TM) i5-7440HQ @ 2.80GHz (4 Cores, 4 Logical Processors) |
| **RAM** | 7.6 GB |
| **GPU** | Intel(R) HD Graphics 6xx (integrated, not used for inference) |
| **OS** | Windows 10 |
| **Storage** | SSD |

## Framework / Runtime

**LM Studio** — local server mode (OpenAI-compatible API on port 1234)  
**Inference script:** Python  
**Model:** Qwen3.5-0.8B

## How to Run

1. Install LM Studio from https://lmstudio.ai
2. Download **Qwen3.5-0.8B** inside LM Studio
3. Go to the **Local Server** tab → click **Start Server** (port 1234)
4. Install dependency: `pip install openai`
5. Run: `python run_model.py`

Prompts and responses are automatically saved to `prompts_and_responses.md`.

## Performance Observations

- **Response speed:** ~30–90 seconds per response (CPU only, no GPU acceleration)
- **Memory usage:** ~1–1.5 GB RAM per inference
- **RAM warning:** System was at 95% memory usage at idle — closing background apps before running is strongly recommended

## Difficulties Encountered

- Very high baseline memory usage (~7.2/7.6 GB at idle) left minimal headroom for inference
- Integrated Intel GPU is not supported for LLM acceleration in LM Studio — CPU-only inference
- Responses are slow but accurate for a 0.8B model running entirely on consumer hardware
