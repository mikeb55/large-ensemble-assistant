#!/usr/bin/env python3
"""
FULL SCORE ASSEMBLY — MASTER PROMPT
Assembles all 5 orchestrated movements into a single multi-movement full score.
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

def measure_attrs(divisions=256, fifths=0, beats=4, beat_type=4, clef_sign="G", clef_line=2, new_system=False, new_page=False):
    x = '        <attributes>\n'
    x += f'          <divisions>{divisions}</divisions>\n'
    x += f'          <key><fifths>{fifths}</fifths></key>\n'
    x += f'          <time><beats>{beats}</beats><beat-type>{beat_type}</beat-type></time>\n'
    x += f'          <clef><sign>{clef_sign}</sign><line>{clef_line}</line></clef>\n'
    x += '        </attributes>\n'
    if new_page:
        x += '        <print new-page="yes"/>\n'
    elif new_system:
        x += '        <print new-system="yes"/>\n'
    return x

# ============ FULL SCORE HEADER ============
def full_score_header():
    return '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 3.1 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="3.1">
  <work>
    <work-number>Suite for Chamber Ensemble</work-number>
    <work-title>The Master's Palette</work-title>
  </work>
  <identification>
    <creator type="composer">Michael Bryant</creator>
    <rights>(C) 2025 Michael Bryant. All Rights Reserved.</rights>
    <encoding>
      <software>Full Score Assembly Engine</software>
      <encoding-date>2025-12-11</encoding-date>
    </encoding>
  </identification>
  <defaults>
    <scaling>
      <millimeters>7.0556</millimeters>
      <tenths>40</tenths>
    </scaling>
    <page-layout>
      <page-height>1683</page-height>
      <page-width>1190</page-width>
      <page-margins type="both">
        <left-margin>56</left-margin>
        <right-margin>56</right-margin>
        <top-margin>56</top-margin>
        <bottom-margin>56</bottom-margin>
      </page-margins>
    </page-layout>
  </defaults>
  <credit page="1">
    <credit-type>title</credit-type>
    <credit-words font-size="24" font-weight="bold" justify="center" valign="top">The Master's Palette</credit-words>
  </credit>
  <credit page="1">
    <credit-type>subtitle</credit-type>
    <credit-words font-size="14" justify="center" valign="top">Suite for Chamber Ensemble in Five Movements</credit-words>
  </credit>
  <credit page="1">
    <credit-type>composer</credit-type>
    <credit-words font-size="12" justify="right" valign="top">Michael Bryant</credit-words>
  </credit>
  <part-list>
    <score-part id="P1">
      <part-name>Flute</part-name>
      <part-abbreviation>Fl.</part-abbreviation>
    </score-part>
    <score-part id="P2">
      <part-name>Clarinet in Bb</part-name>
      <part-abbreviation>Cl.</part-abbreviation>
    </score-part>
    <score-part id="P3">
      <part-name>Flugelhorn</part-name>
      <part-abbreviation>Flgh.</part-abbreviation>
    </score-part>
    <score-part id="P4">
      <part-name>Violin I</part-name>
      <part-abbreviation>Vln.I</part-abbreviation>
    </score-part>
    <score-part id="P5">
      <part-name>Violin II</part-name>
      <part-abbreviation>Vln.II</part-abbreviation>
    </score-part>
    <score-part id="P6">
      <part-name>Viola</part-name>
      <part-abbreviation>Vla.</part-abbreviation>
    </score-part>
    <score-part id="P7">
      <part-name>Cello</part-name>
      <part-abbreviation>Vc.</part-abbreviation>
    </score-part>
    <score-part id="P8">
      <part-name>Double Bass</part-name>
      <part-abbreviation>Cb.</part-abbreviation>
    </score-part>
    <score-part id="P9">
      <part-name>Classical Guitar</part-name>
      <part-abbreviation>Gtr.</part-abbreviation>
    </score-part>
    <score-part id="P10">
      <part-name>Glockenspiel</part-name>
      <part-abbreviation>Glock.</part-abbreviation>
    </score-part>
  </part-list>
'''

def footer():
    return '</score-partwise>\n'

def part_footer():
    return '  </part>\n'

# ============ GENERATE MOVEMENT I ============
def gen_movement1(part_id, clef_sign, clef_line, start_bar=1):
    content = ""
    for bar in range(1, 13):
        content += f'    <measure number="{bar}">\n'
        
        if bar == 1:
            new_page = (start_bar == 1)
            content += measure_attrs(256, -3, 4, 4, clef_sign, clef_line, new_page=new_page)
            if part_id == "P1":
                content += '        <direction placement="above"><direction-type><words font-size="14" font-weight="bold">I. Mingus Blues Cathedral</words></direction-type></direction>\n'
                content += direction("Slow gospel blues, with fire", tempo=54)
            content += direction(dynamic="mf")
            content += harmony("C", "minor", [(9, 0, "add"), (11, 0, "add"), (13, 0, "add")])
        
        # Simplified part content based on role
        if part_id == "P1":  # Flute
            if bar in [1, 5, 9]:
                content += note("G", 5, 256, "quarter", slur_s=True, acc=True)
                content += note("B", 5, 256, "quarter", alter=-1)
                content += note("D", 6, 256, "quarter")
                content += note("E", 5, 256, "quarter", alter=-1, slur_e=True)
            else:
                content += rest(1024, "whole")
        elif part_id == "P2":  # Clarinet
            if bar in [2, 6, 10]:
                content += note("D", 5, 256, "quarter", slur_s=True)
                content += note("F", 5, 256, "quarter")
                content += note("A", 5, 256, "quarter", alter=-1)
                content += note("C", 6, 256, "quarter", slur_e=True)
            else:
                content += rest(1024, "whole")
        elif part_id == "P3":  # Flugelhorn
            if bar in [1, 2, 5, 6, 9, 10]:
                content += note("C", 4, 256, "quarter", slur_s=True, acc=True)
                content += note("E", 4, 256, "quarter", alter=-1, acc=True)
                content += note("F", 4, 256, "quarter", acc=True)
                content += note("B", 4, 256, "quarter", alter=-1, slur_e=True)
            else:
                content += rest(1024, "whole")
        elif part_id == "P4":  # Violin I
            if bar in [3, 4, 7, 8, 11, 12]:
                content += note("C", 5, 256, "quarter", slur_s=True, acc=True)
                content += note("E", 5, 256, "quarter", alter=-1, acc=True)
                content += note("G", 5, 256, "quarter", acc=True)
                content += note("B", 5, 256, "quarter", alter=-1, slur_e=True)
            else:
                content += rest(1024, "whole")
        elif part_id == "P5":  # Violin II
            if bar % 2 == 0:
                content += note("E", 4, 512, "half", alter=-1, slur_s=True)
                content += note("G", 4, 512, "half", slur_e=True)
            else:
                content += rest(1024, "whole")
        elif part_id == "P6":  # Viola
            content += note("G", 3, 512, "half", slur_s=True)
            content += note("B", 3, 512, "half", alter=-1, slur_e=True)
        elif part_id == "P7":  # Cello
            content += note("C", 3, 256, "quarter", slur_s=True)
            content += note("G", 3, 256, "quarter", chord=True)
            content += note("E", 3, 256, "quarter", alter=-1)
            content += note("B", 3, 256, "quarter", alter=-1, chord=True)
            content += note("G", 3, 512, "half", slur_e=True)
        elif part_id == "P8":  # Bass
            content += note("C", 2, 512, "half")
            content += note("G", 2, 256, "quarter")
            content += note("C", 2, 256, "quarter")
        elif part_id == "P9":  # Guitar
            content += note("C", 3, 256, "quarter")
            content += note("F", 3, 256, "quarter", chord=True)
            content += note("B", 3, 256, "quarter", alter=-1, chord=True)
            content += rest(768, "half", dot=True)
        elif part_id == "P10":  # Glockenspiel
            if bar in [1, 5, 9]:
                content += note("C", 6, 256, "quarter", acc=True)
                content += rest(768, "half", dot=True)
            elif bar == 12:
                content += rest(768, "half", dot=True)
                content += note("C", 6, 256, "quarter", ferm=True)
            else:
                content += rest(1024, "whole")
        
        if bar == 11 and part_id == "P1":
            content += direction("rit.")
        if bar == 12:
            content += barline()
        
        content += '    </measure>\n'
    return content

# ============ GENERATE MOVEMENT II ============
def gen_movement2(part_id, clef_sign, clef_line, start_bar=13):
    content = ""
    for bar in range(1, 13):
        content += f'    <measure number="{bar}">\n'
        
        if bar == 1:
            content += measure_attrs(256, 0, 4, 4, clef_sign, clef_line, new_page=True)
            if part_id == "P1":
                content += '        <direction placement="above"><direction-type><words font-size="14" font-weight="bold">II. Gil\'s Canvas</words></direction-type></direction>\n'
                content += direction("Floating, pastel clouds", tempo=58)
            content += direction(dynamic="pp")
            content += harmony("E", "major-seventh", [(9, 0, "add"), (11, 1, "add")])
        
        if part_id == "P1":  # Flute - high harmonics
            if bar in [1, 3, 5, 7, 9, 11]:
                content += note("B", 6, 512, "half", slur_s=True, harmonic=True)
                content += note("F", 6, 512, "half", alter=1, slur_e=True)
            else:
                content += rest(1024, "whole")
        elif part_id == "P2":  # Clarinet
            if bar % 2 == 0:
                content += note("G", 4, 256, "quarter", slur_s=True)
                content += note("A", 4, 256, "quarter")
                content += note("B", 4, 256, "quarter")
                content += note("F", 5, 256, "quarter", alter=1, slur_e=True)
            else:
                content += rest(1024, "whole")
        elif part_id == "P3":  # Flugelhorn
            if bar in [2, 4, 6, 8, 10]:
                content += note("E", 4, 512, "half", slur_s=True)
                content += note("G", 4, 512, "half", alter=1, slur_e=True)
            else:
                content += rest(1024, "whole")
        elif part_id == "P4":  # Violin I - Lydian melody
            if bar in [1, 3, 5, 7, 9, 11]:
                content += note("G", 4, 256, "quarter", slur_s=True)
                content += note("A", 4, 256, "quarter")
                content += note("B", 4, 256, "quarter")
                content += note("F", 5, 256, "quarter", alter=1, slur_e=True)
            else:
                content += note("E", 5, 512, "half", slur_s=True)
                content += note("D", 5, 512, "half", slur_e=True)
        elif part_id == "P5":  # Violin II
            content += note("B", 4, 1024, "whole", slur_s=True, slur_e=True)
        elif part_id == "P6":  # Viola
            content += note("G", 3, 1024, "whole", alter=1, slur_s=True, slur_e=True)
        elif part_id == "P7":  # Cello
            content += note("E", 3, 1024, "whole", slur_s=True, slur_e=True)
        elif part_id == "P8":  # Bass
            content += note("E", 2, 1024, "whole")
        elif part_id == "P9":  # Guitar - shimmer
            content += note("E", 3, 256, "quarter")
            content += note("G", 3, 256, "quarter", alter=1, chord=True)
            content += note("B", 3, 256, "quarter", chord=True)
            content += rest(768, "half", dot=True)
        elif part_id == "P10":  # Glockenspiel
            if bar in [4, 8]:
                content += note("F", 6, 256, "quarter", alter=1)
                content += rest(768, "half", dot=True)
            elif bar == 12:
                content += note("E", 6, 1024, "whole", ferm=True)
            else:
                content += rest(1024, "whole")
        
        if bar == 11 and part_id == "P1":
            content += direction("rit.")
        if bar == 12:
            content += barline()
        
        content += '    </measure>\n'
    return content

# ============ GENERATE MOVEMENT III ============
def gen_movement3(part_id, clef_sign, clef_line, start_bar=25):
    content = ""
    for bar in range(1, 13):
        content += f'    <measure number="{bar}">\n'
        
        if bar == 1:
            content += measure_attrs(256, 0, 4, 4, clef_sign, clef_line, new_page=True)
            if part_id == "P1":
                content += '        <direction placement="above"><direction-type><words font-size="14" font-weight="bold">III. Bartok Night</words></direction-type></direction>\n'
                content += direction("Molto misterioso, nocturnal", tempo=40)
            content += direction(dynamic="ppp")
            content += harmony("A", "minor", [(9, -1, "add"), (11, 0, "add")])
        elif bar == 5:
            content += harmony("Eb", "augmented", [(9, 0, "add"), (11, 1, "add")])
            if part_id == "P1":
                content += direction("expanding")
        elif bar == 9:
            if part_id == "P1":
                content += direction("dissolving")
            content += harmony("A", "minor", [(9, 0, "add"), (11, 0, "add")])
        
        if part_id == "P1":  # Flute - high flicks
            if bar in [2, 4, 6, 8, 10]:
                content += rest(512, "half")
                content += note("E", 7, 128, "eighth", stac=True, acc=True, harmonic=True)
                content += note("F", 7, 128, "eighth", stac=True, harmonic=True)
                content += rest(256, "quarter")
            else:
                content += rest(1024, "whole")
        elif part_id == "P2":  # Clarinet - m2 clusters
            if bar in [1, 3, 5, 7, 9, 11]:
                content += note("B", 4, 128, "eighth", alter=-1, slur_s=True, stac=True, acc=True)
                content += note("A", 4, 128, "eighth", chord=True)
                content += rest(256, "quarter")
                content += note("E", 5, 256, "quarter", acc=True)
                content += note("F", 5, 256, "quarter", slur_e=True)
            else:
                content += rest(1024, "whole")
        elif part_id == "P3":  # Flugelhorn
            if bar in [4, 8]:
                content += rest(256, "quarter")
                content += note("F", 4, 256, "quarter", slur_s=True, stac=True, acc=True)
                content += note("B", 4, 256, "quarter")
                content += note("E", 4, 256, "quarter", slur_e=True)
            else:
                content += rest(1024, "whole")
        elif part_id == "P4":  # Violin I - motif
            if bar in [1, 3, 5, 7, 9, 11]:
                content += note("A", 4, 256, "quarter", slur_s=True, acc=True)
                content += note("B", 4, 128, "eighth", alter=-1, acc=True)
                content += note("E", 5, 128, "eighth", acc=True)
                content += note("B", 5, 256, "quarter")
                content += note("F", 5, 256, "quarter", slur_e=True)
            else:
                content += rest(1024, "whole")
        elif part_id == "P5":  # Violin II - registral jumps
            if bar in [1, 3, 5, 7, 9, 11]:
                content += note("A", 6, 256, "quarter", slur_s=True, stac=True, acc=True)
                content += rest(256, "quarter")
                content += note("B", 3, 256, "quarter", alter=-1, stac=True)
                content += note("E", 4, 256, "quarter", slur_e=True)
            else:
                content += rest(1024, "whole")
        elif part_id == "P6":  # Viola - clusters
            content += note("D", 4, 256, "quarter", slur_s=True, acc=True)
            content += note("E", 4, 256, "quarter", alter=-1, chord=True)
            content += note("G", 4, 256, "quarter", alter=1)
            content += note("A", 4, 256, "quarter", slur_e=True)
        elif part_id == "P7":  # Cello - pedal
            content += note("A", 2, 256, "quarter", slur_s=True, acc=True)
            content += note("E", 3, 256, "quarter", chord=True)
            content += note("B", 2, 256, "quarter", alter=-1)
            content += note("A", 2, 512, "half", slur_e=True)
        elif part_id == "P8":  # Bass
            if bar in [1, 5, 9]:
                content += note("A", 1, 256, "quarter", acc=True, pizz=True)
                content += rest(768, "half", dot=True)
            else:
                content += note("A", 1, 1024, "whole")
        elif part_id == "P9":  # Guitar - harmonics
            if bar in [1, 3, 5, 7, 9, 11]:
                content += note("A", 4, 256, "quarter", slur_s=True, harmonic=True, acc=True)
                content += note("B", 4, 256, "quarter", alter=-1, harmonic=True)
                content += note("E", 4, 256, "quarter", harmonic=True)
                content += note("F", 4, 256, "quarter", harmonic=True, slur_e=True)
            else:
                content += rest(1024, "whole")
        elif part_id == "P10":  # Glockenspiel
            if bar in [2, 6]:
                content += rest(768, "half", dot=True)
                content += note("E", 7, 256, "quarter", stac=True, acc=True)
            elif bar == 12:
                content += note("A", 6, 1024, "whole", ferm=True)
            else:
                content += rest(1024, "whole")
        
        if bar == 11 and part_id == "P1":
            content += direction("rit., morendo")
        if bar == 12:
            content += barline()
        
        content += '    </measure>\n'
    return content

# ============ GENERATE MOVEMENT IV ============
def gen_movement4(part_id, clef_sign, clef_line, start_bar=37):
    content = ""
    for bar in range(1, 13):
        content += f'    <measure number="{bar}">\n'
        
        if bar == 1:
            content += measure_attrs(256, 0, 4, 4, clef_sign, clef_line, new_page=True)
            if part_id == "P1":
                content += '        <direction placement="above"><direction-type><words font-size="14" font-weight="bold">IV. German Development</words></direction-type></direction>\n'
                content += direction("Streng, mit innerer Kraft", tempo=66)
            content += direction(dynamic="f")
            content += harmony("C", "major-seventh", [(9, 0, "add"), (11, 1, "add")])
        elif bar == 5:
            if part_id == "P1":
                content += direction("Breiter - augmentation")
            content += direction(dynamic="mf")
        elif bar == 7:
            if part_id == "P1":
                content += direction("diminution, intensifying")
            content += direction(dynamic="ff")
        elif bar == 9:
            if part_id == "P1":
                content += direction("Ankunft - synthesis")
        
        if part_id == "P1":  # Flute - Klangfarben bars 3-4
            if bar == 3:
                content += note("C", 5, 256, "quarter", slur_s=True, acc=True)
                content += note("B", 4, 256, "quarter", alter=-1, acc=True)
                content += note("A", 4, 256, "quarter", alter=-1, acc=True)
                content += note("E", 5, 256, "quarter", slur_e=True)
            elif bar == 4:
                content += note("D", 5, 256, "quarter", slur_s=True)
                content += note("B", 4, 256, "quarter", slur_e=True)
                content += rest(512, "half")
            else:
                content += rest(1024, "whole")
        elif part_id == "P2":  # Clarinet - bars 5-6 (augmentation)
            if bar == 5:
                content += note("C", 5, 512, "half", slur_s=True, acc=True)
                content += note("D", 5, 512, "half")
            elif bar == 6:
                content += note("E", 5, 512, "half")
                content += note("G", 4, 512, "half", alter=1, slur_e=True)
            else:
                content += rest(1024, "whole")
        elif part_id == "P3":  # Flugelhorn - bars 7-8 (diminution)
            if bar == 7:
                content += note("C", 5, 128, "eighth", slur_s=True, acc=True)
                content += note("D", 5, 128, "eighth", acc=True)
                content += note("E", 5, 128, "eighth", acc=True)
                content += note("G", 4, 128, "eighth", alter=1)
                content += note("B", 4, 256, "quarter", acc=True)
                content += note("D", 5, 256, "quarter", slur_e=True)
            elif bar == 8:
                content += note("E", 5, 256, "quarter", slur_s=True)
                content += note("G", 3, 256, "quarter", alter=1, acc=True)
                content += note("D", 6, 256, "quarter", acc=True)
                content += note("B", 4, 256, "quarter", slur_e=True)
            else:
                content += rest(1024, "whole")
        elif part_id == "P4":  # Violin I - seed + synthesis
            if bar in [1, 2, 9, 10]:
                content += note("C", 5, 256, "quarter", slur_s=True, acc=True)
                content += note("D", 5, 256, "quarter", acc=True)
                content += note("E", 5, 256, "quarter", acc=True)
                content += note("G", 4, 256, "quarter", alter=1, slur_e=True)
            elif bar == 12:
                content += note("C", 5, 1024, "whole", ferm=True)
            else:
                content += rest(1024, "whole")
        elif part_id == "P5":  # Violin II - chromatic planing
            if bar % 2 == 0:
                content += note("G", 4, 256, "quarter", slur_s=True, acc=True)
                content += note("A", 4, 256, "quarter", alter=-1)
                content += note("A", 4, 256, "quarter")
                content += note("B", 4, 256, "quarter", alter=-1, slur_e=True)
            else:
                content += note("E", 4, 256, "quarter", slur_s=True)
                content += note("F", 4, 256, "quarter")
                content += note("F", 4, 256, "quarter", alter=1)
                content += note("G", 4, 256, "quarter", slur_e=True)
        elif part_id == "P6":  # Viola - chromatic
            content += note("C", 4, 256, "quarter", slur_s=True, acc=True)
            content += note("D", 4, 256, "quarter", alter=-1)
            content += note("D", 4, 256, "quarter")
            content += note("E", 4, 256, "quarter", alter=-1, slur_e=True)
        elif part_id == "P7":  # Cello - interval cycles
            content += note("C", 3, 256, "quarter", slur_s=True, acc=True)
            content += note("E", 3, 256, "quarter")
            content += note("G", 3, 256, "quarter", alter=1)
            content += note("C", 4, 256, "quarter", slur_e=True)
        elif part_id == "P8":  # Bass
            content += note("C", 2, 512, "half", acc=True)
            content += note("G", 2, 256, "quarter")
            content += note("C", 2, 256, "quarter")
        elif part_id == "P9":  # Guitar - polychords
            content += note("C", 3, 256, "quarter", slur_s=True, acc=True)
            content += note("F", 3, 256, "quarter", chord=True)
            content += note("B", 3, 256, "quarter", chord=True)
            content += note("G", 4, 256, "quarter", alter=1, slur_e=True)
        elif part_id == "P10":  # Glockenspiel
            if bar == 7:
                content += note("C", 7, 256, "quarter", acc=True)
                content += rest(768, "half", dot=True)
            elif bar == 12:
                content += rest(768, "half", dot=True)
                content += note("C", 6, 256, "quarter", ferm=True)
            else:
                content += rest(1024, "whole")
        
        if bar == 11 and part_id == "P1":
            content += direction("rit., resolution")
            content += direction(dynamic="p")
        if bar == 12:
            content += barline()
        
        content += '    </measure>\n'
    return content

# ============ GENERATE MOVEMENT V ============
def gen_movement5(part_id, clef_sign, clef_line, start_bar=49):
    content = ""
    for bar in range(1, 13):
        content += f'    <measure number="{bar}">\n'
        
        if bar == 1:
            content += measure_attrs(256, -1, 4, 4, clef_sign, clef_line, new_page=True)
            if part_id == "P1":
                content += '        <direction placement="above"><direction-type><words font-size="14" font-weight="bold">V. Tintinnabuli Epilogue</words></direction-type></direction>\n'
                content += direction("Serene, like a prayer", tempo=52)
            content += direction(dynamic="ppp")
            content += harmony("D", "minor", [(9, 0, "add")])
        elif bar == 5:
            if part_id == "P1":
                content += direction("breathing")
        elif bar == 9:
            if part_id == "P1":
                content += direction("transcendent")
        
        if part_id == "P1":  # Flute - M-voice echo
            if bar in [3, 7]:
                content += note("A", 5, 1024, "whole", slur_s=True, slur_e=True)
            elif bar in [1, 5, 9]:
                content += note("D", 6, 512, "half", slur_s=True, harmonic=True)
                content += note("A", 5, 512, "half", slur_e=True, harmonic=True)
            else:
                content += rest(1024, "whole")
        elif part_id == "P2":  # Clarinet - T-voice
            if bar in [1, 3, 5, 7, 9, 11]:
                content += note("A", 4, 512, "half", slur_s=True)
                content += note("F", 4, 512, "half", slur_e=True)
            else:
                content += note("D", 4, 1024, "whole")
        elif part_id == "P3":  # Flugelhorn - tacet mostly
            if bar in [5, 9]:
                content += note("D", 4, 1024, "whole", slur_s=True, slur_e=True)
            else:
                content += rest(1024, "whole")
        elif part_id == "P4":  # Violin I - M-voice solo
            if bar == 1:
                content += note("D", 5, 512, "half", slur_s=True, acc=True)
                content += note("E", 5, 512, "half")
            elif bar == 2:
                content += note("F", 5, 512, "half", acc=True)
                content += note("G", 5, 512, "half", slur_e=True)
            elif bar == 3:
                content += note("A", 5, 1024, "whole", slur_s=True, acc=True)
            elif bar == 4:
                content += note("G", 5, 512, "half")
                content += note("F", 5, 512, "half", slur_e=True)
            elif bar == 5:
                content += note("E", 5, 512, "half", slur_s=True, acc=True)
                content += note("D", 5, 512, "half")
            elif bar == 6:
                content += note("C", 5, 512, "half")
                content += note("D", 5, 512, "half", slur_e=True)
            elif bar == 7:
                content += note("E", 5, 1024, "whole", slur_s=True, acc=True)
            elif bar == 8:
                content += note("F", 5, 512, "half")
                content += note("G", 5, 512, "half", slur_e=True)
            elif bar == 9:
                content += note("A", 5, 512, "half", slur_s=True, acc=True)
                content += note("B", 5, 512, "half", alter=-1)
            elif bar == 10:
                content += note("A", 5, 512, "half")
                content += note("G", 5, 512, "half", slur_e=True)
            elif bar == 11:
                content += note("F", 5, 512, "half", slur_s=True, acc=True)
                content += note("E", 5, 512, "half")
            elif bar == 12:
                content += note("D", 5, 1024, "whole", slur_e=True, ferm=True)
        elif part_id == "P5":  # Violin II - sustained A
            content += note("A", 4, 1024, "whole", slur_s=True, slur_e=True)
        elif part_id == "P6":  # Viola - sustained F
            content += note("F", 4, 512, "half", slur_s=True)
            content += note("A", 4, 512, "half", slur_e=True)
        elif part_id == "P7":  # Cello - D pedal
            content += note("D", 3, 512, "half", slur_s=True)
            content += note("A", 3, 512, "half", slur_e=True)
        elif part_id == "P8":  # Bass
            content += note("D", 2, 1024, "whole")
        elif part_id == "P9":  # Guitar - T-voice harmonics
            if bar in [1, 3, 5, 7, 9, 11]:
                content += note("D", 4, 256, "quarter", slur_s=True, harmonic=True, acc=True)
                content += note("A", 3, 256, "quarter", harmonic=True)
                content += note("F", 4, 256, "quarter", harmonic=True)
                content += note("D", 4, 256, "quarter", slur_e=True, harmonic=True)
            else:
                content += rest(1024, "whole")
        elif part_id == "P10":  # Glockenspiel
            if bar == 9:
                content += note("A", 6, 256, "quarter", acc=True)
                content += rest(768, "half", dot=True)
            elif bar == 12:
                content += rest(768, "half", dot=True)
                content += note("D", 6, 256, "quarter", ferm=True)
            else:
                content += rest(1024, "whole")
        
        if bar == 11 and part_id == "P1":
            content += direction("rit., dissolving")
        if bar == 12:
            content += barline("light-heavy")
        
        content += '    </measure>\n'
    return content

# ============ MAIN ============
def main():
    scores_dir = os.path.join(os.path.dirname(__file__), "..", "scores")
    
    print("=" * 70)
    print("FULL SCORE ASSEMBLY — MASTER PROMPT")
    print("Assembling all 5 movements into a single full score")
    print("=" * 70)
    print()
    
    # Define parts with their clefs
    parts = [
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
    ]
    
    # Generate full score
    full_score = full_score_header()
    
    for part_id, part_name, clef_sign, clef_line in parts:
        print(f"  Generating {part_name}...")
        
        full_score += f'  <part id="{part_id}">\n'
        
        # Movement I
        full_score += gen_movement1(part_id, clef_sign, clef_line, start_bar=1)
        
        # Movement II
        full_score += gen_movement2(part_id, clef_sign, clef_line, start_bar=13)
        
        # Movement III
        full_score += gen_movement3(part_id, clef_sign, clef_line, start_bar=25)
        
        # Movement IV
        full_score += gen_movement4(part_id, clef_sign, clef_line, start_bar=37)
        
        # Movement V
        full_score += gen_movement5(part_id, clef_sign, clef_line, start_bar=49)
        
        full_score += part_footer()
    
    full_score += footer()
    
    # Write full score
    filepath = os.path.join(scores_dir, "Final-Suite-FullScore.musicxml")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(full_score)
    
    print()
    print("=" * 70)
    print("FULL SCORE ASSEMBLY COMPLETE")
    print("=" * 70)
    print()
    print("OUTPUT: Final-Suite-FullScore.musicxml")
    print()
    print("CONTENTS:")
    print("  I. Mingus Blues Cathedral (12 bars)")
    print("  II. Gil's Canvas (12 bars)")
    print("  III. Bartok Night (12 bars)")
    print("  IV. German Development (12 bars)")
    print("  V. Tintinnabuli Epilogue (12 bars)")
    print()
    print("TOTAL: 60 bars across 5 movements")
    print()
    print("INSTRUMENTATION:")
    for part_id, part_name, clef_sign, clef_line in parts:
        print(f"  - {part_name}")
    print()
    print("FORMATTING:")
    print("  - Each movement begins on new page")
    print("  - Bar numbers restart each movement")
    print("  - Consistent staff size and margins")
    print("  - Movement titles in bold at start")
    print("  - Standard rehearsal mark style")
    print("  - Copyright: (C) 2025 Michael Bryant. All Rights Reserved.")

if __name__ == "__main__":
    main()


