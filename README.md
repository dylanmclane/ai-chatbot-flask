# ai-chatbot-flask

Flask backend accessed at http://127.0.0.1:5001/ask?Content-Type=application/json
Using TensorFlow and Hugging Face question-answering pipeline with pretrained model "bert-large-uncased-whole-word-masking-finetuned-squad"

Use Postman to hit the backend with the JSON body format:
{
    "question": "your question",
    "context": "your context"
}
