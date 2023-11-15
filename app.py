from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='templates')
import stanza

try:
    # Initialize CoreNLP
    nlp = stanza.Pipeline()  # This will use the default CoreNLP settings (localhost:9000)
except Exception as e:
    print(f"Error initializing Stanza: {str(e)}")

@app.route('/')
def index():
    return render_template('assesment.html')

@app.route('/process_text', methods=['POST'])
def process_text():
    try:
        user_text = request.json.get('userText')
        processed_text = process_with_corenlp(user_text)
        return jsonify({'processed_data': processed_text})
    except Exception as e:
        print(f"Error processing text: {str(e)}")
        return jsonify({'error': 'An error occurred during text processing'}), 500

def process_with_corenlp(text):
    try:
        doc = nlp(text)
        processed_text = ""
        for sentence in doc.sentences:
            processed_text += f"Sentence: {sentence.text}\n"

        return processed_text
    except Exception as e:
        print(f"Error in CoreNLP processing: {str(e)}")
        return 'Error in CoreNLP processing'


if __name__ == '__main__':
    app.run(debug=True)
