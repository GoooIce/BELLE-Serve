from peft import PeftModel, get_peft_model
# from transformers import LlamaTokenizer, LlamaForCausalLM 
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig



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

    # device_map = {
    #     "transformer.word_embeddings": 0,
    #     "transformer.word_embeddings_layernorm": 0,
    #     "lm_head": "cpu",
    #     "transformer.h": 0,
    #     "transformer.ln_f": 0,
    # }
    quantization_config = BitsAndBytesConfig(llm_int8_enable_fp32_cpu_offload=True)
    model =  AutoModelForCausalLM.from_pretrained(
        base,
        device_map="auto",
        quantization_config=quantization_config,
    )
    
    # model = PeftModel.from_pretrained(model, finetuned, device_map={'': 0})
    # model = get_peft_model(model, {});
    return model, tokenizer
