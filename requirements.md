# Software Requirements Specification (SRS) for Jach

## 1. Introduction

This document outlines the requirements for Jach, a desktop application designed to visualize and explore jazz guitar chord shapes. The application aims to provide guitarists with an interactive tool to understand and practice various chord voicings across different keys.

## 2. Functional Requirements (FRs)

### FR1: Chord Diagram Display
*   The system shall display a graphical representation of a guitar fretboard.
*   The fretboard shall consist of 6 strings and 5 frets.
*   The system shall accurately render the notes of a selected chord on the fretboard, indicating fretted notes, open strings, and muted strings.
*   Each fretted note shall be annotated with its corresponding interval (e.g., R, 3, 5, 7b).

### FR2: Chord Type Selection
*   The system shall provide a dropdown menu or similar control to select different chord types (e.g., Major, Major 7, Dominant 7, Minor 7, Major 6, Minor 6).
*   Upon selection, the displayed chord diagram shall update to reflect the chosen chord type.

### FR3: Root Note Selection (Transposition)
*   The system shall provide a dropdown menu or similar control to select the root note of the chord (e.g., C, C#, D, D#, E, F, F#, G, G#, A, A#, B).
*   Upon selection, the displayed chord diagram shall transpose to the chosen root note, adjusting fret positions accordingly.
*   Fret numbers shall be displayed on the right side of the fretboard, indicating the absolute fret position on the guitar neck, relative to the lowest fret of the displayed chord.

### FR4: Diagram Export
*   The system shall provide a button to export the currently displayed chord diagram as a JPEG image file.
*   The export function shall prompt the user for a save location and filename.

### FR5: Copy to Clipboard
*   The system shall provide a button to copy the currently displayed chord diagram image to the system clipboard.
*   The copied image shall be pasteable into other applications (e.g., word processors, image editors).

### FR6: Dynamic Chord Title
*   The system shall display a dynamic title at the top of the chord diagram, indicating the selected root note and chord type (e.g., "C Major 7").
*   This title shall be included in exported and copied images.

## 3. Non-Functional Requirements (NFRs)

### NFR1: Usability
*   The user interface shall be intuitive and easy to navigate for guitarists of varying technical proficiency.
*   Chord diagrams shall be clear, legible, and visually appealing.

### NFR2: Performance
*   The application shall render chord diagrams and respond to user input (e.g., chord/root selection) with minimal latency.

### NFR3: Maintainability
*   The codebase shall be modular, well-structured, and easy to understand for future enhancements.
*   Chord data shall be stored in an external, easily editable format (e.g., JSON).

### NFR4: Portability
*   The application shall be runnable on common desktop operating systems (Windows, macOS, Linux) using Python and PySide6.

## 4. Technology Stack

*   **Programming Language:** Python 3.11
*   **GUI Framework:** PySide6 (Qt for Python)
*   **Dependency Management:** Micromamba (via `environment.yml`)
*   **Data Format:** JSON (for chord definitions)

## 5. Future Considerations

Future enhancements may include:
*   Chord progression builder and management.
*   Audio playback of chords.
*   Additional chord voicings and types.
*   Integration with music theory concepts (e.g., scale degrees, voice leading).
