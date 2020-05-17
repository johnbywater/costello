from eventsourcing.system.definition import System

from costello.application import Application
from costello.system.commands import Commands
from costello.system.notifications import Notifications


class CostelloSystem(System):
    def __init__(self, infrastructure_class=None, **kwargs):
        super(CostelloSystem, self).__init__(
            Commands | Application | Application | Notifications,
            infrastructure_class=infrastructure_class,
            **kwargs
        )
