# 🤖 AI Chat with Pre-trained Model

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![Python 3.8+](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-yellow?logo=huggingface)

## 📊 GitHub Stats
<div align="center">

![Profile Stats](https://github-readme-stats.vercel.app/api?username=INVINCIBLEYTTW&show_icons=true&theme=dark)
![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=INVINCIBLEYTTW&layout=compact&theme=dark)
![Repo Stats](https://github-readme-stats.vercel.app/api/pin/?username=INVINCIBLEYTTW&repo=ai-chat&theme=dark)

</div>

## 🚀 Quick Start
```bash
git clone https://github.com/INVINCIBLEYTTW/ai-chat.git
pip install -r requirements.txt
python chat.py --model=gpt2
```

## 🛠 Tech Stack
- **Models**: GPT-2, Mistral-7B, LLaMA-3 (via HuggingFace)
- **Inference**: PyTorch 2.0+ (CPU/CUDA)
- **Interface**: Gradio 3.45+

## 📊 Model Benchmarks
| Model | Size | Speed (tokens/sec) | RAM Usage |
|-------|------|-------------------|-----------|
| GPT-2 | 500MB | 45 (CPU) | 2GB |
| Mistral-7B | 14GB | 28 (CUDA) | 8GB VRAM |

## 📌 Usage
```python
from transformers import AutoModelForCausalLM
model = AutoModelForCausalLM.from_pretrained("gpt2")
```

<div align="center">
  
![Code Example](https://via.placeholder.com/600x200/2D3748/FFFFFF?text=Model+Inference+Example)

</div>
```
