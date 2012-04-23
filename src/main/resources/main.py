import os

from pygments import highlight
from pygments.lexers import get_lexer_by_name, get_all_lexers
from pygments.formatters import HtmlFormatter

import simplejson as json

from flask import Flask
from flask import request

LEXERS = json.dumps(map(lambda lexer: {'name':lexer[0], 'alias':lexer[1][0]}, get_all_lexers()))

PORT = os.environ.get('PORT', 5000)

HOST = '0.0.0.0'

app = Flask(__name__)

@app.route('/highlight', methods=['POST'])
def highlight():
    code = request.form['content']
    lexer = get_lexer_by_name(request.form['lang'])
    formatter = HtmlFormatter()
    return highlight(code, lexer, formatter)

@app.route('/lexers', methods=['GET'])
def lexers():
    return LEXERS

app.run(host=HOST, port=PORT)
