from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "Qwen/Qwen2.5-0.5B-Instruct"

print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(model_name)

print("Loading local LLM...")
model = AutoModelForCausalLM.from_pretrained(model_name)

print("Local LLM loaded successfully!")


def generate_answer(question: str):
    messages = [
        {
            "role": "user",
            "content": question
        }
    ]

    inputs = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        tokenize=True,
        return_dict=True,
        return_tensors="pt"
    )

    outputs = model.generate(
        **inputs,
        max_new_tokens=100
    )

    generated_tokens = outputs[0][inputs["input_ids"].shape[-1]:]

    answer = tokenizer.decode(
        generated_tokens,
        skip_special_tokens=True
    )

    return answer