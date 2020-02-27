from flask import Flask, render_template, request, make_response

import form

app = Flask(__name__)
app.secret_key = 'my_secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    comment_form = form.CommentForm(request.form)

    if request.method == 'POST' and comment_form.validate():
        print comment_form.username.data
        print comment_form.email.data
        print comment_form.comment.data
    else:
        print "Error en el formulario"

    title = "Curso Flask"
    return render_template('insert.html', title=title, form=comment_form)


if __name__ == '__main__':
    app.run(port=88, debug=True)
