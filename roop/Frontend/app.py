from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
import os
import base64
import secrets
secret_key = secrets.token_hex(16)

app = Flask(__name__)
app.secret_key = secret_key

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

    # Obtener el número del botón que fue presionado
    button_number = int(request.form['button_number'])

    # Guardar la imagen en una carpeta específica con el nombre del personaje
    character_name = {
        1: 'Hulk',
        2: 'Black Widow',
        3: 'Captain America',
        4: 'Captain Marvel',
        5: 'Hawkeye',
        6: 'Scarlet Witch'
    }.get(button_number, 'Unknown')

    img_name = f"{character_name}.png"
    img_path = os.path.join('roop/images/', img_name)
    with open(img_path, 'wb') as img_file:
        img_file.write(img_bytes)
    flash(f"Imagen guardada correctamente", "success")
    return redirect(url_for('index'))


@app.route('/transform', methods=['POST'])
def transform():
    command = request.json.get('command')
    if command:
        os.system(command)
        return jsonify({'message': 'Transformación completada'})
    return jsonify({'message': 'Error: comando de transformación no proporcionado'}), 400


if __name__ == '__main__':
    app.run(debug=True)