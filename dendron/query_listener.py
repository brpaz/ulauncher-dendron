from ulauncher.api.client.EventListener import EventListener


class KeywordQueryEventListener(EventListener):
    """ Listener that handles the user input """
    def on_event(self, event, extension):
        """ Handles the event """

        query = event.get_argument()

        if query == ":reload":
            return extension.reload_action()

        return extension.search_notes(query)
