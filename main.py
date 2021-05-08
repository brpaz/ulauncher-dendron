""" Main Module """

import logging
import subprocess
from threading import Thread
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import (ItemEnterEvent, KeywordQueryEvent,
                                        PreferencesEvent,
                                        PreferencesUpdateEvent)
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from dendron.dendron import Dendron

logger = logging.getLogger(__name__)


class DendronExtension(Extension):
    """ Main Extension Class  """
    def __init__(self):
        """ Initializes the extension """
        super(DendronExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())
        self.subscribe(PreferencesEvent, PreferencesEventListener())
        self.subscribe(PreferencesUpdateEvent,
                       PreferencesUpdateEventListener())

    def load_notes(self):
        """ Spawns a new Thread and refresh the local cached data """
        th = Thread(target=self.dendron.load_notes)
        th.daemon = True
        th.start()


class PreferencesEventListener(EventListener):
    """ Handles preferences initialization event """
    def on_event(self, event, extension):
        """ Handle event """
        extension.dendron = Dendron(
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


class KeywordQueryEventListener(EventListener):
    """ Listener that handles the user input """

    # pylint: disable=unused-argument,no-self-use
    def on_event(self, event, extension):
        """ Handles the event """

        notes = extension.dendron.search(event.get_argument())
        items = []

        if len(notes) == 0:
            return RenderResultListAction([
                ExtensionResultItem(icon='images/icon.png',
                                    name='No notes found',
                                    highlightable=False)
            ])
        for item in notes[:8]:
            items.append(
                ExtensionResultItem(icon='images/icon.png',
                                    name=item['title'],
                                    description=item['file'],
                                    on_enter=ExtensionCustomAction(
                                        item['path'])))

        return RenderResultListAction(items)


class ItemEnterEventListener(EventListener):
    """ Listener that handles the click on an item """

    # pylint: disable=unused-argument,no-self-use
    def on_event(self, event, extension):
        """ Handles the event """
        file_path = event.get_data()
        cmd = extension.preferences["dendron_cmd"]
        cmd = cmd.replace("%f%", file_path)

        subprocess.run(cmd, shell=True)


if __name__ == '__main__':
    DendronExtension().run()
