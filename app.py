from flask import Flask, render_template, request
import openai
import docx
from docx import Document

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/create-cover-letter', methods=['POST'])
def create_cover_letter():
    # Get the position from the user input
    position = request.form.get('position')
    
    # Get the OpenAI API credentials
    
    openai.api_key = "YOUR KEY HERE"
    
    # Generate the cover letter using the OpenAI API
    prompt = f"Create a cover letter for {position} position"
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    letter = completions.choices[0].text
    
    # Create a new word document
    doc = docx.Document()
    
    # Add the cover letter text to the document
    doc.add_paragraph(letter)
    
    # Save the document
    doc.save('cover_letter.docx')
    
    return 'Cover letter created and saved as cover_letter.docx'


if __name__ == '__main__':
    app.run(debug=True)
    

