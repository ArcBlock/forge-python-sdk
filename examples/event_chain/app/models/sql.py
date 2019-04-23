from event_chain.app import db


class EventModel(db.Model):
    address = db.Column(db.String(64), primary_key=True)
    owner = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return f'<Event {self.address}>'


class ExchangeHashModel(db.Model):
    __tablename__ = 'exchange_txs'
    hash = db.Column(db.String(64), primary_key=True)
    event_address = db.Column(db.String(64))

    def __repr__(self):
        return f'<Exchange Hash {self.hash}>'
