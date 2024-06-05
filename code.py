import openai
import argparse
import os

# Set up your OpenAI API key from an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_terraform_code(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

def main():
    parser = argparse.ArgumentParser(description="Generate Terraform code using OpenAI's GPT model.")
    parser.add_argument("prompt", type=str, help="The prompt describing the infrastructure.")
    args = parser.parse_args()

    terraform_code = generate_terraform_code(args.prompt)
    print("Generated Terraform code:")
    print(terraform_code)

if _name_ == "_main_":
    main()
