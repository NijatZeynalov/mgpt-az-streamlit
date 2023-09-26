from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

def get_device():
    if torch.backends.mps.is_available():
        device = torch.device("mps")
    elif torch.cuda.is_available():
        device = torch.device("cuda")
    else:
        device = torch.device("cpu")
    return device


tokenizer = GPT2Tokenizer.from_pretrained("ai-forever/mGPT-1.3B-azerbaijan")
model = GPT2LMHeadModel.from_pretrained("ai-forever/mGPT-1.3B-azerbaijan")

device = get_device()
print('device', device)
model.to(device)

def generate_response(user_input):
        input_ids = tokenizer.encode(user_input, return_tensors="pt").to(device)

        out = model.generate(
                input_ids,
                min_length=50,
                max_length=180,
                eos_token_id=5,
                top_k=5,
                top_p=0.0,
                no_repeat_ngram_size=3
        )
        generated_text = list(map(tokenizer.decode, out))[0]
        last_dot_index = generated_text.rfind(".")

        # Extract the substring up to the last dot
        result = generated_text[:last_dot_index + 1]

        return result


# delete venv folder and dockerize
