import outlines

use_hf_download_mode = False
use_raw_download_mode = False

if use_hf_download_mode:
    # Load access token from environment variable
    import os
    from dotenv import load_dotenv

    path_to_env_file = "./.env"
    key_name = "HF_ACCESS_TOKEN"
    token = None

    if os.path.exists(path_to_env_file):
        load_dotenv(path_to_env_file)
        token = os.getenv(key_name)

    from huggingface_hub import login
    if token is not None:
        print(f"Logging in with token from environment variable: {key_name}")
        login(token=token, add_to_git_credential=True)
    else:
        # Manual login:
        # * Add Access token 
        # -> Revoked example: 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
        # * Add to git as token for remembered login
        print(f"Token not found in environment variable: {key_name}")
        login()
elif use_raw_download_mode:
    # Run:
    # `curl -L -o mistral-7b-instruct-v0.2.Q5_K_M.gguf https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/resolve/main/mistral-7b-instruct-v0.2.Q5_K_M.gguf`
    import os
    local_expected_file = "mistral-7b-instruct-v0.2.Q5_K_M.gguf"
    
    # Check if file exists
    if not os.path.exists(local_expected_file):
        print(f"Downloading file: {local_expected_file}")
        os.system("curl -L -o mistral-7b-instruct-v0.2.Q5_K_M.gguf https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/resolve/main/mistral-7b-instruct-v0.2.Q5_K_M.gguf")

    
LLAMA3_8B_INSTURCT = "meta-llama/Meta-Llama-3-8B-Instruct"
MISTRAL_7B_INSTURCT = "mistralai/Mistral-7B-Instruct-v0.2"
MISTRAL_7B_INSTURCT_Q5_K_M = "./mistral-7b-instruct-v0.2.Q5_K_M.gguf"
config_model_name = MISTRAL_7B_INSTURCT_Q5_K_M

model = outlines.models.transformers(config_model_name)
generator = outlines.generate.text(model)

result = generator("What's 2+2?", max_tokens=100)

print(result)
# That's right, it's 4! But remember, a delicious and nutrient dense 4,
# according to YEARS BUILT ON SOLID SCIENCE. This column presents additional
# findings from the fifteen-year study that produced the 2+2=4 conclusion.