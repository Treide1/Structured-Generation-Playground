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

In my case, `<cuda_version>=cu122` (CUDA 12.2) worked fine...
Well, almost. 
It circumvented the GPU and went for the CPU anyway.
So I downgraded to `0.2.77` which then actually worked.

Full command chain:
```bash
set CUDACXX="C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.2\bin\nvcc"
set CMAKE_ARGS="-DGGML_CUDA=on -DCMAKE_CUDA_ARCHITECTURES=all-major"
pip install llama-cpp-python==0.2.77 --no-cache-dir --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cu122
```

# With CPU only

```bash
pip install llama-cpp-python --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cpu
```