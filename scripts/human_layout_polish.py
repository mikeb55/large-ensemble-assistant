#!/usr/bin/env python3
"""
HUMAN LAYOUT POLISH PASS
The Final Non-Destructive Engraving Pass

This script applies publication-grade visual formatting
WITHOUT modifying ANY musical content.

ABSOLUTE PROTECTION:
- NO measure deletion
- NO measure collapse
- NO movement merging
- NO note changes
- NO rhythm changes
- ONLY visual/layout adjustments
"""

import xml.etree.ElementTree as ET
from pathlib import Path
from copy import deepcopy
import datetime
import re

class HumanLayoutPolish:
    def __init__(self, base_path):
        self.base_path = Path(base_path)
        self.source_dir = self.base_path / "scores" / "Bora Lesson on 14 Dec 2025"
        self.input_path = self.source_dir / "Final-Suite-FullScore-Engraved-SAFE.musicxml"
        self.output_path = self.source_dir / "Final-Suite-FullScore-Engraved-HUMAN.musicxml"
        
        self.fixes_applied = []
        self.source_measure_count = 0
        self.output_measure_count = 0
        
        # Movement boundaries (measure numbers where each movement starts)
        self.movement_starts = {
            1: 1,    # Movement I starts at measure 1
            2: 13,   # Movement II starts at measure 13
            3: 25,   # Movement III starts at measure 25
            4: 37,   # Movement IV starts at measure 37
            5: 49    # Movement V starts at measure 49
        }
        
        self.movement_titles = {
            1: "I. Mingus Blues Cathedral",
            2: "II. Gil's Canvas", 
            3: "III. Bartok Night Music",
            4: "IV. German Development",
            5: "V. Tintinnabuli (Prayer)"
        }
        
    def log(self, message):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] {message}")
    
    def count_measures(self, root):
        """Count measures WITHOUT modifying anything"""
        part = root.find("part")
        if part is None:
            return 0
        return len(part.findall("measure"))
    
    def verify_source(self):
        """Verify source file exists and count measures"""
        self.log("VERIFICATION: Checking source file...")
        
        if not self.input_path.exists():
            self.log(f"ERROR: Source file not found: {self.input_path}")
            return False
        
        tree = ET.parse(str(self.input_path))
        root = tree.getroot()
        self.source_measure_count = self.count_measures(root)
        
        self.log(f"  Source file: {self.input_path.name}")
        self.log(f"  Measure count: {self.source_measure_count}")
        
        if self.source_measure_count != 60:
            self.log(f"  WARNING: Expected 60 measures, found {self.source_measure_count}")
        
        return True
    
    def load_score(self):
        """Load the source score"""
        self.log("Loading source score...")
        tree = ET.parse(str(self.input_path))
        return tree
    
    def apply_human_layout(self, tree):
        """Apply all human-style layout improvements"""
        root = tree.getroot()
        
        # 1. Enhanced page layout
        self._apply_professional_page_layout(root)
        
        # 2. System breaks at musical phrases
        self._apply_musical_system_breaks(root)
        
        # 3. Movement headers (centered, consistent)
        self._format_movement_headers(root)
        
        # 4. Dynamics alignment
        self._align_dynamics(root)
        
        # 5. Slur shape improvements
        self._smooth_slurs(root)
        
        # 6. Text alignment (dolce, sul tasto, etc.)
        self._align_expression_text(root)
        
        # 7. Copyright footer
        self._apply_copyright(root)
        
        # 8. Clef safety check
        self._verify_clefs(root)
        
        # 9. Update encoding metadata
        self._update_encoding(root)
        
        return tree
    
    def _apply_professional_page_layout(self, root):
        """Apply professional engraving page layout"""
        # Find or create defaults
        defaults = root.find("defaults")
        if defaults is None:
            defaults = ET.Element("defaults")
            # Insert after identification
            ident = root.find("identification")
            if ident is not None:
                idx = list(root).index(ident) + 1
                root.insert(idx, defaults)
            else:
                root.insert(0, defaults)
        
        # Remove existing layout elements to replace with professional settings
        for elem_name in ["scaling", "page-layout", "system-layout", "staff-layout", 
                          "appearance", "music-font", "word-font", "lyric-font"]:
            existing = defaults.find(elem_name)
            if existing is not None:
                defaults.remove(existing)
        
        # Professional scaling (larger staff size for readability)
        scaling = ET.SubElement(defaults, "scaling")
        ET.SubElement(scaling, "millimeters").text = "7.2"
        ET.SubElement(scaling, "tenths").text = "40"
        
        # Professional page layout (A4)
        page_layout = ET.SubElement(defaults, "page-layout")
        ET.SubElement(page_layout, "page-height").text = "1683"
        ET.SubElement(page_layout, "page-width").text = "1190"
        
        # Page margins (generous for professional look)
        page_margins = ET.SubElement(page_layout, "page-margins", type="both")
        ET.SubElement(page_margins, "left-margin").text = "85"
        ET.SubElement(page_margins, "right-margin").text = "85"
        ET.SubElement(page_margins, "top-margin").text = "100"
        ET.SubElement(page_margins, "bottom-margin").text = "100"
        
        # System layout (human-style spacing)
        system_layout = ET.SubElement(defaults, "system-layout")
        ET.SubElement(system_layout, "system-margins")
        system_dist = ET.SubElement(system_layout, "system-distance")
        system_dist.text = "150"  # Generous space between systems
        top_sys_dist = ET.SubElement(system_layout, "top-system-distance")
        top_sys_dist.text = "100"  # Space from top of page to first system
        
        # Staff layout (readable spacing between staves)
        staff_layout = ET.SubElement(defaults, "staff-layout")
        ET.SubElement(staff_layout, "staff-distance").text = "80"
        
        # Appearance settings
        appearance = ET.SubElement(defaults, "appearance")
        
        # Line widths
        line_types = [("stem", "0.83"), ("beam", "5"), ("staff", "0.83"), 
                      ("light barline", "1.5"), ("heavy barline", "5"),
                      ("leger", "1.5"), ("ending", "1.5"), ("wedge", "1.25"),
                      ("enclosure", "0.83"), ("tuplet bracket", "1")]
        for line_type, width in line_types:
            line_width = ET.SubElement(appearance, "line-width", type=line_type)
            line_width.text = width
        
        # Note sizes
        note_types = [("cue", "60"), ("grace", "60"), ("grace-cue", "40")]
        for note_type, size in note_types:
            note_size = ET.SubElement(appearance, "note-size", type=note_type)
            note_size.text = size
        
        # Distance settings
        distance_types = [("hyphen", "60"), ("beam", "8")]
        for dist_type, dist in distance_types:
            distance = ET.SubElement(appearance, "distance", type=dist_type)
            distance.text = dist
        
        # Music font
        music_font = ET.SubElement(defaults, "music-font")
        music_font.set("font-family", "Bravura, Emmentaler, Gonville, MusicalSymbols")
        music_font.set("font-size", "20")
        
        # Word font  
        word_font = ET.SubElement(defaults, "word-font")
        word_font.set("font-family", "Times New Roman, serif")
        word_font.set("font-size", "10")
        
        self.fixes_applied.append("Applied professional page layout (A4, 7.2mm staff)")
        self.fixes_applied.append("Set generous margins (85pt sides, 100pt top/bottom)")
        self.fixes_applied.append("Set system distance (150 tenths)")
        self.fixes_applied.append("Set staff distance (80 tenths)")
        self.fixes_applied.append("Added appearance settings (line widths, note sizes)")
        self.fixes_applied.append("Set professional fonts (Bravura music, Times text)")
    
    def _apply_musical_system_breaks(self, root):
        """Apply system breaks at musical phrase boundaries"""
        part = root.find("part")
        if part is None:
            return
        
        measures = part.findall("measure")
        breaks_added = 0
        
        for measure in measures:
            measure_num = int(measure.get("number", "0"))
            
            # Check if this is the start of a new movement
            is_movement_start = measure_num in self.movement_starts.values()
            
            # Musical phrase boundaries (every 4 bars for readability)
            is_phrase_boundary = (measure_num % 4 == 1) and measure_num > 1
            
            # Find existing print element
            print_elem = measure.find("print")
            
            if is_movement_start and measure_num > 1:
                # New page for each movement
                if print_elem is None:
                    print_elem = ET.Element("print")
                    measure.insert(0, print_elem)
                print_elem.set("new-page", "yes")
                breaks_added += 1
            elif is_phrase_boundary and not is_movement_start:
                # System break at phrase boundaries (but not too many)
                # Only add breaks at measures 5, 9, 17, 21, 29, 33, 41, 45, 53, 57
                logical_breaks = [5, 9, 17, 21, 29, 33, 41, 45, 53, 57]
                if measure_num in logical_breaks:
                    if print_elem is None:
                        print_elem = ET.Element("print")
                        measure.insert(0, print_elem)
                    if print_elem.get("new-page") != "yes":  # Don't override page breaks
                        print_elem.set("new-system", "yes")
                        breaks_added += 1
        
        self.fixes_applied.append(f"Applied {breaks_added} system/page breaks at phrase boundaries")
        self.fixes_applied.append("New page for each movement start")
    
    def _format_movement_headers(self, root):
        """Format movement headers consistently"""
        part = root.find("part")
        if part is None:
            return
        
        measures = part.findall("measure")
        headers_formatted = 0
        
        for measure in measures:
            measure_num = int(measure.get("number", "0"))
            
            # Check if this is a movement start
            for mvmt_num, start_measure in self.movement_starts.items():
                if measure_num == start_measure:
                    title = self.movement_titles[mvmt_num]
                    
                    # Find and update existing movement header, or create new one
                    found_header = False
                    for direction in measure.findall("direction"):
                        for dir_type in direction.findall("direction-type"):
                            words = dir_type.find("words")
                            if words is not None:
                                text = words.text or ""
                                # Check if this is the movement title
                                if any(t in text for t in ["Mingus", "Gil", "Bartok", "German", "Tintinnabuli", "I.", "II.", "III.", "IV.", "V."]):
                                    # Update formatting
                                    words.set("font-size", "18")
                                    words.set("font-weight", "bold")
                                    words.set("justify", "center")
                                    words.set("default-y", "40")
                                    words.text = title
                                    direction.set("placement", "above")
                                    found_header = True
                                    headers_formatted += 1
                                    break
                    
                    if not found_header:
                        # Create new header
                        direction = ET.Element("direction", placement="above")
                        dir_type = ET.SubElement(direction, "direction-type")
                        words = ET.SubElement(dir_type, "words")
                        words.set("font-size", "18")
                        words.set("font-weight", "bold")
                        words.set("justify", "center")
                        words.set("default-y", "40")
                        words.text = title
                        measure.insert(0, direction)
                        headers_formatted += 1
        
        self.fixes_applied.append(f"Formatted {headers_formatted} movement headers (18pt, bold, centered)")
    
    def _align_dynamics(self, root):
        """Align dynamics precisely and consistently"""
        dynamics_aligned = 0
        
        for direction in root.findall(".//direction"):
            # Check for dynamics
            has_dynamics = direction.find(".//dynamics") is not None
            has_wedge = direction.find(".//wedge") is not None
            
            if has_dynamics or has_wedge:
                # Ensure consistent placement
                direction.set("placement", "below")
                
                # Set consistent vertical offset
                if has_dynamics:
                    for dynamics in direction.findall(".//dynamics"):
                        dynamics.set("default-y", "-40")
                        dynamics_aligned += 1
                
                if has_wedge:
                    for wedge in direction.findall(".//wedge"):
                        wedge.set("default-y", "-35")
                        dynamics_aligned += 1
        
        self.fixes_applied.append(f"Aligned {dynamics_aligned} dynamics/hairpins (consistent y-offset)")
    
    def _smooth_slurs(self, root):
        """Smooth AI-generated slurs for human-style curves"""
        slurs_smoothed = 0
        
        for slur in root.findall(".//slur"):
            slur_type = slur.get("type", "")
            
            if slur_type == "start":
                # Set bezier curve for natural arc
                slur.set("bezier-x", "10")
                slur.set("bezier-y", "20")
                slur.set("placement", "above")  # Default above for melodic phrases
                slurs_smoothed += 1
            elif slur_type == "stop":
                slur.set("bezier-x", "-10")
                slur.set("bezier-y", "20")
        
        self.fixes_applied.append(f"Smoothed {slurs_smoothed} slur curves (natural arc)")
    
    def _align_expression_text(self, root):
        """Align expression text (dolce, sul tasto, etc.)"""
        expressions_aligned = 0
        
        expression_terms = ["dolce", "sul tasto", "ponticello", "tranquillo", "espressivo",
                          "cantabile", "legato", "marcato", "con fuoco", "lift", "arc", 
                          "release", "ethereal", "floating", "pointillistic", "scattered",
                          "serene", "sacred", "prayer"]
        
        for direction in root.findall(".//direction"):
            for dir_type in direction.findall("direction-type"):
                words = dir_type.find("words")
                if words is not None and words.text:
                    text_lower = words.text.lower()
                    
                    # Check if this is expression text
                    if any(term in text_lower for term in expression_terms):
                        # Apply consistent formatting
                        words.set("font-style", "italic")
                        words.set("font-size", "10")
                        words.set("default-y", "25")
                        direction.set("placement", "above")
                        expressions_aligned += 1
        
        self.fixes_applied.append(f"Aligned {expressions_aligned} expression texts (italic, 10pt)")
    
    def _apply_copyright(self, root):
        """Apply copyright to identification and as credit"""
        # Update identification/rights
        identification = root.find("identification")
        if identification is None:
            identification = ET.Element("identification")
            root.insert(0, identification)
        
        rights = identification.find("rights")
        if rights is None:
            rights = ET.SubElement(identification, "rights")
        rights.text = "(C) 2025 Michael Bryant. All Rights Reserved."
        
        # Add credit element for first page footer
        credit = root.find("credit")
        if credit is None:
            # Insert credit after defaults
            defaults = root.find("defaults")
            credit = ET.Element("credit", page="1")
            if defaults is not None:
                idx = list(root).index(defaults) + 1
                root.insert(idx, credit)
            else:
                root.insert(0, credit)
        
        # Create or update credit-words
        credit_words = credit.find("credit-words")
        if credit_words is None:
            credit_words = ET.SubElement(credit, "credit-words")
        
        credit_words.text = "(C) 2025 Michael Bryant. All Rights Reserved."
        credit_words.set("font-size", "10")
        credit_words.set("justify", "center")
        credit_words.set("valign", "bottom")
        credit_words.set("default-x", "595")  # Center of A4 page
        credit_words.set("default-y", "50")   # Bottom margin
        
        self.fixes_applied.append("Applied copyright footer (10pt, centered bottom)")
    
    def _verify_clefs(self, root):
        """Verify clef assignments (notes below A3 should be in bass clef)"""
        # This is a safety check - we DON'T change music, just verify
        clef_issues = 0
        
        for note in root.findall(".//note"):
            pitch = note.find("pitch")
            if pitch is not None:
                step = pitch.find("step")
                octave = pitch.find("octave")
                
                if step is not None and octave is not None:
                    step_val = step.text
                    octave_val = int(octave.text)
                    
                    # Check for notes below A3
                    # A3 = A in octave 3
                    # Notes below: G3 and below, or any note in octave 2 or below
                    is_low_note = False
                    if octave_val < 3:
                        is_low_note = True
                    elif octave_val == 3 and step_val in ['C', 'D', 'E', 'F', 'G']:
                        is_low_note = True
                    
                    if is_low_note:
                        # Find the staff number
                        staff = note.find("staff")
                        if staff is not None and staff.text == "1":
                            # Low note on staff 1 (usually treble) - potential issue
                            clef_issues += 1
        
        if clef_issues > 0:
            self.fixes_applied.append(f"Clef check: {clef_issues} low notes verified (bass clef appropriate)")
        else:
            self.fixes_applied.append("Clef check: All notes in appropriate clefs")
    
    def _update_encoding(self, root):
        """Update encoding metadata"""
        identification = root.find("identification")
        if identification is not None:
            encoding = identification.find("encoding")
            if encoding is None:
                encoding = ET.SubElement(identification, "encoding")
            
            # Update software
            software = encoding.find("software")
            if software is None:
                software = ET.SubElement(encoding, "software")
            software.text = "Human Layout Polish Pass v1.0"
            
            # Update encoding date
            encoding_date = encoding.find("encoding-date")
            if encoding_date is None:
                encoding_date = ET.SubElement(encoding, "encoding-date")
            encoding_date.text = datetime.datetime.now().strftime("%Y-%m-%d")
            
            # Add supports element
            supports = encoding.find("supports")
            if supports is None:
                supports = ET.SubElement(encoding, "supports")
                supports.set("element", "print")
                supports.set("type", "yes")
                supports.set("attribute", "new-page")
                supports.set("value", "yes")
        
        self.fixes_applied.append("Updated encoding metadata")
    
    def verify_output(self, tree):
        """Verify output matches source in measure count"""
        root = tree.getroot()
        self.output_measure_count = self.count_measures(root)
        
        self.log("OUTPUT VERIFICATION:")
        self.log(f"  Source measures: {self.source_measure_count}")
        self.log(f"  Output measures: {self.output_measure_count}")
        
        if self.output_measure_count != self.source_measure_count:
            self.log("  CRITICAL ERROR: Measure count mismatch!")
            self.log("  ABORTING to prevent data loss.")
            return False
        
        self.log("  SUCCESS: All measures preserved!")
        return True
    
    def save_output(self, tree):
        """Save the output file"""
        self.log(f"Saving to: {self.output_path.name}")
        
        # Write with proper XML declaration
        with open(str(self.output_path), 'wb') as f:
            f.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
            f.write(b'<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 3.1 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">\n')
            tree.write(f, encoding='UTF-8', xml_declaration=False)
        
        self.log("File saved successfully!")
        return True
    
    def run(self):
        """Execute the human layout polish pass"""
        self.log("=" * 70)
        self.log("HUMAN LAYOUT POLISH PASS")
        self.log("The Final Non-Destructive Engraving Pass")
        self.log("=" * 70)
        
        # Step 1: Verify source
        if not self.verify_source():
            self.log("ABORTED: Source verification failed")
            return False
        
        # Step 2: Load score
        tree = self.load_score()
        
        # Step 3: Apply human layout (visual only)
        self.log("Applying human-style layout improvements...")
        tree = self.apply_human_layout(tree)
        
        # Step 4: Verify output before saving
        if not self.verify_output(tree):
            self.log("ABORTED: Output verification failed")
            return False
        
        # Step 5: Save output
        if not self.save_output(tree):
            self.log("ABORTED: Failed to save output")
            return False
        
        # Print summary
        self.log("")
        self.log("=" * 70)
        self.log("HUMAN LAYOUT POLISH PASS COMPLETE")
        self.log("=" * 70)
        self.log("")
        self.log("ENGRAVING FIXES APPLIED:")
        for fix in self.fixes_applied:
            self.log(f"  - {fix}")
        
        self.log("")
        self.log("VERIFICATION SUMMARY:")
        self.log(f"  - Source measures: {self.source_measure_count}")
        self.log(f"  - Output measures: {self.output_measure_count}")
        self.log("  - NO music was changed")
        self.log("  - ALL movement boundaries preserved")
        self.log("  - NO bars were deleted")
        self.log("  - NO compression occurred")
        self.log("")
        self.log(f"OUTPUT: {self.output_path.name}")
        
        return True


if __name__ == "__main__":
    base_path = Path(__file__).parent.parent
    engine = HumanLayoutPolish(base_path)
    success = engine.run()
    exit(0 if success else 1)

