# refine_test.py

import subprocess
import yaml
import os

def load_yaml_prompt(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def refine_tests(model="llama3", test_file="tests/test_main.cpp", yaml_prompt="yaml/refine_prompt.yaml"):
    # Load generated test code
    with open(test_file, 'r') as f:
        test_code = f.read()

    # Load YAML refine prompt
    prompt_data = load_yaml_prompt(yaml_prompt)

    # Construct refinement prompt
    refine_prompt = f"""
{prompt_data['task']}

Instructions:
{chr(10).join('- ' + instr for instr in prompt_data['instructions'])}

Test Code:
{test_code}

Respond only with valid, refined Google Test code.
"""

    print("⏳ Sending refinement prompt to Ollama...")

    result = subprocess.run(
        ["ollama", "run", model],
        input=refine_prompt.encode(),
        capture_output=True
    )

    response = result.stdout.decode()

    # Save to new file
    os.makedirs("tests", exist_ok=True)
    with open("tests/test_main_refined.cpp", "w") as f:
        f.write(response)

    print("✅ Refined test saved to tests/test_main_refined.cpp")

if __name__ == "__main__":
    refine_tests()
