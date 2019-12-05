from flask import Flask, send_from_directory, render_template

app = Flask(__name__)

@app.route('/cse116')
def cse116():
    return render_template('CSE116.html')


@app.route('/cse116/s19')
def cse116_s19():
    return render_template('old_CSE116.html')


@app.route('/static_files/<path:filename>')
def send_style(filename):
    return send_from_directory('static_files', filename)


if __name__ == '__main__':
    app.run()


import html

html.escape("fsdgafsdg")