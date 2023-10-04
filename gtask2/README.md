# AI Powered Voice Assistant

## Prerequisites

### Azure Speech Service

- Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services).
- [Create a Speech resource](https://portal.azure.com/#create/Microsoft.CognitiveServicesSpeechServices) in the Azure portal.
- Your Speech resource key and region. After your Speech resource is deployed, select Go to resource to view and manage keys. For more information about Azure AI services resources, see [Get the keys for your resource](https://learn.microsoft.com/en-us/azure/ai-services/multi-service-resource?pivots=azportal#get-the-keys-for-your-resource).

### Eleven Labs

- [Create an Eleven Labs account](https://elevenlabs.io/).
- Click on the Profile image and select `Profile`. Then copy your API key.

### Cohere

- [Create a Cohere account](https://cohere.ai/).
- Copy your API key from the dashboard. Feel free to use `trial API key`.

## Usage

Clone this repository

```shell
git clone https://github.com/abdibrokhim/CodeClause-Internship-Solutions/
```

Open a terminal and navigate to the directory where you cloned the repository.

Install the required packages using the following command:

```shell
pip install azure-cognitiveservices-speech elevenlabs langchain keyboard python-dotenv pymupdf cohere chromadb
```
Copy `.env.example` to `.env` and fill in the required values:

```shell
cp .env.example .env
```

```shell

AZURE_API_KEY=your_azure_api_key
AZURE_REGION=your_azure_region
ELEVENLABS_API_KEY=your_elevenlabs_api_key
COHERE_API_KEY=your_cohere_api_key
```

Run the script using the following command:

```shell
python main.py -f PATH_TO_PDF_FILE
```

Replace `PATH_TO_PDF_FILE` with the path to the PDF file you want to be processed. Then you will be asked to speak to the microphone. You can ask any interesting questions based on the content of the PDF file. The script will then process your speech and return the answer to your question.
