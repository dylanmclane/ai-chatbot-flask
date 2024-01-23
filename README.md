# ai-chatbot-flask

Flask backend accessed at using TensorFlow and Hugging Face question-answering pipeline with pretrained model "bert-large-uncased-whole-word-masking-finetuned-squad"

Use Postman to send a POST request to http://127.0.0.1:5001/ask?Content-Type=application/json
with the JSON body format:
{
    "question": "your question",
    "context": "your context"
}
