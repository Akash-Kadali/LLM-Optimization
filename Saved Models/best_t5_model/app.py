import gradio as gr
from transformers import T5Tokenizer, T5ForConditionalGeneration
from peft import PeftModel
import torch
from googletrans import Translator

# Load tokenizer and base model
tokenizer = T5Tokenizer.from_pretrained("./")
base_model = T5ForConditionalGeneration.from_pretrained("t5-small")
model = PeftModel.from_pretrained(base_model, "./")

# Use GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

translator = Translator()

def summarize(text, language='en'):
    if language != 'en':
        text = translator.translate(text, dest='en').text

    input_ids = tokenizer("summarize: " + text, return_tensors="pt", truncation=True, max_length=512).input_ids.to(device)
    output_ids = model.generate(
        input_ids,
        max_length=80,
        min_length=15,
        length_penalty=1.5,
        num_beams=8,
        no_repeat_ngram_size=3,
        early_stopping=True
    )
    summary = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    if language != 'en':
        summary = translator.translate(summary, dest=language).text

    return summary

gr.Interface(
    fn=summarize,
    inputs=[
        gr.Textbox(lines=10, label="Enter Article"),
        gr.Dropdown(choices=["en", "hi", "te", "fr", "es", "de"], value="en", label="Output Language")
    ],
    outputs="textbox",
    title="T5 Summarizer (LoRA Optimized)",
    description="Summarize long text using your fine-tuned T5-small model with LoRA adapters. Supports translation."
).launch()
