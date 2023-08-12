
from gtts import gTTS
from io import BytesIO
import pygame
import tempfile
from pydub import AudioSegment
import streamlit as st
from langchain.vectorstores import FAISS
from langchain import PromptTemplate
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain import PromptTemplate
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import CTransformers
from langchain.chains import RetrievalQA
from output import text_to_asl_video
from textwrap import shorten

DB_FAISS_PATH = 'vectorstore/db_faiss'

custom_prompt_template = """Use the following pieces of information to answer the user's question and quote the right article whenver you can.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context: {context}
Question: {question}

Only return the helpful answer below and nothing else.
Helpful answer:
"""

# Loading the model
def load_llm():
    # Load the locally downloaded model here
    llm = CTransformers(
        model="llama-2-7b-chat.ggmlv3.q4_0.bin",
        model_type="llama",
        max_new_tokens=512,
        temperature=0.5
    )
    return llm
def set_custom_prompt():
    prompt = PromptTemplate(template=custom_prompt_template, input_variables=['context', 'question'])
    return prompt

#Retrieval QA Chain
def retrieval_qa_chain(llm, prompt, db):
    qa_chain = RetrievalQA.from_chain_type(llm=llm,
                                       chain_type='stuff',
                                       retriever=db.as_retriever(search_kwargs={'k': 2}),
                                       return_source_documents=True,
                                       chain_type_kwargs={'prompt': prompt}
                                       )
    return qa_chain
# QA Model Function
def qa_bot():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2",
                                       model_kwargs={'device': 'cpu'})
    db = FAISS.load_local(DB_FAISS_PATH, embeddings)
    llm = load_llm()
    qa_prompt = set_custom_prompt()
    qa = retrieval_qa_chain(llm, qa_prompt, db)
    return qa

def generate_hand_sign_videos(query_text):
    # Convert the text to a list of video URLs
    video_urls = text_to_asl_video(query_text)

    # Generate HTML for the video playlist
    video_playlist = '<div id="video-container"></div><script>'
    video_playlist += '''
    var videos = %s;
    var videoContainer = document.getElementById('video-container');
    var currentIndex = 0;

    function playNextVideo() {
      if (currentIndex < videos.length) {
        videoContainer.innerHTML = '<video width="330" height="200" controls autoplay onended="playNextVideo()"><source src="' + videos[currentIndex] + '" type="video/mp4"></video>';
        currentIndex++;
      }
    }

    playNextVideo();
    ''' % video_urls
    video_playlist += '</script>'

    return video_playlist


# Output function
def final_result(query):
    qa_result = qa_bot()
    response = qa_result({'query': query})
    return response


def generate_hand_sign_videos(query_text):
    # Convert the text to a list of video URLs
    video_urls = text_to_asl_video(query_text)

    # Generate HTML for the video playlist
    video_playlist = '<div id="video-container"></div><script>'
    video_playlist += '''
    var videos = %s;
    var videoContainer = document.getElementById('video-container');
    var currentIndex = 0;

    function playNextVideo() {
      if (currentIndex < videos.length) {
        videoContainer.innerHTML = '<video width="330" height="200" controls autoplay onended="playNextVideo()"><source src="' + videos[currentIndex] + '" type="video/mp4"></video>';
        currentIndex++;
      }
    }

    playNextVideo();
    ''' % video_urls
    video_playlist += '</script>'

    return video_playlist

def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    mp3 = BytesIO()
    tts.save(mp3)
    mp3.seek(0)
    return mp3


def play_audio(audio_file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


def main():
    st.title("Ai For ALL")
    st.write("A lawyer for all with AI on call...")
    user_input = st.text_input("You (Text):", "Enter your queries here...", key="text_input")
    output_format = st.selectbox("Select Output Format:", ["Text", "Speech", "Video"])
    
    response = final_result(user_input)['result']  # Get the model's response and extract the 'result' key

    # Display the full text response
    st.write(f"Bot (Text): {response}")

    # If video is selected, summarize the response and generate/display the hand-sign video
    if output_format == "Video":
        response_text = shorten(response, width=30, placeholder="...")  # Summarize to 30 words
        video_html = generate_hand_sign_videos(response_text)  # Use summarized response
        st.components.v1.html(video_html, height=200)  # Adjust the height as needed

    if output_format == "Speech":
        temp_audio_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mp3')
        tts = gTTS(text=response, lang='en')
        tts.save(temp_audio_file.name)
        play_audio(temp_audio_file.name)


        
if __name__ == "__main__":
    main()


