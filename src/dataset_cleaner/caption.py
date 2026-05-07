import base64
from ollama import chat, ChatResponse
from dataset_cleaner.reporting import get_images
from pathlib import Path

def send_to_ollama(img_encoded, config):
    response: ChatResponse = chat(
        model= config.model, 
        messages = [{
            'role': 'user',
            'content': config.system_prompt,
            'images': [img_encoded]
        }],
        options = {'temperature': 0.6},
        )
    return response

def clean_caption(text: str) -> str:
    lines = text.strip().splitlines()
    lines = [line for line in lines if not (line.startswith("**") and line.endswith(":**"))]
    return "\n".join(lines).strip()

def caption_images(folder, config):
    images = get_images(folder)
    for img in images:
        print(f"Captioning {img.name}...")
        with open(img, 'rb') as f:
            encoded_image = base64.b64encode(f.read()).decode("utf-8")
        ollama_response = send_to_ollama(encoded_image, config)
        name_img_no_ext = img.stem + ".txt"
        with open (img.parent/name_img_no_ext, "w") as file:
            file.write (clean_caption(ollama_response.message.content))
            print(f"Saved {img.stem}.txt") 



    
    
    
    
