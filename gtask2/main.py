from elevenlabs import (
    generate, 
    play, 
    set_api_key)
import azure.cognitiveservices.speech as speechsdk
import os
from langchain.vectorstores import Chroma
from langchain.embeddings import CohereEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import Cohere
from langchain.chains import VectorDBQA
from langchain.document_loaders import PyMuPDFLoader
import argparse
from dotenv import load_dotenv
import keyboard


def get_response(query, file_path, cohere_api_key):
    try:
        print('Original query:', query)

        loader = PyMuPDFLoader(file_path)
        documents = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        texts = text_splitter.split_documents(documents)

        embeddings = CohereEmbeddings(cohere_api_key=cohere_api_key)
        vectordb = Chroma.from_documents(texts, embeddings)

        qa = VectorDBQA.from_chain_type(llm=Cohere(cohere_api_key=cohere_api_key), chain_type="stuff", vectorstore=vectordb)

        prompt = qa.run(query)

        if prompt == "":
            return ""
        
        print('Agent response:', prompt)
        
        return prompt.strip()

    except Exception as e:
        print(e)
        return ""


def voiceover(prompt: str) -> None:
    audio = generate(
        text=prompt,
        voice="Bella",
        model="eleven_monolingual_v1"
    )

    play(audio)


def speech_to_text():

    speech_config = speechsdk.SpeechConfig(subscription=os.getenv("AZURE_API_KEY"), region=os.getenv("AZURE_REGION"))
    speech_config.speech_recognition_language="en-US"

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("Speak into your microphone.")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(speech_recognition_result.text))
        return speech_recognition_result.text
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
        return ""
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")
        return ""


def main():
    load_dotenv()
    set_api_key(os.getenv("ELEVENLABS_API_KEY"))

    parser = argparse.ArgumentParser(description="AI Powered Voice Assistant")
    parser.add_argument('-f', '--file', required=True, help="Path to the PDF file")
    args = parser.parse_args()
    file_path = args.file

    while True:
        query = speech_to_text()

        if query != "":
            try:
                response = get_response(query=query, file_path=file_path, cohere_api_key=os.getenv("COHERE_API_KEY"))

                if response != "":
                    try:
                        voiceover(prompt=response)
                    except Exception as e:
                        print(e)
            except Exception as e:
                print(e)


if __name__ == '__main__':
    main()
