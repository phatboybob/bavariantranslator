'''
Streamlit app that translates text between English and Bavarian
'''

import os

import streamlit as st
from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate


def translate(input_language: str,
              input_text: str,
              output_language: str,
              model,
              ):
    """_summary_

    Args:
        language (str): _description_
        text (str): _description_
    """

    system_template = "Translate the following from {input_language} into {output_language}: {input_text}"

    prompt_template = PromptTemplate(template=system_template,
                                     input_variables=["input_language",
                                                      "input_text",
                                                      "output_language",
                                                      ],
    )
    prompt = prompt_template.invoke({'input_language': input_language,
                                     'input_text': input_text,
                                     'output_language': output_language})
    response = model.invoke(prompt)
    return response.content




st.set_page_config(page_title='Servus',
                   page_icon='🍺',
                   layout='centered',
                   )

st.title('Servus! 🍺')
api_key = st.text_area(label='Enter API Key')
if api_key:
    os.environ['GROQ_API_KEY'] = api_key
    model = init_chat_model("llama3-8b-8192", model_provider="groq")

language_container = st.container()
language = language_container.selectbox(label='Select Original Language',
                                        options=['English', 'Bavarian'],
                                        )


if language == 'English':
    text = st.text_area(label='Enter English Text')
    if st.button('Translate to Bavarian'):
        translated_text = translate(input_language = 'English',
                                    input_text = text,
                                    output_language = 'Bavarian',
                                    model = model,
                                    )
        st.write(translated_text)

if language == 'Bavarian':
    text = st.text_area(label='Enter English Text')
    if st.button('Translate to English'):
        translated_text = translate(input_language = 'Bavarian',
                                    input_text = text,
                                    output_language = 'English',
                                    model = model,
                                    )
        st.write(translated_text)