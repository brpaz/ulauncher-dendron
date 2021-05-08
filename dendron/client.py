import os
import json
import logging

logger = logging.getLogger(__name__)


class DendronClient():
    """ Class that handles all the Dendron logic """
    def __init__(self, workspace_root, vaults=[]):
        """ Class constructor """
        self.workspace_root = workspace_root
        self.vaults = vaults
        self.notes = []

    def set_workspace_root(self, ws):
        """ Sets the Dendron worksapce root """
        self.workspace_root = ws

    def set_vaults(self, vaults=[]):
        """ Set Dendron vaults """
        self.vaults = vaults

    def load_notes(self):
        """ Parses dendron cache files and loads Notes into memory """
        logging.info("Loading dendron notes")
        self.notes = []
        for vault in self.vaults:
            vault_notes = self.__process_vault(vault)
            self.notes = self.notes + vault_notes

    def __process_vault(self, vault):
        """ Processes the notes from a single Dendron vault """
        dendron_cache_file = os.path.join(self.workspace_root, vault,
                                          '.dendron.cache.json')

        if not os.path.isfile(dendron_cache_file):
            logger.warning(
                'Dendron cache file {0} not found'.format(dendron_cache_file))
            return

        with open(dendron_cache_file) as f:
            data = json.load(f)
            return self.__process_notes(data)

    def __process_notes(self, dendron_data={}):
        """ Processes Dendron Cache notes and creates a structure optimized for this extension """
        notes = dendron_data['notes']

        mappedNotes = []
        for file, details in notes.items():
            mappedNotes.append({
                'file':
                file,
                'title':
                details['data']['title'],
                'description':
                details['data']['desc'],
                'vault': {
                    'name': details['data']['vault']['name']
                },
                'path':
                os.path.join(self.workspace_root,
                             details['data']['vault']['fsPath'], file + '.md')
            })

        return mappedNotes

    def search(self, query=None):
        """ Searches notes """
        if not query:
            return self.notes

        query = query.lower()

        return list(
            filter(lambda x: query in x['file'] or query in x['title'],
                   self.notes))
