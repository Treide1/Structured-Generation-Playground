
# Install command (mutline):
# pip install llama-cpp-python \
#  --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cpu
# Single line:
# pip install llama-cpp-python --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cpu

# Other installs:
# pip install transformers datasets accelerate torch
# pip install llama-cpp-python
# Or Alternatvely:
#pip install exllamav2 transformers torch
#pip install mamba_ssm transformers torch
#pip install vllm

from llama_cpp import Llama

llm = Llama(
      model_path="./models/7B/llama-model.gguf",
      # n_gpu_layers=-1, # Uncomment to use GPU acceleration
      # seed=1337, # Uncomment to set a specific seed
      # n_ctx=2048, # Uncomment to increase the context window
)
output = llm(
      "Q: Name the planets in the solar system? A: ", # Prompt
      max_tokens=32, # Generate up to 32 tokens, set to None to generate up to the end of the context window
      stop=["Q:", "\n"], # Stop generating just before the model would generate a new question
      echo=True # Echo the prompt back in the output
) # Generate a completion, can also call create_completion
print(output)