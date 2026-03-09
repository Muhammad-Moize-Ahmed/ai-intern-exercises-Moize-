# Transformer Day 1 Exercise

## 1️⃣ What is Generative AI?

Generative AI refers to a class of machine learning models that can **create new content** — text, images, audio, code, or video — by learning patterns from large amounts of training data. Unlike traditional discriminative models that simply classify or predict labels, generative models learn the underlying distribution of the data and use it to produce novel outputs.

**How it differs from traditional ML:**

Traditional machine learning models are designed to map inputs to fixed outputs — for example, classifying an email as spam or not spam. They are trained on labeled data and optimized for a specific, narrow task. Generative AI, on the other hand, learns to model data itself, not just decisions about it. It can generalize across tasks, produce open-ended outputs, and even perform tasks it was never explicitly trained on (zero-shot generalization).

**3 Real-World Applications:**

1. **Text Generation (LLMs):** Models like GPT-4 and Claude generate human-quality text for writing, coding, Q&A, and summarization.
2. **Image Synthesis:** Models like DALL·E and Stable Diffusion generate photorealistic images from text prompts.
3. **Drug Discovery:** Generative models propose novel molecular structures for pharmaceutical research, dramatically accelerating the discovery pipeline.

---

## 2️⃣ Self-Attention Explained

**Sentence:** `"The cat sat on the mat"`

### Query (Q), Key (K), and Value (V)

Each word in the sentence is represented as a vector. From that vector, three separate vectors are derived via learned weight matrices:

- **Query (Q):** Represents what the current word is *looking for* — its information need.
- **Key (K):** Represents what each word *offers* — its identity or content.
- **Value (V):** Represents the actual *information* a word contributes if it is attended to.

For the word `"cat"`, the Query asks: *"which words are relevant to me?"* The Keys of all words (including `"sat"`, `"mat"`) respond with their relevance scores. The final output is a weighted sum of Values, where weights come from how well Q matched each K.

### Why scale by √d_k?

The dot product of Q and K grows in magnitude as the dimension `d_k` increases. Large values push the softmax function into regions of extremely small gradients, making learning unstable. Dividing by √d_k keeps the scores in a numerically stable range.

### Why apply Softmax?

Softmax converts the raw attention scores into a probability distribution that sums to 1. This allows the model to assign meaningful, normalized weights to each word's Value — so the output is a weighted blend of the most relevant words.

### What problem does attention solve that RNNs struggled with?

RNNs process sequences step-by-step, which means information from early tokens must travel through many hidden states to reach later ones — causing the **vanishing gradient problem** and poor long-range dependency modeling. Self-attention connects every word directly to every other word in a single step, regardless of distance, making it far more effective at capturing long-range relationships.

---

## 3️⃣ Encoder vs Decoder Comparison

| Component | Encoder | Decoder |
|---|---|---|
| **Primary Role** | Understands and encodes the input | Generates output token by token |
| **Self-Attention Type** | Bidirectional (sees full input) | Masked (sees only past tokens) |
| **Cross-Attention** | ❌ Not present | ✅ Attends to encoder output |
| **Masked Attention** | ❌ Not used | ✅ Used to prevent future token leakage |
| **Typical Use Cases** | Classification, NER, embeddings (e.g. BERT) | Text generation, translation (e.g. GPT, T5 decoder) |

**Masked Attention:** In the decoder, self-attention is masked so that when generating token `t`, the model cannot see tokens at positions `t+1` and beyond. This preserves the autoregressive property during training.

**Cross-Attention:** The decoder uses cross-attention to query the encoder's output. This lets the decoder focus on relevant parts of the input sequence while generating each output token — critical for tasks like translation.

---

## 4️⃣ Vision Transformers (ViT) — High-Level Explanation

A **Vision Transformer (ViT)** applies the transformer architecture — originally designed for text — directly to images.

**Image Patches:** An input image (e.g. 224×224 pixels) is divided into fixed-size non-overlapping patches (e.g. 16×16 pixels). A 224×224 image with 16×16 patches produces 196 patches.

**Patches as Tokens:** Each patch is flattened into a 1D vector and projected via a linear layer into an embedding of fixed dimension. This gives us a sequence of patch embeddings — directly analogous to word token embeddings in a text transformer.

**Positional Embeddings:** Unlike CNNs, transformers have no built-in notion of spatial order. Since attention treats all patches equally regardless of position, learnable positional embeddings are added to each patch embedding so the model knows where in the image each patch came from.

**How it differs from CNNs:** CNNs use local convolutional filters that slide across the image, building up spatial hierarchies from local to global features. ViT, by contrast, applies self-attention globally from the very first layer — every patch can directly attend to every other patch. This gives ViT superior performance on large datasets and better ability to model long-range spatial dependencies, though it requires significantly more data to train than CNNs.

---

## ⚙️ Setup

```bash
pip install -r requirements.txt
python attention_demo.py
```
