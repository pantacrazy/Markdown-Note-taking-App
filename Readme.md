# Markdown Notes API
https://roadmap.sh/projects/markdown-note-taking-app
A RESTful API for managing Markdown notes with grammar checking and HTML rendering capabilities. Built with Flask and Python.

## Features

- 📝 Upload and manage Markdown files
- ✅ Grammar and spelling checking
- 🌐 Render Markdown to HTML
- 🔍 List all saved notes
- ✏️ Edit existing notes
- 🗑️ Delete notes
- 📁 File-based storage system

## API Endpoints

| Endpoint | Method | Description | Parameters |
|----------|--------|-------------|------------|
| `/` | GET | List all Markdown files | None |
| `/` | POST | Upload a new Markdown file | `file` (multipart/form-data) |
| `/markdowns/{filename}` | GET | Get raw content of a Markdown file | `filename` |
| `/markdowns/html/{filename}` | GET | Render Markdown as HTML | `filename` |
| `/markdowns/{filename}` | PUT | Update a Markdown file | `file` (multipart/form-data) |
| `/markdowns/{filename}` | DELETE | Delete a Markdown file | `filename` |

## Getting Started

### Prerequisites

- Python 3.9+
- Java 17+ (for grammar checking)
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/pantacrazy/Markdown-Note-taking-App
cd markdown-notes-api
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/MacOS
.venv\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Server

```bash
flask --app app run
```

The API will be available at `http://localhost:5000`

## API Usage Examples

### Upload a Markdown file
```bash
curl -X POST http://localhost:5000/ \
  -F "file=@path/to/your/file.md"
```

### Get list of all Markdown files
```bash
curl http://localhost:5000/
```

### Get raw content of a file
```bash
curl http://localhost:5000/markdowns/example.md
```

### Render Markdown as HTML
```bash
curl http://localhost:5000/markdowns/html/example.md
```

### Update a Markdown file
```bash
curl -X PUT http://localhost:5000/markdowns/example.md \
  -F "file=@path/to/updated/file.md"
```

### Delete a Markdown file
```bash
curl -X DELETE http://localhost:5000/markdowns/example.md
```

## Project Structure

```
markdown-notes-api/
├── app.py                 # Main application file
├── grammar.py             # Grammar checking module
├── markdowns_work.py      # Markdown file management
├── markdowns/             # Directory for storing Markdown files
├── requirements.txt       # Dependencies list
└── README.md              # Project documentation
```

## Grammar Checking

The API uses [language-tool-python](https://github.com/jxmorris12/language_tool_python) for grammar and spell checking. The implementation includes a custom filter to ignore potential false positives for words starting with uppercase letters (typically proper nouns).

### Grammar Check Features:
- Spelling correction
- Grammar suggestions
- Custom filtering for proper nouns
- Error position detection

## Dependencies

- Flask (web framework)
- language-tool-python (grammar checking)
- markdown (Markdown to HTML conversion)
- Werkzeug (file utilities)

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Create a new Pull Request


**Note**: This API is designed for educational purposes and local development. For production use, consider adding authentication, rate limiting, and a proper database solution.