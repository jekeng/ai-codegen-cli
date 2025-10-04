# AI Code Generator & Tester

A Python application that uses AI to generate code and corresponding tests for any programming language. The tool leverages LangChain with Groq's LLM to automatically create code based on your requirements and generate appropriate test cases.

## Features

- 🤖 AI-powered code generation using Groq's LLM
- 🧪 Automatic test case generation
- 🌍 Multi-language support (Python, JavaScript, Java, etc.)
- ⚡ Fast and efficient with Groq's API
- 🔧 Command-line interface for easy usage

## Prerequisites

- Python 3.8 or higher
- Groq API key (get one from [Groq Console](https://console.groq.com/))

## Installation

### 1. Create project directory and setup virtual environment
```bash
# Create project directory
mkdir A
cd A

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 2. Clone the repository
```bash
git clone https://github.com/MahdiAmrollahi/ai-codegen-cli.git .
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the project root:
```bash
GROQ_API_KEY=your_groq_api_key_here
```

## Usage

### Basic Usage
```bash
python main.py
```

This will use the default settings:
- Language: Python
- Task: "return list of numbers from 1 to 10"

### Custom Usage
```bash
# Generate JavaScript code
python main.py --language javascript --task "create a function that calculates fibonacci numbers"

# Generate Python code for a specific task
python main.py --language python --task "implement a binary search algorithm"

# Generate Java code
python main.py --language java --task "create a class for a bank account with deposit and withdraw methods"
```

### Command Line Arguments

- `--language`: Programming language for code generation (default: "python")
- `--task`: Description of what the code should do (default: "return list of numbers from 1 to 10")

## Example Output

When you run the script, you'll get output like this:

```
numbers = list(range(1, 11))
assert len(numbers) == 10
assert numbers[0] == 1
assert numbers[-1] == 10
print("All tests passed!")
--------------------------------
numbers = list(range(1, 11))
print(numbers)
```

## Supported Languages

The tool supports most popular programming languages including:
- Python
- JavaScript
- Java
- C++
- C#
- Go
- Rust
- PHP
- Ruby
- And many more!

## Dependencies

- `langchain-groq`: LangChain integration with Groq

- `langchain`: Core LangChain framework
- `python-dotenv`: Environment variable management
- `argparse`: Command-line argument parsing

## Troubleshooting

### Common Issues

1. **API Key Error**: Make sure your `GROQ_API_KEY` is correctly set in the `.env` file
2. **Import Errors**: Ensure all dependencies are installed in your virtual environment
3. **Network Issues**: Check your internet connection and Groq API status

### Getting Help

If you encounter issues:
1. Check that your virtual environment is activated
2. Verify your API key is correct
3. Ensure all dependencies are installed
4. Check the Groq API status page

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Acknowledgments

- [LangChain](https://langchain.com/) for the framework
- [Groq](https://groq.com/) for the AI API
- The open-source community for inspiration
