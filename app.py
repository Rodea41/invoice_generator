
#! from weasyprint import HTML
from flask import Flask, render_template
import os

#! This creates the invoice pdf off the invoice.html template we used
#html = HTML('invoice.html')
#html.write_pdf('invoice.pdf')

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('invoice.html')  #! Points to the .html file in 'templates' folder

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)




