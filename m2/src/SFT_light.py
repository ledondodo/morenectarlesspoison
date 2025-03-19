# author: Arthur Chansel 324265
# group: MoreNectarLessPoison
# file: SFTT.py

import os
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer
from trl import SFTTrainer

if __name__ == "__main__":

    # Download our model: phi-2
    model_name = "microsoft/phi-2"
    model = AutoModelForCausalLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokenizer.pad_token = tokenizer.eos_token # allow padding? not sure about this...

    # Load dataset: OpenBookQA
    DATASET = "data_OpenBookQA.jsonl"
    subset = range(50) # small range for light training
    dataset = load_dataset('json', data_files=DATASET, split='train').select(subset)

    # --- Training ---

    os.environ["TOKENIZERS_PARALLELISM"] = "false" # remove to improve performances?

    trainer = SFTTrainer(
        model,
        train_dataset=dataset,
        packing=True
    )
    # Change batch size:
    # trainer.args.per_device_train_batch_size = 1
    trainer.train()