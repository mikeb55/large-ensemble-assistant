#!/usr/bin/env python3
"""
Movement I - Charles Mingus-inspired Lead Sheet Generator
48 bars: A(16) - B(16) - A'(16)
Motif A: rising m3 → tritone leap
Motif B: descending blues-inflected 4-note cell
"""

import os

# MusicXML Header
def get_header():
    return '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 3.1 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="3.1">
  <work>
    <work-title>The Master's Palette - Movement I</work-title>
  </work>
  <identification>
    <creator type="composer">Original Composition (Mingus-inspired)</creator>
    <rights>© 2025 Michael Bryant. All Rights Reserved.</rights>
    <encoding>
      <software>Python MusicXML Generator</software>
      <encoding-date>2025-12-11</encoding-date>
    </encoding>
  </identification>
  <defaults>
    <scaling><millimeters>7.0</millimeters><tenths>40</tenths></scaling>
    <page-layout>
      <page-height>1683</page-height>
      <page-width>1190</page-width>
      <page-margins type="both">
        <left-margin>70</left-margin>
        <right-margin>70</right-margin>
        <top-margin>88</top-margin>
        <bottom-margin>88</bottom-margin>
      </page-margins>
    </page-layout>
  </defaults>
  <part-list>
    <score-part id="P1">
      <part-name>Lead Sheet</part-name>
      <score-instrument id="P1-I1">
        <instrument-name>Piano</instrument-name>
      </score-instrument>
    </score-part>
  </part-list>
  <part id="P1">
'''

def get_footer():
    return '''  </part>
</score-partwise>
'''

# Note helper - duration 256 = quarter note
def note(step, octave, dur, ntype, alter=None, dot=False, chord=False, 
         slur_start=False, slur_stop=False, accent=False, staccato=False,
         fermata=False, tie_start=False, tie_stop=False, staff=1):
    xml = "      <note>\n"
    if chord:
        xml += "        <chord/>\n"
    xml += f"        <pitch><step>{step}</step>"
    if alter is not None:
        xml += f"<alter>{alter}</alter>"
    xml += f"<octave>{octave}</octave></pitch>\n"
    xml += f"        <duration>{dur}</duration>\n"
    xml += f"        <type>{ntype}</type>\n"
    if dot:
        xml += "        <dot/>\n"
    if tie_start or tie_stop:
        if tie_start:
            xml += '        <tie type="start"/>\n'
        if tie_stop:
            xml += '        <tie type="stop"/>\n'
    xml += f"        <staff>{staff}</staff>\n"
    # Notations
    notations = []
    if slur_start:
        notations.append('<slur type="start" number="1"/>')
    if slur_stop:
        notations.append('<slur type="stop" number="1"/>')
    if accent:
        notations.append('<articulations><accent/></articulations>')
    if staccato:
        notations.append('<articulations><staccato/></articulations>')
    if fermata:
        notations.append('<fermata type="upright"/>')
    if tie_start:
        notations.append('<tied type="start"/>')
    if tie_stop:
        notations.append('<tied type="stop"/>')
    if notations:
        xml += "        <notations>" + "".join(notations) + "</notations>\n"
    xml += "      </note>\n"
    return xml

def rest(dur, ntype, staff=1):
    return f"      <note><rest/><duration>{dur}</duration><type>{ntype}</type><staff>{staff}</staff></note>\n"

def harmony(root, kind, bass=None, degrees=None):
    """Generate harmony element for chord symbol above staff"""
    xml = '      <harmony print-frame="no">\n'
    xml += f'        <root><root-step>{root[0]}</root-step>'
    if len(root) > 1:
        alt = 1 if root[1] == '#' else -1
        xml += f'<root-alter>{alt}</root-alter>'
    xml += '</root>\n'
    xml += f'        <kind>{kind}</kind>\n'
    if degrees:
        for deg in degrees:
            val, alt, dtype = deg
            xml += f'        <degree><degree-value>{val}</degree-value><degree-alter>{alt}</degree-alter><degree-type>{dtype}</degree-type></degree>\n'
    if bass:
        xml += f'        <bass><bass-step>{bass[0]}</bass-step>'
        if len(bass) > 1:
            balt = 1 if bass[1] == '#' else -1
            xml += f'<bass-alter>{balt}</bass-alter>'
        xml += '</bass>\n'
    xml += '      </harmony>\n'
    return xml

def direction(text, placement="above", dynamic=None, tempo=None):
    xml = f'      <direction placement="{placement}">\n'
    xml += '        <direction-type>\n'
    if text:
        xml += f'          <words font-style="italic">{text}</words>\n'
    if dynamic:
        xml += f'          <dynamics><{dynamic}/></dynamics>\n'
    if tempo:
        xml += f'          <metronome><beat-unit>quarter</beat-unit><per-minute>{tempo}</per-minute></metronome>\n'
    xml += '        </direction-type>\n'
    xml += '      </direction>\n'
    return xml

def barline(style="light-heavy", repeat=None):
    xml = '      <barline location="right">\n'
    xml += f'        <bar-style>{style}</bar-style>\n'
    if repeat:
        xml += f'        <repeat direction="{repeat}"/>\n'
    xml += '      </barline>\n'
    return xml

def attributes(div=256, fifths=-2, beats=4, beattype=4, staves=2, first=False):
    xml = "      <attributes>\n"
    xml += f"        <divisions>{div}</divisions>\n"
    xml += f"        <key><fifths>{fifths}</fifths></key>\n"
    xml += f"        <time><beats>{beats}</beats><beat-type>{beattype}</beat-type></time>\n"
    xml += f"        <staves>{staves}</staves>\n"
    xml += '        <clef number="1"><sign>G</sign><line>2</line></clef>\n'
    xml += '        <clef number="2"><sign>F</sign><line>4</line></clef>\n'
    xml += "      </attributes>\n"
    return xml

def backup(dur):
    return f"      <backup><duration>{dur}</duration></backup>\n"

# ============ SECTION A (bars 1-16): Brooding, building intensity ============
def section_a():
    measures = ""
    
    # Bar 1: Cm9 - Motif A intro (rising m3 to tritone)
    measures += '    <measure number="1">\n'
    measures += attributes(first=True)
    measures += direction("Slow, brooding", tempo=54)
    measures += direction(None, dynamic="mp")
    # Chord: Cm9
    measures += harmony("C", "minor", degrees=[(9, 0, "add")])
    # RH: Motif A - C -> Eb (m3) -> A (tritone from Eb)
    measures += note("C", 5, 256, "quarter", slur_start=True, staff=1)
    measures += note("E", 5, 256, "quarter", alter=-1, staff=1)
    measures += note("A", 5, 384, "quarter", dot=True, accent=True, staff=1)
    measures += note("G", 5, 128, "eighth", slur_stop=True, staff=1)
    measures += backup(1024)
    # LH: Rhythmic voicing (C-Eb-G-Bb in broken pattern)
    measures += note("C", 3, 256, "quarter", staff=2)
    measures += note("G", 3, 128, "eighth", staff=2)
    measures += note("B", 3, 128, "eighth", alter=-1, staff=2)
    measures += note("E", 3, 256, "quarter", alter=-1, staff=2)
    measures += note("G", 3, 256, "quarter", staff=2)
    measures += '    </measure>\n'
    
    # Bar 2: Fm7 - Motif A development
    measures += '    <measure number="2">\n'
    measures += harmony("F", "minor-seventh")
    measures += note("F", 5, 128, "eighth", slur_start=True, staff=1)
    measures += note("A", 5, 128, "eighth", alter=-1, staff=1)
    measures += note("E", 6, 256, "quarter", alter=-1, accent=True, staff=1)
    measures += note("D", 6, 256, "quarter", alter=-1, staff=1)
    measures += note("C", 6, 256, "quarter", slur_stop=True, staff=1)
    measures += backup(1024)
    # LH voicing
    measures += note("F", 2, 384, "quarter", dot=True, staff=2)
    measures += note("E", 3, 128, "eighth", alter=-1, staff=2)
    measures += note("A", 3, 128, "eighth", alter=-1, chord=True, staff=2)
    measures += note("C", 3, 256, "quarter", staff=2)
    measures += note("E", 3, 256, "quarter", alter=-1, chord=True, staff=2)
    measures += '    </measure>\n'
    
    # Bar 3: Db7#11 - Tension
    measures += '    <measure number="3">\n'
    measures += harmony("D", "dominant", degrees=[(11, 1, "add")])
    measures += note("D", 6, 256, "quarter", alter=-1, slur_start=True, staff=1)
    measures += note("G", 5, 256, "quarter", staff=1)
    measures += note("F", 5, 256, "quarter", staff=1)
    measures += note("E", 5, 128, "eighth", alter=-1, staff=1)
    measures += note("D", 5, 128, "eighth", alter=-1, slur_stop=True, staff=1)
    measures += backup(1024)
    # LH: guide tones + tension
    measures += note("D", 2, 256, "quarter", alter=-1, staff=2)
    measures += note("C", 3, 128, "eighth", staff=2)
    measures += note("F", 3, 128, "eighth", chord=True, staff=2)
    measures += note("G", 3, 256, "quarter", staff=2)
    measures += note("B", 2, 256, "quarter", alter=-1, staff=2)
    measures += '    </measure>\n'
    
    # Bar 4: G7alt - Resolution prep
    measures += '    <measure number="4">\n'
    measures += harmony("G", "dominant", degrees=[(9, -1, "add"), (13, -1, "add")])
    measures += note("E", 5, 256, "quarter", alter=-1, slur_start=True, staff=1)
    measures += note("D", 5, 256, "quarter", staff=1)
    measures += note("B", 4, 512, "half", slur_stop=True, staff=1)
    measures += backup(1024)
    # LH
    measures += note("G", 2, 256, "quarter", staff=2)
    measures += note("F", 3, 256, "quarter", staff=2)
    measures += note("A", 3, 128, "eighth", alter=-1, chord=True, staff=2)
    measures += note("D", 3, 256, "quarter", alter=-1, staff=2)
    measures += note("B", 2, 256, "quarter", staff=2)
    measures += '    </measure>\n'
    
    # Bar 5: Cm9 - Return, Motif B intro
    measures += '    <measure number="5">\n'
    measures += harmony("C", "minor", degrees=[(9, 0, "add")])
    # Motif B: descending blues cell (Eb-D-C-Bb)
    measures += note("E", 5, 256, "quarter", alter=-1, slur_start=True, accent=True, staff=1)
    measures += note("D", 5, 256, "quarter", staff=1)
    measures += note("C", 5, 256, "quarter", staff=1)
    measures += note("B", 4, 256, "quarter", alter=-1, slur_stop=True, staff=1)
    measures += backup(1024)
    measures += note("C", 3, 384, "quarter", dot=True, staff=2)
    measures += note("G", 3, 128, "eighth", staff=2)
    measures += note("E", 3, 256, "quarter", alter=-1, chord=True, staff=2)
    measures += note("B", 2, 256, "quarter", alter=-1, staff=2)
    measures += '    </measure>\n'
    
    # Bar 6: Ab13 - rich color
    measures += '    <measure number="6">\n'
    measures += harmony("A", "dominant", degrees=[(13, 0, "add")])
    measures += note("A", 4, 128, "eighth", alter=-1, slur_start=True, staff=1)
    measures += note("C", 5, 128, "eighth", staff=1)
    measures += note("G", 5, 512, "half", staff=1)
    measures += note("F", 5, 256, "quarter", slur_stop=True, staff=1)
    measures += backup(1024)
    measures += note("A", 2, 256, "quarter", alter=-1, staff=2)
    measures += note("E", 3, 256, "quarter", alter=-1, staff=2)
    measures += note("G", 3, 128, "eighth", chord=True, staff=2)
    measures += note("C", 3, 256, "quarter", staff=2)
    measures += note("F", 3, 256, "quarter", chord=True, staff=2)
    measures += '    </measure>\n'
    
    # Bar 7: Bbm7 - Eb7
    measures += '    <measure number="7">\n'
    measures += harmony("B", "minor-seventh")
    measures += note("B", 4, 256, "quarter", alter=-1, slur_start=True, staff=1)
    measures += note("D", 5, 256, "quarter", alter=-1, staff=1)
    measures += harmony("E", "dominant-ninth")
    measures += note("G", 5, 256, "quarter", staff=1)
    measures += note("F", 5, 256, "quarter", slur_stop=True, staff=1)
    measures += backup(1024)
    measures += note("B", 2, 256, "quarter", alter=-1, staff=2)
    measures += note("F", 3, 128, "eighth", staff=2)
    measures += note("A", 3, 128, "eighth", alter=-1, chord=True, staff=2)
    measures += note("E", 2, 256, "quarter", alter=-1, staff=2)
    measures += note("D", 3, 256, "quarter", alter=-1, staff=2)
    measures += '    </measure>\n'
    
    # Bar 8: Abmaj7#11 - Pause
    measures += '    <measure number="8">\n'
    measures += harmony("A", "major-seventh", degrees=[(11, 1, "add")])
    measures += note("E", 5, 512, "half", alter=-1, slur_start=True, staff=1)
    measures += note("D", 5, 256, "quarter", staff=1)
    measures += note("C", 5, 256, "quarter", slur_stop=True, staff=1)
    measures += backup(1024)
    measures += note("A", 2, 384, "quarter", alter=-1, dot=True, staff=2)
    measures += note("G", 3, 128, "eighth", staff=2)
    measures += note("C", 3, 128, "eighth", chord=True, staff=2)
    measures += note("E", 3, 256, "quarter", alter=-1, staff=2)
    measures += note("D", 3, 256, "quarter", staff=2)
    measures += '    </measure>\n'
    
    # Bar 9: Cm9 - Motif A transformed (inverted)
    measures += '    <measure number="9">\n'
    measures += direction(None, dynamic="mf")
    measures += harmony("C", "minor", degrees=[(9, 0, "add")])
    # Inverted Motif A: C -> A (down m3) -> Eb (tritone up)
    measures += note("C", 5, 256, "quarter", slur_start=True, staff=1)
    measures += note("A", 4, 256, "quarter", staff=1)
    measures += note("E", 5, 384, "quarter", alter=-1, dot=True, accent=True, staff=1)
    measures += note("D", 5, 128, "eighth", slur_stop=True, staff=1)
    measures += backup(1024)
    measures += note("C", 3, 256, "quarter", staff=2)
    measures += note("E", 3, 128, "eighth", alter=-1, staff=2)
    measures += note("G", 3, 128, "eighth", chord=True, staff=2)
    measures += note("B", 2, 256, "quarter", alter=-1, staff=2)
    measures += note("D", 3, 256, "quarter", staff=2)
    measures += '    </measure>\n'
    
    # Bar 10: Fm9 - sus
    measures += '    <measure number="10">\n'
    measures += harmony("F", "minor", degrees=[(9, 0, "add")])
    measures += note("F", 5, 256, "quarter", slur_start=True, staff=1)
    measures += note("E", 5, 256, "quarter", alter=-1, staff=1)
    measures += note("C", 5, 256, "quarter", staff=1)
    measures += note("B", 4, 256, "quarter", alter=-1, slur_stop=True, staff=1)
    measures += backup(1024)
    measures += note("F", 2, 256, "quarter", staff=2)
    measures += note("C", 3, 256, "quarter", staff=2)
    measures += note("E", 3, 256, "quarter", alter=-1, chord=True, staff=2)
    measures += note("A", 2, 256, "quarter", alter=-1, staff=2)
    measures += '    </measure>\n'
    
    # Bar 11: Db7#9 - climax build
    measures += '    <measure number="11">\n'
    measures += harmony("D", "dominant", degrees=[(9, 1, "add")])
    measures += note("E", 5, 128, "eighth", slur_start=True, staff=1)
    measures += note("F", 5, 128, "eighth", staff=1)
    measures += note("A", 5, 256, "quarter", alter=-1, accent=True, staff=1)
    measures += note("G", 5, 256, "quarter", staff=1)
    measures += note("F", 5, 256, "quarter", slur_stop=True, staff=1)
    measures += backup(1024)
    measures += note("D", 2, 256, "quarter", alter=-1, staff=2)
    measures += note("A", 2, 256, "quarter", alter=-1, staff=2)
    measures += note("C", 3, 128, "eighth", chord=True, staff=2)
    measures += note("F", 3, 256, "quarter", staff=2)
    measures += note("E", 3, 256, "quarter", staff=2)
    measures += '    </measure>\n'
    
    # Bar 12: G7b9 - tension peak
    measures += '    <measure number="12">\n'
    measures += harmony("G", "dominant", degrees=[(9, -1, "add")])
    measures += note("F", 5, 256, "quarter", slur_start=True, staff=1)
    measures += note("A", 5, 128, "eighth", alter=-1, staff=1)
    measures += note("G", 5, 128, "eighth", staff=1)
    measures += note("F", 5, 256, "quarter", staff=1)
    measures += note("D", 5, 256, "quarter", slur_stop=True, staff=1)
    measures += backup(1024)
    measures += note("G", 2, 256, "quarter", staff=2)
    measures += note("D", 3, 128, "eighth", staff=2)
    measures += note("F", 3, 128, "eighth", chord=True, staff=2)
    measures += note("A", 2, 256, "quarter", alter=-1, staff=2)
    measures += note("B", 2, 256, "quarter", staff=2)
    measures += '    </measure>\n'
    
    # Bar 13: Cm7 - Motif B expanded
    measures += '    <measure number="13">\n'
    measures += direction(None, dynamic="f")
    measures += harmony("C", "minor-seventh")
    # Motif B expanded: G-F-Eb-D-C
    measures += note("G", 5, 256, "quarter", slur_start=True, accent=True, staff=1)
    measures += note("F", 5, 256, "quarter", staff=1)
    measures += note("E", 5, 256, "quarter", alter=-1, staff=1)
    measures += note("D", 5, 256, "quarter", slur_stop=True, staff=1)
    measures += backup(1024)
    measures += note("C", 3, 256, "quarter", staff=2)
    measures += note("G", 3, 256, "quarter", staff=2)
    measures += note("B", 3, 128, "eighth", alter=-1, chord=True, staff=2)
    measures += note("E", 3, 256, "quarter", alter=-1, staff=2)
    measures += note("D", 3, 256, "quarter", staff=2)
    measures += '    </measure>\n'
    
    # Bar 14: Ebmaj7 - Ab13
    measures += '    <measure number="14">\n'
    measures += harmony("E", "major-seventh")
    measures += note("E", 5, 256, "quarter", alter=-1, slur_start=True, staff=1)
    measures += note("G", 5, 256, "quarter", staff=1)
    measures += harmony("A", "dominant", degrees=[(13, 0, "add")])
    measures += note("A", 5, 256, "quarter", alter=-1, staff=1)
    measures += note("G", 5, 256, "quarter", slur_stop=True, staff=1)
    measures += backup(1024)
    measures += note("E", 2, 256, "quarter", alter=-1, staff=2)
    measures += note("B", 2, 256, "quarter", alter=-1, staff=2)
    measures += note("A", 2, 256, "quarter", alter=-1, staff=2)
    measures += note("E", 3, 256, "quarter", alter=-1, staff=2)
    measures += '    </measure>\n'
    
    # Bar 15: Dm7b5 - G7alt
    measures += '    <measure number="15">\n'
    measures += harmony("D", "half-diminished")
    measures += note("F", 5, 256, "quarter", slur_start=True, staff=1)
    measures += note("A", 5, 256, "quarter", alter=-1, staff=1)
    measures += harmony("G", "dominant", degrees=[(9, 1, "add"), (13, -1, "add")])
    measures += note("A", 5, 256, "quarter", alter=-1, staff=1)
    measures += note("G", 5, 256, "quarter", slur_stop=True, staff=1)
    measures += backup(1024)
    measures += note("D", 3, 256, "quarter", staff=2)
    measures += note("A", 3, 128, "eighth", alter=-1, chord=True, staff=2)
    measures += note("F", 3, 128, "eighth", staff=2)
    measures += note("G", 2, 256, "quarter", staff=2)
    measures += note("F", 3, 256, "quarter", staff=2)
    measures += '    </measure>\n'
    
    # Bar 16: Cm9 - section end
    measures += '    <measure number="16">\n'
    measures += harmony("C", "minor", degrees=[(9, 0, "add")])
    measures += note("C", 5, 512, "half", slur_start=True, staff=1)
    measures += note("E", 5, 256, "quarter", alter=-1, staff=1)
    measures += note("D", 5, 256, "quarter", slur_stop=True, staff=1)
    measures += backup(1024)
    measures += note("C", 3, 512, "half", staff=2)
    measures += note("G", 3, 256, "quarter", chord=True, staff=2)
    measures += note("E", 3, 256, "quarter", alter=-1, staff=2)
    measures += note("B", 2, 256, "quarter", alter=-1, chord=True, staff=2)
    measures += '    </measure>\n'
    
    return measures

# ============ SECTION B (bars 17-32): Contrasting, more turbulent ============
def section_b():
    measures = ""
    
    # Bar 17: Ebm9 - new key area
    measures += '    <measure number="17">\n'
    measures += direction("Intensifying", dynamic="mf")
    measures += harmony("E", "minor", degrees=[(9, 0, "add")])
    # Motif A in new context
    measures += note("E", 5, 256, "quarter", alter=-1, slur_start=True, staff=1)
    measures += note("G", 5, 256, "quarter", alter=-1, staff=1)
    measures += note("D", 6, 384, "quarter", alter=-1, dot=True, accent=True, staff=1)
    measures += note("C", 6, 128, "eighth", slur_stop=True, staff=1)
    measures += backup(1024)
    measures += note("E", 2, 256, "quarter", alter=-1, staff=2)
    measures += note("B", 2, 128, "eighth", alter=-1, staff=2)
    measures += note("D", 3, 128, "eighth", alter=-1, chord=True, staff=2)
    measures += note("G", 3, 256, "quarter", alter=-1, staff=2)
    measures += note("F", 3, 256, "quarter", staff=2)
    measures += '    </measure>\n'
    
    # Bar 18: Abm7 - Db7
    measures += '    <measure number="18">\n'
    measures += harmony("A", "minor-seventh")
    measures += note("A", 5, 256, "quarter", alter=-1, slur_start=True, staff=1)
    measures += note("C", 6, 256, "quarter", alter=-1, staff=1)
    measures += harmony("D", "dominant-ninth")
    measures += note("B", 5, 256, "quarter", alter=-1, staff=1)
    measures += note("A", 5, 256, "quarter", alter=-1, slur_stop=True, staff=1)
    measures += backup(1024)
    measures += note("A", 2, 256, "quarter", alter=-1, staff=2)
    measures += note("E", 3, 256, "quarter", alter=-1, staff=2)
    measures += note("D", 2, 256, "quarter", alter=-1, staff=2)
    measures += note("A", 2, 256, "quarter", alter=-1, staff=2)
    measures += '    </measure>\n'
    
    # Bar 19: Gbmaj7#11 - color
    measures += '    <measure number="19">\n'
    measures += harmony("G", "major-seventh", degrees=[(11, 1, "add")])
    measures += note("G", 5, 512, "half", alter=-1, slur_start=True, staff=1)
    measures += note("F", 5, 256, "quarter", staff=1)
    measures += note("D", 5, 256, "quarter", alter=-1, slur_stop=True, staff=1)
    measures += backup(1024)
    measures += note("G", 2, 384, "quarter", alter=-1, dot=True, staff=2)
    measures += note("D", 3, 128, "eighth", alter=-1, staff=2)
    measures += note("F", 3, 128, "eighth", chord=True, staff=2)
    measures += note("B", 2, 256, "quarter", alter=-1, staff=2)
    measures += note("C", 3, 256, "quarter", staff=2)
    measures += '    </measure>\n'
    
    # Bar 20: Fm7 - Bb7
    measures += '    <measure number="20">\n'
    measures += harmony("F", "minor-seventh")
    measures += note("F", 5, 256, "quarter", slur_start=True, staff=1)
    measures += note("A", 5, 256, "quarter", alter=-1, staff=1)
    measures += harmony("B", "dominant", degrees=[(9, 0, "add")])
    measures += note("A", 5, 256, "quarter", alter=-1, staff=1)
    measures += note("G", 5, 256, "quarter", slur_stop=True, staff=1)
    measures += backup(1024)
    measures += note("F", 2, 256, "quarter", staff=2)
    measures += note("C", 3, 128, "eighth", staff=2)
    measures += note("E", 3, 128, "eighth", alter=-1, chord=True, staff=2)
    measures += note("B", 2, 256, "quarter", alter=-1, staff=2)
    measures += note("A", 2, 256, "quarter", alter=-1, staff=2)
    measures += '    </measure>\n'
    
    # Bar 21: Ebm9 - Motif B in new key
    measures += '    <measure number="21">\n'
    measures += harmony("E", "minor", degrees=[(9, 0, "add")])
    # Motif B transposed: Gb-F-Eb-Db
    measures += note("G", 5, 256, "quarter", alter=-1, slur_start=True, accent=True, staff=1)
    measures += note("F", 5, 256, "quarter", staff=1)
    measures += note("E", 5, 256, "quarter", alter=-1, staff=1)
    measures += note("D", 5, 256, "quarter", alter=-1, slur_stop=True, staff=1)
    measures += backup(1024)
    measures += note("E", 2, 256, "quarter", alter=-1, staff=2)
    measures += note("B", 2, 256, "quarter", alter=-1, staff=2)
    measures += note("G", 3, 128, "eighth", alter=-1, chord=True, staff=2)
    measures += note("D", 3, 256, "quarter", alter=-1, staff=2)
    measures += note("F", 3, 256, "quarter", staff=2)
    measures += '    </measure>\n'
    
    # Bar 22: Cb7#9 - tension
    measures += '    <measure number="22">\n'
    measures += harmony("C", "dominant", degrees=[(9, 1, "add")])
    measures += note("D", 5, 128, "eighth", alter=-1, slur_start=True, staff=1)
    measures += note("E", 5, 128, "eighth", alter=-1, staff=1)
    measures += note("G", 5, 256, "quarter", alter=-1, accent=True, staff=1)
    measures += note("F", 5, 256, "quarter", staff=1)
    measures += note("E", 5, 256, "quarter", alter=-1, slur_stop=True, staff=1)
    measures += backup(1024)
    measures += note("C", 2, 256, "quarter", alter=-1, staff=2)
    measures += note("G", 2, 256, "quarter", alter=-1, staff=2)
    measures += note("B", 2, 128, "eighth", alter=-1, chord=True, staff=2)
    measures += note("E", 3, 256, "quarter", alter=-1, staff=2)
    measures += note("D", 3, 256, "quarter", alter=-1, staff=2)
    measures += '    </measure>\n'
    
    # Bar 23: Bbm7 - Eb7alt
    measures += '    <measure number="23">\n'
    measures += harmony("B", "minor-seventh")
    measures += note("D", 5, 256, "quarter", alter=-1, slur_start=True, staff=1)
    measures += note("F", 5, 256, "quarter", staff=1)
    measures += harmony("E", "dominant", degrees=[(9, -1, "add"), (13, -1, "add")])
    measures += note("G", 5, 256, "quarter", alter=-1, staff=1)
    measures += note("F", 5, 256, "quarter", slur_stop=True, staff=1)
    measures += backup(1024)
    measures += note("B", 2, 256, "quarter", alter=-1, staff=2)
    measures += note("F", 3, 128, "eighth", staff=2)
    measures += note("A", 3, 128, "eighth", alter=-1, chord=True, staff=2)
    measures += note("E", 2, 256, "quarter", alter=-1, staff=2)
    measures += note("D", 3, 256, "quarter", alter=-1, staff=2)
    measures += '    </measure>\n'
    
    # Bar 24: Abmaj7 - rest
    measures += '    <measure number="24">\n'
    measures += harmony("A", "major-seventh")
    measures += note("E", 5, 512, "half", alter=-1, slur_start=True, staff=1)
    measures += note("C", 5, 256, "quarter", slur_stop=True, staff=1)
    measures += rest(256, "quarter", staff=1)
    measures += backup(1024)
    measures += note("A", 2, 384, "quarter", alter=-1, dot=True, staff=2)
    measures += note("E", 3, 128, "eighth", alter=-1, staff=2)
    measures += note("G", 3, 128, "eighth", chord=True, staff=2)
    measures += note("C", 3, 256, "quarter", staff=2)
    measures += rest(256, "quarter", staff=2)
    measures += '    </measure>\n'
    
    # Bar 25: Dm7b5 - climax build
    measures += '    <measure number="25">\n'
    measures += direction(None, dynamic="f")
    measures += harmony("D", "half-diminished")
    measures += note("D", 5, 256, "quarter", slur_start=True, accent=True, staff=1)
    measures += note("F", 5, 256, "quarter", staff=1)
    measures += note("A", 5, 256, "quarter", alter=-1, staff=1)
    measures += note("C", 6, 256, "quarter", slur_stop=True, staff=1)
    measures += backup(1024)
    measures += note("D", 3, 256, "quarter", staff=2)
    measures += note("A", 3, 256, "quarter", alter=-1, chord=True, staff=2)
    measures += note("F", 3, 128, "eighth", staff=2)
    measures += note("C", 4, 128, "eighth", staff=2)
    measures += note("A", 3, 256, "quarter", alter=-1, staff=2)
    measures += '    </measure>\n'
    
    # Bar 26: G7#9 - peak tension
    measures += '    <measure number="26">\n'
    measures += harmony("G", "dominant", degrees=[(9, 1, "add")])
    measures += note("B", 5, 256, "quarter", slur_start=True, staff=1)
    measures += note("D", 6, 256, "quarter", staff=1)
    measures += note("C", 6, 256, "quarter", staff=1)
    measures += note("A", 5, 256, "quarter", alter=-1, slur_stop=True, staff=1)
    measures += backup(1024)
    measures += note("G", 2, 256, "quarter", staff=2)
    measures += note("F", 3, 256, "quarter", staff=2)
    measures += note("A", 3, 128, "eighth", alter=1, chord=True, staff=2)
    measures += note("D", 3, 128, "eighth", staff=2)
    measures += note("B", 2, 256, "quarter", staff=2)
    measures += '    </measure>\n'
    
    # Bar 27: Cm9 - momentary resolution
    measures += '    <measure number="27">\n'
    measures += harmony("C", "minor", degrees=[(9, 0, "add")])
    measures += note("G", 5, 512, "half", slur_start=True, staff=1)
    measures += note("E", 5, 256, "quarter", alter=-1, staff=1)
    measures += note("D", 5, 256, "quarter", slur_stop=True, staff=1)
    measures += backup(1024)
    measures += note("C", 3, 384, "quarter", dot=True, staff=2)
    measures += note("G", 3, 128, "eighth", staff=2)
    measures += note("E", 3, 256, "quarter", alter=-1, chord=True, staff=2)
    measures += note("B", 2, 256, "quarter", alter=-1, staff=2)
    measures += '    </measure>\n'
    
    # Bar 28: Fm7 - Bb7
    measures += '    <measure number="28">\n'
    measures += harmony("F", "minor-seventh")
    measures += note("C", 5, 256, "quarter", slur_start=True, staff=1)
    measures += note("E", 5, 256, "quarter", alter=-1, staff=1)
    measures += harmony("B", "dominant")
    measures += note("D", 5, 256, "quarter", staff=1)
    measures += note("F", 5, 256, "quarter", slur_stop=True, staff=1)
    measures += backup(1024)
    measures += note("F", 2, 256, "quarter", staff=2)
    measures += note("C", 3, 256, "quarter", staff=2)
    measures += note("B", 2, 256, "quarter", alter=-1, staff=2)
    measures += note("D", 3, 256, "quarter", staff=2)
    measures += '    </measure>\n'
    
    # Bar 29: Ebmaj7 - Ab7
    measures += '    <measure number="29">\n'
    measures += direction(None, dynamic="ff")
    measures += harmony("E", "major-seventh")
    # Motif A augmented
    measures += note("E", 5, 512, "half", alter=-1, slur_start=True, accent=True, staff=1)
    measures += harmony("A", "dominant")
    measures += note("G", 5, 256, "quarter", staff=1)
    measures += note("D", 6, 256, "quarter", slur_stop=True, staff=1)
    measures += backup(1024)
    measures += note("E", 2, 256, "quarter", alter=-1, staff=2)
    measures += note("B", 2, 256, "quarter", alter=-1, staff=2)
    measures += note("G", 3, 128, "eighth", chord=True, staff=2)
    measures += note("A", 2, 256, "quarter", alter=-1, staff=2)
    measures += note("E", 3, 256, "quarter", alter=-1, staff=2)
    measures += '    </measure>\n'
    
    # Bar 30: Dbmaj7#11 - floating
    measures += '    <measure number="30">\n'
    measures += harmony("D", "major-seventh", degrees=[(11, 1, "add")])
    measures += note("D", 6, 256, "quarter", alter=-1, slur_start=True, staff=1)
    measures += note("C", 6, 256, "quarter", staff=1)
    measures += note("A", 5, 256, "quarter", alter=-1, staff=1)
    measures += note("G", 5, 256, "quarter", slur_stop=True, staff=1)
    measures += backup(1024)
    measures += note("D", 2, 256, "quarter", alter=-1, staff=2)
    measures += note("A", 2, 256, "quarter", alter=-1, staff=2)
    measures += note("C", 3, 128, "eighth", chord=True, staff=2)
    measures += note("F", 3, 256, "quarter", staff=2)
    measures += note("G", 3, 256, "quarter", staff=2)
    measures += '    </measure>\n'
    
    # Bar 31: Dm7b5 - G7alt (ii-V to Cm)
    measures += '    <measure number="31">\n'
    measures += harmony("D", "half-diminished")
    measures += note("F", 5, 256, "quarter", slur_start=True, staff=1)
    measures += note("A", 5, 256, "quarter", alter=-1, staff=1)
    measures += harmony("G", "dominant", degrees=[(9, -1, "add"), (13, -1, "add")])
    measures += note("A", 5, 256, "quarter", alter=-1, accent=True, staff=1)
    measures += note("F", 5, 256, "quarter", slur_stop=True, staff=1)
    measures += backup(1024)
    measures += note("D", 3, 256, "quarter", staff=2)
    measures += note("A", 3, 128, "eighth", alter=-1, chord=True, staff=2)
    measures += note("C", 4, 128, "eighth", staff=2)
    measures += note("G", 2, 256, "quarter", staff=2)
    measures += note("F", 3, 256, "quarter", staff=2)
    measures += '    </measure>\n'
    
    # Bar 32: Cm7 - B section end
    measures += '    <measure number="32">\n'
    measures += harmony("C", "minor-seventh")
    measures += note("E", 5, 512, "half", alter=-1, slur_start=True, staff=1)
    measures += note("D", 5, 256, "quarter", staff=1)
    measures += note("C", 5, 256, "quarter", slur_stop=True, staff=1)
    measures += backup(1024)
    measures += note("C", 3, 512, "half", staff=2)
    measures += note("G", 3, 256, "quarter", chord=True, staff=2)
    measures += note("E", 3, 256, "quarter", alter=-1, staff=2)
    measures += '    </measure>\n'
    
    return measures

# ============ SECTION A' (bars 33-48): Return, transformed ============
def section_a_prime():
    measures = ""
    
    # Bar 33: Cm9 - return of opening
    measures += '    <measure number="33">\n'
    measures += direction("A tempo, with renewed weight", dynamic="mf")
    measures += harmony("C", "minor", degrees=[(9, 0, "add")])
    # Motif A return, slightly ornamented
    measures += note("C", 5, 128, "eighth", slur_start=True, staff=1)
    measures += note("D", 5, 128, "eighth", staff=1)
    measures += note("E", 5, 256, "quarter", alter=-1, staff=1)
    measures += note("A", 5, 384, "quarter", dot=True, accent=True, staff=1)
    measures += note("G", 5, 128, "eighth", slur_stop=True, staff=1)
    measures += backup(1024)
    measures += note("C", 3, 256, "quarter", staff=2)
    measures += note("G", 3, 128, "eighth", staff=2)
    measures += note("B", 3, 128, "eighth", alter=-1, chord=True, staff=2)
    measures += note("E", 3, 256, "quarter", alter=-1, staff=2)
    measures += note("D", 3, 256, "quarter", staff=2)
    measures += '    </measure>\n'
    
    # Bar 34: Fm9 
    measures += '    <measure number="34">\n'
    measures += harmony("F", "minor", degrees=[(9, 0, "add")])
    measures += note("F", 5, 128, "eighth", slur_start=True, staff=1)
    measures += note("G", 5, 128, "eighth", staff=1)
    measures += note("A", 5, 256, "quarter", alter=-1, staff=1)
    measures += note("E", 6, 256, "quarter", alter=-1, accent=True, staff=1)
    measures += note("D", 6, 256, "quarter", alter=-1, slur_stop=True, staff=1)
    measures += backup(1024)
    measures += note("F", 2, 384, "quarter", dot=True, staff=2)
    measures += note("C", 3, 128, "eighth", staff=2)
    measures += note("E", 3, 128, "eighth", alter=-1, chord=True, staff=2)
    measures += note("A", 2, 256, "quarter", alter=-1, staff=2)
    measures += note("G", 3, 256, "quarter", staff=2)
    measures += '    </measure>\n'
    
    # Bar 35: Db7#11 - familiar tension
    measures += '    <measure number="35">\n'
    measures += harmony("D", "dominant", degrees=[(11, 1, "add")])
    measures += note("D", 6, 256, "quarter", alter=-1, slur_start=True, staff=1)
    measures += note("A", 5, 256, "quarter", alter=-1, staff=1)
    measures += note("G", 5, 256, "quarter", staff=1)
    measures += note("F", 5, 256, "quarter", slur_stop=True, staff=1)
    measures += backup(1024)
    measures += note("D", 2, 256, "quarter", alter=-1, staff=2)
    measures += note("A", 2, 256, "quarter", alter=-1, staff=2)
    measures += note("G", 3, 128, "eighth", chord=True, staff=2)
    measures += note("C", 3, 256, "quarter", staff=2)
    measures += note("F", 3, 256, "quarter", staff=2)
    measures += '    </measure>\n'
    
    # Bar 36: G7b9#9 - extreme tension
    measures += '    <measure number="36">\n'
    measures += harmony("G", "dominant", degrees=[(9, -1, "add"), (9, 1, "add")])
    measures += note("E", 5, 256, "quarter", alter=-1, slur_start=True, staff=1)
    measures += note("D", 5, 256, "quarter", staff=1)
    measures += note("B", 4, 512, "half", slur_stop=True, staff=1)
    measures += backup(1024)
    measures += note("G", 2, 256, "quarter", staff=2)
    measures += note("F", 3, 256, "quarter", staff=2)
    measures += note("A", 3, 256, "quarter", alter=-1, chord=True, staff=2)
    measures += note("D", 3, 256, "quarter", alter=-1, staff=2)
    measures += note("B", 2, 256, "quarter", staff=2)
    measures += '    </measure>\n'
    
    # Bar 37: Cm7 - Motif B return transformed
    measures += '    <measure number="37">\n'
    measures += harmony("C", "minor-seventh")
    # Motif B retrograde: Bb-C-D-Eb
    measures += note("B", 4, 256, "quarter", alter=-1, slur_start=True, staff=1)
    measures += note("C", 5, 256, "quarter", staff=1)
    measures += note("D", 5, 256, "quarter", staff=1)
    measures += note("E", 5, 256, "quarter", alter=-1, slur_stop=True, staff=1)
    measures += backup(1024)
    measures += note("C", 3, 384, "quarter", dot=True, staff=2)
    measures += note("E", 3, 128, "eighth", alter=-1, staff=2)
    measures += note("G", 3, 128, "eighth", chord=True, staff=2)
    measures += note("B", 2, 256, "quarter", alter=-1, staff=2)
    measures += note("D", 3, 256, "quarter", staff=2)
    measures += '    </measure>\n'
    
    # Bar 38: Ab13
    measures += '    <measure number="38">\n'
    measures += harmony("A", "dominant", degrees=[(13, 0, "add")])
    measures += note("G", 5, 256, "quarter", slur_start=True, staff=1)
    measures += note("A", 5, 256, "quarter", alter=-1, staff=1)
    measures += note("C", 6, 256, "quarter", staff=1)
    measures += note("B", 5, 256, "quarter", alter=-1, slur_stop=True, staff=1)
    measures += backup(1024)
    measures += note("A", 2, 256, "quarter", alter=-1, staff=2)
    measures += note("E", 3, 256, "quarter", alter=-1, staff=2)
    measures += note("G", 3, 128, "eighth", chord=True, staff=2)
    measures += note("C", 3, 256, "quarter", staff=2)
    measures += note("F", 3, 256, "quarter", staff=2)
    measures += '    </measure>\n'
    
    # Bar 39: Bbm7 - Eb7
    measures += '    <measure number="39">\n'
    measures += harmony("B", "minor-seventh")
    measures += note("B", 5, 256, "quarter", alter=-1, slur_start=True, staff=1)
    measures += note("A", 5, 256, "quarter", alter=-1, staff=1)
    measures += harmony("E", "dominant-ninth")
    measures += note("G", 5, 256, "quarter", staff=1)
    measures += note("F", 5, 256, "quarter", slur_stop=True, staff=1)
    measures += backup(1024)
    measures += note("B", 2, 256, "quarter", alter=-1, staff=2)
    measures += note("F", 3, 128, "eighth", staff=2)
    measures += note("A", 3, 128, "eighth", alter=-1, chord=True, staff=2)
    measures += note("E", 2, 256, "quarter", alter=-1, staff=2)
    measures += note("G", 3, 256, "quarter", staff=2)
    measures += '    </measure>\n'
    
    # Bar 40: Abmaj7 - floating
    measures += '    <measure number="40">\n'
    measures += harmony("A", "major-seventh")
    measures += note("E", 5, 512, "half", alter=-1, slur_start=True, staff=1)
    measures += note("C", 5, 256, "quarter", staff=1)
    measures += note("D", 5, 256, "quarter", slur_stop=True, staff=1)
    measures += backup(1024)
    measures += note("A", 2, 384, "quarter", alter=-1, dot=True, staff=2)
    measures += note("E", 3, 128, "eighth", alter=-1, staff=2)
    measures += note("G", 3, 128, "eighth", chord=True, staff=2)
    measures += note("C", 3, 256, "quarter", staff=2)
    measures += note("D", 3, 256, "quarter", staff=2)
    measures += '    </measure>\n'
    
    # Bar 41: Cm9 - building again
    measures += '    <measure number="41">\n'
    measures += direction(None, dynamic="f")
    measures += harmony("C", "minor", degrees=[(9, 0, "add")])
    # Motif A combined with B
    measures += note("C", 5, 128, "eighth", slur_start=True, staff=1)
    measures += note("E", 5, 128, "eighth", alter=-1, staff=1)
    measures += note("A", 5, 256, "quarter", accent=True, staff=1)
    measures += note("G", 5, 256, "quarter", staff=1)
    measures += note("F", 5, 256, "quarter", slur_stop=True, staff=1)
    measures += backup(1024)
    measures += note("C", 3, 256, "quarter", staff=2)
    measures += note("G", 3, 256, "quarter", staff=2)
    measures += note("E", 3, 128, "eighth", alter=-1, chord=True, staff=2)
    measures += note("B", 2, 256, "quarter", alter=-1, staff=2)
    measures += note("D", 3, 256, "quarter", staff=2)
    measures += '    </measure>\n'
    
    # Bar 42: Fm7 - Bb13
    measures += '    <measure number="42">\n'
    measures += harmony("F", "minor-seventh")
    measures += note("E", 5, 256, "quarter", alter=-1, slur_start=True, staff=1)
    measures += note("D", 5, 256, "quarter", staff=1)
    measures += harmony("B", "dominant", degrees=[(13, 0, "add")])
    measures += note("C", 5, 256, "quarter", staff=1)
    measures += note("B", 4, 256, "quarter", alter=-1, slur_stop=True, staff=1)
    measures += backup(1024)
    measures += note("F", 2, 256, "quarter", staff=2)
    measures += note("E", 3, 256, "quarter", alter=-1, staff=2)
    measures += note("B", 2, 256, "quarter", alter=-1, staff=2)
    measures += note("A", 3, 256, "quarter", alter=-1, staff=2)
    measures += '    </measure>\n'
    
    # Bar 43: Ebmaj7#11 - bright moment
    measures += '    <measure number="43">\n'
    measures += harmony("E", "major-seventh", degrees=[(11, 1, "add")])
    measures += note("E", 5, 384, "quarter", alter=-1, dot=True, slur_start=True, staff=1)
    measures += note("G", 5, 128, "eighth", staff=1)
    measures += note("B", 5, 256, "quarter", alter=-1, staff=1)
    measures += note("A", 5, 256, "quarter", slur_stop=True, staff=1)
    measures += backup(1024)
    measures += note("E", 2, 256, "quarter", alter=-1, staff=2)
    measures += note("B", 2, 256, "quarter", alter=-1, staff=2)
    measures += note("G", 3, 128, "eighth", chord=True, staff=2)
    measures += note("D", 3, 256, "quarter", staff=2)
    measures += note("A", 3, 256, "quarter", staff=2)
    measures += '    </measure>\n'
    
    # Bar 44: Dm7b5 - G7alt
    measures += '    <measure number="44">\n'
    measures += direction(None, dynamic="ff")
    measures += harmony("D", "half-diminished")
    measures += note("A", 5, 256, "quarter", alter=-1, slur_start=True, accent=True, staff=1)
    measures += note("F", 5, 256, "quarter", staff=1)
    measures += harmony("G", "dominant", degrees=[(9, -1, "add"), (13, -1, "add")])
    measures += note("D", 5, 256, "quarter", staff=1)
    measures += note("B", 4, 256, "quarter", slur_stop=True, staff=1)
    measures += backup(1024)
    measures += note("D", 3, 256, "quarter", staff=2)
    measures += note("A", 3, 256, "quarter", alter=-1, chord=True, staff=2)
    measures += note("G", 2, 256, "quarter", staff=2)
    measures += note("F", 3, 256, "quarter", staff=2)
    measures += '    </measure>\n'
    
    # Bar 45: Cm9 - final approach
    measures += '    <measure number="45">\n'
    measures += harmony("C", "minor", degrees=[(9, 0, "add")])
    measures += note("C", 5, 512, "half", slur_start=True, staff=1)
    measures += note("E", 5, 256, "quarter", alter=-1, staff=1)
    measures += note("G", 5, 256, "quarter", slur_stop=True, staff=1)
    measures += backup(1024)
    measures += note("C", 3, 512, "half", staff=2)
    measures += note("G", 3, 256, "quarter", chord=True, staff=2)
    measures += note("E", 3, 256, "quarter", alter=-1, staff=2)
    measures += '    </measure>\n'
    
    # Bar 46: Fm7 - Bb7
    measures += '    <measure number="46">\n'
    measures += harmony("F", "minor-seventh")
    measures += note("A", 5, 256, "quarter", alter=-1, slur_start=True, staff=1)
    measures += note("G", 5, 256, "quarter", staff=1)
    measures += harmony("B", "dominant")
    measures += note("F", 5, 256, "quarter", staff=1)
    measures += note("D", 5, 256, "quarter", slur_stop=True, staff=1)
    measures += backup(1024)
    measures += note("F", 2, 256, "quarter", staff=2)
    measures += note("C", 3, 256, "quarter", staff=2)
    measures += note("B", 2, 256, "quarter", alter=-1, staff=2)
    measures += note("A", 2, 256, "quarter", alter=-1, staff=2)
    measures += '    </measure>\n'
    
    # Bar 47: Ebmaj7 - Dm7b5 - G7alt
    measures += '    <measure number="47">\n'
    measures += direction("rit.", placement="above")
    measures += harmony("E", "major-seventh")
    measures += note("E", 5, 256, "quarter", alter=-1, slur_start=True, staff=1)
    measures += harmony("D", "half-diminished")
    measures += note("F", 5, 256, "quarter", staff=1)
    measures += harmony("G", "dominant", degrees=[(9, -1, "add")])
    measures += note("A", 5, 256, "quarter", alter=-1, staff=1)
    measures += note("G", 5, 256, "quarter", slur_stop=True, staff=1)
    measures += backup(1024)
    measures += note("E", 2, 256, "quarter", alter=-1, staff=2)
    measures += note("D", 3, 256, "quarter", staff=2)
    measures += note("G", 2, 256, "quarter", staff=2)
    measures += note("F", 3, 256, "quarter", staff=2)
    measures += '    </measure>\n'
    
    # Bar 48: Cm9 - final
    measures += '    <measure number="48">\n'
    measures += direction(None, dynamic="p")
    measures += harmony("C", "minor", degrees=[(9, 0, "add")])
    measures += note("C", 5, 1024, "whole", fermata=True, staff=1)
    measures += backup(1024)
    measures += note("C", 3, 1024, "whole", staff=2)
    measures += note("G", 3, 1024, "whole", chord=True, staff=2)
    measures += note("E", 3, 1024, "whole", alter=-1, chord=True, staff=2)
    measures += barline("light-heavy")
    measures += '    </measure>\n'
    
    return measures

def main():
    # Build complete MusicXML
    xml = get_header()
    xml += section_a()
    xml += section_b()
    xml += section_a_prime()
    xml += get_footer()
    
    # Write file
    output_path = os.path.join(os.path.dirname(__file__), "..", "scores", "testV1-Mingus.musicxml")
    output_path = os.path.normpath(output_path)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(xml)
    
    print(f"Generated: {output_path}")
    print("48-bar Mingus-inspired lead sheet complete.")
    print("Form: A(16) - B(16) - A'(16)")
    print("Key: C minor, Tempo: Slow (q=54)")
    print("Features:")
    print("  - Motif A: rising m3 to tritone (C-Eb-A)")
    print("  - Motif B: descending blues cell (Eb-D-C-Bb)")
    print("  - LH: Rhythmic 2-4 note voicings, guide tones, tensions")
    print("  - Harmony: minor 9ths, dominant 7ths, half-dim, maj7#11")
    print("  - Dynamics: mp -> mf -> f -> ff -> p")

if __name__ == "__main__":
    main()



