# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-or-later
import importlib.util
from pathlib import Path
import unittest
FILE = Path(__file__).resolve().parents[1] / "multiplications.py"
spec = importlib.util.spec_from_file_location("app_under_test", FILE)
app = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app)
class ApplicationTests(unittest.TestCase):

    def test_grade(self):
        self.assertEqual(app.grade(0, 20), 1.0)
        self.assertEqual(app.grade(20, 20), 6.0)
        self.assertEqual(app.grade(15, 20), 4.75)

    def test_gui(self):
        window = app.MultiplicationApp()
        try:
            a, b = window.current
            window.answer.set(str(a * b))
            window.check()
            self.assertEqual(window.correct, 1)
            self.assertEqual(window.index, 1)
        finally: window.destroy()

if __name__ == "__main__":
    unittest.main()
