import string
from flask import Flask,request, render_template
from werkzeug import secure_filename

app = Flask(__name__)

FILENAME = ''

@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'
      
@app.route('/result')
def wordCountTable():
	counter = {}
	filename= 'oliver_twist.txt'
	with open(filename,'r') as f:
		for line in f:
			for word in line.split():
				word = word.strip(string.punctuation)
				word = word.strip(" ")
				if word not in counter:
					counter[word] = 1
				else:
					counter[word] += 1

	result = sorted(counter.items(), key = lambda x: (x[1],x[0]), reverse = True)

	return render_template('result.html', result= result,filename=filename)
 

if __name__ == '__main__':
	app.run(debug = True)
