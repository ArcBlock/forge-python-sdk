import logging

from event_chain import ec
from event_chain.application import app
from event_chain.application import models
from event_chain.db import utils
from event_chain.simulation import simulate
from event_chain.utils import helpers

logging.basicConfig(level=logging.DEBUG)
