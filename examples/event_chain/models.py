class Event:
    def __init__(
            self, title, description, total, start_time, end_time, wallet,
            token,
    ):
        self.title = title
        self.description = description
        self.total = total
        self.start_time = start_time
        self.end_time = end_time
        self.wallet = wallet
        self.token = token
        self.tickets = []
        self.participants = []

    def gen_ticket(self):
        for id in range(self.total):
            tx_bytes = self.gen_create_tx(id, self.wallet)
            encoded_tx = self.encode_tx(tx_bytes)
            self.tickets.append(encoded_tx)

    def add_participant(self, address):
        # do we limit here?
        self.participants.append(address)

    def gen_create_tx(self, id, wallet):
        return 0

    def encode_tx(self, bytes):
        return 0


class Ticket:
    def __init__(self, id, create_tx):
        self.id = id
        self.create_tx = create_tx
        self.__unused = True
        self.__bought = False

    def get_exchange_tx(self):
        return self.decode_itx(self.create_tx)

    def is_bought(self):
        self.__bought = True

    def is_used(self):
        self.__unused = False

    def decode_itx(self):
        return 0
