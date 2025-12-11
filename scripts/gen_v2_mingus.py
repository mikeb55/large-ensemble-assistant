#!/usr/bin/env python3
"""
Movement I - "Mingus Blues Cathedral"
12-bar lead sheet with core motif: C4-Eb4-F4-Bb4-A4-F4-Eb4
Form: A(4) - A1(4) - B(4)
"""

import os

def n(step, oct, dur, typ, alt=None, dot=False, chord=False, 
      slur_s=False, slur_e=False, acc=False, stac=False, ferm=False, staff=1):
    """Generate note XML"""
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
    """Harmony/chord symbol"""
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

# Header
HDR = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 3.1 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="3.1">
  <work><work-title>The Master's Palette - Movement I: Mingus Blues Cathedral</work-title></work>
  <identification>
    <creator type="composer">Original Composition</creator>
    <rights>© 2025 Michael Bryant. All Rights Reserved.</rights>
    <encoding><software>Python MusicXML Generator</software><encoding-date>2025-12-11</encoding-date></encoding>
  </identification>
  <defaults>
    <scaling><millimeters>7.0</millimeters><tenths>40</tenths></scaling>
  </defaults>
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
        <key><fifths>-3</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <staves>2</staves>
        <clef number="1"><sign>G</sign><line>2</line></clef>
        <clef number="2"><sign>F</sign><line>4</line></clef>
      </attributes>
'''

def gen():
    m = ""
    
    # ===== BAR 1: Bold opening - Core motif statement =====
    # Motif: C4-Eb4-F4-Bb4-A4-F4-Eb4
    m += '    <measure number="1">\n'
    m += ATTR
    m += d("Slow gospel blues", tempo=58)
    m += d(dyn="mf")
    m += h("C", "minor", [(9, 0, "add")])  # Cm9
    # RH: C-Eb-F-Bb (first 4 notes of motif)
    m += n("C", 4, 256, "quarter", slur_s=True, acc=True)
    m += n("E", 4, 256, "quarter", alt=-1)
    m += n("F", 4, 256, "quarter")
    m += n("B", 4, 256, "quarter", alt=-1, slur_e=True)
    m += bk(1024)
    # LH: Cm9 voicing - rhythmic comping
    m += n("C", 2, 384, "quarter", dot=True, staff=2)
    m += n("G", 2, 384, "quarter", dot=True, chord=True, staff=2)
    m += n("B", 3, 128, "eighth", alt=-1, staff=2)
    m += n("E", 3, 128, "eighth", alt=-1, chord=True, staff=2)
    m += n("D", 3, 256, "quarter", staff=2)
    m += n("G", 3, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # ===== BAR 2: Motif completion + extension =====
    m += '    <measure number="2">\n'
    m += h("F", "minor-seventh")  # Fm7
    # RH: A-F-Eb (last 3 of motif) + extension G
    m += n("A", 4, 256, "quarter", slur_s=True)
    m += n("F", 4, 256, "quarter")
    m += n("E", 4, 256, "quarter", alt=-1)
    m += n("G", 4, 256, "quarter", slur_e=True)
    m += bk(1024)
    # LH: Fm7 voicing
    m += n("F", 2, 256, "quarter", staff=2)
    m += n("C", 3, 256, "quarter", chord=True, staff=2)
    m += n("E", 3, 128, "eighth", alt=-1, staff=2)
    m += n("A", 3, 128, "eighth", alt=-1, chord=True, staff=2)
    m += n("C", 3, 256, "quarter", staff=2)
    m += n("E", 3, 256, "quarter", alt=-1, chord=True, staff=2)
    m += '    </measure>\n'
    
    # ===== BAR 3: Motif sequence up a 4th =====
    m += '    <measure number="3">\n'
    m += h("A", "dominant", [(9, 0, "add"), (13, 0, "add")])  # Ab9(13)
    # RH: Motif transposed up P4: F-Ab-Bb-Eb
    m += n("F", 4, 256, "quarter", alt=-1, slur_s=True, acc=True)
    m += n("A", 4, 256, "quarter", alt=-1)
    m += n("B", 4, 256, "quarter", alt=-1)
    m += n("E", 5, 256, "quarter", alt=-1, slur_e=True)
    m += bk(1024)
    # LH: Ab9 voicing - gospel quartal
    m += n("A", 2, 384, "quarter", alt=-1, dot=True, staff=2)
    m += n("E", 3, 128, "eighth", alt=-1, staff=2)
    m += n("G", 3, 128, "eighth", chord=True, staff=2)
    m += n("C", 3, 256, "quarter", staff=2)
    m += n("F", 3, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # ===== BAR 4: Resolution to V - G7alt =====
    m += '    <measure number="4">\n'
    m += h("G", "dominant", [(9, -1, "add"), (13, -1, "add")])  # G7b9b13
    # RH: Motif fragment descending - Eb-D-C-B
    m += n("E", 5, 256, "quarter", alt=-1, slur_s=True)
    m += n("D", 5, 256, "quarter")
    m += n("C", 5, 256, "quarter")
    m += n("B", 4, 256, "quarter", slur_e=True)
    m += bk(1024)
    # LH: G7alt voicing
    m += n("G", 2, 256, "quarter", staff=2)
    m += n("F", 3, 256, "quarter", staff=2)
    m += n("A", 3, 128, "eighth", alt=-1, chord=True, staff=2)
    m += n("D", 3, 128, "eighth", alt=-1, staff=2)
    m += n("B", 2, 256, "quarter", staff=2)
    m += n("F", 3, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # ===== BAR 5: A1 - Motif with rhythmic displacement =====
    m += '    <measure number="5">\n'
    m += d(dyn="f")
    m += h("C", "minor", [(9, 0, "add")])  # Cm9
    # RH: Motif syncopated - rest + C-Eb-F on upbeats
    m += r(128, "eighth")
    m += n("C", 4, 128, "eighth", slur_s=True, acc=True)
    m += n("E", 4, 256, "quarter", alt=-1)
    m += n("F", 4, 384, "quarter", dot=True)
    m += n("B", 4, 128, "eighth", alt=-1, slur_e=True)
    m += bk(1024)
    # LH: Cm9 rhythmic
    m += n("C", 2, 256, "quarter", staff=2)
    m += n("G", 2, 256, "quarter", chord=True, staff=2)
    m += n("E", 3, 256, "quarter", alt=-1, staff=2)
    m += n("B", 3, 128, "eighth", alt=-1, chord=True, staff=2)
    m += n("D", 3, 128, "eighth", staff=2)
    m += n("G", 3, 256, "quarter", staff=2)
    m += '    </measure>\n'
    
    # ===== BAR 6: Motif inversion =====
    m += '    <measure number="6">\n'
    m += h("E", "major-seventh", [(11, 1, "add")])  # Ebmaj7#11
    # RH: Motif inverted - C down to A, up to G, down to D
    m += n("C", 5, 256, "quarter", slur_s=True)
    m += n("A", 4, 256, "quarter")
    m += n("G", 4, 256, "quarter")
    m += n("D", 4, 256, "quarter", slur_e=True)
    m += bk(1024)
    # LH: Ebmaj7#11
    m += n("E", 2, 384, "quarter", alt=-1, dot=True, staff=2)
    m += n("B", 2, 128, "eighth", alt=-1, staff=2)
    m += n("D", 3, 128, "eighth", chord=True, staff=2)
    m += n("G", 3, 256, "quarter", staff=2)
    m += n("A", 3, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # ===== BAR 7: Motif augmented =====
    m += '    <measure number="7">\n'
    m += h("D", "half-diminished")  # Dm7b5
    # RH: Motif augmented - longer note values
    m += n("D", 4, 384, "quarter", dot=True, slur_s=True)
    m += n("F", 4, 128, "eighth")
    m += n("A", 4, 512, "half", alt=-1, slur_e=True)
    m += bk(1024)
    # LH: Dm7b5 voicing
    m += n("D", 3, 256, "quarter", staff=2)
    m += n("A", 3, 256, "quarter", alt=-1, chord=True, staff=2)
    m += n("C", 3, 256, "quarter", staff=2)
    m += n("F", 3, 256, "quarter", chord=True, staff=2)
    m += n("A", 3, 256, "quarter", alt=-1, staff=2)
    m += '    </measure>\n'
    
    # ===== BAR 8: Tension peak - G7#9 =====
    m += '    <measure number="8">\n'
    m += h("G", "dominant", [(9, 1, "add")])  # G7#9
    # RH: Motif fragment with chromatic approach
    m += n("A", 4, 256, "quarter", alt=-1, slur_s=True, acc=True)
    m += n("G", 4, 256, "quarter")
    m += n("F", 4, 128, "eighth", alt=1)
    m += n("G", 4, 128, "eighth")
    m += n("F", 4, 256, "quarter", slur_e=True)
    m += bk(1024)
    # LH: G7#9 gospel voicing
    m += n("G", 2, 256, "quarter", staff=2)
    m += n("B", 2, 256, "quarter", chord=True, staff=2)
    m += n("F", 3, 256, "quarter", staff=2)
    m += n("A", 3, 128, "eighth", alt=1, chord=True, staff=2)
    m += n("D", 3, 128, "eighth", staff=2)
    m += n("F", 3, 256, "quarter", staff=2)
    m += '    </measure>\n'
    
    # ===== BAR 9: B section - brighter, Bb area =====
    m += '    <measure number="9">\n'
    m += d("Brighter")
    m += h("B", "major-seventh")  # Bbmaj7
    # RH: Motif in relative major - Bb-D-Eb-Ab
    m += n("B", 4, 256, "quarter", alt=-1, slur_s=True, acc=True)
    m += n("D", 5, 256, "quarter")
    m += n("E", 5, 256, "quarter", alt=-1)
    m += n("A", 5, 256, "quarter", alt=-1, slur_e=True)
    m += bk(1024)
    # LH: Bbmaj7
    m += n("B", 2, 384, "quarter", alt=-1, dot=True, staff=2)
    m += n("F", 3, 128, "eighth", staff=2)
    m += n("A", 3, 128, "eighth", chord=True, staff=2)
    m += n("D", 3, 256, "quarter", staff=2)
    m += n("F", 3, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # ===== BAR 10: Eb9 - lydian color =====
    m += '    <measure number="10">\n'
    m += h("E", "dominant", [(9, 0, "add")])  # Eb9
    # RH: Motif sequence - G-Bb-C-F
    m += n("G", 5, 256, "quarter", slur_s=True)
    m += n("B", 5, 256, "quarter", alt=-1)
    m += n("C", 6, 256, "quarter")
    m += n("F", 5, 256, "quarter", slur_e=True)
    m += bk(1024)
    # LH: Eb9
    m += n("E", 2, 256, "quarter", alt=-1, staff=2)
    m += n("B", 2, 256, "quarter", alt=-1, chord=True, staff=2)
    m += n("G", 3, 256, "quarter", staff=2)
    m += n("D", 3, 128, "eighth", alt=-1, chord=True, staff=2)
    m += n("F", 3, 128, "eighth", staff=2)
    m += n("B", 2, 256, "quarter", alt=-1, staff=2)
    m += '    </measure>\n'
    
    # ===== BAR 11: Return to minor - Fm9 =====
    m += '    <measure number="11">\n'
    m += d(dyn="mf")
    m += h("F", "minor", [(9, 0, "add")])  # Fm9
    # RH: Motif descending - F-Eb-C-Bb
    m += n("F", 5, 256, "quarter", slur_s=True)
    m += n("E", 5, 256, "quarter", alt=-1)
    m += n("C", 5, 256, "quarter")
    m += n("B", 4, 256, "quarter", alt=-1, slur_e=True)
    m += bk(1024)
    # LH: Fm9
    m += n("F", 2, 384, "quarter", dot=True, staff=2)
    m += n("C", 3, 128, "eighth", staff=2)
    m += n("E", 3, 128, "eighth", alt=-1, chord=True, staff=2)
    m += n("A", 2, 256, "quarter", alt=-1, staff=2)
    m += n("G", 3, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # ===== BAR 12: Final cadence - Dm7b5 - G7alt - Cm =====
    m += '    <measure number="12">\n'
    m += d("rit.")
    m += d(dyn="p")
    m += h("D", "half-diminished")  # Dm7b5
    # RH: Final motif statement - A-F-Eb-C (motif ending)
    m += n("A", 4, 256, "quarter", slur_s=True)
    m += h("G", "dominant", [(9, -1, "add")])  # G7b9
    m += n("F", 4, 256, "quarter")
    m += h("C", "minor", [(9, 0, "add")])  # Cm9
    m += n("E", 4, 256, "quarter", alt=-1)
    m += n("C", 4, 256, "quarter", slur_e=True, ferm=True)
    m += bk(1024)
    # LH: ii-V-i cadence
    m += n("D", 3, 256, "quarter", staff=2)
    m += n("A", 3, 256, "quarter", alt=-1, chord=True, staff=2)
    m += n("G", 2, 256, "quarter", staff=2)
    m += n("F", 3, 256, "quarter", chord=True, staff=2)
    m += n("C", 2, 256, "quarter", staff=2)
    m += n("G", 2, 256, "quarter", chord=True, staff=2)
    m += n("E", 3, 256, "quarter", alt=-1, chord=True, staff=2)
    m += bar()
    m += '    </measure>\n'
    
    return m

def main():
    xml = HDR + gen() + FTR
    out = os.path.join(os.path.dirname(__file__), "..", "scores", "V2-Mingus-Mvmt1-11-Dec-2025.musicxml")
    out = os.path.normpath(out)
    with open(out, "w", encoding="utf-8") as f:
        f.write(xml)
    print(f"Generated: {out}")

if __name__ == "__main__":
    main()



