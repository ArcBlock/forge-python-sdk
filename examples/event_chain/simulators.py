# create users
# create products
from forge import ForgeSdk

forgeSdk = ForgeSdk()
rpc = forgeSdk.rpc


def create_undelared_wallet():
    wallet = rpc.create_wallet(passphrase='abcde1234')
    print(wallet)


if __name__ == "__main__":
    create_undelared_wallet()
