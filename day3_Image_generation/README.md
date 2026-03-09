# Day 3 – Text to Image Generation: Reverse Prompt Engineering

## Objective

Analyze the reference image and reconstruct it as closely as possible using prompt conditioning on Z-Image Turbo, using the provided SEED.

**SEED used:** `70216`  
**Tool used:** [Z-Image Turbo on Hugging Face](https://huggingface.co/spaces/mrfakename/Z-Image-Turbo)

---

## Reference Image Analysis

The reference image shows:
- A **young Asian woman** with long black hair, wearing **glasses**
- Dressed in a **cream/beige knit sweater**
- Seated at a **round wooden table** in a **cafe setting**
- Typing on a **black laptop** (code visible on screen)
- A **white latte cup and saucer** beside the laptop
- **Large window** behind her with soft natural daylight
- **Side/back profile angle** — candid, not posed
- Warm, soft lighting with shallow depth of field and background bokeh

---

## Iterative Prompt Refinement

### Attempt 1 — Basic Description
```
A woman sitting in a cafe using a laptop
```
**Issue:** Too vague — model produced generic scene, wrong angle, no detail on clothing or lighting.

---

### Attempt 2 — Adding Subject Detail
```
A young Asian woman with glasses and long black hair, wearing a beige sweater, sitting in a cafe on a laptop, coffee cup beside her
```
**Improvement:** Subject detail improved. Lighting still too neutral. Angle not matching.

---

### Attempt 3 — Adding Camera & Lighting Modifiers
```
A young Asian woman with long black hair and glasses, wearing a cozy cream-colored knit sweater, sitting at a round wooden table in a warmly lit cafe, typing on a black laptop, a white latte cup and saucer placed beside the laptop, soft natural light coming through a large window in the background, shallow depth of field, candid side profile angle, photorealistic, 50mm lens, warm tones, bokeh background
```
**Result:** Best match — correct pose, lighting, clothing, and atmosphere.

---

## Final Prompt

```
A young Asian woman with long black hair and glasses, wearing a cozy cream-colored knit sweater, sitting at a round wooden table in a warmly lit cafe, typing on a black laptop, a white latte cup and saucer placed beside the laptop, soft natural light coming through a large window in the background, shallow depth of field, candid side profile angle, photorealistic, 50mm lens, warm tones, bokeh background
```

**SEED:** `70216`

---

## Final Output

See `final_image.png` in this folder.

---

## Key Learnings

- **Vague prompts produce vague images** — specificity is everything.
- **Camera modifiers** (`50mm lens`, `shallow depth of field`, `candid angle`) dramatically change composition.
- **Lighting descriptors** (`warm tones`, `soft natural light`, `bokeh`) define mood and realism.
- **Keeping SEED fixed** allowed fair comparison between prompt iterations — only the prompt changed, not the noise.
- **Style modifiers** like `photorealistic` anchor the model to realistic output rather than illustrated or stylized results.
