import warnings
warnings.filterwarnings("ignore")

import torch
from transformers import (
    MT5ForConditionalGeneration, MT5Tokenizer,
    MBartForConditionalGeneration, MBart50Tokenizer,
    AutoModelForSeq2SeqLM, AutoTokenizer
)

def load_model(model_type):
    if model_type.lower() == "mt5":
        model = MT5ForConditionalGeneration.from_pretrained("best-mt5-model")
        tokenizer = MT5Tokenizer.from_pretrained("best-mt5-model")
    elif model_type.lower() == "mbart":
        model = MBartForConditionalGeneration.from_pretrained("Bestmbartmodel_panbuThokai")
        tokenizer = MBart50Tokenizer.from_pretrained("BestmbartTokenizer_panbuThokai")
    elif model_type.lower() == "nllb":
        model = AutoModelForSeq2SeqLM.from_pretrained("best-nllb-model")
        tokenizer = AutoTokenizer.from_pretrained("best-nllb-model")
    else:
        raise ValueError("Invalid model type. Choose 'mt5', 'mbart', or 'nllb'.")

    device = "cuda" if torch.cuda.is_available() else "cpu"
    return model.to(device), tokenizer, device

def generate(model, tokenizer, input_text, device, model_type):
    inputs = tokenizer(input_text, return_tensors="pt").to(device)
    if model_type == "nllb":
        bos_token_id = tokenizer.convert_tokens_to_ids(">>tam_Taml<<")
        output_ids = model.generate(
            **inputs,
            max_length=128,
            num_beams=5,
            forced_bos_token_id=bos_token_id
        )
    else:
        output_ids = model.generate(
            **inputs,
            max_length=128,
            num_beams=5,
            early_stopping=True
        )
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)

if __name__ == "__main__":
    print("Choose a model: [mt5 / mbart / nllb]")
    model_type = input("Model > ").strip().lower()
    model, tokenizer, device = load_model(model_type)

    print(f" {model_type.upper()} CLI is ready! Type your input:")
    while True:
        try:
            user_input = input("\nInput > ")
            if user_input.lower() in ["exit", "quit"]:
                break
            output = generate(model, tokenizer, user_input, device, model_type)
            print("Output:", output)
        except KeyboardInterrupt:
            print("\nExiting.")
            break
