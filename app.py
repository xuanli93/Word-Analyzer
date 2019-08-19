import string
from flask import Flask,request, render_template
from werkzeug import secure_filename

app = Flask(__name__)

FILENAME = ''

@app.route('/upload')
def upload():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
   if request.method == 'POST':
      f = request.files['file']
      FILENAME=f.filename
      f.save(secure_filename(f.filename))
      return (wordCountTable())

@app.route('/result')
def wordCountTable():
	print('file uploaded successfully')
	counter = {}
	
	with open(FILENAME,'r') as f:
		for line in f:
			for word in line.split():
				word = word.strip(string.punctuation)
				word = word.strip(" ")
				if word not in counter:
					counter[word] = 1
				else:
					counter[word] += 1

	result = sorted(counter.items(), key = lambda x: (x[1],x[0]), reverse = True)

	return render_template('result.html', result= result,filename=FILENAME)
 

if __name__ == '__main__':
	app.run(debug = True)
