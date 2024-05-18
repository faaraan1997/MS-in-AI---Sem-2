from transformers import AutoModelForCausalLM, AutoTokenizer
from PIL import Image

def execute(prompt, image):
    model_id = "vikhyatk/moondream2"
    revision = "2024-04-02"
    model = AutoModelForCausalLM.from_pretrained(
        model_id, trust_remote_code=True, revision=revision
    )
    tokenizer = AutoTokenizer.from_pretrained(model_id, revision=revision)
    
    enc_image = model.encode_image(image)
    answer = model.answer_question(enc_image, prompt, tokenizer)

    return answer