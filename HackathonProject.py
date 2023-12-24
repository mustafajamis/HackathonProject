import sys
import re
import openai

# Set your personal OpenAI API key here
openai.api_key = "Here put your api key" # Information how to so it follow the link https://platform.openai.com/api-keys

def send_code_to_model(perl_file, error=None):
    # Sending Perl code to the model
    print("Sending Perl code to the model...")

    with open(perl_file, 'r') as file:
        perl_code = file.read()

    # Constructing the prompt for OpenAI model
    prompt = f"Here is some Perl code:\n{perl_code}\nPlease convert this code to Python."

    if error is not None:
        prompt += f"\nThe previous attempt to execute the Python code resulted in the following error: {error}"

    # Sending the prompt to OpenAI and receiving the response
    response = openai.Completion.create(
        endpoint="https://api.openai.com/v1/engines/davinci/completions",  # Specify the correct endpoint
        prompt=prompt,
        temperature=0.1,
        max_tokens=2500,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )

    print("Perl code sent to the model.")

    # Extracting Python code from the model's response
    python_code = response['choices'][0]['text']
    match = re.search(r'python\n(.*?)\n', python_code, re.DOTALL)

    return match.group(1)

def write_python_code_to_file(python_code, python_file):
    # Writing Python code to a file
    print("Writing Python code to file...")

    with open(python_file, 'w') as file:
        file.write(python_code)

    print("Python code written to file.")

def execute_python_code(python_file):
    # Executing Python code
    print("Executing Python code...")

    with open(python_file, 'r') as file:
        python_code = file.read()

    try:
        exec(python_code)
    except Exception as e:
        return str(e)

    print("Python code executed.")
    return None

def main():
    print("OpenAI model initialized.")

    # Paths to Perl and Python files
    perl_file = r'Your perl file you want to convert'
    python_file = r'The place where it will save the converted code'
    error = None
    counter = 0

    # Loop for multiple iterations
    while counter < 5:
        print(f"Starting iteration {counter + 1}")

        # Convert Perl code to Python
        python_code = send_code_to_model(perl_file, error)

        # Write the Python code to a file
        write_python_code_to_file(python_code, python_file)

        # Execute the Python code and handle errors
        error = execute_python_code(python_file)

        if error is not None:
            print(f'An error occurred in iteration {counter + 1}: {error}')
        else:
            print('The code executed successfully')
            break

        counter += 1
        print(f"Finished iteration {counter}")

if __name__ == "__main__":
    main()
