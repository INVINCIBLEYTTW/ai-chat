# 🤖 ИИ-чат с предобученной моделью

[![Лицензия: MIT](https://img.shields.io/badge/Лицензия-MIT-blue.svg)](LICENSE)
![Python 3.8+](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-yellow?logo=huggingface)

## 📊 Статистика GitHub
<div align="center">

![Статистика](https://github-readme-stats.vercel.app/api?username=INVINCIBLEYTTW&show_icons=true&theme=dark&locale=ru)
![Языки](https://github-readme-stats.vercel.app/api/top-langs/?username=INVINCIBLEYTTW&layout=compact&theme=dark&locale=ru)
![Репозиторий](https://github-readme-stats.vercel.app/api/pin/?username=INVINCIBLEYTTW&repo=ai-chat&theme=dark)

</div>

## 🚀 Быстрый старт
```bash
git clone https://github.com/INVINCIBLEYTTW/ai-chat.git
pip install -r requirements.txt
python chat.py --model=gpt2
🛠 Технологии
Модели: GPT-2, Mistral-7B, LLaMA-3 (через HuggingFace)

Запуск: PyTorch 2.0+ (CPU/CUDA)

Интерфейс: Gradio 3.45+

📊 Производительность моделей
Модель	Размер	Скорость (токенов/сек)	Память
GPT-2	500MB	45 (CPU)	2GB RAM
Mistral-7B	14GB	28 (CUDA)	8GB VRAM
📌 Пример использования
python
from transformers import AutoModelForCausalLM
model = AutoModelForCausalLM.from_pretrained("gpt2")
<div align="center">
Пример работы

</div> 
