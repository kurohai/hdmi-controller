# -*- coding: utf-8 -*-
from flask import jsonify
from flask import redirect
from flask import render_template
from flask import request
from flask_wtf import FlaskForm
from project import app
from project import hdmi_input_control
from wtforms import StringField
from wtforms.validators import DataRequired



ports = [i + 1 for i in xrange(8)]


class CreateForm(FlaskForm):
    text = StringField('name', validators=[DataRequired()])


@app.route('/')
def start():

    return render_template('printer/index.html', ports=ports)


@app.route('/print/', methods=['GET', 'POST'])
def printer():
    form = CreateForm(request.form)
    if request.method == 'POST' and form.validate():
        from project.models.Printer import Printer
        printer = Printer()
        printer.show_string(form.text.data)
        return render_template('printer/index.html', ports=ports)
    return render_template('printer/print.html', form=form, ports=ports)


@app.route('/remote/<int:port>/', methods=['GET', 'POST'])
def remote(port):

    print(port)
    hdmi_input_control(port)
    data = {'status': 'success', 'port': port}
    # return "port {0) activated".format(port), 200
    return jsonify(data)



@app.before_request
def add_trailing():
    rp = request.path
    if not rp.endswith('/'):
        return redirect(rp + '/')
