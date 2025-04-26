# 🤖 AI Chat with Pre-trained Model

**Локальный чат-бот на основе готовой LLM модели (HuggingFace)**  
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![Python 3.8+](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-yellow?logo=huggingface)
![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?logo=pytorch)

<div align="center">
  
![GitHub repo size](https://img.shields.io/github/repo-size/INVINCIBLEYTTW/ai-chat)
![Downloads](https://img.shields.io/github/downloads/INVINCIBLEYTTW/ai-chat/total?color=blue)
![Last commit](https://img.shields.io/github/last-commit/INVINCIBLEYTTW/ai-chat?color=green)

</div>

---

## 🚀 Быстрый старт

### Установка
```bash
git clone https://github.com/INVINCIBLEYTTW/ai-chat.git
cd ai-chat
pip install -r requirements.txt
Запуск (консольная версия)
bash
python chat.py --model_name="gpt2" --device="cpu"
Запуск (веб-интерфейс)
bash
python web_ui.py --model="mistralai/Mistral-7B-v0.1"
```
✨ Возможности
Автоматическая загрузка моделей с HuggingFace Hub

Поддержка CPU/GPU (через аргумент --device)

Два интерфейса: консольный и Gradio-веб

Кэширование моделей в папке ./models

📸 Скриншоты
<div align="center">
Консольная версия
Консольный чат

Веб-интерфейс
Gradio UI

</div>
🛠 Технологии
Компонент	Версия	Назначение
Transformers	4.36+	Загрузка и управление моделями
PyTorch	2.0+	Инференс моделей
Gradio	3.45+	Веб-интерфейс
SentencePiece	0.1.99	Токенизация
📊 Поддерживаемые модели
Модель	Размер	Минимальные требования
GPT-2	500MB	CPU/2GB RAM
Mistral-7B	14GB	GPU/8GB VRAM
LLaMA-3-8B	16GB	GPU/10GB VRAM
Phi-2	2.7GB	CPU/4GB RAM
❓ FAQ
Как сменить модель?
Измените параметр --model_name при запуске:

bash
python chat.py --model_name="facebook/opt-1.3b"
Где хранятся скачанные модели?
В папке ./models/ (создается автоматически)

Как использовать GPU?
Добавьте аргумент --device cuda:

bash
python chat.py --device cuda
