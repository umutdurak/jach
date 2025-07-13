import sys
import json
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QComboBox
from PySide6.QtGui import QPainter, QPen, QBrush, QColor, QFont
from PySide6.QtCore import Qt

class ChordWidget(QWidget):
    def __init__(self, chords):
        super().__init__()
        self.chords = chords
        self.current_chord = self.chords["Major"][0]

    def set_chord(self, chord_name):
        for chord_type in self.chords.values():
            for chord in chord_type:
                if chord["name"] == chord_name:
                    self.current_chord = chord
                    self.update()
                    return

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # --- Draw Fretboard ---
        fretboard_rect = self.rect().adjusted(20, 20, -20, -20)
        num_frets = 5
        num_strings = 6
        fret_height = fretboard_rect.height() / num_frets
        string_spacing = fretboard_rect.width() / (num_strings - 1)

        painter.setPen(QPen(QColor("#8c8c8c"), 2))
        for i in range(num_frets + 1):
            y = fretboard_rect.top() + i * fret_height
            painter.drawLine(fretboard_rect.left(), y, fretboard_rect.right(), y)

        for i in range(num_strings):
            x = fretboard_rect.left() + i * string_spacing
            painter.drawLine(x, fretboard_rect.top(), x, fretboard_rect.bottom())

        # --- Draw Chord Shape ---
        for string, fret, interval in self.current_chord["positions"]:
            string_index = 5 - string
            x = fretboard_rect.left() + string_index * string_spacing

            if fret == -1:  # Muted string
                painter.setPen(QPen(QColor("#ff0000"), 2))
                painter.drawLine(x - 5, fretboard_rect.top() - 15, x + 5, fretboard_rect.top() - 5)
                painter.drawLine(x + 5, fretboard_rect.top() - 15, x - 5, fretboard_rect.top() - 5)
            elif fret == 0:  # Open string
                painter.setPen(QPen(QColor("#ffffff"), 2))
                painter.drawEllipse(x - 5, fretboard_rect.top() - 15, 10, 10)
            else:  # Fretted note
                y = fretboard_rect.top() + (fret - 0.5) * fret_height
                painter.setBrush(QBrush(QColor("#ffffff")))
                painter.setPen(QPen(QColor("#000000"), 2))
                painter.drawEllipse(x - 10, y - 10, 20, 20)

                painter.setFont(QFont("Arial", 10, QFont.Bold))
                painter.setPen(QPen(QColor("#000000")))
                painter.drawText(x - 10, y - 10, 20, 20, Qt.AlignCenter, interval)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Jazz Chord Visualizer")

        with open("chords.json", "r") as f:
            self.chords = json.load(f)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.chord_selector = QComboBox()
        for chord_type in self.chords:
            for chord in self.chords[chord_type]:
                self.chord_selector.addItem(chord["name"])
        
        self.chord_widget = ChordWidget(self.chords)

        self.layout.addWidget(self.chord_selector)
        self.layout.addWidget(self.chord_widget)

        self.chord_selector.currentTextChanged.connect(self.chord_widget.set_chord)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
