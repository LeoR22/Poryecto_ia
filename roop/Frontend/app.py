from flask import Flask, render_template, request, redirect, url_for
import os
import base64

app = Flask(__name__)
captureCounter = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    global captureCounter
    # Obtener la imagen en base64 y convertirla a bytes
    img_data = request.form['image']
    img_data = img_data.replace('data:image/png;base64,', '')
    img_bytes = base64.b64decode(img_data)

    # Incrementar el contador de capturas
    captureCounter += 1

    # Guardar la imagen en una carpeta específica con el contador como nombre
    img_name = f"captura_{captureCounter}.png"
    img_path = os.path.join('roop/', img_name)
    with open(img_path, 'wb') as img_file:
        img_file.write(img_bytes)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
