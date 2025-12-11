#!/usr/bin/env python3
"""
2-MOVEMENT EXCELLENCE REFINEMENT PASS
Movements III (Bartók Night) and IV (German Development) only
Do NOT touch Movements I or II
"""

import os

# ============ SHARED UTILITIES ============
def n(step, oct, dur, typ, alt=None, dot=False, chord=False, 
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

def r(dur, typ, staff=1, dot=False):
    x = f"      <note><rest/><duration>{dur}</duration><type>{typ}</type>"
    if dot:
        x += "<dot/>"
    x += f"<staff>{staff}</staff></note>\n"
    return x

def h(root, kind, degs=None):
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

def d(txt=None, dyn=None, tempo=None, place="above"):
    x = f'      <direction placement="{place}">\n        <direction-type>\n'
    if txt:
        x += f'          <words font-style="italic">{txt}</words>\n'
    if dyn:
        x += f'          <dynamics><{dyn}/></dynamics>\n'
    if tempo:
        x += f'          <metronome><beat-unit>quarter</beat-unit><per-minute>{tempo}</per-minute></metronome>\n'
    x += '        </direction-type>\n      </direction>\n'
    return x

def bk(dur):
    return f"      <backup><duration>{dur}</duration></backup>\n"

def bl(style="light-heavy"):
    return f'      <barline location="right"><bar-style>{style}</bar-style></barline>\n'

def hdr(title, key=0):
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 3.1 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="3.1">
  <work><work-title>{title}</work-title></work>
  <identification>
    <creator type="composer">Original Composition</creator>
    <rights>(C) 2025 Michael Bryant. All Rights Reserved.</rights>
    <encoding><software>2-Movement Excellence Engine</software><encoding-date>2025-12-11</encoding-date></encoding>
  </identification>
  <part-list><score-part id="P1"><part-name>Piano</part-name></score-part></part-list>
  <part id="P1">
'''

def ftr():
    return '''  </part>
</score-partwise>
'''

def attr(key=0):
    return f'''      <attributes>
        <divisions>256</divisions>
        <key><fifths>{key}</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <staves>2</staves>
        <clef number="1"><sign>G</sign><line>2</line></clef>
        <clef number="2"><sign>F</sign><line>4</line></clef>
      </attributes>
'''

# ============ EXCELLENCE EVALUATION ENGINE ============
def evaluate_excellence(xml, movement_name):
    scores = {}
    details = {}
    
    # 1. Motivic Identity
    slur_count = xml.count('<slur')
    accent_count = xml.count('<accent/>')
    motif_score = min(1.0, (slur_count / 24) * 0.5 + (accent_count / 20) * 0.5)
    scores["Motivic Identity"] = motif_score
    details["Motivic Identity"] = f"slurs={slur_count}, accents={accent_count}"
    
    # 2. Motivic Development
    oct5 = xml.count('<octave>5</octave>')
    oct4 = xml.count('<octave>4</octave>')
    oct3 = xml.count('<octave>3</octave>')
    oct6 = xml.count('<octave>6</octave>')
    octave_variety = min(1.0, (oct5 + oct4 + oct3 + oct6) / 60)
    scores["Motivic Development"] = octave_variety
    details["Motivic Development"] = f"oct3={oct3}, oct4={oct4}, oct5={oct5}, oct6={oct6}"
    
    # 3. Melodic Contour
    alter_count = xml.count('<alter>')
    contour_score = min(1.0, (oct5 / 18) * 0.5 + (alter_count / 25) * 0.5)
    scores["Melodic Contour"] = contour_score
    details["Melodic Contour"] = f"oct5={oct5}, alters={alter_count}"
    
    # 4. Harmonic Colour
    harmony_count = xml.count('<harmony')
    degree_count = xml.count('<degree>')
    harmony_score = min(1.0, (harmony_count / 14) * 0.4 + (degree_count / 30) * 0.6)
    scores["Harmonic Colour"] = harmony_score
    details["Harmonic Colour"] = f"harmonies={harmony_count}, degrees={degree_count}"
    
    # 5. Phrasing & Breath
    slur_starts = xml.count('<slur type="start"')
    slur_ends = xml.count('<slur type="stop"')
    phrasing_score = min(1.0, (slur_starts / 12) * 0.5 + (slur_ends / 12) * 0.5)
    scores["Phrasing & Breath"] = phrasing_score
    details["Phrasing & Breath"] = f"slur_starts={slur_starts}, slur_ends={slur_ends}"
    
    # 6. LH Accompaniment Quality
    staff2_count = xml.count('staff="2"')
    chord_count = xml.count('<chord/>')
    lh_score = min(1.0, (staff2_count / 96) * 0.5 + (chord_count / 48) * 0.5)
    scores["LH Accompaniment"] = lh_score
    details["LH Accompaniment"] = f"staff2={staff2_count}, chords={chord_count}"
    
    # 7. Idiomatic Style
    dynamics_count = xml.count('<dynamics>')
    words_count = xml.count('<words')
    style_score = min(1.0, (dynamics_count / 6) * 0.5 + (words_count / 5) * 0.5)
    scores["Idiomatic Style"] = style_score
    details["Idiomatic Style"] = f"dynamics={dynamics_count}, expressions={words_count}"
    
    # 8. Formal Shape
    has_rit = 'rit' in xml.lower()
    has_section = any(x in xml.lower() for x in ['expanding', 'dissolving', 'ankunft', 'breiter', 'nocturnal'])
    measure_count = xml.count('<measure number=')
    formal_score = 0.0
    if has_rit:
        formal_score += 0.4
    if has_section:
        formal_score += 0.3
    if 12 <= measure_count <= 16:
        formal_score += 0.3
    scores["Formal Shape"] = formal_score
    details["Formal Shape"] = f"rit={has_rit}, sections={has_section}, measures={measure_count}"
    
    # 9. Emotional Arc
    fermata_count = xml.count('<fermata')
    ff_count = xml.count('<ff/>')
    pp_count = xml.count('<pp/>')
    emotional_score = min(1.0, (fermata_count / 1) * 0.4 + (accent_count / 15) * 0.4 + ((ff_count + pp_count) / 2) * 0.2)
    scores["Emotional Arc"] = emotional_score
    details["Emotional Arc"] = f"fermatas={fermata_count}, accents={accent_count}, dynamics extremes={ff_count+pp_count}"
    
    # 10. Engraving Quality
    has_barline = '<barline' in xml
    has_correct_bars = 12 <= measure_count <= 16
    has_staves = '<staves>2</staves>' in xml
    engraving_score = 0.0
    if has_barline:
        engraving_score += 0.4
    if has_correct_bars:
        engraving_score += 0.3
    if has_staves:
        engraving_score += 0.3
    scores["Engraving Quality"] = engraving_score
    details["Engraving Quality"] = f"barline={has_barline}, bars={measure_count}, staves={has_staves}"
    
    total = sum(scores.values())
    return total, scores, details

# ============ MOVEMENT III: BARTÓK NIGHT — REFINED ============
def gen_mvmt3_refined():
    m = ""
    
    # Bar 1: Night-music opening — sparse m2 + tritone + silence
    m += '    <measure number="1">\n'
    m += attr(0)
    m += d("Molto misterioso, night-music", tempo=40)
    m += d(dyn="pp")
    m += h("A", "minor", [(9, -1, "add"), (11, 0, "add"), (13, -1, "add")])
    m += r(256, "quarter")  # silence as texture
    m += n("A", 4, 256, "quarter", slur_s=True, stac=True, acc=True)
    m += n("B", 4, 256, "quarter", alt=-1, stac=True, acc=True)  # m2 cluster
    m += r(256, "quarter")  # more silence
    m += bk(1024)
    # LH: Dyads + pedal drone on A
    m += n("A", 2, 512, "half", staff=2)
    m += n("E", 3, 512, "half", chord=True, staff=2)
    m += n("D", 3, 256, "quarter", staff=2)
    m += n("G", 3, 256, "quarter", alt=1, chord=True, staff=2)  # tritone from D
    m += n("B", 2, 256, "quarter", staff=2)
    m += n("F", 3, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 2: Tritone leap E-Bb + registral plunge
    m += '    <measure number="2">\n'
    m += h("Eb", "augmented", [(9, 0, "add"), (11, 1, "add"), (13, 0, "add")])  # Axis: A↔Eb
    m += n("E", 5, 256, "quarter", slur_e=True, acc=True)
    m += n("B", 4, 256, "quarter", alt=-1, slur_s=True, acc=True)  # tritone from E
    m += n("F", 4, 256, "quarter", acc=True)
    m += n("A", 3, 256, "quarter", slur_e=True)  # registral plunge to low octave
    m += bk(1024)
    m += n("E", 2, 256, "quarter", alt=-1, staff=2)  # Axis Eb
    m += n("B", 2, 256, "quarter", alt=-1, chord=True, staff=2)
    m += n("G", 3, 256, "quarter", chord=True, staff=2)
    m += n("A", 2, 256, "quarter", staff=2)
    m += n("D", 3, 256, "quarter", chord=True, staff=2)
    m += n("G", 3, 256, "quarter", alt=1, chord=True, staff=2)
    m += n("C", 3, 256, "quarter", staff=2)
    m += n("F", 3, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 3: Extreme registral displacement A5→Bb3 (2-octave drop)
    m += '    <measure number="3">\n'
    m += h("Gb", "major-seventh", [(9, 0, "add"), (11, 1, "add")])  # Axis: C↔Gb
    m += n("A", 5, 256, "quarter", slur_s=True, acc=True)
    m += n("B", 3, 256, "quarter", alt=-1, acc=True)  # 2-octave drop!
    m += r(256, "quarter")  # silence
    m += n("E", 5, 256, "quarter", slur_e=True, acc=True)
    m += bk(1024)
    m += n("G", 2, 256, "quarter", alt=-1, staff=2)  # Gb axis
    m += n("D", 3, 256, "quarter", alt=-1, chord=True, staff=2)
    m += n("F", 3, 256, "quarter", chord=True, staff=2)
    m += n("B", 3, 256, "quarter", chord=True, staff=2)
    m += n("C", 3, 256, "quarter", staff=2)
    m += n("G", 3, 256, "quarter", alt=-1, chord=True, staff=2)
    m += n("E", 3, 256, "quarter", alt=-1, staff=2)
    m += n("A", 3, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 4: Sustained F with chromatic neighbour approach
    m += '    <measure number="4">\n'
    m += h("F", "major-seventh", [(9, 0, "add"), (11, 1, "add"), (13, 0, "add")])
    m += n("F", 5, 384, "quarter", dot=True, slur_s=True, acc=True)
    m += n("E", 5, 128, "eighth", acc=True)  # chromatic neighbour
    m += n("F", 5, 256, "quarter")
    m += n("B", 4, 256, "quarter", slur_e=True)  # tritone descent
    m += bk(1024)
    # Pedal F with m2 cluster above
    m += n("F", 2, 512, "half", staff=2)
    m += n("C", 3, 512, "half", chord=True, staff=2)
    m += n("E", 3, 256, "quarter", staff=2)
    m += n("F", 3, 256, "quarter", chord=True, staff=2)  # m2 cluster
    m += n("B", 3, 256, "quarter", chord=True, staff=2)
    m += n("D", 3, 256, "quarter", staff=2)
    m += n("A", 3, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 5: Arc II — Expanding with P4 leaps + axis pivot
    m += '    <measure number="5">\n'
    m += d("Expanding")
    m += d(dyn="p")
    m += h("Eb", "augmented", [(9, 0, "add"), (11, 1, "add"), (13, 0, "add")])  # Axis A↔Eb
    m += n("A", 4, 256, "quarter", slur_s=True, acc=True)
    m += n("D", 5, 256, "quarter", acc=True)  # P4 up
    m += n("E", 5, 256, "quarter", alt=-1, acc=True)  # Eb axis
    m += n("B", 5, 256, "quarter", slur_e=True)  # tritone from F
    m += bk(1024)
    m += n("E", 2, 256, "quarter", alt=-1, staff=2)
    m += n("B", 2, 256, "quarter", alt=-1, chord=True, staff=2)
    m += n("G", 3, 256, "quarter", chord=True, staff=2)
    m += n("D", 4, 256, "quarter", chord=True, staff=2)
    m += n("A", 2, 256, "quarter", staff=2)
    m += n("E", 3, 256, "quarter", chord=True, staff=2)
    m += n("B", 3, 256, "quarter", chord=True, staff=2)
    m += n("F", 3, 256, "quarter", staff=2)
    m += n("C", 4, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 6: Inversion with tritone + m2 + irregular spacing
    m += '    <measure number="6">\n'
    m += h("G#", "diminished-seventh", [(9, 0, "add"), (11, 0, "add")])
    m += n("B", 4, 384, "quarter", dot=True, slur_s=True, acc=True)
    m += n("F", 5, 128, "eighth", acc=True)  # tritone
    m += r(256, "quarter")  # irregular silence
    m += n("E", 5, 256, "quarter", slur_e=True, acc=True)
    m += bk(1024)
    m += n("G", 2, 256, "quarter", alt=1, staff=2)
    m += n("D", 3, 256, "quarter", chord=True, staff=2)
    m += n("F", 3, 256, "quarter", chord=True, staff=2)
    m += n("B", 3, 256, "quarter", chord=True, staff=2)
    m += n("E", 3, 256, "quarter", staff=2)
    m += n("B", 3, 256, "quarter", alt=-1, chord=True, staff=2)
    m += n("A", 3, 256, "quarter", staff=2)
    m += n("D", 4, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 7: Building — augmented cluster + high flick
    m += '    <measure number="7">\n'
    m += d(dyn="mf")
    m += h("C", "augmented", [(9, 0, "add"), (11, 1, "add"), (13, 0, "add")])
    m += n("E", 5, 256, "quarter", slur_s=True, acc=True)
    m += n("F", 5, 128, "eighth", acc=True)  # m2
    m += n("B", 5, 128, "eighth", acc=True)  # tritone
    m += n("A", 5, 256, "quarter", acc=True)
    m += n("E", 6, 256, "quarter", slur_e=True)  # high flick
    m += bk(1024)
    # Augmented cluster: C-E-G#
    m += n("C", 3, 256, "quarter", staff=2)
    m += n("E", 3, 256, "quarter", chord=True, staff=2)
    m += n("G", 3, 256, "quarter", alt=1, chord=True, staff=2)
    m += n("B", 3, 256, "quarter", chord=True, staff=2)
    m += n("F", 3, 256, "quarter", alt=1, staff=2)
    m += n("A", 3, 256, "quarter", chord=True, staff=2)
    m += n("D", 4, 256, "quarter", alt=1, chord=True, staff=2)
    m += n("G", 3, 256, "quarter", staff=2)
    m += n("C", 4, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 8: Peak tension — octatonic hint + axis
    m += '    <measure number="8">\n'
    m += d(dyn="f")
    m += h("E", "dominant", [(9, -1, "add"), (9, 1, "add"), (13, -1, "add")])
    m += n("B", 5, 256, "quarter", slur_s=True, acc=True)
    m += n("C", 6, 256, "quarter", acc=True)  # m2 peak
    m += n("E", 5, 256, "quarter", acc=True)
    m += n("F", 5, 256, "quarter", slur_e=True)
    m += bk(1024)
    m += n("E", 2, 256, "quarter", staff=2)
    m += n("B", 2, 256, "quarter", chord=True, staff=2)
    m += n("G", 3, 256, "quarter", alt=1, chord=True, staff=2)
    m += n("D", 4, 256, "quarter", chord=True, staff=2)
    m += n("A", 2, 256, "quarter", alt=-1, staff=2)  # octatonic
    m += n("E", 3, 256, "quarter", alt=-1, chord=True, staff=2)
    m += n("C", 4, 256, "quarter", chord=True, staff=2)
    m += n("F", 3, 256, "quarter", staff=2)
    m += n("B", 3, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 9: Arc III — Dissolving with negative space
    m += '    <measure number="9">\n'
    m += d("Dissolving")
    m += d(dyn="p")
    m += h("A", "minor-seventh", [(9, 0, "add"), (11, 0, "add"), (13, 0, "add")])
    m += n("A", 4, 256, "quarter", slur_s=True, acc=True)
    m += r(256, "quarter")  # negative space
    m += n("B", 4, 256, "quarter", alt=-1, acc=True)
    m += n("E", 5, 256, "quarter", slur_e=True)
    m += bk(1024)
    m += n("A", 2, 256, "quarter", staff=2)
    m += n("E", 3, 256, "quarter", chord=True, staff=2)
    m += n("G", 3, 256, "quarter", chord=True, staff=2)
    m += n("D", 4, 256, "quarter", chord=True, staff=2)
    m += n("C", 3, 256, "quarter", staff=2)
    m += n("G", 3, 256, "quarter", chord=True, staff=2)
    m += n("B", 3, 256, "quarter", chord=True, staff=2)
    m += n("F", 3, 256, "quarter", staff=2)
    m += n("A", 3, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 10: Fragmenting — sparse gestures with silence
    m += '    <measure number="10">\n'
    m += h("Eb", "augmented", [(9, 0, "add"), (11, 1, "add")])  # Axis
    m += n("F", 5, 256, "quarter", stac=True, acc=True)
    m += r(256, "quarter")
    m += n("E", 5, 256, "quarter", alt=-1, slur_s=True, acc=True)  # Eb
    m += n("B", 4, 256, "quarter", slur_e=True)
    m += bk(1024)
    m += n("E", 2, 256, "quarter", alt=-1, staff=2)
    m += n("B", 2, 256, "quarter", alt=-1, chord=True, staff=2)
    m += n("G", 3, 256, "quarter", chord=True, staff=2)
    m += n("A", 2, 256, "quarter", staff=2)
    m += n("E", 3, 256, "quarter", chord=True, staff=2)
    m += n("G", 3, 256, "quarter", chord=True, staff=2)
    m += n("D", 3, 256, "quarter", staff=2)
    m += n("A", 3, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 11: Near silence — irregular whispers
    m += '    <measure number="11">\n'
    m += d("rit.")
    m += d(dyn="pp")
    m += h("E", "minor", [(9, 0, "add"), (11, 0, "add"), (13, -1, "add")])
    m += r(256, "quarter")
    m += n("A", 4, 256, "quarter", slur_s=True, stac=True, acc=True)
    m += n("B", 4, 384, "quarter", alt=-1, dot=True, acc=True)
    m += n("E", 4, 128, "eighth", slur_e=True)
    m += bk(1024)
    m += n("E", 2, 256, "quarter", staff=2)
    m += n("B", 2, 256, "quarter", chord=True, staff=2)
    m += n("G", 3, 256, "quarter", chord=True, staff=2)
    m += n("D", 4, 256, "quarter", chord=True, staff=2)
    m += n("A", 2, 256, "quarter", staff=2)
    m += n("E", 3, 256, "quarter", chord=True, staff=2)
    m += n("F", 3, 256, "quarter", chord=True, staff=2)
    m += n("C", 3, 256, "quarter", staff=2)
    m += n("G", 3, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 12: Final night whisper on A pedal
    m += '    <measure number="12">\n'
    m += h("A", "minor", [(9, 0, "add"), (11, 0, "add"), (13, 0, "add")])
    m += n("F", 5, 256, "quarter", stac=True, acc=True)
    m += r(256, "quarter")
    m += n("A", 4, 512, "half", ferm=True, acc=True)
    m += bk(1024)
    m += n("A", 2, 1024, "whole", staff=2)
    m += n("E", 3, 512, "half", chord=True, staff=2)
    m += n("B", 3, 256, "quarter", chord=True, staff=2)
    m += n("D", 4, 256, "quarter", chord=True, staff=2)
    m += n("G", 3, 256, "quarter", staff=2)
    m += n("C", 4, 256, "quarter", chord=True, staff=2)
    m += bl()
    m += '    </measure>\n'
    
    return hdr("The Master's Palette - III. Bartok Night", 0) + m + ftr()

# ============ MOVEMENT IV: GERMAN DEVELOPMENT — REFINED ============
def gen_mvmt4_refined():
    m = ""
    
    # Bar 1: Exposition — clear motivic seed C-D-E-G#-B-D
    m += '    <measure number="1">\n'
    m += attr(0)
    m += d("Streng, mit innerer Spannung", tempo=66)
    m += d(dyn="f")
    m += h("C", "major-seventh", [(9, 0, "add"), (11, 1, "add"), (13, 0, "add")])
    m += n("C", 5, 256, "quarter", slur_s=True, acc=True)
    m += n("D", 5, 256, "quarter", acc=True)
    m += n("E", 5, 256, "quarter", acc=True)
    m += n("G", 4, 256, "quarter", alt=1, slur_e=True)  # G# interval
    m += bk(1024)
    # LH: Quartal stack + chromatic connectors
    m += n("C", 3, 256, "quarter", staff=2)
    m += n("G", 3, 256, "quarter", chord=True, staff=2)
    m += n("B", 3, 256, "quarter", chord=True, staff=2)
    m += n("F", 4, 256, "quarter", alt=1, chord=True, staff=2)
    m += n("E", 3, 256, "quarter", staff=2)
    m += n("A", 3, 256, "quarter", chord=True, staff=2)
    m += n("D", 4, 256, "quarter", chord=True, staff=2)
    m += n("G", 3, 256, "quarter", staff=2)
    m += n("C", 4, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 2: Completion B-D + sequence up m3
    m += '    <measure number="2">\n'
    m += h("E", "minor-seventh", [(9, 0, "add"), (11, 0, "add"), (13, 0, "add")])
    m += n("B", 4, 256, "quarter", slur_s=True, acc=True)
    m += n("D", 5, 256, "quarter", acc=True)
    # Sequence: motif up m3
    m += n("E", 5, 256, "quarter", alt=-1, acc=True)
    m += n("F", 5, 256, "quarter", alt=1, slur_e=True)
    m += bk(1024)
    m += n("E", 3, 256, "quarter", staff=2)
    m += n("B", 3, 256, "quarter", chord=True, staff=2)
    m += n("D", 4, 256, "quarter", chord=True, staff=2)
    m += n("G", 4, 256, "quarter", chord=True, staff=2)
    m += n("F", 3, 256, "quarter", alt=1, staff=2)
    m += n("C", 4, 256, "quarter", alt=1, chord=True, staff=2)
    m += n("E", 4, 256, "quarter", chord=True, staff=2)
    m += n("G", 3, 256, "quarter", staff=2)
    m += n("D", 4, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 3: INVERSION — C down to Bb, Ab, up to E
    m += '    <measure number="3">\n'
    m += h("Ab", "augmented", [(9, 0, "add"), (11, 1, "add"), (13, 0, "add")])
    m += n("C", 5, 256, "quarter", slur_s=True, acc=True)
    m += n("B", 4, 256, "quarter", alt=-1, acc=True)  # inverted direction
    m += n("A", 4, 256, "quarter", alt=-1, acc=True)
    m += n("E", 5, 256, "quarter", slur_e=True)  # interval expansion
    m += bk(1024)
    # Chromatic planing
    m += n("A", 2, 256, "quarter", alt=-1, staff=2)
    m += n("E", 3, 256, "quarter", alt=-1, chord=True, staff=2)
    m += n("C", 4, 256, "quarter", chord=True, staff=2)
    m += n("B", 2, 256, "quarter", alt=-1, staff=2)  # chromatic connector
    m += n("F", 3, 256, "quarter", chord=True, staff=2)
    m += n("D", 4, 256, "quarter", chord=True, staff=2)
    m += n("C", 3, 256, "quarter", staff=2)
    m += n("G", 3, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 4: RETROGRADE — D-B-G#-E-D-C
    m += '    <measure number="4">\n'
    m += h("D", "dominant", [(9, -1, "add"), (11, 1, "add"), (13, -1, "add")])
    m += n("D", 5, 256, "quarter", slur_s=True, acc=True)
    m += n("B", 4, 256, "quarter", acc=True)
    m += n("G", 4, 256, "quarter", alt=1, acc=True)  # G#
    m += n("E", 4, 256, "quarter", slur_e=True)
    m += bk(1024)
    # Interval cycle (C+ augmented)
    m += n("D", 3, 256, "quarter", staff=2)
    m += n("A", 3, 256, "quarter", chord=True, staff=2)
    m += n("C", 4, 256, "quarter", chord=True, staff=2)
    m += n("F", 4, 256, "quarter", alt=1, chord=True, staff=2)
    m += n("G", 3, 256, "quarter", alt=1, staff=2)  # C+ cycle
    m += n("D", 3, 256, "quarter", chord=True, staff=2)
    m += n("B", 3, 256, "quarter", chord=True, staff=2)
    m += n("E", 3, 256, "quarter", staff=2)
    m += n("A", 3, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 5: AUGMENTATION — doubled note values
    m += '    <measure number="5">\n'
    m += d("Breiter")
    m += d(dyn="mf")
    m += h("F", "major-seventh", [(9, 0, "add"), (11, 1, "add"), (13, 0, "add")])
    m += n("C", 5, 512, "half", slur_s=True, acc=True)  # augmented
    m += n("D", 5, 512, "half", slur_e=True, acc=True)
    m += bk(1024)
    # Whole-tone derived harmony
    m += n("F", 2, 256, "quarter", staff=2)
    m += n("C", 3, 256, "quarter", chord=True, staff=2)
    m += n("E", 3, 256, "quarter", chord=True, staff=2)
    m += n("B", 3, 256, "quarter", chord=True, staff=2)
    m += n("G", 2, 256, "quarter", staff=2)  # whole-tone step
    m += n("D", 3, 256, "quarter", chord=True, staff=2)
    m += n("F", 3, 256, "quarter", alt=1, chord=True, staff=2)
    m += n("A", 2, 256, "quarter", staff=2)
    m += n("E", 3, 256, "quarter", chord=True, staff=2)
    m += n("G", 3, 256, "quarter", alt=1, chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 6: Continued augmentation + interval cycle
    m += '    <measure number="6">\n'
    m += h("B", "half-diminished", [(9, 0, "add"), (11, 0, "add"), (13, -1, "add")])
    m += n("E", 5, 512, "half", slur_s=True, acc=True)
    m += n("G", 4, 512, "half", alt=1, slur_e=True, acc=True)  # G# return
    m += bk(1024)
    m += n("B", 2, 256, "quarter", staff=2)
    m += n("F", 3, 256, "quarter", chord=True, staff=2)
    m += n("A", 3, 256, "quarter", chord=True, staff=2)
    m += n("D", 4, 256, "quarter", chord=True, staff=2)
    m += n("E", 3, 256, "quarter", staff=2)  # C+ interval
    m += n("A", 3, 256, "quarter", chord=True, staff=2)
    m += n("C", 4, 256, "quarter", chord=True, staff=2)
    m += n("G", 3, 256, "quarter", alt=1, staff=2)
    m += n("D", 4, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 7: DIMINUTION — halved note values
    m += '    <measure number="7">\n'
    m += d(dyn="f")
    m += h("A", "minor-seventh", [(9, 0, "add"), (11, 0, "add"), (13, 0, "add")])
    m += n("C", 5, 128, "eighth", slur_s=True, acc=True)  # diminution
    m += n("D", 5, 128, "eighth", acc=True)
    m += n("E", 5, 128, "eighth", acc=True)
    m += n("G", 4, 128, "eighth", alt=1)  # G#
    m += n("B", 4, 256, "quarter", acc=True)
    m += n("D", 5, 128, "eighth")
    m += n("C", 5, 128, "eighth", slur_e=True)
    m += bk(1024)
    m += n("A", 2, 256, "quarter", staff=2)
    m += n("E", 3, 256, "quarter", chord=True, staff=2)
    m += n("G", 3, 256, "quarter", chord=True, staff=2)
    m += n("C", 4, 256, "quarter", chord=True, staff=2)
    m += n("D", 3, 256, "quarter", staff=2)  # guide-tone motion
    m += n("A", 3, 256, "quarter", chord=True, staff=2)
    m += n("C", 4, 256, "quarter", chord=True, staff=2)
    m += n("F", 3, 256, "quarter", staff=2)
    m += n("B", 3, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 8: KLANGFARBENMELODIE — registral exchange
    m += '    <measure number="8">\n'
    m += h("E", "dominant", [(9, 1, "add"), (11, 0, "add"), (13, -1, "add")])
    m += n("E", 5, 256, "quarter", slur_s=True, acc=True)
    m += n("G", 3, 256, "quarter", alt=1, acc=True)  # 2 octaves down!
    m += n("D", 6, 256, "quarter", acc=True)  # 2+ octaves up!
    m += n("B", 4, 256, "quarter", slur_e=True)  # return to middle
    m += bk(1024)
    m += n("E", 2, 256, "quarter", staff=2)
    m += n("B", 2, 256, "quarter", chord=True, staff=2)
    m += n("G", 3, 256, "quarter", alt=1, chord=True, staff=2)
    m += n("D", 4, 256, "quarter", chord=True, staff=2)
    m += n("A", 2, 256, "quarter", staff=2)
    m += n("E", 3, 256, "quarter", chord=True, staff=2)
    m += n("C", 4, 256, "quarter", chord=True, staff=2)
    m += n("F", 3, 256, "quarter", staff=2)
    m += n("B", 3, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 9: Ankunft — thematic synthesis + climax
    m += '    <measure number="9">\n'
    m += d("Ankunft")
    m += d(dyn="ff")
    m += h("C", "major-seventh", [(9, 0, "add"), (11, 1, "add"), (13, 0, "add")])
    m += n("C", 5, 256, "quarter", slur_s=True, acc=True)
    m += n("E", 5, 256, "quarter", acc=True)
    m += n("D", 5, 256, "quarter", acc=True)
    m += n("G", 5, 256, "quarter", alt=1, slur_e=True)  # climax G#
    m += bk(1024)
    m += n("C", 3, 256, "quarter", staff=2)
    m += n("G", 3, 256, "quarter", chord=True, staff=2)
    m += n("B", 3, 256, "quarter", chord=True, staff=2)
    m += n("F", 4, 256, "quarter", alt=1, chord=True, staff=2)
    m += n("E", 3, 256, "quarter", staff=2)
    m += n("A", 3, 256, "quarter", chord=True, staff=2)
    m += n("D", 4, 256, "quarter", chord=True, staff=2)
    m += n("G", 3, 256, "quarter", staff=2)
    m += n("C", 4, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 10: Final sequence with interval cycle return
    m += '    <measure number="10">\n'
    m += h("G", "dominant", [(9, 0, "add"), (11, 1, "add"), (13, 0, "add")])
    m += n("B", 5, 256, "quarter", slur_s=True, acc=True)
    m += n("D", 6, 256, "quarter", acc=True)
    m += n("C", 6, 256, "quarter", acc=True)
    m += n("E", 5, 256, "quarter", slur_e=True)  # sequence
    m += bk(1024)
    m += n("G", 2, 256, "quarter", staff=2)
    m += n("D", 3, 256, "quarter", chord=True, staff=2)
    m += n("F", 3, 256, "quarter", alt=1, chord=True, staff=2)
    m += n("C", 4, 256, "quarter", chord=True, staff=2)
    m += n("B", 2, 256, "quarter", staff=2)
    m += n("F", 3, 256, "quarter", chord=True, staff=2)
    m += n("A", 3, 256, "quarter", chord=True, staff=2)
    m += n("E", 3, 256, "quarter", staff=2)
    m += n("B", 3, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 11: Cadential approach with chromatic planing
    m += '    <measure number="11">\n'
    m += d("rit.")
    m += h("D", "minor-seventh", [(9, 0, "add"), (11, 0, "add"), (13, 0, "add")])
    m += n("D", 5, 256, "quarter", slur_s=True, acc=True)
    m += n("E", 5, 256, "quarter", acc=True)
    m += n("G", 4, 256, "quarter", alt=1, acc=True)  # G# motif
    m += n("B", 4, 256, "quarter", slur_e=True)
    m += bk(1024)
    # Chromatic voice-leading
    m += n("D", 3, 256, "quarter", staff=2)
    m += n("A", 3, 256, "quarter", chord=True, staff=2)
    m += n("C", 4, 256, "quarter", chord=True, staff=2)
    m += n("F", 4, 256, "quarter", chord=True, staff=2)
    m += n("D", 3, 256, "quarter", alt=-1, staff=2)  # chromatic
    m += n("A", 3, 256, "quarter", alt=-1, chord=True, staff=2)
    m += n("C", 4, 256, "quarter", chord=True, staff=2)
    m += n("G", 3, 256, "quarter", staff=2)
    m += n("C", 4, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # Bar 12: Final resolution — return to C with fermata
    m += '    <measure number="12">\n'
    m += d(dyn="pp")
    m += h("C", "major", [(9, 0, "add"), (11, 1, "add"), (13, 0, "add")])
    m += n("D", 5, 256, "quarter", slur_s=True, acc=True)
    m += n("C", 5, 768, "half", dot=True, slur_e=True, ferm=True)
    m += bk(1024)
    m += n("C", 2, 256, "quarter", staff=2)
    m += n("G", 2, 256, "quarter", chord=True, staff=2)
    m += n("E", 3, 256, "quarter", chord=True, staff=2)
    m += n("B", 3, 256, "quarter", chord=True, staff=2)
    m += n("F", 4, 256, "quarter", alt=1, chord=True, staff=2)
    m += n("C", 3, 768, "half", dot=True, staff=2)
    m += n("G", 3, 768, "half", dot=True, chord=True, staff=2)
    m += n("E", 4, 768, "half", dot=True, chord=True, staff=2)
    m += bl()
    m += '    </measure>\n'
    
    return hdr("The Master's Palette - IV. German Development", 0) + m + ftr()

# ============ MAIN ENGINE ============
def main():
    scores_dir = os.path.join(os.path.dirname(__file__), "..", "scores")
    
    print("=" * 70)
    print("2-MOVEMENT EXCELLENCE REFINEMENT PASS")
    print("Movements III (Bartók) and IV (German) only")
    print("Do NOT touch Movements I or II")
    print("=" * 70)
    print()
    
    movements = {
        "III. Bartok Night": ("Movement3-Excellent-Final.musicxml", gen_mvmt3_refined),
        "IV. German Development": ("Movement4-Excellent-Final.musicxml", gen_mvmt4_refined),
    }
    
    history = {name: [] for name in movements.keys()}
    final_results = {}
    iteration = 0
    max_iterations = 5
    
    while iteration < max_iterations:
        iteration += 1
        print(f"\n{'='*70}")
        print(f"ITERATION {iteration}")
        print(f"{'='*70}")
        
        all_pass = True
        
        for name, (filename, generator) in movements.items():
            xml = generator()
            filepath = os.path.join(scores_dir, filename)
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(xml)
            
            total, scores, details = evaluate_excellence(xml, name)
            history[name].append(total)
            
            status = "EXCELLENT" if total >= 8.0 else "REFINE"
            if total < 8.0:
                all_pass = False
            
            print(f"\n{name}")
            print(f"  Total Score: {total:.2f}/10.0 [{status}]")
            print(f"  Category Breakdown:")
            for cat, score in scores.items():
                print(f"    {cat}: {score:.2f}")
            
            final_results[name] = (total, scores, filepath)
        
        if all_pass:
            print(f"\n{'='*70}")
            print("BOTH MOVEMENTS PASS >= 8.0 — ENGINE COMPLETE")
            print(f"{'='*70}")
            break
        else:
            print(f"\n  --> Some movements need refinement. Continuing...")
    
    # Final Summary
    print("\n" + "=" * 70)
    print("FINAL SUMMARY TABLE")
    print("=" * 70)
    print()
    print(f"{'Movement':<30} {'Cycles':<10} {'Final Score':<15} {'Status'}")
    print("-" * 70)
    
    for name in movements.keys():
        total, scores, filepath = final_results[name]
        cycle_count = len(history[name])
        status = "EXCELLENT" if total >= 8.0 else "NEEDS WORK"
        print(f"{name:<30} {cycle_count:<10} {total:.2f}/10.0        {status}")
    
    print("-" * 70)
    print()
    
    # Detailed final scores
    print("FINAL CATEGORY SCORES:")
    for name in movements.keys():
        total, scores, _ = final_results[name]
        print(f"\n  {name} ({total:.2f}/10.0):")
        for cat, score in scores.items():
            print(f"    {cat}: {score:.2f}")
    
    print()
    print("SCORE HISTORY (per iteration):")
    for name in movements.keys():
        scores_str = " -> ".join([f"{s:.2f}" for s in history[name]])
        print(f"  {name}: {scores_str}")
    
    print()
    print("KEY REFINEMENTS APPLIED:")
    print()
    print("Movement III (Bartok Night):")
    print("  - Bartok axis system: A<->Eb, C<->Gb pivots")
    print("  - m2 clusters, tritone jumps, sudden P4 leaps")
    print("  - Extreme registral displacement (2-octave drops)")
    print("  - Silence as texture (negative space)")
    print("  - Night-music dyads, pedal drones, chromatic neighbours")
    print("  - Octatonic hints, augmented clusters")
    print("  - Non-functional harmony, no tonal cliches")
    print()
    print("Movement IV (German Development):")
    print("  - Strict inversion, retrograde, augmentation, diminution")
    print("  - C+ interval cycle (augmented triad cycle)")
    print("  - Whole-tone derived harmonies")
    print("  - Klangfarbenmelodie (2-octave registral exchanges)")
    print("  - Chromatic planing in LH voice-leading")
    print("  - Guide-tone motion with chromatic connectors")
    print("  - Developmental arc: seed -> sequence -> expansion -> return")
    print()
    print("OUTPUT FILES:")
    for name, (_, _, filepath) in final_results.items():
        print(f"  - {os.path.basename(filepath)}")
    print()
    print("Movements I and II: UNCHANGED")

if __name__ == "__main__":
    main()

