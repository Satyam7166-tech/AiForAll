# AiForALL: A Chatbot on Labor Law


**Developed by:** Nidin A, Sneha S, Shebin Kurin Thomas, and Satyam Gupta.

## Introduction

Many people in India, including the hearing, speech-impaired and those living in rural areas, face problems such as low pay and exploitative working conditions. These individuals may not be aware of their rights and may have difficulty interacting with lawyers or seeking legal assistance.
Our project, AiForALL, is a state-of-the-art chatbot that assists with labor law inquiries. Our aim is to address these issues on labor law by providing an accessible and user-friendly platform for these individuals to learn about their rights and take action against those who abuse them. The chatbot takes text as input and can provide outputs in multiple formats: text, voice, and sign language video.


## Features

- **Text-to-Text**: Simple text-based Q&A for all your labor law queries.
- **Text-to-Voice**: Get your answers in an audible format.
- **Text-to-Sign Language**: A unique feature that converts responses into sign language videos, aiding the deaf community in understanding labor law.

# Install required dependencies, open terminal

**pip install -r requirements.txt**

# Requirements : 
1. **`gtts`**: Google Text-to-Speech conversion library.
2. **`io`**: Python's standard library for handling streams.
3. **`pygame`**: Library for creating games and multimedia applications.
4. **`tempfile`**: Python's standard library for generating temporary files and directories.
5. **`pydub`**: Library for audio processing.
6. **`streamlit`**: Python library for creating web applications.
7. **`langchain`**: Seems to be a custom or specialized library, given the multiple modules imported from it (like `vectorstores`, `embeddings`, `llms`, and `chains`).
8. **'output'**: Not sure about this; it might be a local module or another custom library.
9. **'textwrap'**: Python's standard library for wrapping and filling text.
10. **`torch`**: A scientific computing framework that offers wide support for deep learning algorithms using tensors and dynamic neural networks in Python.
11. **`accelerate`**: A library from Hugging Face for easy and fast acceleration of PyTorch models using mixed precision and distributed training.
12. **`bitsandbytes`**: An optimized library for training deep learning models using 8-bit optimizers, which can significantly accelerate training without compromising accuracy.
13. **`transformers`**: A library by Hugging Face that provides pre-trained models for Natural Language Processing (NLP) tasks like text classification, translation, and more. It includes models like BERT, GPT-2, T5, and others.
14. **`sentence_transformers`**: A library for computing dense vector representations of sentences and paragraphs, often based on models from the `transformers` library. Useful for semantic search applications and other NLP tasks where sentence embeddings are required.
15. **`faiss_cpu`**: A library developed by Facebook AI for efficient similarity search and clustering of dense vectors. The `faiss_cpu` version is optimized for CPU usage.
16. **`chainlit`**: As of my last training data in September 2021, I'm not familiar with a library named "chainlit". It might be a new, niche, or specialized library. You might want to refer to the library's official documentation or repository for a brief description.
17. **`IPython.display`** : A module within IPython for displaying rich media outputs in Jupyter notebooks, such as images, audio, and video.
18. **`requests`** : A popular Python library for making HTTP requests to web services, simplifying the process of sending and receiving data.
20. **`json`** : A module in Python's standard library for encoding and decoding JSON formatted data.

## Usage

The input for this project is taken in two ways, one, Text and the other Real Time Hand Sign videos through the Web Camera. The video from the Web Cam will be then will convert these signs into text and this text is stored in text file and fed to the chatbot as input. 

Now execute our main program.
**python model-run.py**
Do note that you must have the llama-2-7b-chat.ggmlv3.q4_0.bin model in the same directory.

The working flow of the main program is as follows : 
Working Flow:

1. **Initialization:** The application starts, displaying a title "Ai For ALL" and a subtitle "A lawyer for all with AI on call...".
   
3. **User Input:** Users can enter their queries and select an output format: Text, Speech, or Video.
   
5. **Processing:** When a user submits a query:
    - The FAISS vector store retrieves relevant document sections.
    - The generative model generates an answer using the context from the document and the user's question.
    
6. **Response Generation:**
    - For "Text" format: The bot's response is directly displayed.
    - For "Video" format: The response is summarized and converted to a series of hand sign videos, which are then displayed.
    - For "Speech" format: The response is converted to speech using `gTTS`, and the audio is played using `pygame`.

In essence, this Streamlit application acts as a law-related chatbot that can provide answers in text, audio, or ASL video formats. The use of hand sign videos is a unique feature, making the chatbot more accessible to users with hearing impairments.

After this, we run the Output File :
**python Output.py**

Working Flow:

1. **User Interface Initialization:**
    - Using Streamlit, the application displays a title and allows users to enter their queries. They can also choose the desired output format: Text, Speech, or Video.

2. **Query Processing:**
    - FAISS Vector Store: When a query is submitted, the application uses the FAISS vector store to search for relevant sections from stored documents. FAISS allows for efficient similarity search in a collection of vectors, making it suitable for retrieving relevant document sections quickly.
    - Generative Model (Llama): The retrieved document section (context) and user's query are passed to a generative model named "Llama". This model, guided by the custom prompt template, generates a relevant answer based on the provided context and question.

3. **Response Generation:**
    - Text: If the user selected the Text output format, the bot's response is directly displayed on the interface.
    - Video (ASL):
        - The bot's response is summarized to a shorter version.
        - This summarized text is then converted into American Sign Language (ASL) videos using the `text_to_asl_video` function. This feature makes the application accessible to users with hearing impairments.
    - Speech:
        - The bot's response is converted to speech using `gTTS` (Google Text-to-Speech), which generates spoken language from written text.
        - The generated audio is played to the user using the `pygame` library, providing an auditory response.


# Install required dependencies, open terminal

**pip install -r requirements.txt**


# Now execute our main program.

**python model-run.py**

Do note that you must have the llama-2-7b-chat.ggmlv3.q4_0.bin [model](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/blob/main/llama-2-7b-chat.ggmlv3.q4_0.bin) in the same directory. 

We welcome contributions from the community. Please fork the repository and submit a pull request with your changes.


## Acknowledgement 

We want to thank the Intel oneAPI community for their invaluable toolkits and the Developer Cloud platform. These resources have greatly enhanced our capabilities and streamlined our development processes. Their dedication to fostering innovation is evident in the robustness and versatility of the Intel one API suite. Furthermore, the opportunity to explore and integrate Intel one API into our projects has been an enriching experience, significantly influencing our advancements in the field. I deeply appreciate the unwavering support and guidance from the community, and I look forward to our continued collaboration.

