from peft import PeftModel, get_peft_model
# from transformers import LlamaTokenizer, LlamaForCausalLM 
# from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from transformers import BloomTokenizerFast, BloomForCausalLM


def load_model(
    base="YeungNLP/firefly-1b4",
    finetuned="tloen/alpaca-lora-7b",
):
    tokenizer =  BloomTokenizerFast.from_pretrained(base)


    model =  BloomForCausalLM.from_pretrained(
        base
    )
    model = model.to('cuda')

    return model, tokenizer
