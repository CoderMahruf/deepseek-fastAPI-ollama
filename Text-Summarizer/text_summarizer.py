import requests 
import gradio as gr 

# Deepseek API Endponint
OLLAMA_URL = 'http://localhost:11434/api/generate'

def summarize_text(text):
    '''
    Using DeePseek AI to summarize a given text 
    '''
    payload = {
        'model':'deepseek-r1',
        'prompt':f'Summeraize the following text in **3 bullet points**: \n\n{text}',
        'stream':False,
    }
    response = requests.post(OLLAMA_URL,json=payload)
    if response.status_code == 200:
        return response.json().get("response","No summary generated.")
    else:
        return f"Error {response.text}"

# Create Gradio interface
interface = gr.Interface(
    fn=summarize_text,inputs=gr.Textbox(lines=10,
    placeholder = 'Enter text to summarize'),
    outputs=gr.Textbox(label='Summarized Text'),
    title = 'AI-Powered Text Summarizer',
    description='Enter a long text DeepSeek AI will generate a concise summary.'
)

# Launch the web app 
if __name__ == '__main__':
    interface.launch()
