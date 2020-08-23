from flask import *
import dj
import urllib, os
app = Flask(__name__)
app.config['MEDIA'] = 'pdf'
@app.route('/unduh/<path:filename>',methods=['GET','POST'])
def unduh(filename):
	return send_from_directory(app.config['MEDIA'], filename, as_attachment=True)
@app.route('/',methods=['GET','POST'])
def index():
	return "Hallo World"
@app.route('/doujinshi/<path:nuklir>',methods=['GET','POST'])
def DownConverter(nuklir):
	try:
		judul=dj.parser(nuklir)
		return {
			'status':True,
			'content':'/unduh/%s'%(urllib.parse.quote(judul))
			}
	except IndexError:
		return {
			'status':False,
			'pesan':'kode nulir salah'
			}
if __name__ == '__main__':
	if 'pdf' in os.listdir():
		pass
	else:
		os.mkdir('pdf')
	app.run(host='0.0.0.0',port=int(os.environ.get('PORT','5000')), debug=True)
