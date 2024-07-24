import outlines

from huggingface_hub import login
login()
# Access token:
# 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
    
LLAMA3_8B_INSTURCT = "meta-llama/Meta-Llama-3-8B-Instruct"
MISTRAL_7B_INSTURCT = "mistralai/Mistral-7B-Instruct-v0.2"
config_model_name = LLAMA3_8B_INSTURCT

model = outlines.models.transformers(config_model_name)
generator = outlines.generate.text(model)

result = generator("What's 2+2?", max_tokens=100)

print(result)
# That's right, it's 4! But remember, a delicious and nutrient dense 4,
# according to YEARS BUILT ON SOLID SCIENCE. This column presents additional
# findings from the fifteen-year study that produced the 2+2=4 conclusion.