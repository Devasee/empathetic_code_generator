Empathetic Code Reviewer

This application generates encouraging, mentor-like code review reports using the Groq API and the Llama3 model.

Prerequisites

Before starting, ensure you have:

- Python 3.10 or newer
- A reliable internet connection (required for API requests)
- The `requests` Python package

Setup

To get started:

1. Clone this repository or download it as a ZIP file.
2. Open your terminal in the project directory.
3. Install the required dependencies:

Input Preparation

The tool expects an `input_data.json` file.

Edit this file to include your code snippet and any comments for review. The format should be:

```json
{
  "code_snippet": "<your code here>",
  "review_comments": [
 "Comment one",
 "Comment two"
  ]
}

You may leave the file empty if you don't have input ready yet.

How to Run

Open your terminal and navigate to the project folder.

Execute the following command:
python main.py input_data.json

(If your Python installation uses a different command or path, adjust accordingly.)

The review report will be generated and saved as report.md after the script completes.

Notes

The script uses the Groq API, with the API key already set in the code.
Make sure your JSON input matches the required format to prevent errors.
```
