# create users
# create products
from time import sleep

import app
import helpers


def simulate():
    echo = app.register_user('echoHuan')
    riley = app.register_user('rileyshu')

    app.create_event(
        'study together',
        2,
        helpers.gen_timestamp(2019, 2, 9, 1),
        helpers.gen_timestamp(2019, 3, 1, 3),
        20,
        riley.wallet,
        riley.token,
    )
    app.create_event(
        'play together',
        2,
        helpers.gen_timestamp(2019, 2, 9, 1),
        helpers.gen_timestamp(2019, 3, 1, 3),
        20,
        echo.wallet,
        echo.token,
    )
    sleep(5)

    app.list_users()
    app.list_events()


if __name__ == "__main__":
    simulate()
