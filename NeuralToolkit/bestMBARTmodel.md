# Best mBART Model for Tamil Sandhi Correction (Panbu Thokai)

This repository contains the tokenizer and model configuration files for the best-performing mBART model fine-tuned to detect and correct Sandhi errors in Tamil *Panbu Thokai* constructions.

The model is part of the **TamilSandhi** neuro-symbolic AI framework for morphophonemic correction in Tamil. It is intended for research use and reproducibility. Model weights are included here in `safetensors` format.

---

## Directory Structure
BestMBARTmodel_panbuThokai/
┣  Bestmbartmodel_panbuThokai/
┃ ┣ config.json
┃ ┣ generation_config.json
┃ ┗ model.safetensors

┣ BestmbartTokenizer_panbuThokai/
┃ ┣ sentencepiece.bpe.model
┃ ┣ special_tokens_map.json
┃ ┗ tokenizer_config.json
