from transformers import AutoModelForCausalLM, AutoTokenizer
import os

MODELS = {
    "1": {"name": "gpt2", "size": "500MB"},
    "2": {"name": "facebook/opt-1.3b", "size": "2.7GB"},
    "3": {"name": "mistralai/Mistral-7B-v0.1", "size": "14GB"}
}

def download_model(model_name):
    print(f"⏳ Скачиваю {model_name}...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    print("✅ Модель загружена!")
    return model, tokenizer

def chat_loop(model, tokenizer):
    print("\n💬 Начинаем диалог (для выхода введите 'exit')")
    while True:
        input_text = input("Ты: ")
        if input_text.lower() == 'exit':
            break
        
        inputs = tokenizer(input_text, return_tensors="pt")
        outputs = model.generate(**inputs, max_new_tokens=50)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        print(f"Бот: {response[len(input_text):]}")

if __name__ == "__main__":
    print("🛠 Доступные модели:")
    for key, value in MODELS.items():
        print(f"{key}. {value['name']} ({value['size']})")
    
    choice = input("Выберите модель (1-3): ")
    if choice in MODELS:
        model, tokenizer = download_model(MODELS[choice]["name"])
        chat_loop(model, tokenizer)
    else:
        print("❌ Неверный выбор")
