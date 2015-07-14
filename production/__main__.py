import subprocess
import sys

from flask import Flask, flash, redirect, request, render_template, url_for

DEBUG = False
SECRET_KEY = 'this is needed for flash messages'

BINARY = '/usr/local/bin/youtube-dl'

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/', methods=['GET', 'POST'])
def download():
    if request.method == 'POST':
        url = request.form['url']
        try:
            audio = request.form['audio']
        except:
        	audio = '--no-progress'
        try:
        	playlist = request.form['playlist']
        except:
        	playlist = '--no-playlist'
        try:
            playlist_flip = request.form['playlist_flip']
        except:
            playlist_flip = '--no-color'
        try:
        	dest_dir = request.form['dest_dir']
        except:
        	dest_dir = ''
        try:
            description = request.form['description']
        except:
            description = '--add-metadata'


        output = '/media/Youtube/%s/%%(autonumber)s-%%(title)s.%%(ext)s' % dest_dir
        p = subprocess.Popen([BINARY, audio, playlist, playlist_flip, description, '-o', output, url])
        p.communicate()
        flash('Successfully downloaded!', 'success')
        return redirect(url_for('download'))
    return render_template('download.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
