from ulauncher.api.client.EventListener import EventListener


class ItemEnterEventListener(EventListener):
    """ Listener that handles the click on an item """
    def on_event(self, event, extension):
        """ Handles the event """
        data = event.get_data()

        if data['action'] == 'open_note':
            extension.open_note(data['path'])

        if data['action'] == 'reload':
            extension.load_notes()
