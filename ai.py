import pickle
import torch
import requests

# 1. Arbitrary code execution via unsafe pickle loading
def load_model_from_pickle(file_path):
    with open(file_path, "rb") as f:
        model = pickle.load(f)  # Vulnerable: arbitrary code execution
    return model

# 2. Unsafe external call
def download_weights(url):
    r = requests.get(url)
    open("weights.bin", "wb").write(r.content)  # Vulnerable: Unvalidated input, no HTTPS check

# 3. Hardcoded secret
API_KEY = "hardcoded-secret-1234"  # Vulnerable: Hardcoded credential

# 4. Insecure eval for prompt-response
def run_custom_logic(logic_str, x):
    return eval(logic_str)  # Vulnerable: eval injection risk

# 5. Dependency on a vulnerable package (add to requirements.txt)
# requests==2.19.0  # Example: known vulnerabilities
