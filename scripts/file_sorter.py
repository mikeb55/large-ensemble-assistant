#!/usr/bin/env python3
"""
FILE SORTER - MASTER SUITE ORGANIZER
Scans project and moves files to correct folders.
"""

import os
import shutil
import re

def get_unique_path(dest_path):
    """Get unique path by appending _v2, _v3, etc. if file exists."""
    if not os.path.exists(dest_path):
        return dest_path
    
    base, ext = os.path.splitext(dest_path)
    counter = 2
    while os.path.exists(f"{base}_v{counter}{ext}"):
        counter += 1
    return f"{base}_v{counter}{ext}"

def move_file(src, dest_folder, project_root):
    """Move file to destination folder, handling conflicts."""
    filename = os.path.basename(src)
    dest_path = os.path.join(project_root, dest_folder, filename)
    dest_path = get_unique_path(dest_path)
    
    try:
        shutil.move(src, dest_path)
        print(f"  {filename} -> {dest_folder}/")
        return True
    except Exception as e:
        print(f"  ERROR: {filename}: {e}")
        return False

def main():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    scores_dir = os.path.join(project_root, "scores")
    
    print("=" * 60)
    print("FILE SORTER - MASTER SUITE ORGANIZER")
    print("=" * 60)
    print()
    
    moved_count = 0
    
    # === MOVE MOVEMENT FILES ===
    print("Moving Movement files -> Movements/")
    if os.path.exists(scores_dir):
        for f in os.listdir(scores_dir):
            if f.endswith('.musicxml') or f.endswith('.sib'):
                if re.match(r'^Movement[1-5]', f, re.IGNORECASE):
                    src = os.path.join(scores_dir, f)
                    if os.path.isfile(src):
                        if move_file(src, "Movements", project_root):
                            moved_count += 1
    
    # === MOVE LEAD SHEETS ===
    print("\nMoving Lead Sheet files -> LeadSheets/")
    if os.path.exists(scores_dir):
        for f in os.listdir(scores_dir):
            if 'LeadSheet' in f or 'leadsheet' in f.lower():
                if f.endswith('.musicxml') or f.endswith('.sib') or f.endswith('.xml'):
                    src = os.path.join(scores_dir, f)
                    if os.path.isfile(src):
                        if move_file(src, "LeadSheets", project_root):
                            moved_count += 1
    
    # === MOVE FULL SCORES ===
    print("\nMoving Full Score files -> FullScore/")
    if os.path.exists(scores_dir):
        for f in os.listdir(scores_dir):
            if 'FullScore' in f or 'Full-Score' in f or 'Suite-Full' in f:
                if f.endswith('.musicxml') or f.endswith('.xml'):
                    src = os.path.join(scores_dir, f)
                    if os.path.isfile(src):
                        if move_file(src, "FullScore", project_root):
                            moved_count += 1
    
    # === MOVE PUBLICATION FILES ===
    print("\nMoving Publication files -> Publication/")
    masters_palette_pub = os.path.join(scores_dir, "MastersPalette")
    if os.path.exists(masters_palette_pub):
        for f in os.listdir(masters_palette_pub):
            src = os.path.join(masters_palette_pub, f)
            if os.path.isfile(src):
                if move_file(src, "Publication", project_root):
                    moved_count += 1
        # Move Source folder contents
        source_dir = os.path.join(masters_palette_pub, "Source")
        if os.path.exists(source_dir):
            for f in os.listdir(source_dir):
                src = os.path.join(source_dir, f)
                if os.path.isfile(src):
                    if move_file(src, "FullScore", project_root):
                        moved_count += 1
        # Move Parts folder contents
        parts_dir = os.path.join(masters_palette_pub, "Parts")
        if os.path.exists(parts_dir):
            for f in os.listdir(parts_dir):
                src = os.path.join(parts_dir, f)
                if os.path.isfile(src):
                    if move_file(src, "Publication/Parts-PDF", project_root):
                        moved_count += 1
    
    # === MOVE AUDIO FILES ===
    print("\nMoving Audio files -> AudioMockups/")
    for root, dirs, files in os.walk(project_root):
        # Skip target directories
        if any(skip in root for skip in ['AudioMockups', 'Movements', 'LeadSheets', 'FullScore', 'Parts', 'Publication', 'Logs']):
            continue
        for f in files:
            if f.endswith('.wav') or f.endswith('.mp3') or f.endswith('.ogg'):
                src = os.path.join(root, f)
                if move_file(src, "AudioMockups", project_root):
                    moved_count += 1
    
    # === MOVE LOG FILES ===
    print("\nMoving Log files -> Logs/")
    for root, dirs, files in os.walk(project_root):
        if 'Logs' in root:
            continue
        for f in files:
            if f.endswith('.log') or 'refinement' in f.lower() or 'cycle' in f.lower():
                if 'cursor' in f.lower() or f.endswith('.log'):
                    src = os.path.join(root, f)
                    if os.path.isfile(src):
                        if move_file(src, "Logs", project_root):
                            moved_count += 1
    
    print()
    print("=" * 60)
    print(f"SORTING COMPLETE - {moved_count} files moved")
    print("=" * 60)

if __name__ == "__main__":
    main()


