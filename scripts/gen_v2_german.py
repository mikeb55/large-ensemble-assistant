#!/usr/bin/env python3
"""
Movement IV - "German Development"
12-bar lead sheet - German modernist Fortspinnung style
Core motif: C5-D5-E5-G#4-B4-D5
Form: Exposition(4) - Transformation(4) - Arrival(4)
"""

import os

def n(step, oct, dur, typ, alt=None, dot=False, chord=False, 
      slur_s=False, slur_e=False, acc=False, stac=False, ferm=False, staff=1):
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
    if nots:
        x += "        <notations>" + "".join(nots) + "</notations>\n"
    x += "      </note>\n"
    return x

def r(dur, typ, staff=1):
    return f"      <note><rest/><duration>{dur}</duration><type>{typ}</type><staff>{staff}</staff></note>\n"

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

def bar(style="light-heavy"):
    return f'      <barline location="right"><bar-style>{style}</bar-style></barline>\n'

HDR = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 3.1 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="3.1">
  <work><work-title>The Master's Palette - Movement IV: German Development</work-title></work>
  <identification>
    <creator type="composer">Original Composition</creator>
    <rights>© 2025 Michael Bryant. All Rights Reserved.</rights>
    <encoding><software>Python MusicXML Generator</software><encoding-date>2025-12-11</encoding-date></encoding>
  </identification>
  <part-list>
    <score-part id="P1"><part-name>Piano</part-name></score-part>
  </part-list>
  <part id="P1">
'''

FTR = '''  </part>
</score-partwise>
'''

ATTR = '''      <attributes>
        <divisions>256</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <staves>2</staves>
        <clef number="1"><sign>G</sign><line>2</line></clef>
        <clef number="2"><sign>F</sign><line>4</line></clef>
      </attributes>
'''

def gen():
    m = ""
    
    # ===== BAR 1: EXPOSITION - Motif statement C-D-E-G#-B-D =====
    m += '    <measure number="1">\n'
    m += ATTR
    m += d("Streng, mit Kraft", tempo=72)
    m += d(dyn="f")
    m += h("C", "major", [(11, 1, "add")])  # C(#11) - quartal implication
    # RH: Core motif C5-D5-E5-G#4-B4-D5
    m += n("C", 5, 256, "quarter", slur_s=True, acc=True)
    m += n("D", 5, 256, "quarter")
    m += n("E", 5, 256, "quarter")
    m += n("G", 4, 256, "quarter", alt=1, slur_e=True)
    m += bk(1024)
    # LH: Quartal dyads - independent counterpoint
    m += n("C", 3, 256, "quarter", staff=2)
    m += n("F", 3, 256, "quarter", chord=True, staff=2)
    m += n("G", 3, 256, "quarter", staff=2)
    m += n("D", 4, 256, "quarter", chord=True, staff=2)
    m += n("E", 3, 256, "quarter", staff=2)
    m += n("A", 3, 256, "quarter", chord=True, staff=2)
    m += n("B", 2, 256, "quarter", staff=2)
    m += n("F", 3, 256, "quarter", alt=1, chord=True, staff=2)
    m += '    </measure>\n'
    
    # ===== BAR 2: Motif completion + sequence =====
    m += '    <measure number="2">\n'
    m += h("E", "minor", [(9, 0, "add")])  # Em(add9) - modal
    # RH: B4-D5 completion, then sequence up
    m += n("B", 4, 256, "quarter", slur_s=True)
    m += n("D", 5, 256, "quarter")
    m += n("E", 5, 256, "quarter")
    m += n("F", 5, 256, "quarter", alt=1, slur_e=True)
    m += bk(1024)
    # LH: Chromatic planing dyads
    m += n("E", 3, 256, "quarter", staff=2)
    m += n("B", 3, 256, "quarter", chord=True, staff=2)
    m += n("F", 3, 256, "quarter", alt=1, staff=2)
    m += n("C", 4, 256, "quarter", alt=1, chord=True, staff=2)
    m += n("G", 3, 256, "quarter", staff=2)
    m += n("D", 4, 256, "quarter", chord=True, staff=2)
    m += n("A", 3, 256, "quarter", alt=-1, staff=2)
    m += n("E", 4, 256, "quarter", alt=-1, chord=True, staff=2)
    m += '    </measure>\n'
    
    # ===== BAR 3: Inversion of motif =====
    m += '    <measure number="3">\n'
    m += h("G#", "augmented")  # G#+ - symmetrical
    # RH: Motif inverted - C down to Bb, down to Ab, up to E
    m += n("C", 5, 256, "quarter", slur_s=True, acc=True)
    m += n("B", 4, 256, "quarter", alt=-1)
    m += n("A", 4, 256, "quarter", alt=-1)
    m += n("E", 5, 256, "quarter", slur_e=True)
    m += bk(1024)
    # LH: Tritone stacks
    m += n("G", 2, 256, "quarter", alt=1, staff=2)
    m += n("D", 3, 256, "quarter", chord=True, staff=2)
    m += n("C", 3, 256, "quarter", staff=2)
    m += n("F", 3, 256, "quarter", alt=1, chord=True, staff=2)
    m += n("E", 3, 256, "quarter", alt=-1, staff=2)
    m += n("A", 3, 256, "quarter", chord=True, staff=2)
    m += n("D", 3, 256, "quarter", staff=2)
    m += n("G", 3, 256, "quarter", alt=1, chord=True, staff=2)
    m += '    </measure>\n'
    
    # ===== BAR 4: Retrograde fragment =====
    m += '    <measure number="4">\n'
    m += h("D", "dominant", [(9, -1, "add")])  # D7b9 - tension
    # RH: Retrograde D-B-G#-E-D-C
    m += n("D", 5, 256, "quarter", slur_s=True)
    m += n("B", 4, 256, "quarter")
    m += n("G", 4, 256, "quarter", alt=1)
    m += n("E", 4, 256, "quarter", slur_e=True)
    m += bk(1024)
    # LH: Stack of 5ths
    m += n("D", 3, 384, "quarter", dot=True, staff=2)
    m += n("A", 3, 128, "eighth", chord=True, staff=2)
    m += n("E", 3, 256, "quarter", staff=2)
    m += n("B", 3, 256, "quarter", chord=True, staff=2)
    m += n("A", 2, 256, "quarter", alt=-1, staff=2)
    m += n("E", 3, 256, "quarter", alt=-1, chord=True, staff=2)
    m += '    </measure>\n'
    
    # ===== BAR 5: TRANSFORMATION - Augmented motif =====
    m += '    <measure number="5">\n'
    m += d("Breiter")
    m += d(dyn="mf")
    m += h("F", "major-seventh", [(11, 1, "add")])  # Fmaj7#11
    # RH: Motif augmented - longer values
    m += n("C", 5, 512, "half", slur_s=True)
    m += n("D", 5, 512, "half", slur_e=True)
    m += bk(1024)
    # LH: Modal clusters
    m += n("F", 2, 256, "quarter", staff=2)
    m += n("C", 3, 256, "quarter", chord=True, staff=2)
    m += n("E", 3, 256, "quarter", staff=2)
    m += n("B", 3, 256, "quarter", chord=True, staff=2)
    m += n("A", 3, 256, "quarter", staff=2)
    m += n("E", 4, 256, "quarter", chord=True, staff=2)
    m += n("G", 3, 256, "quarter", staff=2)
    m += n("D", 4, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # ===== BAR 6: Continued augmentation =====
    m += '    <measure number="6">\n'
    m += h("B", "half-diminished")  # Bm7b5
    # RH: E5-G#4 stretched
    m += n("E", 5, 512, "half", slur_s=True)
    m += n("G", 4, 512, "half", alt=1, slur_e=True)
    m += bk(1024)
    # LH: Contrapuntal line
    m += n("B", 2, 256, "quarter", staff=2)
    m += n("F", 3, 256, "quarter", chord=True, staff=2)
    m += n("A", 3, 256, "quarter", staff=2)
    m += n("D", 4, 256, "quarter", chord=True, staff=2)
    m += n("G", 3, 256, "quarter", alt=1, staff=2)
    m += n("D", 4, 256, "quarter", alt=1, chord=True, staff=2)
    m += n("F", 3, 256, "quarter", staff=2)
    m += n("C", 4, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # ===== BAR 7: Diminution - rapid motif =====
    m += '    <measure number="7">\n'
    m += d(dyn="f")
    m += h("A", "minor", [(9, 0, "add")])  # Am9
    # RH: Motif diminished - quick notes
    m += n("C", 5, 128, "eighth", slur_s=True, acc=True)
    m += n("D", 5, 128, "eighth")
    m += n("E", 5, 128, "eighth")
    m += n("G", 4, 128, "eighth", alt=1)
    m += n("B", 4, 256, "quarter")
    m += n("D", 5, 256, "quarter")
    m += n("C", 5, 256, "quarter", slur_e=True)
    m += bk(1024)
    # LH: Driving quartal motion
    m += n("A", 2, 256, "quarter", staff=2)
    m += n("E", 3, 256, "quarter", chord=True, staff=2)
    m += n("D", 3, 256, "quarter", staff=2)
    m += n("G", 3, 256, "quarter", chord=True, staff=2)
    m += n("C", 3, 256, "quarter", staff=2)
    m += n("F", 3, 256, "quarter", chord=True, staff=2)
    m += n("B", 2, 256, "quarter", staff=2)
    m += n("E", 3, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # ===== BAR 8: Registral split =====
    m += '    <measure number="8">\n'
    m += h("E", "dominant", [(9, 1, "add")])  # E7#9
    # RH: Wide leaps - registral extremes
    m += n("E", 5, 256, "quarter", slur_s=True)
    m += n("G", 4, 256, "quarter", alt=1)
    m += n("D", 6, 256, "quarter")
    m += n("B", 4, 256, "quarter", slur_e=True)
    m += bk(1024)
    # LH: Chromatic bass motion
    m += n("E", 2, 256, "quarter", staff=2)
    m += n("B", 2, 256, "quarter", chord=True, staff=2)
    m += n("F", 2, 256, "quarter", staff=2)
    m += n("C", 3, 256, "quarter", chord=True, staff=2)
    m += n("F", 2, 256, "quarter", alt=1, staff=2)
    m += n("C", 3, 256, "quarter", alt=1, chord=True, staff=2)
    m += n("G", 2, 256, "quarter", staff=2)
    m += n("D", 3, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # ===== BAR 9: ARRIVAL - Thematic synthesis =====
    m += '    <measure number="9">\n'
    m += d("Ankunft")
    m += d(dyn="ff")
    m += h("C", "major-seventh")  # Cmaj7
    # RH: Motif combined with inversion
    m += n("C", 5, 256, "quarter", slur_s=True, acc=True)
    m += n("E", 5, 256, "quarter")
    m += n("D", 5, 256, "quarter")
    m += n("G", 5, 256, "quarter", alt=1, slur_e=True)
    m += bk(1024)
    # LH: Full quartal voicing
    m += n("C", 3, 256, "quarter", staff=2)
    m += n("G", 3, 256, "quarter", chord=True, staff=2)
    m += n("D", 4, 256, "quarter", chord=True, staff=2)
    m += n("B", 2, 256, "quarter", staff=2)
    m += n("F", 3, 256, "quarter", alt=1, chord=True, staff=2)
    m += n("E", 3, 256, "quarter", staff=2)
    m += n("A", 3, 256, "quarter", chord=True, staff=2)
    m += n("D", 3, 256, "quarter", staff=2)
    m += '    </measure>\n'
    
    # ===== BAR 10: Final sequence =====
    m += '    <measure number="10">\n'
    m += h("G", "dominant", [(11, 1, "add")])  # G7#11
    # RH: Sequence of head motif
    m += n("B", 5, 256, "quarter", slur_s=True)
    m += n("D", 6, 256, "quarter")
    m += n("C", 6, 256, "quarter")
    m += n("E", 5, 256, "quarter", slur_e=True)
    m += bk(1024)
    # LH: Lydian dominant
    m += n("G", 2, 256, "quarter", staff=2)
    m += n("D", 3, 256, "quarter", chord=True, staff=2)
    m += n("F", 3, 256, "quarter", alt=1, staff=2)
    m += n("C", 4, 256, "quarter", chord=True, staff=2)
    m += n("B", 3, 256, "quarter", staff=2)
    m += n("F", 4, 256, "quarter", chord=True, staff=2)
    m += n("A", 3, 256, "quarter", staff=2)
    m += n("E", 4, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # ===== BAR 11: Cadential preparation =====
    m += '    <measure number="11">\n'
    m += d("rit.")
    m += h("D", "minor", [(11, 0, "add")])  # Dm(add11)
    # RH: Final motif statement
    m += n("D", 5, 256, "quarter", slur_s=True)
    m += n("E", 5, 256, "quarter")
    m += n("G", 4, 256, "quarter", alt=1)
    m += n("B", 4, 256, "quarter", slur_e=True)
    m += bk(1024)
    # LH: Resolving motion
    m += n("D", 3, 256, "quarter", staff=2)
    m += n("A", 3, 256, "quarter", chord=True, staff=2)
    m += n("G", 3, 256, "quarter", staff=2)
    m += n("C", 4, 256, "quarter", chord=True, staff=2)
    m += n("F", 3, 256, "quarter", staff=2)
    m += n("B", 3, 256, "quarter", chord=True, staff=2)
    m += n("E", 3, 256, "quarter", staff=2)
    m += n("A", 3, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # ===== BAR 12: Final - C with added tensions =====
    m += '    <measure number="12">\n'
    m += d(dyn="p")
    m += h("C", "major", [(9, 0, "add"), (11, 1, "add")])  # C(add9,#11)
    # RH: Final C-D-C resolution
    m += n("D", 5, 256, "quarter", slur_s=True)
    m += n("C", 5, 768, "half", dot=True, slur_e=True, ferm=True)
    m += bk(1024)
    # LH: Final quartal stack
    m += n("C", 2, 1024, "whole", staff=2)
    m += n("G", 2, 1024, "whole", chord=True, staff=2)
    m += n("D", 3, 1024, "whole", chord=True, staff=2)
    m += n("F", 3, 1024, "whole", alt=1, chord=True, staff=2)
    m += bar()
    m += '    </measure>\n'
    
    return m

def main():
    xml = HDR + gen() + FTR
    out = os.path.join(os.path.dirname(__file__), "..", "scores", "V2-German-Mvmt4-11-Dec-2025.musicxml")
    out = os.path.normpath(out)
    with open(out, "w", encoding="utf-8") as f:
        f.write(xml)
    print(f"Generated: {out}")

if __name__ == "__main__":
    main()



