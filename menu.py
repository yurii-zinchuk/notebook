"""This module contains class to navigate in the Notebook"""

from notebook import *
import sys


class Menu:
    """
    A class to navigate in the notebook.
    """

    def __init__(self):
        """Initialize a menu, add an empty notebook and choices."""
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit,
        }

    def display_menu(self):
        """Display menu on the screen."""
        print(
            """
            Notebook Menu
            1. Show all Notes
            2. Search Notes
            3. Add Note
            4. Modify Note
            5. Quit
        """
        )

    def run(self):
        """Start executing the program, take user choices."""
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def show_notes(self, notes: Note = None):
        """Show notes contents.

        Args:
            notes (Note, optional): Note to show conctents. Defaults to None.
        """
        if notes == []:
            print("Not such note.")
        elif notes is None:
            notes = self.notebook.notes
        if notes:
            for note in notes:
                print("{0}: {1}\n{2}\ncreated: {3}".format(
                    note.id, note.tags, note.memo, note.creation_date))

    def search_notes(self):
        """Searches notes in the notebook and show them."""
        filterr = input("Search for: ")
        notes = self.notebook.search(filterr)
        self.show_notes(notes)

    def add_note(self):
        """Add a new note to the notebook."""
        memo = input("Enter a memo: ")
        self.notebook.new_note(memo)
        print("Your note has been added.")

    def modify_note(self):
        """Change memo or tags of the note."""
        idd = input("Enter a note id: ")
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        if memo:
            self.notebook.modify_memo(idd, memo)
        if tags:
            self.notebook.modify_tags(idd, tags)

    def quit(self):
        """Stop the program."""
        print("Thank you for using your notebook today.")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()
