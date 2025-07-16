import sys
import json
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QPushButton, QFileDialog
from PySide6.QtGui import QPainter, QPen, QBrush, QColor, QFont, QPixmap
from PySide6.QtCore import Qt

class ChordWidget(QWidget):
    def __init__(self, chords):
        super().__init__()
        self.chords = chords
        self.current_chord = self.chords["Major"][0]
        self.root_note = "C"
        self.notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

    def set_chord(self, chord_name):
        for chord_type in self.chords.values():
            for chord in chord_type:
                if chord["name"] == chord_name:
                    self.current_chord = chord
                    self.update()
                    return

    def set_root(self, root_note):
        self.root_note = root_note
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        fretboard_rect = self.rect().adjusted(20, 20, -20, -20)
        num_frets = 12
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

        root_offset = self.notes.index(self.root_note)

        for string, fret, interval in self.current_chord["positions"]:
            string_index = 5 - string
            x = fretboard_rect.left() + string_index * string_spacing
            new_fret = fret + root_offset

            if new_fret == -1:
                painter.setPen(QPen(QColor("#ff0000"), 2))
                painter.drawLine(x - 5, fretboard_rect.top() - 15, x + 5, fretboard_rect.top() - 5)
                painter.drawLine(x + 5, fretboard_rect.top() - 15, x - 5, fretboard_rect.top() - 5)
            elif new_fret == 0:
                painter.setPen(QPen(QColor("#ffffff"), 2))
                painter.drawEllipse(x - 5, fretboard_rect.top() - 15, 10, 10)
            else:
                y = fretboard_rect.top() + (new_fret - 0.5) * fret_height
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

        self.selectors_layout = QHBoxLayout()
        self.chord_selector = QComboBox()
        self.root_selector = QComboBox()

        for chord_type in self.chords:
            for chord in self.chords[chord_type]:
                self.chord_selector.addItem(chord["name"])
        
        self.notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        for note in self.notes:
            self.root_selector.addItem(note)

        self.selectors_layout.addWidget(self.chord_selector)
        self.selectors_layout.addWidget(self.root_selector)

        self.chord_widget = ChordWidget(self.chords)

        self.export_button = QPushButton("Export as JPEG")
        self.export_button.clicked.connect(self.export_chord)

        self.layout.addLayout(self.selectors_layout)
        self.layout.addWidget(self.chord_widget)
        self.layout.addWidget(self.export_button)

        self.chord_selector.currentTextChanged.connect(self.chord_widget.set_chord)
        self.root_selector.currentTextChanged.connect(self.chord_widget.set_root)

    def export_chord(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Chord Diagram", "", "JPEG Files (*.jpg)")
        if file_name:
            pixmap = self.chord_widget.grab()
            pixmap.save(file_name, "jpg")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
