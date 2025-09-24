

# AI-Powered Customer Service Chatbot
### Build-an-End-to-End-System---Evaluation
![Chatbot Screenshot](assets/screenshot.png)

An intelligent customer service assistant for an electronics store, built with OpenAI's GPT models and featuring a multi-step processing pipeline with content moderation and response evaluation.

## 🚀 Features

- **Multi-step Processing Pipeline**: Implements a robust 7-step process for handling user queries
- **Content Moderation**: Built-in safety checks for both input and output
- **Product Recognition**: Automatically identifies products mentioned in customer queries
- **Response Evaluation**: AI-powered quality assessment of generated responses
- **Multiple Interfaces**: 
  - Jupyter notebook with interactive widgets
  - Streamlit web application
- **Conversation Memory**: Maintains context across multiple interactions

## 🏗️ System Architecture

The chatbot follows a sophisticated processing pipeline:

1. **Input Moderation**: Checks user input for inappropriate content
2. **Product Extraction**: Identifies relevant products from user queries
3. **Information Lookup**: Retrieves product information
4. **Response Generation**: Creates helpful, contextual responses
5. **Output Moderation**: Validates assistant responses
6. **Quality Evaluation**: AI assessment of response quality
7. **Final Decision**: Serves response or escalates to human agent

## 🛠️ Tech Stack

- **Python 3.10+**
- **OpenAI GPT-4/GPT-3.5-turbo**: Core language model
- **Streamlit**: Web interface
- **Jupyter Notebooks**: Development and testing
- **ipywidgets**: Interactive notebook interface
- **python-dotenv**: Environment variable management

## 📋 Prerequisites

- Python 3.10 or higher
- OpenAI API key
- Virtual environment (recommended)

## ⚙️ Installation

1. **Clone the repository**
```bash
git clone <your-repository-url>
cd your-chatbot-project
```

2. **Create and activate virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key:
# OPENAI_API_KEY=your_api_key_here
```

## 🚀 Usage

### Streamlit Web App
```bash
streamlit run chatbot.py
```
Then open your browser to `http://localhost:8501`

### Jupyter Notebook
```bash
jupyter notebook "main code.ipynb"
```

### Command Line Testing
```python
from main_code import process_user_message

user_input = "Tell me about your phones and cameras"
response, context = process_user_message(user_input, [])
print(response)
```

## 📁 Project Structure

```
your-chatbot-project/
├── src/
│   ├── main_code.ipynb          # Main development notebook
│   └── chatbot.py               # Streamlit application
├── notebooks/
│   └── evaluation/              # Analysis and testing notebooks
├── requirements.txt             # Python dependencies
├── .env.example                 # Environment variables template
├── .gitignore                   # Git ignore rules
└── README.md                    # This file
```

## 🔧 Configuration

### Supported Products
The chatbot currently recognizes these product categories:
- Smartphones (SmartX Pro Phone)
- Cameras (FotoSnap DSLR, FotoSnap Compact)
- TVs (TCL, Samsung models)

### Model Settings
- **Default Model**: GPT-4
- **Temperature**: 0.7 (adjustable)
- **Max Tokens**: 500 (adjustable)

## 📊 Key Functions

### `process_user_message(user_input, all_messages, debug=True)`
Main processing function that handles the complete pipeline.

**Parameters:**
- `user_input`: User's message string
- `all_messages`: Conversation history
- `debug`: Enable/disable debug output

**Returns:**
- `response`: Generated response string
- `updated_messages`: Updated conversation context

### `get_completion_from_messages(messages, model, temperature, max_tokens)`
Interfaces with OpenAI API for generating responses.

### `find_category_and_product_only(user_input, product_list)`
Extracts mentioned products from user input.

## 🧪 Testing

Run the notebook cells sequentially to test different components:

1. **Basic API Connection**: Test OpenAI connectivity
2. **Product Recognition**: Test product extraction logic
3. **Full Pipeline**: Test complete message processing
4. **Interactive Chat**: Use widget interface for live testing

## 🔒 Security & Moderation

- Input validation and sanitization
- OpenAI Moderation API integration
- Response quality evaluation
- Automatic escalation to human agents when needed

## 🚀 Deployment

### Local Development
```bash
streamlit run chatbot.py
```

### Production Deployment
Consider these platforms:
- **Streamlit Cloud**: Easy deployment for Streamlit apps
- **Heroku**: General-purpose hosting
- **AWS/GCP/Azure**: Enterprise deployment

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🐛 Troubleshooting

### Common Issues

**API Key Errors**
```bash
# Ensure your .env file contains:
OPENAI_API_KEY=your_actual_api_key
```

**Streamlit Warnings**
```bash
# Run Streamlit properly:
streamlit run chatbot.py
# Not: python chatbot.py
```

**Missing Dependencies**
```bash
pip install -r requirements.txt
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- OpenAI for providing the GPT models
- Streamlit team for the excellent framework
- Contributors and testers

## 📞 Support

For questions, issues, or contributions:
- Open an issue on GitHub
- Contact: [your-email@example.com]
- Documentation: [Link to detailed docs]

---

Built with ❤️ and AI
