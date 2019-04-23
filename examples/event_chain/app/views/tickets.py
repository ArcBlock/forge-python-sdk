from event_chain.app import controllers
from event_chain.app import models
from event_chain.app import utils
from flask import Blueprint
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for

tickets = Blueprint(
    'tickets',
    __name__,
    template_folder='templates',
)


@tickets.route("/account")
def all():
    if not session.get('user'):
        return redirect(url_for('admin.login'))
    tickets = controllers.list_unused_tickets(session.get('user').address)
    num_tickets = len(tickets)
    user = models.get_participant_state(session.get('user').address)
    events = get_event_for_ticket(tickets)
    ticket_lists = utils.chunks(tickets, 3)
    return render_template(
        'tickets/tickets.html', ticket_lists=ticket_lists, events=events,
        user=user, view_only=False, num_tickets=num_tickets
    )


def get_event_for_ticket(tickets):
    res = {}
    for ticket in tickets:
        event_address = ticket.ticket_info.event_address
        event = models.get_event_state(event_address)
        res[ticket.address] = event
    return res
