import requests 
import gradio as gr 

# Deepseek API URL
OLLAMA_URL = 'http://localhost:11434/api/generate'

def analyze_sentiment(text):
    """
    Uses DeepSeek AI to classify sentiment as positive, negetive,or neutral.
    """
    prompt = f"Classify the sentiment of the following text as Positive,Negetive,or Nuetral:\n\n{text}"
    payload = {
        'model':'deepseek-r1',
        'prompt': prompt,
        'stream':False
    }
    response = requests.post(OLLAMA_URL,json=payload)

    if response.status_code == 200:
        return response.json().get('response','No sentiment detected.')
    else:
        return f"Error {response.text}"
    
# Create Gradio Interface
interface = gr.Interface(
    fn = analyze_sentiment,
    inputs = gr.Textbox(lines=3,placeholder="Enter a sentence for sentiment analysis."),
    outputs = gr.Textbox(label="Sentiment Result"),
    title = 'AI-Powered Sentiment Analysis',
    description = 'Enter a sentence, and DeepSeek AI will classify its sentiment as Positive,Negetive, or Nuetral.'
)

# Launch the web app 
if __name__ == '__main__':
    interface.launch()

# # Test Sentiment Analysis  
# if __name__ == '__main__':
#     # sample_text = "The movie was absolutely fantastic! I enjoyed every minute of it."
#     sample_text = "The service was terrible. I waited an hour,and my order was wrong."
#     print("Sentiment Analysis Result")
#     print(analyze_sentiment(sample_text))