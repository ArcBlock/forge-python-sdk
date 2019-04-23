import logging
import sys

import event_chain.config.config as config
from event_chain.app import create_app
from event_chain.app import utils
from flask import g
from flask import redirect
from flask import url_for

application = create_app()


@application.before_request
def before_request():
    g.logger = logging.getLogger('app')
    g.logger.setLevel(level=logging.DEBUG)


@application.route("/", methods=['GET', 'POST'])
def home():
    return redirect(url_for('events.all'))


@application.context_processor
def inject_poke_url():
    poke_url = utils.gen_did_url(
        f'{config.SERVER_ADDRESS}{url_for("api_mobile.poke")}',
        'RequestAuth')
    return dict(poke_url=poke_url)


if __name__ == '__main__':
    run_type = sys.argv[1]

    application.jinja_env.auto_reload = True
    application.config['TEMPLATES_AUTO_RELOAD'] = True

    if run_type == 'debug':
        application.run(debug=True, host='0.0.0.0')
    else:
        application.run(
            debug=False, host='0.0.0.0'
        )
