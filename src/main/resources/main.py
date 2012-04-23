import os

import pygments
from pygments.lexers import get_lexer_by_name, get_all_lexers
from pygments.formatters import HtmlFormatter

import simplejson as json

from flask import Flask
from flask import request

HOST = '0.0.0.0'

app = Flask(__name__)

@app.route('/highlight', methods=['POST'])
def highlight():
    code = request.form['content']
    lexer = get_lexer_by_name(request.form['lang'])
    formatter = HtmlFormatter()
    return pygments.highlight(code, lexer, formatter)

_lexers = json.dumps(map(lambda lexer: {'name':lexer[0], 'alias':lexer[1][0]}, get_all_lexers()))

@app.route('/lexers', methods=['GET'])
def lexers():
    return _lexers

port = os.environ.get('PORT', 5000)

app.run(host=HOST, port=port)
