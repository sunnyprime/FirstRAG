from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "Qwen/Qwen2.5-0.5B-Instruct"

print("1. Loading tokenizer...")

tokenizer = AutoTokenizer.from_pretrained(model_name)

print("2. Loading model...")

model = AutoModelForCausalLM.from_pretrained(model_name)

print("3. Model loaded successfully!")

messages = [
    {
        "role": "user",
        "content": "What is RAG? Answer in one simple sentence."
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

print("\nLLM Answer:")
print(answer)