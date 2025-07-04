import subprocess
import yaml
import os

def load_yaml_prompt(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def call_ollama(model="llama3", cpp_file="main.cpp", yaml_prompt="yaml/prompt_strict.yaml"):
    # Load C++ code
    with open(cpp_file, 'r') as f:
        cpp_code = f.read()

    # Load YAML prompt
    prompt_data = load_yaml_prompt(yaml_prompt)

    # Construct prompt
    full_prompt = f"""
{prompt_data['task']}

Instructions:
{chr(10).join('- ' + item for item in prompt_data['instructions'])}

C++ Code:
{cpp_code}

Respond only with valid Google Test C++ code.
"""

    print("⏳ Sending prompt to Ollama...")

    # Run Ollama with subprocess
    result = subprocess.run(
        ["ollama", "run", model],
        input=full_prompt.encode(),
        capture_output=True
    )

    response = result.stdout.decode()

    # Save response to test_main.cpp
    os.makedirs("tests", exist_ok=True)
    with open("tests/test_main.cpp", "w") as f:
        f.write(response)

    print("✅ Unit test generated at tests/test_main.cpp")

if __name__ == "__main__":
    call_ollama()
