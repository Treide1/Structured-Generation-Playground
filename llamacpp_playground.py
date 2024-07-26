from common import joined_path

from llama_cpp import Llama
path = R"C:\Users\Lukas\Desktop\projects\outlines_playground\Structured-Generation-Playground\mistral-7b-instruct-v0.2.Q5_K_M.gguf"
llm = Llama(model_path=path, n_gpu_layers=-1, n_ctx=3584, n_batch=521, verbose=True)
# adjust n_gpu_layers as per your GPU and model
output = llm("Q: Name the planets in the solar system? A: ", max_tokens=32, stop=["Q:", "\n"], echo=True)
print(output)