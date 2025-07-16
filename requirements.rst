.. _srs:

=================================================
Software Requirements Specification (SRS) for Jach
=================================================

.. sectnum::

1. Introduction
===============

This document outlines the requirements for Jach, a desktop application designed to visualize and explore jazz guitar chord shapes. The application aims to provide guitarists with an interactive tool to understand and practice various chord voicings across different keys.

2. Functional Requirements (FRs)
=================================

2.1. FR1: Chord Diagram Display
-------------------------------
*   **ID:** FR1
*   **Description:** The system shall display a graphical representation of a guitar fretboard, consisting of 6 strings and 5 frets. It shall accurately render the notes of a selected chord on the fretboard, indicating fretted notes, open strings, and muted strings. Each fretted note shall be annotated with its corresponding interval (e.g., R, 3, 5, 7b).
*   **Priority:** High
*   **Status:** Implemented
*   **Verification Method:** Manual inspection of the displayed diagram against expected output.
*   **Notes:** Includes white background, larger circles/annotations, and correct fret numbering.

2.2. FR2: Chord Type Selection
------------------------------
*   **ID:** FR2
*   **Description:** The system shall provide a dropdown menu or similar control to select different chord types (e.g., Major, Major 7, Dominant 7, Minor 7, Major 6, Minor 6). Upon selection, the displayed chord diagram shall update to reflect the chosen chord type.
*   **Priority:** High
*   **Status:** Implemented
*   **Verification Method:** Manual testing of dropdown functionality and visual update.

2.3. FR3: Root Note Selection (Transposition)
---------------------------------------------
*   **ID:** FR3
*   **Description:** The system shall provide a dropdown menu or similar control to select the root note of the chord (e.g., C, C#, D, D#, E, F, F#, G, G#, A, A#, B). Upon selection, the displayed chord diagram shall transpose to the chosen root note, adjusting fret positions accordingly. Fret numbers shall be displayed on the right side of the fretboard, indicating the absolute fret position on the guitar neck, relative to the lowest fret of the displayed chord.
*   **Priority:** High
*   **Status:** Implemented
*   **Verification Method:** Manual testing of dropdown functionality and visual update for various root notes.

2.4. FR4: Diagram Export
------------------------
*   **ID:** FR4
*   **Description:** The system shall provide a button to export the currently displayed chord diagram as a JPEG image file. The export function shall prompt the user for a save location and filename.
*   **Priority:** High
*   **Status:** Implemented
*   **Verification Method:** Manual testing of export functionality and verification of saved JPEG file.

2.5. FR5: Copy to Clipboard
---------------------------
*   **ID:** FR5
*   **Description:** The system shall provide a button to copy the currently displayed chord diagram image to the system clipboard. The copied image shall be pasteable into other applications (e.g., word processors, image editors).
*   **Priority:** High
*   **Status:** Implemented
*   **Verification Method:** Manual testing of copy functionality and pasting into external applications.

2.6. FR6: Dynamic Chord Title
-----------------------------
*   **ID:** FR6
*   **Description:** The system shall display a dynamic title at the top of the chord diagram, indicating the selected root note and chord type (e.g., "C Major 7"). This title shall be included in exported and copied images.
*   **Priority:** High
*   **Status:** Implemented
*   **Verification Method:** Manual inspection of the displayed title and verification in exported/copied images.

3. Non-Functional Requirements (NFRs)
=====================================

3.1. NFR1: Usability
--------------------
*   **ID:** NFR1
*   **Description:** The user interface shall be intuitive and easy to navigate for guitarists of varying technical proficiency. Chord diagrams shall be clear, legible, and visually appealing.
*   **Priority:** High
*   **Status:** Implemented
*   **Verification Method:** User acceptance testing and visual inspection.

3.2. NFR2: Performance
----------------------
*   **ID:** NFR2
*   **Description:** The application shall render chord diagrams and respond to user input (e.g., chord/root selection) with minimal latency.
*   **Priority:** Medium
*   **Status:** Implemented
*   **Verification Method:** Manual observation during usage.

3.3. NFR3: Maintainability
--------------------------
*   **ID:** NFR3
*   **Description:** The codebase shall be modular, well-structured, and easy to understand for future enhancements. Chord data shall be stored in an external, easily editable format (e.g., JSON).
*   **Priority:** High
*   **Status:** Implemented
*   **Verification Method:** Code review and adherence to coding standards.

3.4. NFR4: Portability
----------------------
*   **ID:** NFR4
*   **Description:** The application shall be runnable on common desktop operating systems (Windows, macOS, Linux) using Python and PySide6.
*   **Priority:** Medium
*   **Status:** Implemented (Tested on macOS)
*   **Verification Method:** Testing on target operating systems.

4. Technology Stack
===================

*   **Programming Language:** Python 3.11
*   **GUI Framework:** PySide6 (Qt for Python)
*   **Dependency Management:** Micromamba (via `environment.yml`)
*   **Data Format:** JSON (for chord definitions)

5. Future Considerations
========================

Future enhancements may include:
*   Chord progression builder and management.
*   Audio playback of chords.
*   Additional chord voicings and types.
*   Integration with music theory concepts (e.g., scale degrees, voice leading).
