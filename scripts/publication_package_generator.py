#!/usr/bin/env python3
"""
PUBLICATION PACKAGE GENERATOR
Creates a complete publication-ready folder structure for "The Master's Palette"
"""

import os
import shutil
from datetime import datetime

def create_folder_structure(base_path):
    """Create the publication folder structure."""
    folders = [
        base_path,
        os.path.join(base_path, "Parts"),
        os.path.join(base_path, "Source"),
    ]
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
    return folders

def generate_title_page(base_path):
    """Generate title page content."""
    content = """================================================================================
                           THE MASTER'S PALETTE
================================================================================

                    Suite for Hybrid Chamber Ensemble
                          in Five Movements

                                  *


                     I. Mingus Blues Cathedral
                     II. Gil's Canvas
                     III. Bartok Night
                     IV. German Development
                     V. Tintinnabuli Epilogue


                                  *


                            Music by
                        MICHAEL BRYANT


                              2025




================================================================================
              © 2025 Michael Bryant. All Rights Reserved.
================================================================================

                         Duration: ca. 6-8 minutes

                            INSTRUMENTATION:

                    Flute
                    Clarinet in Bb
                    Flugelhorn
                    Violin I
                    Violin II
                    Viola
                    Cello
                    Double Bass
                    Classical Guitar
                    Glockenspiel

================================================================================
"""
    filepath = os.path.join(base_path, "TitlePage.txt")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return filepath

def generate_movement_index(base_path):
    """Generate movement index content."""
    content = """================================================================================
                           THE MASTER'S PALETTE
                            Movement Index
================================================================================

MOVEMENT I — MINGUS BLUES CATHEDRAL
    Tempo: Quarter = 54 (Slow gospel blues, with fire)
    Duration: ca. 1:30
    Key Center: C minor / Blues
    Character: Earthy, spiritual, blues-cathedral grandeur
    Bars: 12
    Rehearsal Marks: A, B, C

MOVEMENT II — GIL'S CANVAS
    Tempo: Quarter = 58 (Floating, pastel clouds)
    Duration: ca. 1:30
    Key Center: Eb major / Lydian
    Character: Impressionistic, floating, ethereal
    Bars: 12
    Rehearsal Marks: D, E, F

MOVEMENT III — BARTÓK NIGHT
    Tempo: Quarter = 40 (Molto misterioso, nocturnal)
    Duration: ca. 2:00
    Key Center: A minor / Modal
    Character: Pointillistic, nocturnal, insect-like textures
    Bars: 12
    Rehearsal Marks: G, H, I

MOVEMENT IV — GERMAN DEVELOPMENT
    Tempo: Quarter = 66 (Streng, mit innerer Kraft)
    Duration: ca. 1:20
    Key Center: C major / Chromatic
    Character: Motivic development, Fortspinnung, Klangfarbenmelodie
    Bars: 12
    Rehearsal Marks: J, K, L

MOVEMENT V — TINTINNABULI EPILOGUE
    Tempo: Quarter = 52 (Serene, like a prayer)
    Duration: ca. 1:40
    Key Center: D minor / Aeolian
    Character: Transparent, prayer-like, transcendent
    Bars: 12
    Rehearsal Marks: M, N, O

================================================================================
                        TOTAL DURATION: ca. 8 minutes
================================================================================

                  © 2025 Michael Bryant. All Rights Reserved.
"""
    filepath = os.path.join(base_path, "MovementIndex.txt")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return filepath

def generate_program_notes(base_path):
    """Generate program notes content."""
    content = """================================================================================
                           THE MASTER'S PALETTE
                             Program Notes
================================================================================

"The Master's Palette" is a suite for hybrid chamber ensemble exploring five
distinct musical languages, each paying homage to a different compositional
tradition while maintaining a unified motivic and harmonic identity.

The work is scored for an unusual combination: winds (flute, clarinet,
flugelhorn), strings (two violins, viola, cello, double bass), classical
guitar, and glockenspiel. This instrumentation allows for a wide range of
timbral colors, from the warm intimacy of chamber music to the power of
orchestral writing.

--------------------------------------------------------------------------------
                              THE MOVEMENTS
--------------------------------------------------------------------------------

I. MINGUS BLUES CATHEDRAL

The opening movement draws inspiration from the visceral, gospel-inflected
jazz of Charles Mingus. The core motif (C-Eb-F-Bb-A-F-Eb) permeates the
texture, appearing in the flugelhorn and strings with characteristic blues
inflections. The harmony employs rich extended chords (9ths, 11ths, 13ths)
and polychordal structures that create a "cathedral" of sound above the
earthy blues foundation.


II. GIL'S CANVAS

Named for the legendary arranger Gil Evans, this movement floats in a world
of pastel harmonies and Lydian colors. The motif (G-A-B-F#-E-D) unfolds in
long, breathing phrases, supported by cloud-like voicings that emphasize
the #11 and major 9th colors Evans favored. The guitar provides shimmering
harmonic support while the strings create sustained curtains of sound.


III. BARTÓK NIGHT

The central movement evokes Bartók's "night music" style—sparse, pointillistic
textures alternating with sudden bursts of activity. The motif (A-Bb-E-B-F)
is fragmented and scattered across registers, creating an atmosphere of
nocturnal mystery. Quartal harmonies, chromatic clusters, and extended
techniques (harmonics, pizzicato) contribute to the unsettled, insect-like
quality of this movement.


IV. GERMAN DEVELOPMENT

This movement employs classical developmental techniques—Fortspinnung
(spinning out) and Klangfarbenmelodie (tone-color melody)—in a modern
context. The motif (C-D-E-G#-B-D) undergoes rigorous transformation:
inversion, augmentation, diminution, and sequential expansion. The melody
passes between instruments, creating a kaleidoscopic effect while
maintaining strict motivic integrity.


V. TINTINNABULI EPILOGUE

The finale draws on the Tintinnabuli style associated with Arvo Pärt.
A simple stepwise M-voice in D Aeolian is accompanied by a T-voice
outlining the D minor triad. The texture is deliberately sparse and
transparent, creating a sense of transcendence and resolution. The
glockenspiel provides crystalline highlights, while the strings sustain
pure triadic harmonies in their softest dynamics.

--------------------------------------------------------------------------------
                           PERFORMANCE NOTES
--------------------------------------------------------------------------------

- Dynamics should be carefully balanced to maintain clarity of the motivic
  material throughout.

- In Movement III, pauses and silences are as important as the notes;
  performers should embrace the negative space.

- The Tintinnabuli finale requires extreme patience and sustained
  concentration to achieve the desired ethereal quality.

- All movements should flow attacca or with minimal pause between them.

--------------------------------------------------------------------------------

                  © 2025 Michael Bryant. All Rights Reserved.
"""
    filepath = os.path.join(base_path, "ProgramNotes.txt")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return filepath

def generate_license(base_path):
    """Generate license content."""
    content = """================================================================================
                           THE MASTER'S PALETTE
                         License and Copyright
================================================================================

                COPYRIGHT NOTICE

    © 2025 Michael Bryant. All Rights Reserved.

--------------------------------------------------------------------------------

                TERMS OF USE

This musical score and all associated materials (parts, program notes,
recordings) are the exclusive property of Michael Bryant.

PERMITTED USES:
- Private study and practice
- Educational use with proper attribution
- Performance with written permission from the copyright holder
- Recording with written permission and appropriate licensing

PROHIBITED USES:
- Reproduction or distribution without written permission
- Commercial use without licensing agreement
- Modification or derivative works without permission
- Upload to public repositories without authorization

--------------------------------------------------------------------------------

                PERFORMANCE RIGHTS

For performance rights and licensing inquiries, please contact:

    Michael Bryant
    [Contact information to be added]

All performances must include proper attribution:
    "The Master's Palette" by Michael Bryant
    © 2025 Michael Bryant. All Rights Reserved.

--------------------------------------------------------------------------------

                PUBLISHER INFORMATION

    Self-published by the composer
    First Edition: December 2025

--------------------------------------------------------------------------------

                CATALOG INFORMATION

    Work Number: MB-2025-001
    ISMN: [To be assigned]
    Duration: ca. 8 minutes
    Difficulty: Advanced

================================================================================
              © 2025 Michael Bryant. All Rights Reserved.
================================================================================
"""
    filepath = os.path.join(base_path, "License.txt")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return filepath

def generate_parts_readme(base_path):
    """Generate readme for parts folder."""
    content = """================================================================================
                           THE MASTER'S PALETTE
                              Parts Folder
================================================================================

This folder should contain individual parts extracted from the full score.

REQUIRED PARTS:

    01_Flute.pdf
    02_Clarinet_in_Bb.pdf
    03_Flugelhorn.pdf
    04_Violin_I.pdf
    05_Violin_II.pdf
    06_Viola.pdf
    07_Cello.pdf
    08_Double_Bass.pdf
    09_Classical_Guitar.pdf
    10_Glockenspiel.pdf

--------------------------------------------------------------------------------

EXTRACTION INSTRUCTIONS:

1. Open Final-Suite-FullScore-Engraved.musicxml in Sibelius or Dorico
2. Use Layout > Extract Parts (or equivalent)
3. Apply professional part layout settings:
   - 2-4 bars per system
   - Multi-measure rests combined
   - Page turns at appropriate rests
   - Cue notes before entrances after long rests
4. Export each part as PDF
5. Name files according to the list above
6. Place all PDFs in this Parts folder

--------------------------------------------------------------------------------

PART-SPECIFIC NOTES:

- Clarinet: Written in Bb transposition
- Guitar: Written at sounding pitch (8va)
- Glockenspiel: Written at sounding pitch (sounds 2 octaves higher)

--------------------------------------------------------------------------------

              © 2025 Michael Bryant. All Rights Reserved.
================================================================================
"""
    filepath = os.path.join(base_path, "Parts", "README.txt")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return filepath

def generate_publication_readme(base_path):
    """Generate main readme for publication package."""
    content = """================================================================================
                           THE MASTER'S PALETTE
                    Suite for Hybrid Chamber Ensemble
                           Publication Package
================================================================================

                        © 2025 Michael Bryant
                         All Rights Reserved

================================================================================

PACKAGE CONTENTS:

    MastersPalette/
    +-- README.txt              (this file)
    +-- TitlePage.txt           (convert to PDF)
    +-- MovementIndex.txt       (convert to PDF)
    +-- ProgramNotes.txt        (convert to PDF)
    +-- License.txt             (convert to PDF)
    +-- Parts/
    |   +-- README.txt          (extraction instructions)
    +-- Source/
        +-- Final-Suite-FullScore-Engraved.musicxml

================================================================================

PDF GENERATION INSTRUCTIONS:

1. FULL SCORE:
   - Open Source/Final-Suite-FullScore-Engraved.musicxml in Sibelius
   - Review layout and spacing
   - Export as PDF: FullScore.pdf
   - Move to MastersPalette folder

2. PARTS:
   - Extract parts from the full score
   - Apply professional part layout
   - Export each as PDF
   - Place in Parts/ folder

3. DOCUMENTATION:
   - Convert each .txt file to PDF using preferred method
   - Maintain formatting and typography
   - Use consistent fonts (Times New Roman or similar)

================================================================================

INSTRUMENTATION:

    Woodwinds:
        Flute
        Clarinet in Bb
    
    Brass:
        Flugelhorn
    
    Strings:
        Violin I
        Violin II
        Viola
        Cello
        Double Bass
    
    Plucked:
        Classical Guitar
    
    Percussion:
        Glockenspiel

================================================================================

MOVEMENT STRUCTURE:

    I.   Mingus Blues Cathedral     q = 54    ca. 1:30
    II.  Gil's Canvas               q = 58    ca. 1:30
    III. Bartok Night               q = 40    ca. 2:00
    IV.  German Development         q = 66    ca. 1:20
    V.   Tintinnabuli Epilogue      q = 52    ca. 1:40
    
    Total Duration: ca. 8 minutes

================================================================================

CONTACT:

    Composer: Michael Bryant
    Year: 2025
    
    For performance rights, licensing, and inquiries:
    [Contact information to be added]

================================================================================
              © 2025 Michael Bryant. All Rights Reserved.
================================================================================
"""
    filepath = os.path.join(base_path, "README.txt")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return filepath

def copy_source_files(base_path, scores_dir):
    """Copy source MusicXML files to the package."""
    source_folder = os.path.join(base_path, "Source")
    
    # Copy the engraved full score
    source_file = os.path.join(scores_dir, "Final-Suite-FullScore-Engraved.musicxml")
    if os.path.exists(source_file):
        shutil.copy2(source_file, source_folder)
        return True
    return False

def main():
    print("=" * 70)
    print("PUBLICATION PACKAGE GENERATOR")
    print("The Master's Palette - Suite for Hybrid Chamber Ensemble")
    print("=" * 70)
    print()
    
    # Set up paths
    scripts_dir = os.path.dirname(__file__)
    project_dir = os.path.dirname(scripts_dir)
    scores_dir = os.path.join(project_dir, "scores")
    package_dir = os.path.join(scores_dir, "MastersPalette")
    
    print("Creating publication folder structure...")
    create_folder_structure(package_dir)
    print(f"  Created: {package_dir}")
    print()
    
    print("Generating publication documents...")
    
    # Generate all documents
    files_created = []
    
    filepath = generate_title_page(package_dir)
    files_created.append(("Title Page", filepath))
    print("  [OK] TitlePage.txt")
    
    filepath = generate_movement_index(package_dir)
    files_created.append(("Movement Index", filepath))
    print("  [OK] MovementIndex.txt")
    
    filepath = generate_program_notes(package_dir)
    files_created.append(("Program Notes", filepath))
    print("  [OK] ProgramNotes.txt")
    
    filepath = generate_license(package_dir)
    files_created.append(("License", filepath))
    print("  [OK] License.txt")
    
    filepath = generate_parts_readme(package_dir)
    files_created.append(("Parts README", filepath))
    print("  [OK] Parts/README.txt")
    
    filepath = generate_publication_readme(package_dir)
    files_created.append(("Main README", filepath))
    print("  [OK] README.txt")
    
    print()
    print("Copying source files...")
    if copy_source_files(package_dir, scores_dir):
        print("  [OK] Source/Final-Suite-FullScore-Engraved.musicxml")
    else:
        print("  [!] Source file not found - please copy manually")
    
    print()
    print("=" * 70)
    print("PUBLICATION PACKAGE COMPLETE")
    print("=" * 70)
    print()
    print(f"Location: {package_dir}")
    print()
    print("FOLDER STRUCTURE:")
    print()
    print("    MastersPalette/")
    print("    +-- README.txt")
    print("    +-- TitlePage.txt           -> Convert to TitlePage.pdf")
    print("    +-- MovementIndex.txt       -> Convert to MovementIndex.pdf")
    print("    +-- ProgramNotes.txt        -> Convert to ProgramNotes.pdf")
    print("    +-- License.txt             -> Convert to License.pdf")
    print("    +-- Parts/")
    print("    |   +-- README.txt          (extraction instructions)")
    print("    +-- Source/")
    print("        +-- Final-Suite-FullScore-Engraved.musicxml")
    print()
    print("NEXT STEPS:")
    print()
    print("  1. Open Source/Final-Suite-FullScore-Engraved.musicxml in Sibelius")
    print("  2. Export full score as FullScore.pdf")
    print("  3. Extract and export individual parts to Parts/ folder")
    print("  4. Convert .txt documents to .pdf")
    print("  5. Package complete!")
    print()
    print("COPYRIGHT: © 2025 Michael Bryant. All Rights Reserved.")
    print()

if __name__ == "__main__":
    main()

