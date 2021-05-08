""" Extension preferences Listeners """

import logging
from ulauncher.api.client.EventListener import EventListener
from dendron.client import DendronClient

logger = logging.getLogger(__name__)


class PreferencesEventListener(EventListener):
    """ Handles preferences initialization event """
    def on_event(self, event, extension):
        """ Handle event """
        extension.dendron = DendronClient(
            event.preferences["dendron_workspace_root"],
            event.preferences["dendron_vaults"].split(","),
        )

        extension.load_notes()


class PreferencesUpdateEventListener(EventListener):
    """ Handles Preferences Update event """
    def on_event(self, event, extension):
        logging.info("Preferences Update")
        if event.id == 'dendron_workspace_root':
            extension.dendron.set_workspace_root(event.new_value)
            extension.dendron.load_notes()

        if event.id == 'dendron_vaults':
            extension.dendron.set_vaults(event.new_value.split(","))
            extension.load_notes()
