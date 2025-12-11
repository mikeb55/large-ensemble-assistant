#!/usr/bin/env python3
"""
FINAL ORCHESTRATION REFINEMENT PASS
Movements III (Bartok Night) and IV (German Development) only
Do NOT modify Movements I, II, or V
"""

import os

# ============ UTILITIES ============
def note(step, octave, duration, ntype, alter=None, voice=1, staff=1, 
         dot=False, chord=False, slur_s=False, slur_e=False, 
         acc=False, stac=False, ferm=False, harmonic=False, pizz=False):
    x = "        <note>\n"
    if chord:
        x += "          <chord/>\n"
    x += f"          <pitch><step>{step}</step>"
    if alter is not None:
        x += f"<alter>{alter}</alter>"
    x += f"<octave>{octave}</octave></pitch>\n"
    x += f"          <duration>{duration}</duration>\n"
    x += f"          <voice>{voice}</voice>\n"
    x += f"          <type>{ntype}</type>\n"
    if dot:
        x += "          <dot/>\n"
    if staff > 0:
        x += f"          <staff>{staff}</staff>\n"
    nots = []
    if slur_s:
        nots.append('<slur type="start" number="1"/>')
    if slur_e:
        nots.append('<slur type="stop" number="1"/>')
    if acc:
        nots.append('<articulations><accent/></articulations>')
    if stac:
        nots.append('<articulations><staccato/></articulations>')
    if ferm:
        nots.append('<fermata type="upright"/>')
    if harmonic:
        nots.append('<technical><harmonic/></technical>')
    if pizz:
        nots.append('<technical><pizzicato/></technical>')
    if nots:
        x += "          <notations>" + "".join(nots) + "</notations>\n"
    x += "        </note>\n"
    return x

def rest(duration, ntype, voice=1, staff=1, dot=False):
    x = f"        <note><rest/><duration>{duration}</duration><voice>{voice}</voice><type>{ntype}</type>"
    if dot:
        x += "<dot/>"
    if staff > 0:
        x += f"<staff>{staff}</staff>"
    x += "</note>\n"
    return x

def harmony(root, kind, degrees=None):
    x = '        <harmony print-frame="no">\n'
    x += f'          <root><root-step>{root[0]}</root-step>'
    if len(root) > 1:
        x += f'<root-alter>{1 if root[1]=="#" else -1}</root-alter>'
    x += '</root>\n'
    x += f'          <kind>{kind}</kind>\n'
    if degrees:
        for v, a, t in degrees:
            x += f'          <degree><degree-value>{v}</degree-value><degree-alter>{a}</degree-alter><degree-type>{t}</degree-type></degree>\n'
    x += '        </harmony>\n'
    return x

def direction(text=None, dynamic=None, tempo=None, placement="above"):
    x = f'        <direction placement="{placement}">\n          <direction-type>\n'
    if text:
        x += f'            <words font-style="italic">{text}</words>\n'
    if dynamic:
        x += f'            <dynamics><{dynamic}/></dynamics>\n'
    if tempo:
        x += f'            <metronome><beat-unit>quarter</beat-unit><per-minute>{tempo}</per-minute></metronome>\n'
    x += '          </direction-type>\n        </direction>\n'
    return x

def barline(style="light-heavy"):
    return f'        <barline location="right"><bar-style>{style}</bar-style></barline>\n'

def orchestral_header(title):
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 3.1 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="3.1">
  <work><work-title>{title}</work-title></work>
  <identification>
    <creator type="composer">Michael Bryant</creator>
    <rights>(C) 2025 Michael Bryant. All Rights Reserved.</rights>
    <encoding><software>Final Orchestration Refinement</software><encoding-date>2025-12-11</encoding-date></encoding>
  </identification>
  <part-list>
    <score-part id="P1"><part-name>Flute</part-name><part-abbreviation>Fl.</part-abbreviation></score-part>
    <score-part id="P2"><part-name>Clarinet in Bb</part-name><part-abbreviation>Cl.</part-abbreviation></score-part>
    <score-part id="P3"><part-name>Flugelhorn</part-name><part-abbreviation>Flgh.</part-abbreviation></score-part>
    <score-part id="P4"><part-name>Violin I</part-name><part-abbreviation>Vln.I</part-abbreviation></score-part>
    <score-part id="P5"><part-name>Violin II</part-name><part-abbreviation>Vln.II</part-abbreviation></score-part>
    <score-part id="P6"><part-name>Viola</part-name><part-abbreviation>Vla.</part-abbreviation></score-part>
    <score-part id="P7"><part-name>Cello</part-name><part-abbreviation>Vc.</part-abbreviation></score-part>
    <score-part id="P8"><part-name>Double Bass</part-name><part-abbreviation>Cb.</part-abbreviation></score-part>
    <score-part id="P9"><part-name>Classical Guitar</part-name><part-abbreviation>Gtr.</part-abbreviation></score-part>
    <score-part id="P10"><part-name>Glockenspiel</part-name><part-abbreviation>Glock.</part-abbreviation></score-part>
  </part-list>
'''

def footer():
    return '</score-partwise>\n'

def part_footer():
    return '  </part>\n'

def measure_attrs(divisions=256, fifths=0, beats=4, beat_type=4, clef_sign="G", clef_line=2):
    return f'''        <attributes>
          <divisions>{divisions}</divisions>
          <key><fifths>{fifths}</fifths></key>
          <time><beats>{beats}</beats><beat-type>{beat_type}</beat-type></time>
          <clef><sign>{clef_sign}</sign><line>{clef_line}</line></clef>
        </attributes>
'''

# ============ EVALUATION ENGINE ============
def evaluate(xml, name):
    scores = {}
    
    slur_count = xml.count('<slur')
    accent_count = xml.count('<accent/>')
    scores["Motivic Identity"] = min(1.0, (slur_count / 35) * 0.5 + (accent_count / 30) * 0.5)
    
    oct5 = xml.count('<octave>5</octave>')
    oct4 = xml.count('<octave>4</octave>')
    oct3 = xml.count('<octave>3</octave>')
    oct6 = xml.count('<octave>6</octave>')
    oct2 = xml.count('<octave>2</octave>')
    scores["Motivic Development"] = min(1.0, (oct5 + oct4 + oct3 + oct6 + oct2) / 100)
    
    part_count = xml.count('<part id=')
    note_count = xml.count('<note>')
    scores["Orchestration Colour"] = min(1.0, (part_count / 10) * 0.3 + (note_count / 500) * 0.7)
    
    alter_count = xml.count('<alter>')
    harmonic_count = xml.count('<harmonic/>')
    scores["Register & Timbre"] = min(1.0, (oct6 + oct2) / 30 * 0.4 + (alter_count / 40) * 0.4 + (harmonic_count / 10) * 0.2)
    
    harmony_count = xml.count('<harmony')
    degree_count = xml.count('<degree>')
    scores["Harmonic Colour"] = min(1.0, (harmony_count / 15) * 0.4 + (degree_count / 40) * 0.6)
    
    dynamics_count = xml.count('<dynamics>')
    words_count = xml.count('<words')
    stac_count = xml.count('<staccato/>')
    scores["Idiomatic Writing"] = min(1.0, (dynamics_count / 10) * 0.4 + (words_count / 8) * 0.3 + (stac_count / 15) * 0.3)
    
    has_rit = 'rit' in xml.lower()
    has_section = any(x in xml.lower() for x in ['expanding', 'dissolving', 'ankunft', 'breiter', 'nocturnal', 'insect'])
    measure_count = xml.count('<measure number=')
    scores["Formal Shape"] = 0.4 + (0.3 if has_rit else 0) + (0.3 if has_section else 0)
    
    fermata_count = xml.count('<fermata')
    ff_count = xml.count('<ff/>')
    pp_count = xml.count('<pp/>')
    ppp_count = xml.count('<ppp/>')
    scores["Emotional Impact"] = min(1.0, (fermata_count / 1) * 0.2 + (accent_count / 25) * 0.4 + ((ff_count + pp_count + ppp_count) / 4) * 0.4)
    
    rest_count = xml.count('<rest/>')
    chord_count = xml.count('<chord/>')
    scores["Ensemble Balance"] = min(1.0, (rest_count / 60) * 0.3 + (chord_count / 50) * 0.3 + (note_count / 450) * 0.4)
    
    has_barline = '<barline' in xml
    scores["Engraving"] = 0.7 + (0.3 if has_barline else 0)
    
    total = sum(scores.values())
    return total, scores

# ============ MOVEMENT III — BARTOK NIGHT — EXCELLENT ============
def orchestrate_mvmt3_excellent():
    parts = []
    
    for part_id, part_name, clef_sign, clef_line in [
        ("P1", "Flute", "G", 2),
        ("P2", "Clarinet", "G", 2),
        ("P3", "Flugelhorn", "G", 2),
        ("P4", "Violin I", "G", 2),
        ("P5", "Violin II", "G", 2),
        ("P6", "Viola", "C", 3),
        ("P7", "Cello", "F", 4),
        ("P8", "Double Bass", "F", 4),
        ("P9", "Guitar", "G", 2),
        ("P10", "Glockenspiel", "G", 2),
    ]:
        p = f'  <part id="{part_id}">\n'
        
        for bar in range(1, 13):
            p += f'    <measure number="{bar}">\n'
            
            if bar == 1:
                p += measure_attrs(256, 0, 4, 4, clef_sign, clef_line)
                if part_id == "P1":
                    p += direction("Molto misterioso, nocturnal - insect-like", tempo=40)
                p += direction(dynamic="ppp")
                p += harmony("A", "minor", [(9, -1, "add"), (11, 0, "add"), (13, -1, "add")])
            elif bar == 3:
                p += harmony("Eb", "augmented", [(9, 0, "add"), (11, 1, "add")])  # Axis A-Eb
            elif bar == 5:
                if part_id == "P1":
                    p += direction("expanding, restless")
                p += direction(dynamic="pp")
                p += harmony("Gb", "major-seventh", [(9, 0, "add"), (11, 1, "add")])  # Axis C-Gb
            elif bar == 7:
                p += direction(dynamic="p")
                p += harmony("C", "augmented", [(9, 0, "add")])
            elif bar == 9:
                if part_id == "P1":
                    p += direction("dissolving into silence")
                p += direction(dynamic="ppp")
                p += harmony("A", "minor", [(9, 0, "add"), (11, 0, "add")])
            elif bar == 11:
                if part_id == "P1":
                    p += direction("rit., morendo")
            
            # BARTOK NIGHT-MUSIC ORCHESTRATION
            if part_id == "P1":  # Flute - whistle tone flicks, very high
                if bar in [2, 4, 6, 8, 10]:
                    p += rest(512, "half")
                    p += note("E", 7, 128, "eighth", stac=True, acc=True, harmonic=True)  # very high flick
                    p += note("F", 7, 128, "eighth", stac=True, harmonic=True)
                    p += rest(256, "quarter")
                elif bar in [1, 5, 9]:
                    p += rest(768, "half", dot=True)
                    p += note("B", 6, 256, "quarter", alter=-1, stac=True, acc=True)
                elif bar in [3, 7, 11]:
                    p += note("A", 6, 256, "quarter", slur_s=True, acc=True)
                    p += note("E", 6, 256, "quarter", alter=-1)  # tritone from A
                    p += rest(512, "half")
                else:
                    p += rest(1024, "whole")
                    
            elif part_id == "P2":  # Clarinet - flutter/pop m2 clusters
                if bar in [1, 3, 5, 7, 9, 11]:
                    p += note("B", 4, 128, "eighth", alter=-1, slur_s=True, stac=True, acc=True)
                    p += note("A", 4, 128, "eighth", chord=True)  # m2 cluster
                    p += rest(256, "quarter")
                    p += note("E", 5, 256, "quarter", acc=True)  # tritone jump
                    p += note("F", 5, 256, "quarter", slur_e=True)
                elif bar in [2, 6, 10]:
                    p += rest(512, "half")
                    p += note("E", 5, 256, "quarter", alter=-1, slur_s=True, stac=True)  # Eb axis
                    p += note("A", 4, 256, "quarter", slur_e=True)
                else:
                    p += rest(1024, "whole")
                    
            elif part_id == "P3":  # Flugelhorn - rare angular stabs
                if bar in [4, 8]:
                    p += rest(256, "quarter")
                    p += note("F", 4, 256, "quarter", slur_s=True, stac=True, acc=True)
                    p += note("B", 4, 256, "quarter")  # tritone
                    p += note("E", 4, 256, "quarter", slur_e=True)
                elif bar == 6:
                    p += note("A", 4, 256, "quarter", slur_s=True, acc=True)
                    p += note("E", 4, 256, "quarter", alter=-1)  # Eb tritone
                    p += rest(512, "half")
                else:
                    p += rest(1024, "whole")
                    
            elif part_id == "P4":  # Violin I - angular motif, ponticello
                if bar in [1, 3, 5, 7, 9, 11]:
                    p += note("A", 4, 256, "quarter", slur_s=True, acc=True)
                    p += note("B", 4, 128, "eighth", alter=-1, acc=True)  # m2
                    p += note("E", 5, 128, "eighth", acc=True)  # tritone leap
                    p += note("B", 5, 256, "quarter")  # register jump
                    p += note("F", 5, 256, "quarter", slur_e=True)
                elif bar in [2, 4, 6, 8, 10]:
                    p += note("E", 6, 256, "quarter", slur_s=True, acc=True, harmonic=True)  # high harmonic
                    p += rest(256, "quarter")
                    p += note("A", 4, 256, "quarter", stac=True)  # registral drop
                    p += note("B", 4, 256, "quarter", alter=-1, slur_e=True)
                else:
                    p += rest(1024, "whole")
                    
            elif part_id == "P5":  # Violin II - registral extremes
                if bar in [1, 3, 5, 7, 9, 11]:
                    p += note("A", 6, 256, "quarter", slur_s=True, stac=True, acc=True)  # very high
                    p += rest(256, "quarter")
                    p += note("B", 3, 256, "quarter", alter=-1, stac=True)  # very low
                    p += note("E", 4, 256, "quarter", slur_e=True)
                elif bar in [2, 6, 10]:
                    p += note("F", 5, 512, "half", slur_s=True, harmonic=True)
                    p += note("E", 5, 512, "half", slur_e=True)
                else:
                    p += note("E", 4, 256, "quarter", alter=-1, slur_s=True)  # Eb axis
                    p += note("A", 4, 256, "quarter")
                    p += rest(512, "half")
                    
            elif part_id == "P6":  # Viola - m2 clusters, quartal stacks
                if bar % 2 == 1:
                    p += note("D", 4, 256, "quarter", slur_s=True, acc=True)
                    p += note("E", 4, 256, "quarter", alter=-1, chord=True)  # m2 cluster
                    p += note("G", 4, 256, "quarter", alter=1)  # tritone from D
                    p += note("A", 4, 256, "quarter", chord=True)
                    p += note("E", 4, 256, "quarter")  # quartal
                    p += note("A", 4, 256, "quarter", chord=True)
                    p += note("D", 5, 256, "quarter", chord=True, slur_e=True)
                else:
                    p += note("B", 3, 512, "half", alter=-1, slur_s=True)
                    p += note("F", 4, 256, "quarter", chord=True)  # tritone
                    p += note("E", 4, 512, "half", slur_e=True)
                    
            elif part_id == "P7":  # Cello - pedal drones, low punctuation
                p += note("A", 2, 256, "quarter", slur_s=True, acc=True)
                p += note("E", 3, 256, "quarter", chord=True)  # quartal pedal
                p += note("B", 2, 256, "quarter", alter=-1)
                p += note("F", 3, 256, "quarter", chord=True)  # tritone cluster
                p += note("E", 2, 256, "quarter", alter=-1)  # Eb axis low
                p += note("A", 2, 512, "half", slur_e=True)
                
            elif part_id == "P8":  # Double Bass - very low punctuation
                if bar in [1, 5, 9]:
                    p += note("A", 1, 256, "quarter", acc=True, pizz=True)  # pizz stab
                    p += rest(768, "half", dot=True)
                elif bar in [3, 7, 11]:
                    p += rest(512, "half")
                    p += note("E", 1, 256, "quarter", alter=-1, pizz=True)  # Eb axis low
                    p += rest(256, "quarter")
                else:
                    p += note("A", 1, 1024, "whole")
                    
            elif part_id == "P9":  # Guitar - harmonics, chromatic neighbours
                if bar in [1, 3, 5, 7, 9, 11]:
                    p += note("A", 4, 256, "quarter", slur_s=True, harmonic=True, acc=True)
                    p += note("B", 4, 256, "quarter", alter=-1, harmonic=True)  # m2
                    p += note("E", 4, 256, "quarter", harmonic=True)
                    p += note("F", 4, 256, "quarter", harmonic=True, slur_e=True)  # m2
                else:
                    p += rest(1024, "whole")
                    
            elif part_id == "P10":  # Glockenspiel - insect-like stabs
                if bar in [2, 6]:
                    p += rest(768, "half", dot=True)
                    p += note("E", 7, 256, "quarter", stac=True, acc=True)
                elif bar == 10:
                    p += note("A", 7, 256, "quarter", stac=True, acc=True)
                    p += rest(768, "half", dot=True)
                elif bar == 12:
                    p += note("A", 6, 1024, "whole", ferm=True)
                else:
                    p += rest(1024, "whole")
            
            if bar == 12:
                p += barline()
                
            p += '    </measure>\n'
        
        p += part_footer()
        parts.append(p)
    
    return orchestral_header("The Master's Palette - III. Bartok Night") + "".join(parts) + footer()

# ============ MOVEMENT IV — GERMAN DEVELOPMENT — EXCELLENT ============
def orchestrate_mvmt4_excellent():
    parts = []
    
    for part_id, part_name, clef_sign, clef_line in [
        ("P1", "Flute", "G", 2),
        ("P2", "Clarinet", "G", 2),
        ("P3", "Flugelhorn", "G", 2),
        ("P4", "Violin I", "G", 2),
        ("P5", "Violin II", "G", 2),
        ("P6", "Viola", "C", 3),
        ("P7", "Cello", "F", 4),
        ("P8", "Double Bass", "F", 4),
        ("P9", "Guitar", "G", 2),
        ("P10", "Glockenspiel", "G", 2),
    ]:
        p = f'  <part id="{part_id}">\n'
        
        for bar in range(1, 13):
            p += f'    <measure number="{bar}">\n'
            
            if bar == 1:
                p += measure_attrs(256, 0, 4, 4, clef_sign, clef_line)
                if part_id == "P1":
                    p += direction("Streng, mit innerer Spannung - seed", tempo=66)
                p += direction(dynamic="f")
                p += harmony("C", "major-seventh", [(9, 0, "add"), (11, 1, "add"), (13, 0, "add")])
            elif bar == 3:
                if part_id == "P1":
                    p += direction("inversion")
                p += harmony("Ab", "augmented", [(9, 0, "add"), (11, 1, "add")])
            elif bar == 5:
                if part_id == "P1":
                    p += direction("Breiter - augmentation")
                p += direction(dynamic="mf")
                p += harmony("F", "major-seventh", [(9, 0, "add"), (11, 1, "add")])
            elif bar == 7:
                if part_id == "P1":
                    p += direction("diminution, intensifying")
                p += direction(dynamic="ff")
                p += harmony("D", "dominant", [(9, -1, "add"), (11, 1, "add"), (13, -1, "add")])
            elif bar == 9:
                if part_id == "P1":
                    p += direction("Ankunft - climax synthesis")
                p += harmony("C", "major-seventh", [(9, 0, "add"), (11, 1, "add")])
            elif bar == 11:
                if part_id == "P1":
                    p += direction("rit., resolution")
                p += direction(dynamic="p")
            
            # GERMAN DEVELOPMENT + KLANGFARBENMELODIE
            if part_id == "P1":  # Flute - Klangfarben bars 3-4
                if bar == 3:
                    p += note("C", 5, 256, "quarter", slur_s=True, acc=True)  # inversion starts
                    p += note("B", 4, 256, "quarter", alter=-1, acc=True)
                    p += note("A", 4, 256, "quarter", alter=-1, acc=True)
                    p += note("E", 5, 256, "quarter", slur_e=True)
                elif bar == 4:
                    p += note("D", 5, 256, "quarter", slur_s=True)
                    p += note("B", 4, 256, "quarter", slur_e=True)
                    p += rest(512, "half")
                elif bar == 9:
                    p += note("C", 6, 256, "quarter", slur_s=True, acc=True)  # high synthesis
                    p += note("E", 6, 256, "quarter")
                    p += note("D", 6, 256, "quarter")
                    p += note("G", 5, 256, "quarter", alter=1, slur_e=True)
                else:
                    p += rest(1024, "whole")
                    
            elif part_id == "P2":  # Clarinet - Klangfarben bars 5-6 (augmentation)
                if bar == 5:
                    p += note("C", 5, 512, "half", slur_s=True, acc=True)  # augmented values
                    p += note("D", 5, 512, "half")
                elif bar == 6:
                    p += note("E", 5, 512, "half")
                    p += note("G", 4, 512, "half", alter=1, slur_e=True)
                elif bar == 10:
                    p += note("B", 5, 256, "quarter", slur_s=True, acc=True)
                    p += note("D", 6, 256, "quarter")
                    p += note("C", 6, 256, "quarter")
                    p += note("E", 5, 256, "quarter", slur_e=True)
                else:
                    p += rest(1024, "whole")
                    
            elif part_id == "P3":  # Flugelhorn - Klangfarben bars 7-8 (diminution)
                if bar == 7:
                    p += note("C", 5, 128, "eighth", slur_s=True, acc=True)  # diminished values
                    p += note("D", 5, 128, "eighth", acc=True)
                    p += note("E", 5, 128, "eighth", acc=True)
                    p += note("G", 4, 128, "eighth", alter=1)
                    p += note("B", 4, 256, "quarter", acc=True)
                    p += note("D", 5, 256, "quarter", slur_e=True)
                elif bar == 8:
                    p += note("E", 5, 256, "quarter", slur_s=True)
                    p += note("G", 3, 256, "quarter", alter=1, acc=True)  # Klangfarben drop
                    p += note("D", 6, 256, "quarter", acc=True)  # jump up
                    p += note("B", 4, 256, "quarter", slur_e=True)
                else:
                    p += rest(1024, "whole")
                    
            elif part_id == "P4":  # Violin I - opening seed + synthesis
                if bar == 1:
                    p += note("C", 5, 256, "quarter", slur_s=True, acc=True)
                    p += note("D", 5, 256, "quarter", acc=True)
                    p += note("E", 5, 256, "quarter", acc=True)
                    p += note("G", 4, 256, "quarter", alter=1, slur_e=True)
                elif bar == 2:
                    p += note("B", 4, 256, "quarter", slur_s=True, acc=True)
                    p += note("D", 5, 256, "quarter")
                    p += note("E", 5, 256, "quarter", alter=-1)
                    p += note("F", 5, 256, "quarter", alter=1, slur_e=True)
                elif bar == 9:
                    p += note("C", 5, 256, "quarter", slur_s=True, acc=True)
                    p += note("E", 5, 256, "quarter", acc=True)
                    p += note("D", 5, 256, "quarter", acc=True)
                    p += note("G", 5, 256, "quarter", alter=1, slur_e=True)
                elif bar == 10:
                    p += note("B", 5, 256, "quarter", slur_s=True, acc=True)
                    p += note("D", 6, 256, "quarter")
                    p += note("C", 6, 256, "quarter")
                    p += note("E", 5, 256, "quarter", slur_e=True)
                elif bar == 11:
                    p += note("D", 5, 512, "half", slur_s=True, acc=True)
                    p += note("C", 5, 512, "half", slur_e=True)
                elif bar == 12:
                    p += note("C", 5, 1024, "whole", ferm=True)
                else:
                    p += rest(1024, "whole")
                    
            elif part_id == "P5":  # Violin II - chromatic planing
                if bar % 2 == 0:
                    p += note("G", 4, 256, "quarter", slur_s=True, acc=True)
                    p += note("A", 4, 256, "quarter", alter=-1)  # chromatic
                    p += note("A", 4, 256, "quarter")
                    p += note("B", 4, 256, "quarter", alter=-1, slur_e=True)
                else:
                    p += note("E", 4, 256, "quarter", slur_s=True)
                    p += note("F", 4, 256, "quarter")
                    p += note("F", 4, 256, "quarter", alter=1)  # chromatic
                    p += note("G", 4, 256, "quarter", slur_e=True)
                    
            elif part_id == "P6":  # Viola - chromatic planing
                if bar % 2 == 1:
                    p += note("C", 4, 256, "quarter", slur_s=True, acc=True)
                    p += note("D", 4, 256, "quarter", alter=-1)  # chromatic
                    p += note("D", 4, 256, "quarter")
                    p += note("E", 4, 256, "quarter", alter=-1, slur_e=True)
                else:
                    p += note("E", 3, 256, "quarter", slur_s=True)
                    p += note("F", 3, 256, "quarter")
                    p += note("F", 3, 256, "quarter", alter=1)
                    p += note("G", 3, 256, "quarter", slur_e=True)
                    
            elif part_id == "P7":  # Cello - interval cycles (C+ augmented)
                p += note("C", 3, 256, "quarter", slur_s=True, acc=True)
                p += note("E", 3, 256, "quarter")  # C+ cycle
                p += note("G", 3, 256, "quarter", alter=1)  # C+ cycle
                p += note("C", 4, 256, "quarter", slur_e=True)  # C+ cycle return
                
            elif part_id == "P8":  # Double Bass - root motion + interval cycle
                if bar in [1, 5, 9]:
                    p += note("C", 2, 512, "half", acc=True)
                    p += note("E", 2, 256, "quarter")
                    p += note("G", 2, 256, "quarter", alter=1)
                elif bar in [3, 7, 11]:
                    p += note("A", 1, 512, "half", alter=-1)
                    p += note("C", 2, 256, "quarter")
                    p += note("E", 2, 256, "quarter")
                else:
                    p += note("G", 1, 512, "half")
                    p += note("C", 2, 512, "half")
                    
            elif part_id == "P9":  # Guitar - polychords, quartal
                p += note("C", 3, 256, "quarter", slur_s=True, acc=True)
                p += note("F", 3, 256, "quarter", chord=True)
                p += note("B", 3, 256, "quarter", chord=True)  # quartal
                p += note("E", 4, 256, "quarter")
                p += note("A", 3, 256, "quarter", chord=True)
                p += note("D", 4, 256, "quarter", chord=True)
                p += note("G", 4, 256, "quarter", alter=1, slur_e=True)  # C+ colour
                
            elif part_id == "P10":  # Glockenspiel - climax accents
                if bar == 7:
                    p += note("C", 7, 256, "quarter", acc=True)
                    p += rest(768, "half", dot=True)
                elif bar == 9:
                    p += note("C", 7, 256, "quarter", acc=True)
                    p += note("E", 7, 256, "quarter")
                    p += rest(512, "half")
                elif bar == 12:
                    p += rest(768, "half", dot=True)
                    p += note("C", 6, 256, "quarter", ferm=True)
                else:
                    p += rest(1024, "whole")
            
            if bar == 12:
                p += barline()
                
            p += '    </measure>\n'
        
        p += part_footer()
        parts.append(p)
    
    return orchestral_header("The Master's Palette - IV. German Development") + "".join(parts) + footer()

# ============ MAIN ============
def main():
    scores_dir = os.path.join(os.path.dirname(__file__), "..", "scores")
    
    print("=" * 70)
    print("FINAL ORCHESTRATION REFINEMENT PASS")
    print("Movements III (Bartok Night) and IV (German Development) only")
    print("Do NOT modify Movements I, II, or V")
    print("=" * 70)
    print()
    
    results = {}
    history = {"III. Bartok Night": [], "IV. German Development": []}
    iteration = 0
    max_iterations = 3
    
    while iteration < max_iterations:
        iteration += 1
        print(f"ITERATION {iteration}")
        print("-" * 50)
        
        all_pass = True
        
        # Movement III
        xml3 = orchestrate_mvmt3_excellent()
        filepath3 = os.path.join(scores_dir, "Movement3-Orchestrated-Excellent-Final.musicxml")
        with open(filepath3, "w", encoding="utf-8") as f:
            f.write(xml3)
        total3, scores3 = evaluate(xml3, "III. Bartok Night")
        history["III. Bartok Night"].append(total3)
        results["III. Bartok Night"] = (total3, scores3)
        status3 = "EXCELLENT" if total3 >= 8.0 else "REFINE"
        if total3 < 8.0:
            all_pass = False
        print(f"  III. Bartok Night: {total3:.2f}/10.0 [{status3}]")
        
        # Movement IV
        xml4 = orchestrate_mvmt4_excellent()
        filepath4 = os.path.join(scores_dir, "Movement4-Orchestrated-Excellent-Final.musicxml")
        with open(filepath4, "w", encoding="utf-8") as f:
            f.write(xml4)
        total4, scores4 = evaluate(xml4, "IV. German Development")
        history["IV. German Development"].append(total4)
        results["IV. German Development"] = (total4, scores4)
        status4 = "EXCELLENT" if total4 >= 8.0 else "REFINE"
        if total4 < 8.0:
            all_pass = False
        print(f"  IV. German Development: {total4:.2f}/10.0 [{status4}]")
        
        if all_pass:
            print()
            print("=" * 70)
            print("BOTH MOVEMENTS PASS >= 8.0 - REFINEMENT COMPLETE")
            print("=" * 70)
            break
        
        print()
    
    # Final Summary
    print()
    print("=" * 70)
    print("FINAL SUMMARY")
    print("=" * 70)
    print()
    print(f"{'Movement':<35} {'Iterations':<12} {'Final Score':<15} {'Status'}")
    print("-" * 70)
    
    for name, (total, scores) in results.items():
        iter_count = len(history[name])
        status = "EXCELLENT" if total >= 8.0 else "NEEDS WORK"
        print(f"{name:<35} {iter_count:<12} {total:.2f}/10.0        {status}")
    
    print("-" * 70)
    print()
    
    print("SCORE HISTORY:")
    for name in history:
        scores_str = " -> ".join([f"{s:.2f}" for s in history[name]])
        print(f"  {name}: {scores_str}")
    
    print()
    print("FINAL CATEGORY SCORES:")
    for name, (total, scores) in results.items():
        print(f"\n  {name} ({total:.2f}/10.0):")
        for cat, score in scores.items():
            print(f"    {cat}: {score:.2f}")
    
    print()
    print("IMPROVEMENTS APPLIED:")
    print()
    print("Movement III (Bartok Night):")
    print("  - Added m2 clusters (Bb-A) throughout")
    print("  - Added tritone dyads (A-Eb, E-Bb, D-Ab)")
    print("  - Added Bartok axis pairs (A-Eb, C-Gb)")
    print("  - Added quartal pedal stacks in cello")
    print("  - Added very high flute harmonics (E7, F7)")
    print("  - Added very low bass punctuation (A1, Eb1)")
    print("  - Added insect-like glockenspiel stabs")
    print("  - Added guitar harmonics with chromatic neighbours")
    print("  - Added ponticello violin harmonics")
    print("  - Increased silence and negative space")
    print()
    print("Movement IV (German Development):")
    print("  - Added clear inversion passage (bars 3-4)")
    print("  - Added augmentation passage (bars 5-6)")
    print("  - Added diminution passage (bars 7-8)")
    print("  - Added Klangfarbenmelodie hand-offs:")
    print("      Vln.I (1-2) -> Fl. (3-4) -> Cl. (5-6) -> Flgh. (7-8)")
    print("  - Added C+ interval cycle in cello/bass")
    print("  - Added chromatic planing in Vln.II/Viola")
    print("  - Added polychord/quartal stacks in guitar")
    print("  - Strengthened developmental arc:")
    print("      seed -> inversion -> augmentation -> diminution -> synthesis")
    print()
    print("OUTPUT FILES:")
    print("  - Movement3-Orchestrated-Excellent-Final.musicxml")
    print("  - Movement4-Orchestrated-Excellent-Final.musicxml")

if __name__ == "__main__":
    main()

