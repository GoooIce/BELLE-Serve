from peft import PeftModel
from transformers import AutoTokenizer, AutoModelForCausalLM #, LlamaTokenizer, LlamaForCausalLM 

def load_model(
    base="BelleGroup/BELLE-7B-2M",
    finetuned="tloen/alpaca-lora-7b",
):
    # tokenizer = LlamaTokenizer.from_pretrained(base)
    # tokenizer.pad_token_id = 0
    # tokenizer.padding_side = "left"

    # model = LlamaForCausalLM.from_pretrained(
    #     base,
    #     load_in_8bit=True,
    #     device_map="auto",
    # )
    tokenizer =  AutoTokenizer.from_pretrained(base, add_eos_token=True)

    model =  AutoModelForCausalLM.from_pretrained(
        base,
        load_in_8bit=True,
        device_map="auto",
    )
    
    model = PeftModel.from_pretrained(model, finetuned, device_map={'': 0})
    return model, tokenizer

