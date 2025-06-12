import torch
import gradio as gr
import warnings
from transformers import (
    MT5ForConditionalGeneration, MT5Tokenizer,
    MBartForConditionalGeneration, MBart50Tokenizer,
    AutoModelForSeq2SeqLM, AutoTokenizer
)

# Suppress warnings and logs
warnings.filterwarnings("ignore")
from transformers.utils import logging
logging.set_verbosity_error()

device = "cuda" if torch.cuda.is_available() else "cpu"

def load_model_and_tokenizer(model_choice):
    if model_choice == "mT5":
        model = MT5ForConditionalGeneration.from_pretrained("best-mt5-model").to(device)
        tokenizer = MT5Tokenizer.from_pretrained("best-mt5-model")
    elif model_choice == "mBART":
        model = MBartForConditionalGeneration.from_pretrained("Bestmbartmodel_panbuThokai").to(device)
        tokenizer = MBart50Tokenizer.from_pretrained("BestmbartTokenizer_panbuThokai")
        tokenizer.src_lang = "ta_IN"
        tokenizer.tgt_lang = "ta_IN"
    elif model_choice == "NLLB":
        model = AutoModelForSeq2SeqLM.from_pretrained("best-nllb-model").to(device)
        tokenizer = AutoTokenizer.from_pretrained("best-nllb-model")
        tokenizer.src_lang = "tam_Taml"
    else:
        raise ValueError("Invalid model")
    return model, tokenizer

loaded_models = {}

def predict(input_text, model_choice):
    if model_choice not in loaded_models:
        model, tokenizer = load_model_and_tokenizer(model_choice)
        loaded_models[model_choice] = (model, tokenizer)
    else:
        model, tokenizer = loaded_models[model_choice]

    

    if model_choice == "NLLB":
        inputs = tokenizer(f">>tam_Taml<< {input_text}", return_tensors="pt").to(device)
        bos_token_id = tokenizer.convert_tokens_to_ids(">>tam_Taml<<")
        output = model.generate(
            **inputs,
            max_length=128,
            num_beams=5,
            forced_bos_token_id=bos_token_id
        )
    else:
        inputs = tokenizer(input_text, return_tensors="pt").to(device)
        output = model.generate(
            **inputs,
            max_length=128,
            num_beams=5,
            early_stopping=True
        )

    return tokenizer.decode(output[0], skip_special_tokens=True)

iface = gr.Interface(
    fn=predict,
    inputs=[
        gr.Textbox(lines=4, placeholder="Enter Tamil sentence here..."),
        gr.Dropdown(["mT5", "mBART", "NLLB"], label="Select Model")
    ],
    outputs="text",
    title="Neural Tamil Sandhi Correction",
    description="Select mT5, mBART, or NLLB to correct Sandhi errors in Tamil text. NLLB is configured to always output Tamil."
)

if __name__ == "__main__":
    iface.launch()