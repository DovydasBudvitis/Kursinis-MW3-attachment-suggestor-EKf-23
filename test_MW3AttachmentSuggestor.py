import unittest
from unittest.mock import patch, MagicMock
from tkinter import Tk
from tkinter import messagebox
from MW3AttachmentSuggestor import MW3AttachmentSuggestor

class TestMW3AttachmentSuggestor(unittest.TestCase):
    def setUp(self):
        self.window = Tk()
        self.app = MW3AttachmentSuggestor(self.window)

    def tearDown(self):
        self.window.destroy()

    def test_submit_playstyle(self):
        # Testuojame, ar playstyle yra pasirinktas
        self.assertFalse(self.app._playstyle_selected)
        self.app._playstylebox.curselection = MagicMock(return_value=(0,))
        self.app.submit_playstyle()
        self.assertTrue(self.app._playstyle_selected)
        self.assertNotEqual(self.app._selected_playstyle, "")

    def test_submit_weapon(self):
        # Testuojame, ar weapon yra pasirinktas
        self.assertFalse(self.app._weapon_selected)
        self.app._weaponbox.curselection = MagicMock(return_value=(0,))
        self.app.submit_weapon()
        self.assertTrue(self.app._weapon_selected)
        self.assertNotEqual(self.app._selected_weapon, "")

    @patch('AttachmentSuggestor.AttachmentSuggestion.suggest_attachments')
    @patch('MW3AttachmentSuggestor.messagebox.showerror')
    def test_on_submit_without_selection(self, mock_showerror, mock_suggest_attachments):
        # Testuojame, ar išmetamas klaidos pranešimas, kai nėra pasirinktas nei playstyle, nei weapon
        self.app.on_submit()
        mock_showerror.assert_called_once_with(title='ERROR!', message='Please select both a playstyle and a weapon')
        mock_suggest_attachments.assert_not_called()

    @patch('AttachmentSuggestor.AttachmentSuggestion.suggest_attachments')
    @patch('MW3AttachmentSuggestor.Toplevel')
    def test_on_submit_with_selection(self, mock_Toplevel, mock_suggest_attachments):
        # Testuojame, ar attachment'ų sąrašas yra sugeneruojamas, kai yra pasirinktas tiek playstyle, tiek weapon
        self.app._playstyle_selected = True
        self.app._weapon_selected = True
        self.app.on_submit()
        mock_Toplevel.assert_called_once()
        mock_suggest_attachments.assert_called_once()

    @patch('MW3AttachmentSuggestor.Toplevel')
    def test_open_new_window(self):
    # Testuojame, ar išmetamas NotImplementedError
        with self.assertRaises(NotImplementedError):
            self.app.open_new_window()


if __name__ == "__main__":
    unittest.main()
