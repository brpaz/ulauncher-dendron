import logging
import subprocess
from threading import Thread
from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent, \
    PreferencesEvent, PreferencesUpdateEvent
from ulauncher.api.shared.action.ExtensionCustomAction import \
    ExtensionCustomAction
from ulauncher.api.shared.action.RenderResultListAction import \
    RenderResultListAction
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from dendron.preferences import PreferencesEventListener, PreferencesUpdateEventListener
from dendron.query_listener import KeywordQueryEventListener
from dendron.item_listener import ItemEnterEventListener

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
        """ Load Dendron notes into memory """
        th = Thread(target=self.dendron.load_notes)
        th.daemon = True
        th.start()

    def search_notes(self, query):
        """ Search notes """
        notes = self.dendron.search(query)
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
                                    on_enter=ExtensionCustomAction({
                                        'action':
                                        'open_note',
                                        'path':
                                        item['path']
                                    })))
        return RenderResultListAction(items)

    def open_note(self, path):
        """ Open the selected note on the configured Dendron workspace """
        cmd = self.preferences["dendron_cmd"]
        cmd = cmd.replace("%f%", path)

        subprocess.run(cmd, shell=True)

    def reload_action(self):
        """ Shows reload action """
        return RenderResultListAction([
            ExtensionResultItem(icon='images/icon.png',
                                name='Reload notes',
                                highlightable=False,
                                on_enter=ExtensionCustomAction(
                                    {'action': 'reload'}))
        ])
