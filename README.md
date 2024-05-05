# AiForALL: A Lawyer for all with AI on call..


**Developed by:** Satyam Gupta, Sneha S, Shebin Kurin Thomas, and Nidin A.

Video Link: https://drive.google.com/drive/folders/1mh6V2M1CDUCcLAE090XfJcG68vKjVdlc?usp=sharing

## Introduction

Many people in India, including the hearing, speech-impaired and those living in rural areas, face problems such as low pay and exploitative working conditions. These individuals may not be aware of their rights and may have difficulty interacting with lawyers or seeking legal assistance.
Our project, AiForALL, is a state-of-the-art chatbot that assists with labour law inquiries. Our aim is to address these issues on labor law by providing an accessible and user-friendly platform for these individuals to learn about their rights and take action against those who abuse them. The chatbot takes text as input and can provide outputs in multiple formats: text, voice, and sign language video.

## Our Mantra

We believe in a more just world where everyone can stand up to what is not right. And we believe this, at some level, can be achieved through having more knowledge of the law. It is not possible for everyone to understand the complex language of the law or to remember all the rights. However, Large Language Models can... At the same time, we wish to bring this understanding of the law to hearing or speech-impaired people... #You don't necessarily need to speak to speeak out...
## Features

- **Text-to-Text**: Simple text-based Q&A for all your labor law queries.
- **Text-to-Voice**: Get your answers in an audible format.
- **Text-to-Sign Language**: A unique feature that converts responses into sign language videos, aiding the deaf community in understanding labor law.

# Install required dependencies, open terminal

**pip install -r requirements.txt**
# Requirements : 
1. **IDC**: Intel Developer Cloud
2. **`gtts`**: Google Text-to-Speech conversion library.
3. **`io`**: Python's standard library for handling streams.
4. **`pygame`**: Library for creating games and multimedia applications.
5. **`tempfile`**: Python's standard library for generating temporary files and directories.
6. **`pydub`**: Library for audio processing.
7. **`streamlit`**: Python library for creating web applications.
8. **`langchain`**: Seems to be a custom or specialized library, given the multiple modules imported from it (like `vectorstores`, `embeddings`, `llms`, and `chains`).
9. **'output'**: Not sure about this; it might be a local module or another custom library.
10. **'textwrap'**: Python's standard library for wrapping and filling text.
11. **`torch`**: A scientific computing framework that offers wide support for deep learning algorithms using tensors and dynamic neural networks in Python.
12. **`accelerate`**: A library from Hugging Face for easy and fast acceleration of PyTorch models using mixed precision and distributed training.
13. **`bitsandbytes`**: An optimized library for training deep learning models using 8-bit optimizers, which can significantly accelerate training without compromising accuracy.
14. **`transformers`**: A library by Hugging Face that provides pre-trained models for Natural Language Processing (NLP) tasks like text classification, translation, and more. It includes models like BERT, GPT-2, T5, and others.
15. **`sentence_transformers`**: A library for computing dense vector representations of sentences and paragraphs, often based on models from the `transformers` library. Useful for semantic search applications and other NLP tasks where sentence embeddings are required.
16. **`faiss_cpu`**: A library developed by Facebook AI for efficient similarity search and clustering of dense vectors. The `faiss_cpu` version is optimized for CPU usage.
17. **`chainlit`**: As of my last training data in September 2021, I'm not familiar with a library named "chainlit". It might be a new, niche, or specialized library. You might want to refer to the library's official documentation or repository for a brief description.
18. **`IPython.display`** : A module within IPython for displaying rich media outputs in Jupyter notebooks, such as images, audio, and video.
19. **`requests`** : A popular Python library for making HTTP requests to web services, simplifying the process of sending and receiving data.
20. **`json`** : A module in Python's standard library for encoding and decoding JSON formatted data.

## Model Architecture

![image](https://github.com/Satyam7166-tech/AiForAll/assets/62897696/27154d35-08d0-448b-b2e1-108b95118344)


## Usage

The input for this project is taken in two ways, one, Text and the other is Real Time Hand Sign videos through the users Web Camera. The video from the Web Cam will be then will convert these signs into text and this text is stored in text file and fed to the chatbot as input. The entire project is Developed on **Intel Developer** code using **Tensorflow_CPU** notebook

Now execute our main program.
**python model-run.py**
Do note that you must have the llama-2-7b-chat.ggmlv3.q4_0.bin model in the same directory and 'pip install' all those required libraries within requirements.txt


The working flow of the main program is as follows : 
Working Flow:

1. **Initialization:** The application is built in streamlit, an open source framework. Our application interface, displays the title saying "Ai For ALL" and a subtitle "A lawyer for all with AI on call...".
   
2. **User Input:** The interface has the user input prompt where the users can enter their queries and select an output format: Text or Video. Below is an image displaying the user input prompts with those two options.

   ![image](https://github.com/Satyam7166-tech/AiForAll/assets/62897696/b0352059-7764-42ab-858d-7d89e3d3c487)

   
3. **Processing:** When a user submits a query:
    - The query from the user is directed to the FAISS vector database where the input text from the user is converted into vectors. The vector representation for text is designed to produce similar vectors for all the texts , where similar vectors are defined as those that are nearby in Euclidean space. Then based on similarites it retrieves relevant information within FAISS vector database.
    - The generative model generates an answer using the context from the document and the user's question.
    
4. **Response Generation:**
    - For "Text" format: The bot's response is directly displayed.
    - For "Video" format: The response is summarized and converted to a series of hand sign videos, which are then displayed.
    - For "Speech" format: The response is converted to speech using `gTTS`, and the audio is played using `pygame`.

In essence, this Streamlit application acts as a law-related chatbot that can provide answers in text, audio, or ASL video formats. The use of hand sign videos is a unique feature, making the chatbot more accessible to users with hearing impairments.

After this, we run the Output File :
**python Output.py**

Working Flow:   

1. **User Interface Initialization:**
    - Using Streamlit, the application displays a title and allows users to enter their queries. They can also choose the desired output format: Text or Handsign Video.

   ![image](https://github.com/Satyam7166-tech/AiForAll/assets/62897696/dff632a1-cbc3-4039-9fa6-0d54eb16ce9c)


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
     
## Future Works
 - Our project AiForAll aimed at providing law support to all the people. But as we have trained this model just with labor law, our future enhancement will be focused on training this model with the whole of Indian constitutional law, where any law related queries can be answered. 
 - We would also like to enhance the input feature where the users can input their queries in different languages to give a multilingual aspect to the model, or in the form of handsign video, a relevant audio regarding their problems.
- Considering the handsign output format, an animation of hand gestures would be a feasible model to obtain an interactive and easier way of communication for the hearing impaired people.
- We plan to expand our domain from labour laws and aim to fine-tune our LLM on every constitution of the world so that anyone, irrespective of their nationality, can be more aware of legal laws.

- 
  
## Acknowledgement 

We want to thank the Intel oneAPI community for their invaluable toolkits and the Developer Cloud platform. These resources have greatly enhanced our capabilities and streamlined our development processes. Their dedication to fostering innovation is evident in the robustness and versatility of the Intel one API suite. Furthermore, the opportunity to explore and integrate Intel one API into our projects has been an enriching experience, significantly influencing our advancements in the field. I deeply appreciate the unwavering support and guidance from the community, and I look forward to our continued collaboration.

