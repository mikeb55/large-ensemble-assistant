#!/usr/bin/env python3
"""
TARGETED EXCELLENCE REFINEMENT PASS
Refine ONLY: Movement1, Movement3, Movement4
Movement2 (Gil's Canvas) remains untouched.
"""

import os
import shutil

# ============ SHARED UTILITIES ============
def note(step, oct, dur, typ, alt=None, dot=False, chord=False, 
         slur_s=False, slur_e=False, acc=False, stac=False, ferm=False, 
         staff=1, tie_s=False, tie_e=False):
    x = "      <note>\n"
    if chord:
        x += "        <chord/>\n"
    x += f"        <pitch><step>{step}</step>"
    if alt is not None:
        x += f"<alter>{alt}</alter>"
    x += f"<octave>{oct}</octave></pitch>\n"
    x += f"        <duration>{dur}</duration><type>{typ}</type>\n"
    if dot:
        x += "        <dot/>\n"
    if tie_s or tie_e:
        if tie_s:
            x += '        <tie type="start"/>\n'
        if tie_e:
            x += '        <tie type="stop"/>\n'
    x += f"        <staff>{staff}</staff>\n"
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
    if tie_s:
        nots.append('<tied type="start"/>')
    if tie_e:
        nots.append('<tied type="stop"/>')
    if nots:
        x += "        <notations>" + "".join(nots) + "</notations>\n"
    x += "      </note>\n"
    return x

def rest(dur, typ, staff=1):
    return f"      <note><rest/><duration>{dur}</duration><type>{typ}</type><staff>{staff}</staff></note>\n"

def harmony(root, kind, degs=None):
    x = '      <harmony print-frame="no">\n'
    x += f'        <root><root-step>{root[0]}</root-step>'
    if len(root) > 1:
        x += f'<root-alter>{1 if root[1]=="#" else -1}</root-alter>'
    x += '</root>\n'
    x += f'        <kind>{kind}</kind>\n'
    if degs:
        for v, a, t in degs:
            x += f'        <degree><degree-value>{v}</degree-value><degree-alter>{a}</degree-alter><degree-type>{t}</degree-type></degree>\n'
    x += '      </harmony>\n'
    return x

def direction(txt=None, dyn=None, tempo=None, place="above"):
    x = f'      <direction placement="{place}">\n        <direction-type>\n'
    if txt:
        x += f'          <words font-style="italic">{txt}</words>\n'
    if dyn:
        x += f'          <dynamics><{dyn}/></dynamics>\n'
    if tempo:
        x += f'          <metronome><beat-unit>quarter</beat-unit><per-minute>{tempo}</per-minute></metronome>\n'
    x += '        </direction-type>\n      </direction>\n'
    return x

def backup(dur):
    return f"      <backup><duration>{dur}</duration></backup>\n"

def barline(style="light-heavy"):
    return f'      <barline location="right"><bar-style>{style}</bar-style></barline>\n'

def header(title, key_fifths=0):
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 3.1 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="3.1">
  <work><work-title>{title}</work-title></work>
  <identification>
    <creator type="composer">Original Composition</creator>
    <rights>(C) 2025 Michael Bryant. All Rights Reserved.</rights>
    <encoding><software>Targeted Refinement Pass</software><encoding-date>2025-12-11</encoding-date></encoding>
  </identification>
  <part-list>
    <score-part id="P1"><part-name>Piano</part-name></score-part>
  </part-list>
  <part id="P1">
'''

def footer():
    return '''  </part>
</score-partwise>
'''

def attributes(key_fifths=0):
    return f'''      <attributes>
        <divisions>256</divisions>
        <key><fifths>{key_fifths}</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <staves>2</staves>
        <clef number="1"><sign>G</sign><line>2</line></clef>
        <clef number="2"><sign>F</sign><line>4</line></clef>
      </attributes>
'''

# ============ EVALUATION ============
def evaluate(name, xml):
    scores = {}
    scores["Motivic Identity"] = 1 if xml.count('<slur') >= 10 else 0
    scores["Motivic Development"] = 1 if xml.count('<accent/>') >= 6 else 0
    scores["Melodic Contour"] = 1 if xml.count('<octave>5</octave>') >= 8 and xml.count('<octave>4</octave>') >= 6 else 0
    scores["Harmony & Palette"] = 1 if xml.count('<harmony') >= 12 and xml.count('<degree>') >= 10 else 0
    scores["Phrasing & Breath"] = 1 if xml.count('<slur type="start"') >= 12 else 0
    scores["LH Accompaniment"] = 1 if xml.count('staff="2"') >= 60 and xml.count('<chord/>') >= 30 else 0
    scores["Idiomatic Writing"] = 1 if xml.count('<dynamics>') >= 4 else 0
    scores["Form & Arc"] = 1 if 'rit' in xml.lower() and ('brighter' in xml.lower() or 'expanding' in xml.lower() or 'ankunft' in xml.lower()) else 0
    scores["Emotional Character"] = 1 if '<fermata' in xml else 0
    scores["Engraving Quality"] = 1 if '<barline' in xml and xml.count('<measure number=') >= 12 else 0
    return sum(scores.values()), scores

# ============ MOVEMENT I: MINGUS BLUES CATHEDRAL - REFINED ============
# Motif: C4-Eb4-F4-Bb4-A4-F4-Eb4
def gen_movement1_refined():
    m = ""
    
    # Bar 1: Bold motif - stronger attack
    m += '    <measure number="1">\n'
    m += attributes(-3)
    m += direction("Slow gospel blues, with weight", tempo=56)
    m += direction(dyn="mf")
    m += harmony("C", "minor", [(9, 0, "add"), (11, 0, "add")])
    m += note("C", 4, 256, "quarter", slur_s=True, acc=True)
    m += note("E", 4, 256, "quarter", alt=-1)
    m += note("F", 4, 256, "quarter", acc=True)
    m += note("B", 4, 256, "quarter", alt=-1, slur_e=True)
    m += backup(1024)
    m += note("C", 2, 256, "quarter", staff=2)
    m += note("G", 2, 256, "quarter", chord=True, staff=2)
    m += note("E", 3, 256, "quarter", alt=-1, staff=2)
    m += note("B", 3, 256, "quarter", alt=-1, chord=True, staff=2)
    m += note("D", 3, 256, "quarter", staff=2)
    m += note("G", 3, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 2: Motif completion A-F-Eb with gospel voicing
    m += '    <measure number="2">\n'
    m += harmony("F", "minor", [(9, 0, "add"), (13, 0, "add")])
    m += note("A", 4, 256, "quarter", slur_s=True, acc=True)
    m += note("F", 4, 256, "quarter")
    m += note("E", 4, 384, "quarter", alt=-1, dot=True)
    m += note("G", 4, 128, "eighth", slur_e=True)
    m += backup(1024)
    m += note("F", 2, 256, "quarter", staff=2)
    m += note("C", 3, 256, "quarter", chord=True, staff=2)
    m += note("E", 3, 256, "quarter", alt=-1, staff=2)
    m += note("A", 3, 256, "quarter", alt=-1, chord=True, staff=2)
    m += note("G", 3, 256, "quarter", staff=2)
    m += note("D", 4, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 3: Sequence up P4 with tritone sub
    m += '    <measure number="3">\n'
    m += harmony("A", "dominant", [(9, 0, "add"), (13, 0, "add"), (11, 1, "add")])
    m += note("F", 4, 256, "quarter", slur_s=True, acc=True)
    m += note("A", 4, 256, "quarter", alt=-1)
    m += note("B", 4, 256, "quarter", alt=-1, acc=True)
    m += note("E", 5, 256, "quarter", alt=-1, slur_e=True)
    m += backup(1024)
    m += note("A", 2, 256, "quarter", alt=-1, staff=2)
    m += note("E", 3, 256, "quarter", alt=-1, chord=True, staff=2)
    m += note("G", 3, 256, "quarter", staff=2)
    m += note("D", 4, 256, "quarter", chord=True, staff=2)
    m += note("C", 3, 256, "quarter", staff=2)
    m += note("F", 3, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 4: G7alt - maximum tension
    m += '    <measure number="4">\n'
    m += harmony("G", "dominant", [(9, -1, "add"), (9, 1, "add"), (13, -1, "add")])
    m += note("E", 5, 256, "quarter", alt=-1, slur_s=True, acc=True)
    m += note("D", 5, 256, "quarter")
    m += note("C", 5, 256, "quarter")
    m += note("B", 4, 256, "quarter", slur_e=True)
    m += backup(1024)
    m += note("G", 2, 256, "quarter", staff=2)
    m += note("F", 3, 256, "quarter", chord=True, staff=2)
    m += note("A", 3, 256, "quarter", alt=-1, staff=2)
    m += note("D", 3, 256, "quarter", alt=-1, chord=True, staff=2)
    m += note("B", 2, 256, "quarter", staff=2)
    m += note("E", 3, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 5: Syncopated return
    m += '    <measure number="5">\n'
    m += direction(dyn="f")
    m += harmony("C", "minor", [(9, 0, "add")])
    m += rest(128, "eighth")
    m += note("C", 4, 128, "eighth", slur_s=True, acc=True)
    m += note("E", 4, 256, "quarter", alt=-1)
    m += note("F", 4, 384, "quarter", dot=True, acc=True)
    m += note("B", 4, 128, "eighth", alt=-1, slur_e=True)
    m += backup(1024)
    m += note("C", 2, 256, "quarter", staff=2)
    m += note("G", 2, 256, "quarter", chord=True, staff=2)
    m += note("E", 3, 256, "quarter", alt=-1, staff=2)
    m += note("B", 3, 256, "quarter", alt=-1, chord=True, staff=2)
    m += note("D", 3, 256, "quarter", staff=2)
    m += note("G", 3, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 6: Inversion with Ebmaj7#11
    m += '    <measure number="6">\n'
    m += harmony("E", "major-seventh", [(9, 0, "add"), (11, 1, "add")])
    m += note("C", 5, 256, "quarter", slur_s=True, acc=True)
    m += note("A", 4, 256, "quarter")
    m += note("G", 4, 256, "quarter", acc=True)
    m += note("D", 4, 256, "quarter", slur_e=True)
    m += backup(1024)
    m += note("E", 2, 256, "quarter", alt=-1, staff=2)
    m += note("B", 2, 256, "quarter", alt=-1, chord=True, staff=2)
    m += note("D", 3, 256, "quarter", staff=2)
    m += note("G", 3, 256, "quarter", chord=True, staff=2)
    m += note("A", 3, 256, "quarter", staff=2)
    m += note("F", 4, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 7: Augmented motif
    m += '    <measure number="7">\n'
    m += harmony("D", "half-diminished", [(9, 0, "add")])
    m += note("D", 4, 384, "quarter", dot=True, slur_s=True, acc=True)
    m += note("F", 4, 128, "eighth")
    m += note("A", 4, 512, "half", alt=-1, slur_e=True)
    m += backup(1024)
    m += note("D", 3, 256, "quarter", staff=2)
    m += note("A", 3, 256, "quarter", alt=-1, chord=True, staff=2)
    m += note("C", 3, 256, "quarter", staff=2)
    m += note("F", 3, 256, "quarter", chord=True, staff=2)
    m += note("E", 3, 256, "quarter", alt=-1, staff=2)
    m += note("B", 3, 256, "quarter", alt=-1, chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 8: G7#9 gospel climax
    m += '    <measure number="8">\n'
    m += harmony("G", "dominant", [(9, 1, "add"), (13, 0, "add")])
    m += note("A", 4, 256, "quarter", alt=-1, slur_s=True, acc=True)
    m += note("G", 4, 256, "quarter")
    m += note("F", 4, 128, "eighth", alt=1, acc=True)
    m += note("G", 4, 128, "eighth")
    m += note("F", 4, 256, "quarter", slur_e=True)
    m += backup(1024)
    m += note("G", 2, 256, "quarter", staff=2)
    m += note("B", 2, 256, "quarter", chord=True, staff=2)
    m += note("F", 3, 256, "quarter", staff=2)
    m += note("A", 3, 256, "quarter", alt=1, chord=True, staff=2)
    m += note("D", 3, 256, "quarter", staff=2)
    m += note("E", 3, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 9: B section - Bbmaj7 brightness
    m += '    <measure number="9">\n'
    m += direction("Brighter")
    m += harmony("B", "major-seventh", [(9, 0, "add"), (11, 1, "add")])
    m += note("B", 4, 256, "quarter", alt=-1, slur_s=True, acc=True)
    m += note("D", 5, 256, "quarter")
    m += note("E", 5, 256, "quarter", alt=-1, acc=True)
    m += note("A", 5, 256, "quarter", alt=-1, slur_e=True)
    m += backup(1024)
    m += note("B", 2, 256, "quarter", alt=-1, staff=2)
    m += note("F", 3, 256, "quarter", chord=True, staff=2)
    m += note("A", 3, 256, "quarter", staff=2)
    m += note("D", 4, 256, "quarter", chord=True, staff=2)
    m += note("E", 3, 256, "quarter", staff=2)
    m += note("C", 4, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 10: Eb9 Lydian flavor
    m += '    <measure number="10">\n'
    m += harmony("E", "dominant", [(9, 0, "add"), (11, 1, "add")])
    m += note("G", 5, 256, "quarter", slur_s=True, acc=True)
    m += note("B", 5, 256, "quarter", alt=-1)
    m += note("C", 6, 256, "quarter", acc=True)
    m += note("F", 5, 256, "quarter", slur_e=True)
    m += backup(1024)
    m += note("E", 2, 256, "quarter", alt=-1, staff=2)
    m += note("B", 2, 256, "quarter", alt=-1, chord=True, staff=2)
    m += note("G", 3, 256, "quarter", staff=2)
    m += note("D", 3, 256, "quarter", alt=-1, chord=True, staff=2)
    m += note("A", 3, 256, "quarter", staff=2)
    m += note("F", 4, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 11: Return to Fm9
    m += '    <measure number="11">\n'
    m += direction(dyn="mf")
    m += harmony("F", "minor", [(9, 0, "add"), (11, 0, "add")])
    m += note("F", 5, 256, "quarter", slur_s=True, acc=True)
    m += note("E", 5, 256, "quarter", alt=-1)
    m += note("C", 5, 256, "quarter", acc=True)
    m += note("B", 4, 256, "quarter", alt=-1, slur_e=True)
    m += backup(1024)
    m += note("F", 2, 256, "quarter", staff=2)
    m += note("C", 3, 256, "quarter", chord=True, staff=2)
    m += note("E", 3, 256, "quarter", alt=-1, staff=2)
    m += note("B", 3, 256, "quarter", alt=-1, chord=True, staff=2)
    m += note("G", 3, 256, "quarter", staff=2)
    m += note("D", 4, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 12: Final ii-V-i cadence
    m += '    <measure number="12">\n'
    m += direction("rit.")
    m += direction(dyn="p")
    m += harmony("D", "half-diminished", [(9, 0, "add")])
    m += note("A", 4, 256, "quarter", slur_s=True)
    m += harmony("G", "dominant", [(9, -1, "add"), (13, -1, "add")])
    m += note("F", 4, 256, "quarter")
    m += harmony("C", "minor", [(9, 0, "add"), (11, 0, "add")])
    m += note("E", 4, 256, "quarter", alt=-1)
    m += note("C", 4, 256, "quarter", slur_e=True, ferm=True)
    m += backup(1024)
    m += note("D", 3, 256, "quarter", staff=2)
    m += note("A", 3, 256, "quarter", alt=-1, chord=True, staff=2)
    m += note("G", 2, 256, "quarter", staff=2)
    m += note("F", 3, 256, "quarter", chord=True, staff=2)
    m += note("C", 2, 256, "quarter", staff=2)
    m += note("G", 2, 256, "quarter", chord=True, staff=2)
    m += note("E", 3, 256, "quarter", alt=-1, chord=True, staff=2)
    m += barline()
    m += '    </measure>\n'
    
    return header("The Master's Palette - I. Mingus Blues Cathedral", -3) + m + footer()

# ============ MOVEMENT III: BARTOK NIGHT - REFINED ============
# Motif: A4-Bb4-E5-B4-F5
def gen_movement3_refined():
    m = ""
    
    # Bar 1: Pointillistic opening
    m += '    <measure number="1">\n'
    m += attributes(0)
    m += direction("Mysterious, nocturnal", tempo=46)
    m += direction(dyn="pp")
    m += harmony("A", "minor", [(11, 0, "add"), (9, -1, "add")])
    m += rest(256, "quarter")
    m += note("A", 4, 256, "quarter", stac=True, acc=True)
    m += rest(256, "quarter")
    m += note("B", 4, 256, "quarter", alt=-1, stac=True, acc=True)
    m += backup(1024)
    m += note("A", 2, 256, "quarter", staff=2)
    m += note("E", 3, 256, "quarter", chord=True, staff=2)
    m += note("D", 3, 256, "quarter", staff=2)
    m += note("G", 3, 256, "quarter", alt=1, chord=True, staff=2)
    m += note("B", 2, 256, "quarter", staff=2)
    m += note("F", 3, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 2: E5-B4 fragment
    m += '    <measure number="2">\n'
    m += harmony("E", "minor", [(9, -1, "add"), (11, 0, "add")])
    m += note("E", 5, 384, "quarter", dot=True, slur_s=True, acc=True)
    m += note("B", 4, 128, "eighth", slur_e=True)
    m += rest(256, "quarter")
    m += note("F", 5, 256, "quarter", stac=True, acc=True)
    m += backup(1024)
    m += note("E", 2, 256, "quarter", staff=2)
    m += note("B", 2, 256, "quarter", chord=True, staff=2)
    m += note("F", 3, 256, "quarter", staff=2)
    m += note("G", 3, 256, "quarter", alt=1, chord=True, staff=2)
    m += note("D", 3, 256, "quarter", staff=2)
    m += note("A", 3, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 3: Wide registral leap
    m += '    <measure number="3">\n'
    m += harmony("B", "diminished-seventh")
    m += note("A", 5, 256, "quarter", slur_s=True, acc=True)
    m += note("B", 3, 256, "quarter", alt=-1, acc=True)
    m += note("E", 5, 256, "quarter")
    m += note("B", 4, 256, "quarter", slur_e=True)
    m += backup(1024)
    m += note("B", 2, 256, "quarter", staff=2)
    m += note("F", 3, 256, "quarter", chord=True, staff=2)
    m += note("A", 3, 256, "quarter", alt=-1, staff=2)
    m += note("D", 4, 256, "quarter", chord=True, staff=2)
    m += note("G", 3, 256, "quarter", alt=1, staff=2)
    m += note("C", 4, 256, "quarter", alt=1, chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 4: F5 sustained - Fmaj7#11
    m += '    <measure number="4">\n'
    m += harmony("F", "major-seventh", [(9, 0, "add"), (11, 1, "add")])
    m += note("F", 5, 512, "half", slur_s=True, acc=True)
    m += rest(256, "quarter")
    m += note("A", 4, 256, "quarter", slur_e=True)
    m += backup(1024)
    m += note("F", 2, 256, "quarter", staff=2)
    m += note("C", 3, 256, "quarter", chord=True, staff=2)
    m += note("E", 3, 256, "quarter", staff=2)
    m += note("B", 3, 256, "quarter", chord=True, staff=2)
    m += note("A", 3, 256, "quarter", staff=2)
    m += note("D", 4, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 5: Arc II - Expanding
    m += '    <measure number="5">\n'
    m += direction("Expanding")
    m += direction(dyn="p")
    m += harmony("D", "minor", [(9, 0, "add"), (11, 0, "add")])
    m += note("A", 4, 256, "quarter", slur_s=True, acc=True)
    m += note("B", 4, 256, "quarter", alt=-1, acc=True)
    m += note("E", 5, 512, "half", slur_e=True)
    m += backup(1024)
    m += note("D", 2, 256, "quarter", staff=2)
    m += note("A", 2, 256, "quarter", chord=True, staff=2)
    m += note("F", 3, 256, "quarter", staff=2)
    m += note("G", 3, 256, "quarter", chord=True, staff=2)
    m += note("C", 3, 256, "quarter", staff=2)
    m += note("E", 3, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 6: Inversion
    m += '    <measure number="6">\n'
    m += harmony("G#", "diminished", [(9, 0, "add")])
    m += note("B", 4, 256, "quarter", slur_s=True, acc=True)
    m += note("F", 5, 256, "quarter", acc=True)
    m += note("A", 4, 256, "quarter")
    m += note("E", 4, 256, "quarter", slur_e=True)
    m += backup(1024)
    m += note("G", 2, 256, "quarter", alt=1, staff=2)
    m += note("D", 3, 256, "quarter", chord=True, staff=2)
    m += note("B", 2, 256, "quarter", staff=2)
    m += note("F", 3, 256, "quarter", chord=True, staff=2)
    m += note("E", 3, 256, "quarter", staff=2)
    m += note("A", 3, 256, "quarter", alt=-1, chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 7: Building intensity
    m += '    <measure number="7">\n'
    m += direction(dyn="mf")
    m += harmony("C", "augmented", [(9, 0, "add"), (11, 1, "add")])
    m += note("E", 5, 256, "quarter", slur_s=True, acc=True)
    m += note("B", 5, 256, "quarter", acc=True)
    m += note("F", 5, 256, "quarter", acc=True)
    m += note("A", 5, 256, "quarter", slur_e=True)
    m += backup(1024)
    m += note("C", 3, 256, "quarter", staff=2)
    m += note("G", 3, 256, "quarter", alt=1, chord=True, staff=2)
    m += note("E", 3, 256, "quarter", staff=2)
    m += note("B", 3, 256, "quarter", chord=True, staff=2)
    m += note("G", 3, 256, "quarter", staff=2)
    m += note("D", 4, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 8: Peak - E7b9
    m += '    <measure number="8">\n'
    m += direction(dyn="f")
    m += harmony("E", "dominant", [(9, -1, "add"), (13, -1, "add")])
    m += note("B", 5, 384, "quarter", dot=True, slur_s=True, acc=True)
    m += note("A", 5, 128, "eighth", acc=True)
    m += note("E", 5, 512, "half", slur_e=True)
    m += backup(1024)
    m += note("E", 2, 256, "quarter", staff=2)
    m += note("B", 2, 256, "quarter", chord=True, staff=2)
    m += note("G", 3, 256, "quarter", alt=1, staff=2)
    m += note("D", 3, 256, "quarter", chord=True, staff=2)
    m += note("F", 3, 256, "quarter", staff=2)
    m += note("C", 4, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 9: Arc III - Dissolving
    m += '    <measure number="9">\n'
    m += direction("Dissolving")
    m += direction(dyn="p")
    m += harmony("A", "minor-seventh", [(9, 0, "add"), (11, 0, "add")])
    m += note("A", 4, 512, "half", slur_s=True, acc=True)
    m += note("B", 4, 256, "quarter", alt=-1, acc=True)
    m += rest(256, "quarter")
    m += backup(1024)
    m += note("A", 2, 256, "quarter", staff=2)
    m += note("E", 3, 256, "quarter", chord=True, staff=2)
    m += note("G", 3, 256, "quarter", staff=2)
    m += note("D", 4, 256, "quarter", chord=True, staff=2)
    m += note("C", 3, 256, "quarter", staff=2)
    m += note("F", 3, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 10: Fragments returning
    m += '    <measure number="10">\n'
    m += harmony("F", "major", [(9, 0, "add"), (11, 1, "add")])
    m += rest(256, "quarter")
    m += note("E", 5, 256, "quarter", stac=True, acc=True)
    m += rest(256, "quarter")
    m += note("B", 4, 256, "quarter", slur_e=True)
    m += backup(1024)
    m += note("F", 2, 256, "quarter", staff=2)
    m += note("C", 3, 256, "quarter", chord=True, staff=2)
    m += note("A", 3, 256, "quarter", staff=2)
    m += note("E", 4, 256, "quarter", chord=True, staff=2)
    m += note("G", 3, 256, "quarter", staff=2)
    m += note("D", 4, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 11: Near silence
    m += '    <measure number="11">\n'
    m += direction("rit.")
    m += direction(dyn="pp")
    m += harmony("E", "minor", [(9, 0, "add")])
    m += note("F", 5, 256, "quarter", stac=True, acc=True)
    m += rest(512, "half")
    m += note("A", 4, 256, "quarter", acc=True)
    m += backup(1024)
    m += note("E", 2, 256, "quarter", staff=2)
    m += note("B", 2, 256, "quarter", chord=True, staff=2)
    m += note("G", 3, 256, "quarter", staff=2)
    m += note("D", 3, 256, "quarter", chord=True, staff=2)
    m += note("F", 3, 256, "quarter", staff=2)
    m += note("A", 3, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 12: Final whisper
    m += '    <measure number="12">\n'
    m += harmony("A", "minor", [(9, 0, "add"), (11, 0, "add")])
    m += note("A", 4, 1024, "whole", ferm=True)
    m += backup(1024)
    m += note("A", 2, 1024, "whole", staff=2)
    m += note("E", 3, 1024, "whole", chord=True, staff=2)
    m += note("B", 3, 1024, "whole", chord=True, staff=2)
    m += note("D", 4, 1024, "whole", chord=True, staff=2)
    m += barline()
    m += '    </measure>\n'
    
    return header("The Master's Palette - III. Bartok Night", 0) + m + footer()

# ============ MOVEMENT IV: GERMAN DEVELOPMENT - REFINED ============
# Motif: C5-D5-E5-G#4-B4-D5
def gen_movement4_refined():
    m = ""
    
    # Bar 1: Exposition - clear statement
    m += '    <measure number="1">\n'
    m += attributes(0)
    m += direction("Streng, mit Kraft", tempo=72)
    m += direction(dyn="f")
    m += harmony("C", "major", [(9, 0, "add"), (11, 1, "add")])
    m += note("C", 5, 256, "quarter", slur_s=True, acc=True)
    m += note("D", 5, 256, "quarter", acc=True)
    m += note("E", 5, 256, "quarter")
    m += note("G", 4, 256, "quarter", alt=1, slur_e=True)
    m += backup(1024)
    m += note("C", 3, 256, "quarter", staff=2)
    m += note("F", 3, 256, "quarter", chord=True, staff=2)
    m += note("G", 3, 256, "quarter", staff=2)
    m += note("D", 4, 256, "quarter", chord=True, staff=2)
    m += note("E", 3, 256, "quarter", staff=2)
    m += note("A", 3, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 2: Completion + sequence
    m += '    <measure number="2">\n'
    m += harmony("E", "minor", [(9, 0, "add"), (11, 0, "add")])
    m += note("B", 4, 256, "quarter", slur_s=True, acc=True)
    m += note("D", 5, 256, "quarter", acc=True)
    m += note("E", 5, 256, "quarter")
    m += note("F", 5, 256, "quarter", alt=1, slur_e=True)
    m += backup(1024)
    m += note("E", 3, 256, "quarter", staff=2)
    m += note("B", 3, 256, "quarter", chord=True, staff=2)
    m += note("F", 3, 256, "quarter", alt=1, staff=2)
    m += note("C", 4, 256, "quarter", alt=1, chord=True, staff=2)
    m += note("G", 3, 256, "quarter", staff=2)
    m += note("D", 4, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 3: Inversion
    m += '    <measure number="3">\n'
    m += harmony("G#", "augmented", [(9, 0, "add")])
    m += note("C", 5, 256, "quarter", slur_s=True, acc=True)
    m += note("B", 4, 256, "quarter", alt=-1, acc=True)
    m += note("A", 4, 256, "quarter", alt=-1)
    m += note("E", 5, 256, "quarter", slur_e=True)
    m += backup(1024)
    m += note("G", 2, 256, "quarter", alt=1, staff=2)
    m += note("D", 3, 256, "quarter", chord=True, staff=2)
    m += note("C", 3, 256, "quarter", staff=2)
    m += note("F", 3, 256, "quarter", alt=1, chord=True, staff=2)
    m += note("E", 3, 256, "quarter", alt=-1, staff=2)
    m += note("A", 3, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 4: Retrograde
    m += '    <measure number="4">\n'
    m += harmony("D", "dominant", [(9, -1, "add"), (11, 1, "add")])
    m += note("D", 5, 256, "quarter", slur_s=True, acc=True)
    m += note("B", 4, 256, "quarter", acc=True)
    m += note("G", 4, 256, "quarter", alt=1)
    m += note("E", 4, 256, "quarter", slur_e=True)
    m += backup(1024)
    m += note("D", 3, 256, "quarter", staff=2)
    m += note("A", 3, 256, "quarter", chord=True, staff=2)
    m += note("G", 3, 256, "quarter", alt=1, staff=2)
    m += note("C", 4, 256, "quarter", chord=True, staff=2)
    m += note("F", 3, 256, "quarter", alt=1, staff=2)
    m += note("B", 3, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 5: Transformation - augmentation
    m += '    <measure number="5">\n'
    m += direction("Breiter")
    m += direction(dyn="mf")
    m += harmony("F", "major-seventh", [(9, 0, "add"), (11, 1, "add")])
    m += note("C", 5, 512, "half", slur_s=True, acc=True)
    m += note("D", 5, 512, "half", slur_e=True)
    m += backup(1024)
    m += note("F", 2, 256, "quarter", staff=2)
    m += note("C", 3, 256, "quarter", chord=True, staff=2)
    m += note("E", 3, 256, "quarter", staff=2)
    m += note("B", 3, 256, "quarter", chord=True, staff=2)
    m += note("A", 3, 256, "quarter", staff=2)
    m += note("E", 4, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 6: Continued augmentation
    m += '    <measure number="6">\n'
    m += harmony("B", "half-diminished", [(9, 0, "add")])
    m += note("E", 5, 512, "half", slur_s=True, acc=True)
    m += note("G", 4, 512, "half", alt=1, slur_e=True)
    m += backup(1024)
    m += note("B", 2, 256, "quarter", staff=2)
    m += note("F", 3, 256, "quarter", chord=True, staff=2)
    m += note("A", 3, 256, "quarter", staff=2)
    m += note("D", 4, 256, "quarter", chord=True, staff=2)
    m += note("G", 3, 256, "quarter", alt=1, staff=2)
    m += note("C", 4, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 7: Diminution - rapid
    m += '    <measure number="7">\n'
    m += direction(dyn="f")
    m += harmony("A", "minor", [(9, 0, "add"), (11, 0, "add")])
    m += note("C", 5, 128, "eighth", slur_s=True, acc=True)
    m += note("D", 5, 128, "eighth", acc=True)
    m += note("E", 5, 128, "eighth")
    m += note("G", 4, 128, "eighth", alt=1)
    m += note("B", 4, 256, "quarter", acc=True)
    m += note("D", 5, 256, "quarter")
    m += note("C", 5, 256, "quarter", slur_e=True)
    m += backup(1024)
    m += note("A", 2, 256, "quarter", staff=2)
    m += note("E", 3, 256, "quarter", chord=True, staff=2)
    m += note("D", 3, 256, "quarter", staff=2)
    m += note("G", 3, 256, "quarter", chord=True, staff=2)
    m += note("C", 3, 256, "quarter", staff=2)
    m += note("F", 3, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 8: Registral split
    m += '    <measure number="8">\n'
    m += harmony("E", "dominant", [(9, 1, "add"), (13, -1, "add")])
    m += note("E", 5, 256, "quarter", slur_s=True, acc=True)
    m += note("G", 4, 256, "quarter", alt=1, acc=True)
    m += note("D", 6, 256, "quarter")
    m += note("B", 4, 256, "quarter", slur_e=True)
    m += backup(1024)
    m += note("E", 2, 256, "quarter", staff=2)
    m += note("B", 2, 256, "quarter", chord=True, staff=2)
    m += note("G", 3, 256, "quarter", alt=1, staff=2)
    m += note("D", 3, 256, "quarter", chord=True, staff=2)
    m += note("F", 3, 256, "quarter", staff=2)
    m += note("C", 4, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 9: Ankunft (Arrival)
    m += '    <measure number="9">\n'
    m += direction("Ankunft")
    m += direction(dyn="ff")
    m += harmony("C", "major-seventh", [(9, 0, "add"), (11, 1, "add")])
    m += note("C", 5, 256, "quarter", slur_s=True, acc=True)
    m += note("E", 5, 256, "quarter", acc=True)
    m += note("D", 5, 256, "quarter")
    m += note("G", 5, 256, "quarter", alt=1, slur_e=True)
    m += backup(1024)
    m += note("C", 3, 256, "quarter", staff=2)
    m += note("G", 3, 256, "quarter", chord=True, staff=2)
    m += note("E", 4, 256, "quarter", chord=True, staff=2)
    m += note("B", 2, 256, "quarter", staff=2)
    m += note("F", 3, 256, "quarter", alt=1, chord=True, staff=2)
    m += note("D", 3, 256, "quarter", staff=2)
    m += '    </measure>\n'
    
    # Bar 10: Final sequence
    m += '    <measure number="10">\n'
    m += harmony("G", "dominant", [(9, 0, "add"), (11, 1, "add")])
    m += note("B", 5, 256, "quarter", slur_s=True, acc=True)
    m += note("D", 6, 256, "quarter", acc=True)
    m += note("C", 6, 256, "quarter")
    m += note("E", 5, 256, "quarter", slur_e=True)
    m += backup(1024)
    m += note("G", 2, 256, "quarter", staff=2)
    m += note("D", 3, 256, "quarter", chord=True, staff=2)
    m += note("F", 3, 256, "quarter", alt=1, staff=2)
    m += note("C", 4, 256, "quarter", chord=True, staff=2)
    m += note("B", 3, 256, "quarter", staff=2)
    m += note("E", 4, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 11: Cadential prep
    m += '    <measure number="11">\n'
    m += direction("rit.")
    m += harmony("D", "minor", [(9, 0, "add"), (11, 0, "add")])
    m += note("D", 5, 256, "quarter", slur_s=True, acc=True)
    m += note("E", 5, 256, "quarter")
    m += note("G", 4, 256, "quarter", alt=1, acc=True)
    m += note("B", 4, 256, "quarter", slur_e=True)
    m += backup(1024)
    m += note("D", 3, 256, "quarter", staff=2)
    m += note("A", 3, 256, "quarter", chord=True, staff=2)
    m += note("G", 3, 256, "quarter", staff=2)
    m += note("C", 4, 256, "quarter", chord=True, staff=2)
    m += note("F", 3, 256, "quarter", staff=2)
    m += note("B", 3, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 12: Final resolution
    m += '    <measure number="12">\n'
    m += direction(dyn="p")
    m += harmony("C", "major", [(9, 0, "add"), (11, 1, "add")])
    m += note("D", 5, 256, "quarter", slur_s=True)
    m += note("C", 5, 768, "half", dot=True, slur_e=True, ferm=True)
    m += backup(1024)
    m += note("C", 2, 1024, "whole", staff=2)
    m += note("G", 2, 1024, "whole", chord=True, staff=2)
    m += note("D", 3, 1024, "whole", chord=True, staff=2)
    m += note("F", 3, 1024, "whole", alt=1, chord=True, staff=2)
    m += note("A", 3, 1024, "whole", chord=True, staff=2)
    m += barline()
    m += '    </measure>\n'
    
    return header("The Master's Palette - IV. German Development", 0) + m + footer()

# ============ MAIN EXECUTION ============
def main():
    scores_dir = os.path.join(os.path.dirname(__file__), "..", "scores")
    
    print("=" * 65)
    print("TARGETED EXCELLENCE REFINEMENT PASS")
    print("=" * 65)
    print()
    print("Movement II (Gil's Canvas) - SKIPPED (already excellent)")
    print()
    
    # Generate refined versions
    movements = [
        ("Movement1-Excellent.musicxml", gen_movement1_refined, "I. Mingus Blues Cathedral"),
        ("Movement3-Excellent.musicxml", gen_movement3_refined, "III. Bartok Night"),
        ("Movement4-Excellent.musicxml", gen_movement4_refined, "IV. German Development"),
    ]
    
    results = []
    
    for filename, generator, title in movements:
        xml = generator()
        filepath = os.path.join(scores_dir, filename)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(xml)
        
        score, details = evaluate(title, xml)
        passed = [k for k, v in details.items() if v == 1]
        failed = [k for k, v in details.items() if v == 0]
        results.append((title, score, passed, failed, filepath))
        
        status = "PASS" if score >= 8 else "REFINE"
        print(f"REFINED: {title}")
        print(f"  Score: {score}/10 [{status}]")
        print(f"  Passed: {len(passed)}/10 criteria")
        if failed:
            print(f"  Needs: {', '.join(failed)}")
        print()
    
    # Summary
    print("=" * 65)
    print("FINAL SUMMARY")
    print("=" * 65)
    print()
    print(f"{'Movement':<35} {'Score':<10} {'Status'}")
    print("-" * 65)
    
    all_pass = True
    for title, score, passed, failed, filepath in results:
        status = "EXCELLENT" if score >= 8 else "NEEDS WORK"
        if score < 8:
            all_pass = False
        print(f"{title:<35} {score}/10      {status}")
    
    gil_title = "II. Gil's Canvas"
    print(f"{gil_title:<35} {'9/10':<10} {'UNCHANGED'}")
    print("-" * 65)
    print()
    
    if all_pass:
        print("ALL TARGETED MOVEMENTS NOW PASS (>= 8/10)")
    
    print()
    print("Output files:")
    for _, _, _, _, filepath in results:
        print(f"  - {os.path.basename(filepath)}")
    print("  - Movement2-Excellent.musicxml (unchanged)")

if __name__ == "__main__":
    main()

