import openai 
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form['user_input']

    with open('output.txt', 'w') as f:
        f.write(user_input) 

    return 'Successfully wrote to file'


@app.route('/search', methods=['POST'])
def search(prompt):
    openai.api_key = "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"
    response = openai.Completion.create(engine="text-davinci-002", prompt=prompt)
    return response["choices"][0]["text"]
     

def create_js_file(prompt):
    response = search(prompt)
    with open('response.js', 'w') as f:
        f.write(f"var response = '{response}';")
        
                     


if __name__ == '__main__':
    app.run()

#import os

#import openai
#from flask import Flask, redirect, render_template, request, url_for

#app = Flask(__name__)
#openai.api_key = os.getenv("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")



#@app.route("/", methods=("GET", "POST"))
#def index():
#    if request.method == "POST":
#        animal = request.form["animal"]
#        response = openai.Completion.create(
#            model="text-davinci-003",
#            prompt=generate_prompt(animal),
#            temperature=0.6,
#        )
#        return redirect(url_for("index", result=response.choices[0].text))

#    result = request.args.get("result")
#    return render_template("index.html", result=result)



#    '''
#        <form method="POST" action="/search">
#            <input type="text" name="query">
#            <input type="submit" value="Search">
#        </form>
#    '''


#"""Create a cover letter for a Customer Service Specialist.

#Job: Customer Service
#Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
#Animal: Dog
#Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
#Animal: {}
#Names:""".format(
#        animal.capitalize()
#    )