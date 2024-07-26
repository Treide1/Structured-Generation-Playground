import outlines
import pydantic
import llama_cpp

# Shortened version. Doesn't matter.
class Character(pydantic.BaseModel):
    name: str
    age: int

# Download the model from Hugging Face (if necessary)
# curl -L -o mistral-7b-instruct-v0.2.Q5_K_M.gguf https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/resolve/main/mistral-7b-instruct-v0.2.Q5_K_M.gguf

model_path=".\mistral-7b-instruct-v0.2.Q5_K_M.gguf"
model = outlines.models.LlamaCpp(
    model=llama_cpp.Llama(model_path=model_path)
)

# Construct structured sequence generator
generator = outlines.generate.json(model, Character) # ERROR

character = generator("Give me a character description", max_tokens=100)
print(f"Generated character: {character}") 