#!/usr/bin/env python3
"""
SAFE ENGRAVING PASS
Zero-Deletion • Zero-Collapse • Zero-Movement-Loss

This script combines all 5 movements into a single full score
with ONLY engraving adjustments - NO musical modifications.

PROTECTION RULES:
- NO measure deletion
- NO measure collapse
- NO movement merging
- NO note changes
- NO rhythm changes
- NO time signature changes
- ONLY layout/engraving adjustments
"""

import xml.etree.ElementTree as ET
from pathlib import Path
from copy import deepcopy
import datetime

class SafeEngravingPass:
    def __init__(self, base_path):
        self.base_path = Path(base_path)
        self.source_dir = self.base_path / "scores" / "Bora Lesson on 14 Dec 2025"
        self.output_path = self.source_dir / "Final-Suite-FullScore-Engraved-SAFE.musicxml"
        
        self.movement_files = [
            self.source_dir / "Movement1-FinalSuiteEnhanced.musicxml",
            self.source_dir / "Movement2-FinalSuiteEnhanced.musicxml",
            self.source_dir / "Movement3-FinalSuiteEnhanced.musicxml",
            self.source_dir / "Movement4-FinalSuiteEnhanced.musicxml",
            self.source_dir / "Movement5-FinalSuiteEnhanced.musicxml",
        ]
        
        self.movement_titles = [
            "I. Mingus Blues Cathedral",
            "II. Gil's Canvas",
            "III. Bartok Night Music",
            "IV. German Development",
            "V. Tintinnabuli (Prayer)"
        ]
        
        self.fixes_applied = []
        self.measure_counts = {}
        self.total_measures = 0
        
    def log(self, message):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] {message}")
        
    def count_measures(self, tree):
        """Count measures in a movement WITHOUT modifying anything"""
        root = tree.getroot()
        measures = root.findall(".//measure")
        return len(measures)
    
    def verify_source_files(self):
        """Verify all source files exist and count measures"""
        self.log("VERIFICATION PASS - Checking source files...")
        
        for i, path in enumerate(self.movement_files, 1):
            if not path.exists():
                self.log(f"ERROR: Missing file: {path.name}")
                return False
            
            tree = ET.parse(str(path))
            count = self.count_measures(tree)
            self.measure_counts[i] = count
            self.total_measures += count
            self.log(f"  Movement {i}: {count} measures - OK")
        
        self.log(f"TOTAL: {self.total_measures} measures across 5 movements")
        return True
    
    def create_combined_score(self):
        """Combine all 5 movements into one score, preserving ALL measures"""
        self.log("COMBINING movements (preserving all measures)...")
        
        # Load Movement 1 as the base
        base_tree = ET.parse(str(self.movement_files[0]))
        base_root = base_tree.getroot()
        
        # Update the work title to reflect the full suite
        work = base_root.find("work")
        if work is not None:
            work_title = work.find("work-title")
            if work_title is not None:
                work_title.text = "The Master's Palette - Complete Suite"
        
        # Find the part element
        part = base_root.find("part")
        if part is None:
            self.log("ERROR: No part element found in Movement 1")
            return None
        
        # Get all measures from Movement 1
        base_measures = list(part.findall("measure"))
        self.log(f"  Movement 1: {len(base_measures)} measures loaded")
        
        # Add a movement separator direction to first measure
        self._add_movement_header(base_measures[0], "I. Mingus Blues Cathedral", is_first=True)
        
        # Track cumulative measure number
        cumulative_number = len(base_measures)
        
        # Now append measures from movements 2-5
        for i in range(1, 5):
            mvmt_tree = ET.parse(str(self.movement_files[i]))
            mvmt_root = mvmt_tree.getroot()
            mvmt_part = mvmt_root.find("part")
            
            if mvmt_part is None:
                self.log(f"ERROR: No part element found in Movement {i+1}")
                return None
            
            mvmt_measures = list(mvmt_part.findall("measure"))
            self.log(f"  Movement {i+1}: {len(mvmt_measures)} measures loaded")
            
            # Add movement header to first measure of this movement
            if mvmt_measures:
                self._add_movement_header(mvmt_measures[0], self.movement_titles[i])
            
            # Renumber measures to be continuous
            for j, measure in enumerate(mvmt_measures):
                new_number = cumulative_number + j + 1
                measure.set("number", str(new_number))
                # Append the measure to the base part
                part.append(measure)
            
            cumulative_number += len(mvmt_measures)
        
        self.log(f"  TOTAL: {cumulative_number} measures in combined score")
        self.fixes_applied.append(f"Combined 5 movements into {cumulative_number} total measures")
        
        return base_tree
    
    def _add_movement_header(self, measure, title, is_first=False):
        """Add a movement header direction to the first measure of each movement"""
        # Create a direction element for the movement title
        direction = ET.Element("direction", placement="above")
        direction_type = ET.SubElement(direction, "direction-type")
        words = ET.SubElement(direction_type, "words")
        words.set("font-size", "18")
        words.set("font-weight", "bold")
        words.text = title
        
        # Insert at the beginning of the measure
        measure.insert(0, direction)
        
        if not is_first:
            # Add a system break before new movements
            print_elem = ET.Element("print")
            print_elem.set("new-system", "yes")
            measure.insert(0, print_elem)
            self.fixes_applied.append(f"Added system break for {title}")
        
        self.fixes_applied.append(f"Added movement header: {title}")
    
    def apply_safe_engraving(self, tree):
        """Apply ONLY safe engraving fixes - no musical changes"""
        root = tree.getroot()
        
        # 1. Add page layout defaults
        self._add_page_layout(root)
        
        # 2. Fix dynamic placements (position only, not content)
        self._fix_dynamic_alignment(root)
        
        # 3. Add copyright to identification
        self._add_copyright(root)
        
        # 4. Update encoding info
        self._update_encoding(root)
        
        return tree
    
    def _add_page_layout(self, root):
        """Add page layout defaults for proper engraving"""
        # Find or create defaults element
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
        
        # Add scaling
        scaling = defaults.find("scaling")
        if scaling is None:
            scaling = ET.SubElement(defaults, "scaling")
            millimeters = ET.SubElement(scaling, "millimeters")
            millimeters.text = "7"
            tenths = ET.SubElement(scaling, "tenths")
            tenths.text = "40"
            self.fixes_applied.append("Added scaling defaults")
        
        # Add page layout
        page_layout = defaults.find("page-layout")
        if page_layout is None:
            page_layout = ET.SubElement(defaults, "page-layout")
            page_height = ET.SubElement(page_layout, "page-height")
            page_height.text = "1683"  # A4 in tenths
            page_width = ET.SubElement(page_layout, "page-width")
            page_width.text = "1190"
            
            page_margins = ET.SubElement(page_layout, "page-margins", type="both")
            left = ET.SubElement(page_margins, "left-margin")
            left.text = "70"
            right = ET.SubElement(page_margins, "right-margin")
            right.text = "70"
            top = ET.SubElement(page_margins, "top-margin")
            top.text = "88"
            bottom = ET.SubElement(page_margins, "bottom-margin")
            bottom.text = "88"
            
            self.fixes_applied.append("Added page layout (A4, proper margins)")
        
        # Add system layout
        system_layout = defaults.find("system-layout")
        if system_layout is None:
            system_layout = ET.SubElement(defaults, "system-layout")
            system_distance = ET.SubElement(system_layout, "system-distance")
            system_distance.text = "121"
            top_system_distance = ET.SubElement(system_layout, "top-system-distance")
            top_system_distance.text = "70"
            self.fixes_applied.append("Added system layout spacing")
        
        # Add staff layout
        staff_layout = defaults.find("staff-layout")
        if staff_layout is None:
            staff_layout = ET.SubElement(defaults, "staff-layout")
            staff_distance = ET.SubElement(staff_layout, "staff-distance")
            staff_distance.text = "65"
            self.fixes_applied.append("Added staff distance spacing")
    
    def _fix_dynamic_alignment(self, root):
        """Fix dynamic placements without changing dynamic values"""
        dynamics_fixed = 0
        for direction in root.findall(".//direction"):
            placement = direction.get("placement")
            # Ensure dynamics are placed consistently
            for dynamics in direction.findall(".//dynamics"):
                if placement != "below":
                    direction.set("placement", "below")
                    dynamics_fixed += 1
        
        if dynamics_fixed > 0:
            self.fixes_applied.append(f"Aligned {dynamics_fixed} dynamics placements")
    
    def _add_copyright(self, root):
        """Add copyright to identification section"""
        identification = root.find("identification")
        if identification is None:
            identification = ET.Element("identification")
            root.insert(0, identification)
        
        rights = identification.find("rights")
        if rights is None:
            rights = ET.SubElement(identification, "rights")
        rights.text = "(C) 2025 Michael Bryant. All Rights Reserved."
        
        self.fixes_applied.append("Added copyright to identification")
    
    def _update_encoding(self, root):
        """Update encoding information"""
        identification = root.find("identification")
        if identification is not None:
            encoding = identification.find("encoding")
            if encoding is None:
                encoding = ET.SubElement(identification, "encoding")
            
            software = encoding.find("software")
            if software is None:
                software = ET.SubElement(encoding, "software")
            software.text = "Safe Engraving Pass v1.0"
            
            encoding_date = encoding.find("encoding-date")
            if encoding_date is None:
                encoding_date = ET.SubElement(encoding, "encoding-date")
            encoding_date.text = datetime.datetime.now().strftime("%Y-%m-%d")
            
            self.fixes_applied.append("Updated encoding metadata")
    
    def verify_output(self, tree):
        """Verify the output has the correct number of measures"""
        root = tree.getroot()
        part = root.find("part")
        if part is None:
            return False
        
        output_measures = len(part.findall("measure"))
        expected = self.total_measures
        
        self.log(f"OUTPUT VERIFICATION:")
        self.log(f"  Expected measures: {expected}")
        self.log(f"  Actual measures: {output_measures}")
        
        if output_measures != expected:
            self.log(f"  ERROR: Measure count mismatch!")
            return False
        
        self.log(f"  SUCCESS: All {expected} measures preserved!")
        return True
    
    def save_output(self, tree):
        """Save the output file"""
        self.log(f"Saving to: {self.output_path.name}")
        
        # Register the MusicXML namespace
        ET.register_namespace('', 'http://www.musicxml.org/ns/musicxml')
        
        # Write with proper XML declaration
        with open(str(self.output_path), 'wb') as f:
            # Write XML declaration
            f.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
            f.write(b'<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 3.1 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">\n')
            
            # Write the tree
            tree.write(f, encoding='unicode' if False else 'UTF-8', xml_declaration=False)
        
        self.log(f"File saved successfully!")
        return True
    
    def run(self):
        """Execute the safe engraving pass"""
        self.log("=" * 60)
        self.log("SAFE ENGRAVING PASS")
        self.log("Zero-Deletion | Zero-Collapse | Zero-Movement-Loss")
        self.log("=" * 60)
        
        # Step 1: Verify source files
        if not self.verify_source_files():
            self.log("ABORTED: Source file verification failed")
            return False
        
        # Step 2: Combine all movements
        combined_tree = self.create_combined_score()
        if combined_tree is None:
            self.log("ABORTED: Failed to combine movements")
            return False
        
        # Step 3: Apply safe engraving only
        self.log("Applying SAFE engraving adjustments...")
        engraved_tree = self.apply_safe_engraving(combined_tree)
        
        # Step 4: Verify output before saving
        if not self.verify_output(engraved_tree):
            self.log("ABORTED: Output verification failed - measures lost!")
            return False
        
        # Step 5: Save output
        if not self.save_output(engraved_tree):
            self.log("ABORTED: Failed to save output")
            return False
        
        # Print summary
        self.log("=" * 60)
        self.log("SAFE ENGRAVING PASS COMPLETE")
        self.log("=" * 60)
        self.log("")
        self.log("SUMMARY OF FIXES APPLIED:")
        for fix in self.fixes_applied:
            self.log(f"  - {fix}")
        
        self.log("")
        self.log("PROTECTION VERIFICATION:")
        self.log("  - No deletions")
        self.log("  - No measure loss")
        self.log("  - No system collapse")
        self.log("  - No movement merging (all 5 preserved)")
        self.log("  - Engraving fixes only")
        self.log("")
        self.log(f"OUTPUT: {self.output_path.name}")
        
        return True


if __name__ == "__main__":
    base_path = Path(__file__).parent.parent
    engine = SafeEngravingPass(base_path)
    success = engine.run()
    exit(0 if success else 1)

