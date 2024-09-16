from flask import Flask, request, jsonify
from torch_utils import transform_image, get_pred

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'png','jpg','jpeg'}
def allowed_file(filename):
    #name.png etc
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/predict", methods= ['POST'])
def predict():
    # 1 load image
    if request.method == 'POST':
        file = request.files.get('file')
        if file is None or file.filename == '':
            return jsonify({'error':'No file'})
        if not allowed_file(file.filename):
            return jsonify({'error':'Format not supported'})
        
        #try:
        img_bytes = file.read()
        # 2 transform image to tensor
        tensor = transform_image(img_bytes)
        # 3 make prediction
        pred = get_pred(tensor)
        data = {'Prediction': pred.item(), 'Class name': str(pred.item())}
        # 4 return json
        return jsonify(data)
        #except:
        #    return jsonify({'error':'Error, try agian'}) 
        
if __name__ == '__main__':
    app.run(debug=True)