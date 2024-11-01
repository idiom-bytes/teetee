from flask import Blueprint, render_template, request, flash

upload_bp = Blueprint('upload_bp', __name__)

@upload_bp.route('/upload/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return render_template('upload.html', file_content='')
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return render_template('upload.html', file_content='')
        if file and file.filename.endswith('.txt'):
            file_content = file.read().decode('utf-8')
            return render_template('upload.html', file_content=file_content)
        else:
            flash('Not a text file')
            return render_template('upload.html', file_content='')
    return render_template('upload.html', file_content='')