from pygments import highlight
from pygments.lexers import get_lexer_by_name, get_all_lexers
from pygments.formatters import HtmlFormatter

import simplejson as json

from flask import Flask
from flask import request

app = Flask(__name__)

LEXERS = json.dumps(map(lambda lexer: {'name':lexer[0], 'alias':lexer[1][0]}, get_all_lexers()))

@app.route('/highlight', methods=['POST'])
def highlight():
    lexer = get_lexer_by_name(request.form['lang'])
    formatter = HtmlFormatter()
    code = request.form['content']
    return highlight(code, lexer, formatter)

@app.route('/lexers', methods=['GET'])
def lexers():
    return LEXERS

app.run()
