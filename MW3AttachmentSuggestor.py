from tkinter import *
from tkinter import messagebox
import WeaponEnums
from AttachmentSuggestor import AttachmentSuggestion

class GUIElementFactory:
    """Factory class for creating GUI elements."""
    def create_label(self, master, **kwargs):
        """Create a Label widget."""
        return Label(master, **kwargs)

    def create_button(self, master, **kwargs):
        """Create a Button widget."""
        return Button(master, **kwargs)

    def create_listbox(self, master, **kwargs):
        """Create a Listbox widget."""
        return Listbox(master, **kwargs)

class AttachmentSuggestorBase:
    """Base class for attachment suggestion."""
    def __init__(self, master):
        """Initialize the base class."""
        self.master = master
        master.geometry("800x600")
        master.title("MW3 Attachment Suggestor")
        master.config(background='black')

        self._playstyle_selected = False
        self._weapon_selected = False
        self._selected_playstyle = ""
        self._selected_weapon = ""
        self._attachments = {}
        self._gui_factory = GUIElementFactory()

        self.create_widgets()

    def create_widgets(self):
        """Create GUI widgets."""
        raise NotImplementedError("Subclasses must implement create_widgets method")

    def submit_playstyle(self):
        """Submit the selected playstyle."""
        self._playstyle_selected = True
        self._selected_playstyle = self._get_selected_playstyle()
        print(self._selected_playstyle)

    def submit_weapon(self):
        """Submit the selected weapon."""
        self._weapon_selected = True
        self._selected_weapon = self._get_selected_weapon()
        print(self._selected_weapon)

    def open_new_window(self):
        """Open a new window for attachment suggestions."""
        raise NotImplementedError("Subclasses must implement open_new_window method")

    def on_submit(self):
        """Handle submission of playstyle and weapon."""
        if self._playstyle_selected and self._weapon_selected:
            self._attachments = AttachmentSuggestion.suggest_attachments()
            self.open_new_window()
        else:
            messagebox.showerror(title='ERROR!', message='Please select both a playstyle and a weapon')

    def _get_selected_playstyle(self):
        """Get the selected playstyle."""
        return self._playstylebox.get(self._playstylebox.curselection())

    def _get_selected_weapon(self):
        """Get the selected weapon."""
        return self._weaponbox.get(self._weaponbox.curselection())

    @property
    def selected_playstyle(self):
        """Property to access the selected playstyle."""
        return self._selected_playstyle

    @property
    def selected_weapon(self):
        """Property to access the selected weapon."""
        return self._selected_weapon

    @property
    def attachments(self):
        """Property to access the attachments."""
        return self._attachments

class MW3AttachmentSuggestor(AttachmentSuggestorBase):
    """Class for MW3 attachment suggestion."""
    def create_widgets(self):
        """Create GUI widgets for MW3 attachment suggestion."""
        self.label = self._gui_factory.create_label(self.master, text='MW3 Attachment suggestor', font=('Terminal', 20, 'bold'),
                                                     fg='red', bg='black', relief=RAISED, bd=7)
        self.label.pack()
        icon = PhotoImage(file='MW3ICON2.png')
        self.master.iconphoto(True, icon)
        self.master.config(background='black')

        self._playstylebox = self._gui_factory.create_listbox(self.master, bg='black', font=('Terminal', 13, 'bold'),
                                                              fg='red', width='14', relief=RAISED, bd=7)
        self._playstylebox.place(x='560', y='100')
        self._playstylebox.insert(0, "Close-range")
        self._playstylebox.insert(1, "Long-range")
        self._playstylebox.insert(2, "Sniper-Support")
        self._playstylebox.insert(3, "Sniper")
        self._playstylebox.insert(4, "All-rounder")

        self._submit_button2 = self._gui_factory.create_button(self.master, text="Select", command=self.submit_playstyle,
                                                               font=('Terminal', 13, 'bold'), fg='red', bg='black',
                                                               relief=RAISED, bd=7)
        self._submit_button2.place(x='560', y='300')

        self._attachment_button = self._gui_factory.create_button(self.master, text="Submit", command=self.on_submit,
                                                                  font=('Terminal', 13, 'bold'), fg='red', bg='black',
                                                                  relief=RAISED, bd=7)
        self._attachment_button.place(x='350', y='350')

        self._weaponbox = self._gui_factory.create_listbox(self.master, bg='black', font=('Terminal', 13, 'bold'),
                                                            fg='red', width='14', relief=RAISED, bd=7)
        self._weaponbox.place(x='50', y='100')

        weapons = []
        for weapon_type in WeaponEnums.PrimaryWeapons:
            for weapon in weapon_type.value:
                weapons.append(weapon.value)

        for index, weapon in enumerate(weapons, start=1):
            self._weaponbox.insert(index, weapon)

        self._submit_button = self._gui_factory.create_button(self.master, text="Select", command=self.submit_weapon,
                                                              font=('Terminal', 13, 'bold'), fg='red', bg='black',
                                                              relief=RAISED, bd=7)
        self._submit_button.place(x='50', y='300')

    def open_new_window(self):
        """Open a new window for attachment suggestions."""
        def resuggest():
            self._attachments = AttachmentSuggestion.suggest_attachments()
            attachment_list.delete(0, END)  # Clear previous attachments
            for attachment_type, attachment in self._attachments.items():
                attachment_list.insert(END, f"{attachment_type}: {attachment}")

        def save_to_file_new_window():
            filename = "attachments.txt"
            with open(filename, "w") as file:
                for attachment_type, attachment in self._attachments.items():
                    file.write(f"{attachment_type}: {attachment}\n")
            messagebox.showinfo(title="Success", message=f"Attachments saved to {filename}")

        new_window = Toplevel(self.master)
        new_window.geometry("600x400")
        new_window.title("MW3 Attachment Suggestions")
        new_window.config(background='black')

        resuggest_button = Button(new_window, text="Resuggest", command=resuggest,
                                  font=('Terminal', 13, 'bold'), fg='red', bg='black',
                                  relief=RAISED, bd=7)
        resuggest_button.pack()

        playstyle_label = Label(new_window, text=f"Selected Playstyle: {self.selected_playstyle}",
                                bg='black', fg='white')
        playstyle_label.pack()

        weapon_label = Label(new_window, text=f"Selected Weapon: {self.selected_weapon}",
                             bg='black', fg='white')
        weapon_label.pack()

        attachment_list = Listbox(new_window, font=('Terminal', 13, 'bold'), fg='red', bg='black',
                                  width=50, relief=RAISED, bd=7)
        attachment_list.pack()
        for attachment_type, attachment in self._attachments.items():
            attachment_list.insert(END, f"{attachment_type}: {attachment}")

        save_button_new_window = Button(new_window, text="Save to File",
                                        command=save_to_file_new_window,
                                        font=('Terminal', 13, 'bold'), fg='red', bg='black',
                                        relief=RAISED, bd=7)
        save_button_new_window.pack()

def main():
    """Main function to create and run the application."""
    window = Tk()
    app = MW3AttachmentSuggestor(window)
    window.mainloop()

if __name__ == "__main__":
    main()
