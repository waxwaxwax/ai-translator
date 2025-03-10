# AI Translator Application

A web-based translation application powered by Azure OpenAI's GPT-4o model. This application allows users to translate text between various languages through a simple web interface.

## Features

- Text translation using advanced AI language model
- Support for multiple target languages
- Simple and intuitive user interface
- Real-time translation results

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **AI Service**: Azure OpenAI GPT-4o

## Prerequisites

- Python 3.6 or higher
- Azure OpenAI API access
- Azure OpenAI Endpoint and API Key

## Setup Instructions

1. **Clone the repository**

   ```bash
   git clone <your-repository-url>
   cd translation-app
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**

   Create a `.env` file in the root directory with the following variables:

   ```
   AZURE_OPENAI_ENDPOINT=your_azure_openai_endpoint
   AZURE_OPENAI_KEY=your_azure_openai_api_key
   ```

4. **Run the application**

   ```bash
   python app.py
   ```

5. **Access the application**

   Open your web browser and navigate to `http://localhost:5000`

## Usage

1. Enter the text you want to translate in the input field
2. Select the target language from the dropdown menu
3. Click the "Translate" button
4. View the translated text in the results area

## Deployment

This application includes a `startup.sh` script for Azure App Service deployment.

## License

[Your chosen license]

## Acknowledgements

- Azure OpenAI for providing the GPT-4o model API
- Flask for the web framework
