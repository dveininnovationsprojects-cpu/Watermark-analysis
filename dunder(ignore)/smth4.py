from flask import Flask,send_file,render_template,redirect,request
from io import BytesIO
app=Flask(__name__)

@app.route('/',methods=['post','get'])
def index():
    if request.method=='POST':
        file=request.files['image']
        print(file)
        file=file.read()
        return send_file(BytesIO(file),mimetype='application/pdf',as_attachment=True,download_name='file.pdf')
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)