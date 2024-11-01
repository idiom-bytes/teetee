from flask import Blueprint, render_template, request
import base64

upload_bp = Blueprint('upload_bp', __name__)

@upload_bp.route('/upload/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('upload.html')
        
        file = request.files['file']
        if file.filename == '':
            return render_template('upload.html')
        
        if file and file.filename.endswith('.txt'):
            file_content = file.read().decode('utf-8')
            return render_template('upload.html', file_content=file_content, file_type='text')
        
        if file and (file.filename.endswith('.png') or file.filename.endswith('.jpg')):
            # Convert image to base64 string
            file_data = file.read()
            encoded_img = base64.b64encode(file_data).decode('utf-8')
            img_src = f"data:image/{file.filename.split('.')[-1]};base64,{encoded_img}"
            return render_template('upload.html', file_content=img_src, file_type='image')
        
        return render_template('upload.html')
    
    return render_template('upload.html')
