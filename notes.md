we will try to learn using both open source and closed source models.
here we dont have api keys of openAI ,anthropic and gemini as they are paid so we will just try to learn how can we use it and its code nothing else.

nowadays llms are not that used widely so will not focus on them or main focus will be chatmodels.


# Open-Source Models

## What are Open-Source Models?

Open-source models are language models whose model weights/code are made available for others to use, modify, and deploy, depending on their license.

They can be used in two main ways:

```text
                    Open-Source Models
                    /                 \
                   /                   \
        Using HF Inference API     Running Locally
```

### 1. Using Hugging Face (HF) Inference API

The model is hosted on Hugging Face's infrastructure.

Your application sends a request through the internet:

```text
Your Application
       ↓
   Internet
       ↓
Hugging Face
       ↓
    Model
       ↓
   Response
```

You don't need to download and run the entire model on your own computer.

### 2. Running Locally

You download the model and run it on your own computer/server.

```text
Your Computer
      ↓
Download Model
      ↓
Run Model Locally
```

The model's computation happens on your own hardware.

---

# Some Famous Open-Source Models

| Model | Developer | Parameters | Best Use Case |
|---|---|---:|---|
| LLaMA-2-7B/13B/70B | Meta AI | 7B–70B | General-purpose text generation |
| Mixtral-8x7B | Mistral AI | 8x7B (MoE) | Efficient & fast responses |
| Mistral-7B | Mistral AI | 7B | Best small-scale model |
| Falcon-7B/40B | TII UAE | 7B–40B | High-speed inference |
| BLOOM-176B | BigScience | 176B | Multilingual text generation |
| GPT-J-6B | EleutherAI | 6B | Lightweight and efficient |
| GPT-NeoX-20B | EleutherAI | 20B | Large-scale applications |
| StableLM | Stability AI | 3B–7B | Compact models for chatbots |

---

# Where to Find Open-Source Models?

### Hugging Face

**Hugging Face** is one of the largest repositories/platforms for open-source AI models.

It provides access to many different:

- Language models
- Embedding models
- Vision models
- Audio models
- Multimodal models

You can find models and their documentation on Hugging Face.

---

# Ways to Use Open-Source Models

There are two main approaches:

### 1. Using HF Inference API

Instead of running the model yourself, you send requests to Hugging Face's API.

Advantages:

- No need to download the model.
- No need to have powerful hardware.
- Model runs on Hugging Face's infrastructure.
- Easier to get started.

### 2. Running Locally

Download the model and run it on your own machine.

Advantages:

- More control over the model.
- Data can remain on your machine.
- No need to send every request to an external API.
- Can customize or fine-tune the model.


# Disadvantages of Open-Source Models

### 1. High Hardware Requirements

Running large models such as LLaMA-2-70B requires expensive GPUs.

Larger models generally require more:

- RAM/VRAM
- GPU power
- Storage
- Computing resources

### 2. Setup Complexity

Running models locally can require installing dependencies such as:

- PyTorch
- CUDA
- Transformers
- Other model-specific libraries

Therefore, local setup can be more complicated than simply calling an API.

### 3. Lack of RLHF

Some open-source models may have less extensive human-feedback-based alignment/fine-tuning than proprietary models.

This can make them weaker at instruction-following compared with some highly aligned proprietary models.

### 4. Limited Multimodal Abilities

Some open-source models may have limited support for:

- Images
- Audio
- Video

compared with multimodal proprietary models such as GPT-4V mentioned in the lecture.

---

# Important for Learning LangChain

For this tutorial, **you don't necessarily need to purchase an API**.

The important thing is to understand:

```text
Application
     ↓
LangChain
     ↓
Model
     ↓
Response
```

You mainly want to learn **how LangChain connects to and interacts with models**.

You can follow the instructor's code to understand:

- How a model is initialized
- How prompts are sent
- How responses are received
- How LangChain provides a common interface
- How open-source models can be integrated
- Difference between using an API and running a model locally

You can learn the code and understand the workflow even if you don't actually run every paid API example.

---

# Key Takeaway

There are essentially two ways to use an open-source model:

```text
Open-Source Model
       |
       +-------------------------+
       |                         |
       ↓                         ↓
Hugging Face API            Run Locally
       |                         |
       ↓                         ↓
Internet/API required       Your own hardware
       |                         |
       ↓                         ↓
Easy setup                  More setup
```

