"""This module contains classes for Notebook realization"""

import datetime


last_id = 0


class Note:
    """
    A class to represent single Note.
    """

    def __init__(self, memo: str, tags=""):
        """Initialize a note with its meno and tags.

        Args:
            memo (str): Content of the note.
            tags (str, optional): Tags of the note. Defaults to ''.
        """
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filterr: str) -> bool:
        """Find whether note matches the search by memo or tags.

        Args:
            filter (str): Text to match.

        Returns:
            bool: Whether matches.
        """
        return filterr in self.memo or filterr in self.tags


class Notebook:
    """
    A class to represent a Notebool consisting of notes.
    """

    def __init__(self):
        """Initialize a notebook wiht empty list."""
        self.notes = []

    def new_note(self, memo: str, tags=""):
        """Create new note and add ot notebook.

        Args:
            memo (str): Content of the note.
            tags (str, optional): Tags of the note. Defaults to ''.
        """
        self.notes.append(Note(memo, tags))

    def modify_memo(self, note_id: int, memo: str):
        """Modify memo of the note with its ID given.

        Args:
            note_id (int): ID of the note.
            memo (str): New contents of the note.
        """
        for note in self.notes:
            if str(note.id) == note_id:
                note.memo = memo
                break

    def modify_tags(self, note_id: int, tags: str):
        """Modify meno of the note with its ID given.

        Args:
            note_id (int): ID of the note.
            tags (str): New tags of the note.
        """
        for note in self.notes:
            if str(note.id) == note_id:
                note.tags = tags
                break

    def search(self, filterr: str) -> list:
        """Return all notes from the notebook that match the filter.

        Args:
            filterr (str): Filter to find notes.

        Returns:
            list: All notes that match.
        """
        return [note for note in self.notes if note.match(filterr)]
