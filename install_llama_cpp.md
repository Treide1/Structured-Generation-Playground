# How to install the Python package `llama-cpp-python`

Install instructions from: https://pypi.org/project/llama-cpp-python/

# With CUDA (GPU support)

Get your cuda version, also named "release":
```bash
nvcc --version
```

Install the package using your `<cuda_version>`:
```bash
pip install llama-cpp-python --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/<cuda_version>
```

In my case, cuda 12.2 worked fine.

# With CPU only

```bash
pip install llama-cpp-python --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cpu
```