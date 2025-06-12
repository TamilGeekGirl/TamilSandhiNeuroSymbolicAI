##  Best NLLB model for Tamil Sandhi Correction (Panbu Thokai)
This folder contains all necessary configuration and tokenizer files to reproduce the preprocessing and inference settings used in the TamilSandhi project. These files are compatible with Hugging Face Transformers and can be used to initialize the model architecture and tokenizer settings. This will be published in Huggingface in the future. 
## Files Overview

| File                      | Description                                                                                                                |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------|
| `config.json`             | Model architecture configuration (e.g., number of layers, hidden size). Used to recreate the model class without weights.  |
| `generation_config.json`  | Optional config that defines generation parameters such as `max_length`, `num_beams`, and `do_sample`.                     |
| `tokenizer_config.json`   | Metadata describing the tokenizer type, lowercasing rules, padding behavior, etc.                                          |
| `tokenizer.json`          | Tokenizer vocabulary and merge rules stored in a fast, serialized format used by Hugging Face `AutoTokenizer`.             |
| `sentencepiece.bpe.model` | SentencePiece model file used to tokenize raw Tamil input into subword units.                                              |
| `special_tokens_map.json` | Specifies special tokens (e.g., `<pad>`, `<unk>`, `<cls>`, `<sep>`) used during tokenization and decoding.                 |

## Download link (Onedrive)
https://1drv.ms/f/c/d03204a730e16502/EliywB3yerBEgK7D0bDLCtEBwCh8JXz-DMXYPjViIInQ4Q
