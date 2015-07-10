import subprocess
import sys

from flask import Flask, flash, redirect, request, render_template, url_for

DEBUG = False
SECRET_KEY = 'this is needed for flash messages'

BINARY = '/usr/local/bin/youtube-dl'
DEST_DIR = '/media/youtube'
OUTPUT_TEMPLATE = '%s/%%(title)s-%%(id)s.%%(ext)s' % DEST_DIR

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/', methods=['GET', 'POST'])
def download():
    if request.method == 'POST':
        url = request.form['url']
        p = subprocess.Popen([BINARY, '-o', OUTPUT_TEMPLATE, '-q', url])
        p.communicate()
        flash('Successfully downloaded!', 'success')
        return redirect(url_for('download'))
    return render_template('/download.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)
