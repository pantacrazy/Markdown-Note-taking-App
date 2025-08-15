import markdown
from flask import Flask,jsonify,render_template,request,redirect,url_for
from markupsafe import escape
from werkzeug.utils import secure_filename
from markdowns_work import mark
from grammar import grammar_check
import os
app = Flask(__name__)
@app.route('/')
def index():
    object_mark=mark()
    return jsonify(object_mark.get_markdowns())
    

@app.route('/', methods=['POST'])
def insert_markdown():
    if 'file' not in request.files:
        return "No file part", 400
    grammar=grammar_check()
    os.makedirs('markdowns', exist_ok=True)
    file = request.files['file']
    content = file.read().decode('utf-8')
    if file.filename == '':
        return "No selected file", 400
    file.seek(0)
    # Guarda el archivo
    file.save(os.path.join('markdowns', secure_filename(file.filename)))
    return jsonify({'message':'File Saved Successfully','grammar_errors':str(grammar.check(content))})

@app.route('/markdowns/<filename>',methods=['GET'])
def get_markdowns(filename):
    os.makedirs('markdowns', exist_ok=True)
    markdown_file = os.path.join('markdowns', filename)
    if os.path.exists(markdown_file):
        with open(markdown_file, 'r') as file:
            markdown_text = file.read()
        return jsonify(markdown_text)
    else:
        return jsonify({'error': 'File not found'}), 404

@app.route('/markdowns/html/<filename>',methods=['GET'])
def get_html(filename):
    os.makedirs('markdowns', exist_ok=True)
    markdown_file = os.path.join('markdowns', filename)
    if os.path.exists(markdown_file):
        with open(markdown_file, 'r') as file:
            markdown_text = file.read()
        html_text = markdown.markdown(markdown_text)
        return f'''<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8">
                      <title>Indice</title></head><body>
                      {escape(html_text)}
</body>
</html>'''
    else:
        return jsonify({'error': 'File not found'}), 404

@app.route('/markdowns/<filename>',methods=['DELETE'])
def delete_markdown(filename):
    os.makedirs('markdowns', exist_ok=True)
    markdown_file = os.path.join('markdowns', filename)
    if os.path.exists(markdown_file):
        os.remove(markdown_file)
        return jsonify({'message': 'File has been deleted'})
    else:
        return jsonify({'error': 'File not found'}), 404

@app.route('/markdowns/<filename>',methods=['PUT'])
def edit_markdown(filename):
    if 'file' not in request.files:
        return "No file part", 400
    os.makedirs('markdowns', exist_ok=True)
    markdown_file = os.path.join('markdowns', filename)
    grammar=grammar_check()
    file = request.files['file']
    text_file=file.read().decode('utf-8')
    if os.path.exists(markdown_file):
        if file.filename =='':
            return "No valid filename", 400
        file.seek(0)
        file.save(os.path.join('markdowns', secure_filename(file.filename)))

        return jsonify({'message': 'File has been edited','grammar_errors':str(grammar.check(text_file))})
    else:
        return jsonify({'error': 'File not found'}), 404