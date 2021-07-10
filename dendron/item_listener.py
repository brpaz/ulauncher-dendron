from ulauncher.api.client.EventListener import EventListener


class ItemEnterEventListener(EventListener):
    """ Listener that handles the click on an item """
    def on_event(self, event, extension):
        """ Handles the event """
        data = event.get_data()

        if data['action'] == 'open_note':
            extension.open_in_dendron(data['path'])

        if data['action'] == 'preview_note':
            extension.open_in_quickmd(data['path'])

        if data['action'] == 'reload':
            extension.load_notes()
