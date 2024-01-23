from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
model_name = "bert-large-uncased-whole-word-masking-finetuned-squad"  # Choosing the model
qa_pipeline = pipeline("question-answering", model=model_name)

@app.route("/ask", methods=["POST"])
def ask():
    # Extract question and context from the request
    data = request.get_json()
    question = data.get("question")
    context = data.get("context")

    # Check if both question and context are provided
    if not question or not context:
        return jsonify({"error": "Please provide both question and context"})

    try:
        # Use the model to find the answer
        answer = qa_pipeline({'question': question, 'context': context})
        return jsonify(answer)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True, port=5000)