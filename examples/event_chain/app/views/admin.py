from event_chain.app import controllers
from event_chain.app import utils
from event_chain.app.forms.admin import RegisterForm
from flask import Blueprint
from flask import g
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for

admin = Blueprint(
    'admin',
    __name__
)


@admin.route("/login", methods=['GET', 'POST'])
def login():
    form = RegisterForm()
    if form.validate_on_submit():
        user = controllers.load_user(
            moniker=form.name.data,
            passphrase=form.passphrase.data,
            address=form.address.data,
        )
        session['user'] = user
        return redirect(url_for('/'))
    else:
        utils.flash_errors(form)
    return render_template('admin/login.html', form=form)


@admin.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = controllers.register_user(
            form.name.data,
            form.passphrase.data
        )
        session['user'] = user
        g.logger.debug(
            'New User registered! wallet: {}, token: {}'.format(
                user.wallet,
                user.token,
            ),
        )
        g.logger.debug("form is validated!!")
    else:
        utils.flash_errors(form)
        return render_template('admin/login.html', form=form)
    return redirect('/')


@admin.route("/logout", methods=['GET', 'POST'])
def logout():
    session['user'] = None
    return redirect('/')
