#!/usr/bin/env python3
"""
Movement II - "Gil's Canvas"
12-bar lead sheet - Gil Evans Lydian cloud style
Core motif: G4-A4-B4-F#5-E5-D5
Form: A(4) - A1(4) - Coda(4)
"""

import os

def n(step, oct, dur, typ, alt=None, dot=False, chord=False, 
      slur_s=False, slur_e=False, acc=False, ferm=False, staff=1, tie_s=False, tie_e=False):
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
  <work><work-title>The Master's Palette - Movement II: Gil's Canvas</work-title></work>
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
        <key><fifths>1</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <staves>2</staves>
        <clef number="1"><sign>G</sign><line>2</line></clef>
        <clef number="2"><sign>F</sign><line>4</line></clef>
      </attributes>
'''

def gen():
    m = ""
    
    # ===== BAR 1: Floating entrance - Motif G-A-B-F#-E-D =====
    m += '    <measure number="1">\n'
    m += ATTR
    m += d("Floating, ethereal", tempo=52)
    m += d(dyn="p")
    m += h("G", "major-seventh", [(11, 1, "add")])  # Gmaj7#11
    # RH: G-A-B (first 3 of motif) elongated
    m += n("G", 4, 512, "half", slur_s=True)
    m += n("A", 4, 256, "quarter")
    m += n("B", 4, 256, "quarter", slur_e=True)
    m += bk(1024)
    # LH: Gmaj7#11 sustained pad with inner voice
    m += n("G", 2, 512, "half", staff=2)
    m += n("D", 3, 512, "half", chord=True, staff=2)
    m += n("F", 3, 256, "quarter", alt=1, staff=2)
    m += n("A", 3, 256, "quarter", chord=True, staff=2)
    m += n("B", 3, 256, "quarter", staff=2)
    m += n("D", 4, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # ===== BAR 2: Motif completion F#-E-D =====
    m += '    <measure number="2">\n'
    m += h("D", "major-seventh", [(9, 0, "add")])  # Dmaj9
    # RH: F#5-E5-D5 (last 3) with extension
    m += n("F", 5, 384, "quarter", alt=1, dot=True, slur_s=True)
    m += n("E", 5, 128, "eighth")
    m += n("D", 5, 512, "half", slur_e=True)
    m += bk(1024)
    # LH: Dmaj9 voicing
    m += n("D", 2, 512, "half", staff=2)
    m += n("A", 2, 512, "half", chord=True, staff=2)
    m += n("C", 3, 256, "quarter", alt=1, staff=2)
    m += n("E", 3, 256, "quarter", chord=True, staff=2)
    m += n("F", 3, 256, "quarter", alt=1, staff=2)
    m += n("A", 3, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # ===== BAR 3: Motif reordered - E-D-G-A =====
    m += '    <measure number="3">\n'
    m += h("A", "major-seventh", [(11, 1, "add")])  # Amaj7#11
    # RH: Reordered motif fragment
    m += n("E", 5, 256, "quarter", slur_s=True)
    m += n("D", 5, 256, "quarter")
    m += n("G", 5, 256, "quarter")
    m += n("A", 5, 256, "quarter", slur_e=True)
    m += bk(1024)
    # LH: Amaj7#11 - Lydian cluster
    m += n("A", 2, 384, "quarter", dot=True, staff=2)
    m += n("E", 3, 128, "eighth", staff=2)
    m += n("G", 3, 256, "quarter", alt=1, chord=True, staff=2)
    m += n("D", 3, 256, "quarter", alt=1, staff=2)
    m += n("C", 4, 256, "quarter", alt=1, chord=True, staff=2)
    m += '    </measure>\n'
    
    # ===== BAR 4: Long held note - breathing =====
    m += '    <measure number="4">\n'
    m += h("E", "major-seventh", [(9, 0, "add")])  # Emaj9
    # RH: Long B with gentle descent
    m += n("B", 5, 768, "half", dot=True, slur_s=True)
    m += n("A", 5, 256, "quarter", slur_e=True)
    m += bk(1024)
    # LH: Emaj9 - sustain with motion
    m += n("E", 2, 512, "half", staff=2)
    m += n("B", 2, 512, "half", chord=True, staff=2)
    m += n("G", 3, 256, "quarter", alt=1, staff=2)
    m += n("D", 4, 256, "quarter", alt=1, chord=True, staff=2)
    m += n("F", 3, 256, "quarter", alt=1, staff=2)
    m += n("A", 3, 256, "quarter", chord=True, staff=2)
    m += '    </measure>\n'
    
    # ===== BAR 5: A1 - Motif in higher register =====
    m += '    <measure number="5">\n'
    m += d(dyn="mp")
    m += h("B", "major-seventh", [(11, 1, "add")])  # Bmaj7#11
    # RH: Motif up octave, contracted rhythm
    m += n("G", 5, 256, "quarter", slur_s=True)
    m += n("A", 5, 256, "quarter")
    m += n("B", 5, 256, "quarter")
    m += n("F", 6, 256, "quarter", alt=1, slur_e=True)
    m += bk(1024)
    # LH: Bmaj7#11
    m += n("B", 2, 384, "quarter", dot=True, staff=2)
    m += n("F", 3, 128, "eighth", alt=1, staff=2)
    m += n("A", 3, 256, "quarter", alt=1, chord=True, staff=2)
    m += n("D", 3, 256, "quarter", alt=1, staff=2)
    m += n("E", 4, 256, "quarter", alt=1, chord=True, staff=2)
    m += '    </measure>\n'
    
    # ===== BAR 6: Descending dissolution =====
    m += '    <measure number="6">\n'
    m += h("F#", "minor-seventh", [(9, 0, "add")])  # F#m9
    # RH: E-D from motif, dissolving
    m += n("E", 6, 512, "half", slur_s=True)
    m += n("D", 6, 256, "quarter")
    m += n("B", 5, 256, "quarter", slur_e=True)
    m += bk(1024)
    # LH: F#m9 voicing
    m += n("F", 2, 512, "half", alt=1, staff=2)
    m += n("C", 3, 512, "half", alt=1, chord=True, staff=2)
    m += n("E", 3, 256, "quarter", staff=2)
    m += n("G", 3, 256, "quarter", alt=1, chord=True, staff=2)
    m += n("A", 3, 256, "quarter", staff=2)
    m += '    </measure>\n'
    
    # ===== BAR 7: Long-line expansion =====
    m += '    <measure number="7">\n'
    m += h("C", "major-seventh", [(11, 1, "add")])  # Cmaj7#11
    # RH: Expanded intervals - G-B-F#-A
    m += n("G", 5, 256, "quarter", slur_s=True)
    m += n("B", 5, 384, "quarter", dot=True)
    m += n("F", 5, 128, "eighth", alt=1)
    m += n("A", 5, 256, "quarter", slur_e=True)
    m += bk(1024)
    # LH: Cmaj7#11 - floating
    m += n("C", 3, 384, "quarter", dot=True, staff=2)
    m += n("G", 3, 128, "eighth", staff=2)
    m += n("B", 3, 256, "quarter", chord=True, staff=2)
    m += n("E", 3, 256, "quarter", staff=2)
    m += n("F", 3, 256, "quarter", alt=1, chord=True, staff=2)
    m += '    </measure>\n'
    
    # ===== BAR 8: Suspension, breathing =====
    m += '    <measure number="8">\n'
    m += h("G", "major", [(9, 0, "add"), (11, 1, "add")])  # Gadd9#11
    # RH: Held D with ornament
    m += n("D", 5, 768, "half", dot=True, slur_s=True)
    m += n("E", 5, 256, "quarter", slur_e=True)
    m += bk(1024)
    # LH: G add9#11
    m += n("G", 2, 512, "half", staff=2)
    m += n("D", 3, 512, "half", chord=True, staff=2)
    m += n("A", 3, 256, "quarter", staff=2)
    m += n("C", 4, 256, "quarter", alt=1, chord=True, staff=2)
    m += n("B", 3, 256, "quarter", staff=2)
    m += '    </measure>\n'
    
    # ===== BAR 9: Coda - Motif fragment in pianissimo =====
    m += '    <measure number="9">\n'
    m += d("Coda - dissolving")
    m += d(dyn="pp")
    m += h("E", "major-seventh", [(11, 1, "add")])  # Emaj7#11
    # RH: G-A-B only, stretched
    m += n("G", 5, 512, "half", slur_s=True)
    m += n("A", 5, 512, "half", slur_e=True)
    m += bk(1024)
    # LH: Emaj7#11 sustained
    m += n("E", 2, 1024, "whole", staff=2)
    m += n("B", 2, 1024, "whole", chord=True, staff=2)
    m += n("G", 3, 1024, "whole", alt=1, chord=True, staff=2)
    m += '    </measure>\n'
    
    # ===== BAR 10: Continuation =====
    m += '    <measure number="10">\n'
    m += h("A", "major-seventh", [(9, 0, "add")])  # Amaj9
    # RH: B held, fading
    m += n("B", 5, 768, "half", dot=True, slur_s=True)
    m += n("F", 5, 256, "quarter", alt=1, slur_e=True)
    m += bk(1024)
    # LH: Amaj9
    m += n("A", 2, 512, "half", staff=2)
    m += n("E", 3, 512, "half", chord=True, staff=2)
    m += n("G", 3, 256, "quarter", alt=1, staff=2)
    m += n("B", 3, 256, "quarter", chord=True, staff=2)
    m += n("C", 4, 256, "quarter", alt=1, staff=2)
    m += '    </measure>\n'
    
    # ===== BAR 11: Final descent =====
    m += '    <measure number="11">\n'
    m += d("rit.")
    m += h("D", "major-seventh", [(11, 1, "add")])  # Dmaj7#11
    # RH: E-D final gesture
    m += n("E", 5, 512, "half", slur_s=True)
    m += n("D", 5, 512, "half", slur_e=True)
    m += bk(1024)
    # LH: Dmaj7#11
    m += n("D", 2, 512, "half", staff=2)
    m += n("A", 2, 512, "half", chord=True, staff=2)
    m += n("G", 3, 256, "quarter", alt=1, staff=2)
    m += n("C", 4, 256, "quarter", alt=1, chord=True, staff=2)
    m += n("F", 3, 256, "quarter", alt=1, staff=2)
    m += '    </measure>\n'
    
    # ===== BAR 12: Final chord =====
    m += '    <measure number="12">\n'
    m += h("G", "major-seventh", [(9, 0, "add"), (11, 1, "add")])  # Gmaj9#11
    # RH: Final G
    m += n("G", 5, 1024, "whole", ferm=True)
    m += bk(1024)
    # LH: Gmaj9#11 final
    m += n("G", 2, 1024, "whole", staff=2)
    m += n("D", 3, 1024, "whole", chord=True, staff=2)
    m += n("F", 3, 1024, "whole", alt=1, chord=True, staff=2)
    m += n("A", 3, 1024, "whole", chord=True, staff=2)
    m += bar()
    m += '    </measure>\n'
    
    return m

def main():
    xml = HDR + gen() + FTR
    out = os.path.join(os.path.dirname(__file__), "..", "scores", "V2-Gil-Mvmt2-11-Dec-2025.musicxml")
    out = os.path.normpath(out)
    with open(out, "w", encoding="utf-8") as f:
        f.write(xml)
    print(f"Generated: {out}")

if __name__ == "__main__":
    main()



