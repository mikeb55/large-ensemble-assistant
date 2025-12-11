#!/usr/bin/env python3
"""Movement I - Mingus Gospel Cathedral - FINAL with Criteria of Excellence"""

# Chord symbol helper - Sibelius-compatible format
def ch(root, kind, alter=0, text=''):
    s = f'<harmony><root><root-step>{root}</root-step>'
    if alter: s += f'<root-alter>{alter}</root-alter>'
    s += f'</root><kind'
    if text: s += f' text="{text}"'
    s += f'>{kind}</kind></harmony>'
    return s

# Note helper
def n(p, o, d, t, st, a=0, dot=False, ss=False, se=False, fm=False):
    s = '<note><pitch><step>'+p+'</step>'
    if a: s += f'<alter>{a}</alter>'
    s += f'<octave>{o}</octave></pitch><duration>{d}</duration><type>{t}</type>'
    if dot: s += '<dot/>'
    s += f'<staff>{st}</staff>'
    if ss or se or fm:
        s += '<notations>'
        if ss: s += '<slur type="start"/>'
        if se: s += '<slur type="stop"/>'
        if fm: s += '<fermata/>'
        s += '</notations>'
    s += '</note>'
    return s

def r(d, t, st):
    return f'<note><rest/><duration>{d}</duration><type>{t}</type><staff>{st}</staff></note>'

def attrs():
    return '''<attributes><divisions>480</divisions><key><fifths>-3</fifths><mode>minor</mode></key>
<time><beats>4</beats><beat-type>4</beat-type></time><staves>2</staves>
<clef number="1"><sign>G</sign><line>2</line></clef>
<clef number="2"><sign>F</sign><line>4</line></clef></attributes>'''

def dir(txt='', reh='', tmp=0, dyn=''):
    s = '<direction placement="above"><direction-type>'
    if reh: s += f'<rehearsal>{reh}</rehearsal>'
    if tmp: s += f'<metronome><beat-unit>quarter</beat-unit><per-minute>{tmp}</per-minute></metronome>'
    if txt: s += f'<words font-style="italic">{txt}</words>'
    if dyn: s += f'<dynamics><{dyn}/></dynamics>'
    s += '</direction-type></direction>'
    return s

mvmt = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
<work><work-title>The Master's Palette - I. Mingus Gospel Cathedral</work-title></work>
<identification><creator type="composer">Michael Bryant</creator><rights>© 2025 Michael Bryant. All Rights Reserved.</rights></identification>
<part-list><score-part id="P1"><part-name>Piano</part-name></score-part></part-list>
<part id="P1">
'''

# M1: Motif C-Eb-F statement with gospel LH
mvmt += f'''<measure number="1">
{attrs()}
{dir(reh='A', tmp=72)}
{dir(txt='Fierce gospel soul', dyn='mf')}
{ch('C','dominant-13th',0,'7(9,13)')}
{r(120,'16th',1)}
{n('C',5,120,'16th',1,ss=True)}{n('E',5,120,'16th',1,-1)}{n('F',5,360,'eighth',1,dot=True)}
{n('G',5,240,'eighth',1)}{n('A',5,480,'quarter',1)}{n('G',5,480,'quarter',1,se=True)}
{n('C',3,360,'eighth',2,dot=True)}{n('G',3,120,'16th',2)}{n('B',3,240,'eighth',2,-1)}{n('E',4,240,'eighth',2,-1)}
{n('G',3,360,'eighth',2,dot=True)}{n('C',4,120,'16th',2)}{n('E',4,240,'eighth',2,-1)}{n('B',3,240,'eighth',2,-1)}
</measure>
'''

# M2: Continuation
mvmt += f'''<measure number="2">
{ch('F','suspended-fourth',0,'13sus')}
{n('F',5,360,'eighth',1,dot=True,ss=True)}{n('E',5,120,'16th',1,-1)}{n('C',5,240,'eighth',1)}{n('B',4,480,'quarter',1,-1)}
{n('A',4,720,'quarter',1,-1,dot=True,se=True)}{n('G',4,240,'eighth',1)}
{n('F',2,360,'eighth',2,dot=True)}{n('C',3,120,'16th',2)}{n('E',3,240,'eighth',2,-1)}{n('B',3,240,'eighth',2,-1)}
{n('D',4,360,'eighth',2,dot=True)}{n('A',3,120,'16th',2,-1)}{n('C',4,240,'eighth',2)}{n('F',3,240,'eighth',2)}
</measure>
'''

# M3: Motif restated with variation
mvmt += f'''<measure number="3">
{ch('C','minor-ninth',0,'m9')}
{n('C',5,120,'16th',1,ss=True)}{n('E',5,120,'16th',1,-1)}{n('F',5,240,'eighth',1)}{n('G',5,480,'quarter',1)}
{n('A',5,360,'eighth',1,-1,dot=True)}{n('G',5,120,'16th',1)}{n('F',5,480,'quarter',1,se=True)}
{n('C',3,360,'eighth',2,dot=True)}{n('G',3,120,'16th',2)}{n('B',3,240,'eighth',2,-1)}{n('D',4,240,'eighth',2)}
{n('E',4,360,'eighth',2,-1,dot=True)}{n('B',3,120,'16th',2,-1)}{n('D',4,240,'eighth',2)}{n('G',3,240,'eighth',2)}
</measure>
'''

# M4: Dominant resolution
mvmt += f'''<measure number="4">
{ch('G','dominant',0,'7(b9,#9)')}
{n('E',5,480,'quarter',1,-1,ss=True)}{n('D',5,240,'eighth',1)}{n('C',5,240,'eighth',1)}
{n('B',4,720,'quarter',1,dot=True)}{n('A',4,240,'eighth',1,-1,se=True)}
{n('G',2,360,'eighth',2,dot=True)}{n('D',3,120,'16th',2)}{n('F',3,240,'eighth',2)}{n('A',3,240,'eighth',2,-1)}
{n('B',3,360,'eighth',2,dot=True)}{n('F',3,120,'16th',2)}{n('A',3,240,'eighth',2,-1)}{n('D',3,240,'eighth',2)}
</measure>
'''

# M5-8: A section continues
mvmt += f'''<measure number="5">
{ch('C','dominant-13th',0,'7(9,13)')}
{n('C',5,120,'16th',1,ss=True)}{n('E',5,120,'16th',1,-1)}{n('F',5,120,'16th',1)}{n('G',5,120,'16th',1)}
{n('B',5,480,'quarter',1,-1)}{n('A',5,480,'quarter',1)}{n('G',5,480,'quarter',1,se=True)}
{n('C',3,360,'eighth',2,dot=True)}{n('G',3,120,'16th',2)}{n('B',3,240,'eighth',2,-1)}{n('E',4,240,'eighth',2,-1)}
{n('A',3,360,'eighth',2,dot=True)}{n('C',4,120,'16th',2)}{n('E',4,240,'eighth',2,-1)}{n('G',3,240,'eighth',2)}
</measure>
'''

mvmt += f'''<measure number="6">
{ch('A','major-seventh',-1,'maj7(#11)')}
{n('E',5,720,'quarter',1,-1,dot=True,ss=True)}{n('C',5,240,'eighth',1)}{n('A',4,480,'quarter',1,-1)}
{n('G',4,480,'quarter',1,se=True)}
{n('A',2,360,'eighth',2,-1,dot=True)}{n('E',3,120,'16th',2,-1)}{n('G',3,240,'eighth',2)}{n('C',4,240,'eighth',2)}
{n('D',4,360,'eighth',2,dot=True)}{n('G',3,120,'16th',2)}{n('C',4,240,'eighth',2)}{n('E',3,240,'eighth',2,-1)}
</measure>
'''

mvmt += f'''<measure number="7">
{ch('D','dominant',0,'7(b9)')}
{n('F',5,360,'eighth',1,dot=True,ss=True)}{n('E',5,120,'16th',1,-1)}{n('C',5,240,'eighth',1)}{n('B',4,240,'eighth',1)}
{n('D',5,960,'half',1,se=True)}
{n('D',3,360,'eighth',2,dot=True)}{n('A',3,120,'16th',2)}{n('C',4,240,'eighth',2)}{n('E',4,240,'eighth',2,-1)}
{n('F',3,360,'eighth',2,1,dot=True)}{n('C',4,120,'16th',2)}{n('E',4,240,'eighth',2,-1)}{n('A',3,240,'eighth',2)}
</measure>
'''

mvmt += f'''<measure number="8">
{ch('G','suspended-fourth',0,'7sus')}
{n('G',5,1200,'half',1,dot=True)}{r(240,'eighth',1)}{n('D',5,240,'eighth',1)}
{n('G',2,360,'eighth',2,dot=True)}{n('D',3,120,'16th',2)}{n('F',3,240,'eighth',2)}{n('C',4,240,'eighth',2)}
{n('D',4,360,'eighth',2,dot=True)}{n('F',3,120,'16th',2)}{n('C',4,240,'eighth',2)}{n('G',3,240,'eighth',2)}
</measure>
'''

# A2 section (m9-16): Sequence up
mvmt += f'''<measure number="9">
{dir(reh='A2')}
{dir(txt='Sequence up - intensifying')}
{ch('E','major-ninth',-1,'maj9')}
{r(120,'16th',1)}
{n('E',5,120,'16th',1,-1,ss=True)}{n('G',5,120,'16th',1,-1)}{n('A',5,360,'eighth',1,-1,dot=True)}
{n('B',5,240,'eighth',1,-1)}{n('C',6,480,'quarter',1)}{n('B',5,480,'quarter',1,-1,se=True)}
{n('E',3,360,'eighth',2,-1,dot=True)}{n('B',3,120,'16th',2,-1)}{n('D',4,240,'eighth',2)}{n('G',4,240,'eighth',2,-1)}
{n('F',4,360,'eighth',2,dot=True)}{n('B',3,120,'16th',2,-1)}{n('D',4,240,'eighth',2)}{n('E',3,240,'eighth',2,-1)}
</measure>
'''

mvmt += f'''<measure number="10">
{ch('A','dominant-ninth',-1,'7(9)')}
{n('A',5,360,'eighth',1,-1,dot=True,ss=True)}{n('G',5,120,'16th',1,-1)}{n('E',5,240,'eighth',1,-1)}{n('D',5,480,'quarter',1,-1)}
{n('C',5,720,'quarter',1,dot=True,se=True)}{n('B',4,240,'eighth',1,-1)}
{n('A',2,360,'eighth',2,-1,dot=True)}{n('E',3,120,'16th',2,-1)}{n('G',3,240,'eighth',2,-1)}{n('C',4,240,'eighth',2)}
{n('B',3,360,'eighth',2,-1,dot=True)}{n('E',3,120,'16th',2,-1)}{n('G',3,240,'eighth',2,-1)}{n('A',3,240,'eighth',2,-1)}
</measure>
'''

mvmt += f'''<measure number="11">
{ch('D','major-seventh',-1,'maj7(#11)')}
{n('D',5,120,'16th',1,-1,ss=True)}{n('F',5,120,'16th',1)}{n('A',5,240,'eighth',1,-1)}{n('C',6,480,'quarter',1)}
{n('B',5,360,'eighth',1,-1,dot=True)}{n('A',5,120,'16th',1,-1)}{n('G',5,480,'quarter',1,-1,se=True)}
{n('D',3,360,'eighth',2,-1,dot=True)}{n('A',3,120,'16th',2,-1)}{n('C',4,240,'eighth',2)}{n('F',4,240,'eighth',2)}
{n('G',4,360,'eighth',2,dot=True)}{n('C',4,120,'16th',2)}{n('F',4,240,'eighth',2)}{n('A',3,240,'eighth',2,-1)}
</measure>
'''

mvmt += f'''<measure number="12">
{ch('G','dominant',0,'7(#9)')}
{n('F',5,480,'quarter',1,ss=True)}{n('E',5,240,'eighth',1,-1)}{n('D',5,240,'eighth',1)}
{n('F',5,720,'quarter',1,dot=True)}{n('E',5,240,'eighth',1,-1,se=True)}
{n('G',2,360,'eighth',2,dot=True)}{n('D',3,120,'16th',2)}{n('F',3,240,'eighth',2)}{n('B',3,240,'eighth',2)}
{n('A',3,360,'eighth',2,-1,dot=True)}{n('D',3,120,'16th',2)}{n('F',3,240,'eighth',2)}{n('G',3,240,'eighth',2)}
</measure>
'''

mvmt += f'''<measure number="13">
{ch('C','minor-seventh',0,'m7')}
{n('C',5,120,'16th',1,ss=True)}{n('E',5,120,'16th',1,-1)}{n('F',5,120,'16th',1)}{n('G',5,120,'16th',1)}
{n('A',5,480,'quarter',1,-1)}{n('B',5,480,'quarter',1,-1)}{n('A',5,480,'quarter',1,-1,se=True)}
{n('C',3,360,'eighth',2,dot=True)}{n('G',3,120,'16th',2)}{n('B',3,240,'eighth',2,-1)}{n('E',4,240,'eighth',2,-1)}
{n('G',3,360,'eighth',2,dot=True)}{n('B',3,120,'16th',2,-1)}{n('E',4,240,'eighth',2,-1)}{n('C',4,240,'eighth',2)}
</measure>
'''

mvmt += f'''<measure number="14">
{ch('F','minor-ninth',0,'m9')}
{n('C',6,720,'quarter',1,dot=True,ss=True)}{n('A',5,240,'eighth',1,-1)}{n('G',5,480,'quarter',1)}
{n('F',5,480,'quarter',1,se=True)}
{n('F',2,360,'eighth',2,dot=True)}{n('C',3,120,'16th',2)}{n('E',3,240,'eighth',2,-1)}{n('A',3,240,'eighth',2,-1)}
{n('G',3,360,'eighth',2,dot=True)}{n('C',3,120,'16th',2)}{n('E',3,240,'eighth',2,-1)}{n('F',3,240,'eighth',2)}
</measure>
'''

mvmt += f'''<measure number="15">
{ch('B','dominant-ninth',-1,'7(9)')}
{n('F',5,360,'eighth',1,dot=True,ss=True)}{n('E',5,120,'16th',1,-1)}{n('C',5,240,'eighth',1)}{n('B',4,240,'eighth',1,-1)}
{n('D',5,960,'half',1,se=True)}
{n('B',2,360,'eighth',2,-1,dot=True)}{n('F',3,120,'16th',2)}{n('A',3,240,'eighth',2,-1)}{n('D',4,240,'eighth',2)}
{n('C',4,360,'eighth',2,dot=True)}{n('F',3,120,'16th',2)}{n('A',3,240,'eighth',2,-1)}{n('B',3,240,'eighth',2,-1)}
</measure>
'''

mvmt += f'''<measure number="16">
{ch('E','major-seventh',-1,'maj7')}
{n('E',5,1200,'half',1,-1,dot=True)}{r(240,'eighth',1)}{n('G',5,240,'eighth',1,-1)}
{n('E',3,360,'eighth',2,-1,dot=True)}{n('B',3,120,'16th',2,-1)}{n('D',4,240,'eighth',2)}{n('G',4,240,'eighth',2,-1)}
{n('F',4,360,'eighth',2,dot=True)}{n('B',3,120,'16th',2,-1)}{n('D',4,240,'eighth',2)}{n('E',3,240,'eighth',2,-1)}
</measure>
'''

# B section (m17-24): Inverted motif, cathedral
mvmt += f'''<measure number="17">
{dir(reh='B')}
{dir(txt='Cathedral - inverted motif', dyn='mp')}
{ch('A','major-seventh',-1,'maj7(#11)')}
{n('E',5,720,'quarter',1,-1,dot=True,ss=True)}{n('D',5,240,'eighth',1)}{n('C',5,480,'quarter',1)}
{n('A',4,480,'quarter',1,-1,se=True)}
{n('A',2,480,'quarter',2,-1)}{n('E',3,480,'quarter',2,-1)}{n('G',3,240,'eighth',2)}{n('C',4,240,'eighth',2)}
{n('D',4,480,'quarter',2)}
</measure>
'''

mvmt += f'''<measure number="18">
{ch('D','major-ninth',-1,'maj9')}
{n('F',5,960,'half',1,ss=True)}{n('A',5,480,'quarter',1,-1)}{n('G',5,480,'quarter',1,-1,se=True)}
{n('D',3,480,'quarter',2,-1)}{n('A',3,480,'quarter',2,-1)}{n('C',4,240,'eighth',2)}{n('F',4,240,'eighth',2)}
{n('E',4,480,'quarter',2,-1)}
</measure>
'''

mvmt += f'''<measure number="19">
{ch('G','major-seventh',-1,'maj7')}
{n('G',5,480,'quarter',1,-1,ss=True)}{n('F',5,240,'eighth',1)}{n('D',5,240,'eighth',1,-1)}
{n('B',4,720,'quarter',1,-1,dot=True)}{n('A',4,240,'eighth',1,-1,se=True)}
{n('G',2,480,'quarter',2,-1)}{n('D',3,480,'quarter',2,-1)}{n('F',3,240,'eighth',2)}{n('B',3,240,'eighth',2,-1)}
{n('D',4,480,'quarter',2,-1)}
</measure>
'''

mvmt += f'''<measure number="20">
{ch('C','suspended-fourth',0,'7sus')}
{n('C',5,1920,'whole',1)}
{n('C',3,480,'quarter',2)}{n('G',3,480,'quarter',2)}{n('B',3,240,'eighth',2,-1)}{n('F',4,240,'eighth',2)}
{n('E',4,480,'quarter',2,-1)}
</measure>
'''

mvmt += f'''<measure number="21">
{ch('F','minor-11th',0,'m11')}
{n('F',5,240,'eighth',1,ss=True)}{n('E',5,240,'eighth',1,-1)}{n('C',5,480,'quarter',1)}
{n('A',4,720,'quarter',1,-1,dot=True)}{n('G',4,240,'eighth',1,se=True)}
{n('F',2,480,'quarter',2)}{n('C',3,480,'quarter',2)}{n('E',3,240,'eighth',2,-1)}{n('B',3,240,'eighth',2,-1)}
{n('C',4,480,'quarter',2)}
</measure>
'''

mvmt += f'''<measure number="22">
{ch('B','major-seventh',-1,'maj7(#11)')}
{n('D',5,720,'quarter',1,dot=True,ss=True)}{n('F',5,240,'eighth',1)}{n('A',5,480,'quarter',1)}
{n('G',5,480,'quarter',1,se=True)}
{n('B',2,480,'quarter',2,-1)}{n('F',3,480,'quarter',2)}{n('A',3,240,'eighth',2)}{n('D',4,240,'eighth',2)}
{n('E',4,480,'quarter',2)}
</measure>
'''

mvmt += f'''<measure number="23">
{ch('E','minor-seventh',-1,'m7')}
{n('G',5,360,'eighth',1,dot=True,ss=True)}{n('E',5,120,'16th',1,-1)}{n('D',5,240,'eighth',1)}{n('C',5,240,'eighth',1)}
{n('B',4,960,'half',1,-1,se=True)}
{n('E',3,360,'eighth',2,-1,dot=True)}{n('B',3,120,'16th',2,-1)}{n('D',4,240,'eighth',2)}{n('G',4,240,'eighth',2,-1)}
{n('B',3,360,'eighth',2,-1,dot=True)}{n('D',4,120,'16th',2)}{n('G',4,240,'eighth',2,-1)}{n('E',4,480,'quarter',2,-1)}
</measure>
'''

mvmt += f'''<measure number="24">
{ch('G','dominant',0,'7(b9,#9)')}
{n('B',4,1200,'half',1,dot=True)}{r(240,'eighth',1)}{n('G',5,240,'eighth',1)}
{n('G',2,360,'eighth',2,dot=True)}{n('D',3,120,'16th',2)}{n('F',3,240,'eighth',2)}{n('A',3,240,'eighth',2,-1)}
{n('B',3,360,'eighth',2,dot=True)}{n('F',3,120,'16th',2)}{n('A',3,240,'eighth',2,-1)}{n('G',3,240,'eighth',2)}
</measure>
'''

# Coda (m25-32): Triumphant return
mvmt += f'''<measure number="25">
{dir(reh='Coda')}
{dir(txt='Triumphant return', dyn='f')}
{ch('C','dominant-13th',0,'7(9,13)')}
{r(120,'16th',1)}
{n('C',5,120,'16th',1,ss=True)}{n('E',5,120,'16th',1,-1)}{n('F',5,360,'eighth',1,dot=True)}
{n('G',5,240,'eighth',1)}{n('A',5,480,'quarter',1)}{n('B',5,480,'quarter',1,-1,se=True)}
{n('C',3,360,'eighth',2,dot=True)}{n('G',3,120,'16th',2)}{n('B',3,240,'eighth',2,-1)}{n('E',4,240,'eighth',2,-1)}
{n('A',3,360,'eighth',2,dot=True)}{n('C',4,120,'16th',2)}{n('E',4,240,'eighth',2,-1)}{n('G',3,240,'eighth',2)}
</measure>
'''

mvmt += f'''<measure number="26">
{ch('F','dominant-ninth',0,'7(9)')}
{n('C',6,360,'eighth',1,dot=True,ss=True)}{n('A',5,120,'16th',1)}{n('G',5,240,'eighth',1)}{n('F',5,480,'quarter',1)}
{n('E',5,720,'quarter',1,-1,dot=True,se=True)}{n('D',5,240,'eighth',1)}
{n('F',2,360,'eighth',2,dot=True)}{n('C',3,120,'16th',2)}{n('E',3,240,'eighth',2,-1)}{n('A',3,240,'eighth',2)}
{n('G',3,360,'eighth',2,dot=True)}{n('C',3,120,'16th',2)}{n('E',3,240,'eighth',2,-1)}{n('F',3,240,'eighth',2)}
</measure>
'''

mvmt += f'''<measure number="27">
{ch('C','minor-ninth',0,'m9')}
{n('E',5,240,'eighth',1,-1,ss=True)}{n('C',5,120,'16th',1)}{n('E',5,120,'16th',1,-1)}{n('F',5,360,'eighth',1,dot=True)}
{n('G',5,120,'16th',1)}{n('A',5,480,'quarter',1,-1)}{n('G',5,480,'quarter',1,se=True)}
{n('C',3,360,'eighth',2,dot=True)}{n('G',3,120,'16th',2)}{n('B',3,240,'eighth',2,-1)}{n('D',4,240,'eighth',2)}
{n('E',4,360,'eighth',2,-1,dot=True)}{n('B',3,120,'16th',2,-1)}{n('D',4,240,'eighth',2)}{n('C',4,240,'eighth',2)}
</measure>
'''

mvmt += f'''<measure number="28">
{ch('G','dominant',0,'7(b9)')}
{n('F',5,360,'eighth',1,dot=True,ss=True)}{n('E',5,120,'16th',1,-1)}{n('D',5,240,'eighth',1)}{n('C',5,240,'eighth',1)}
{n('B',4,960,'half',1,se=True)}
{n('G',2,360,'eighth',2,dot=True)}{n('D',3,120,'16th',2)}{n('F',3,240,'eighth',2)}{n('A',3,240,'eighth',2,-1)}
{n('B',3,360,'eighth',2,dot=True)}{n('F',3,120,'16th',2)}{n('A',3,240,'eighth',2,-1)}{n('G',3,240,'eighth',2)}
</measure>
'''

mvmt += f'''<measure number="29">
{ch('C','dominant-13th',0,'7(9,13)')}
{n('C',5,120,'16th',1,ss=True)}{n('E',5,120,'16th',1,-1)}{n('F',5,240,'eighth',1)}{n('G',5,360,'eighth',1,dot=True)}
{n('A',5,120,'16th',1)}{n('G',5,720,'quarter',1,dot=True,se=True)}{n('E',5,240,'eighth',1,-1)}
{n('C',3,360,'eighth',2,dot=True)}{n('G',3,120,'16th',2)}{n('B',3,240,'eighth',2,-1)}{n('E',4,240,'eighth',2,-1)}
{n('A',3,360,'eighth',2,dot=True)}{n('C',4,120,'16th',2)}{n('E',4,240,'eighth',2,-1)}{n('G',3,240,'eighth',2)}
</measure>
'''

mvmt += f'''<measure number="30">
{ch('A','major-seventh',-1,'maj7')}
{n('E',5,720,'quarter',1,-1,dot=True,ss=True)}{n('C',5,240,'eighth',1)}{n('A',4,960,'half',1,-1,se=True)}
{n('A',2,360,'eighth',2,-1,dot=True)}{n('E',3,120,'16th',2,-1)}{n('G',3,240,'eighth',2)}{n('C',4,240,'eighth',2)}
{n('E',4,360,'eighth',2,-1,dot=True)}{n('G',3,120,'16th',2)}{n('C',4,240,'eighth',2)}{n('A',3,240,'eighth',2,-1)}
</measure>
'''

mvmt += f'''<measure number="31">
{ch('G','suspended-fourth',0,'7sus')}
{n('D',5,480,'quarter',1,ss=True)}{n('C',5,240,'eighth',1)}{n('B',4,240,'eighth',1,-1)}
{n('G',4,960,'half',1,se=True)}
{n('G',2,360,'eighth',2,dot=True)}{n('D',3,120,'16th',2)}{n('F',3,240,'eighth',2)}{n('C',4,240,'eighth',2)}
{n('D',4,360,'eighth',2,dot=True)}{n('F',3,120,'16th',2)}{n('C',4,240,'eighth',2)}{n('G',3,240,'eighth',2)}
</measure>
'''

mvmt += f'''<measure number="32">
{ch('C','minor',0,'m(add9)')}
<note><pitch><step>C</step><octave>5</octave></pitch><duration>1920</duration><type>whole</type><staff>1</staff><notations><fermata/></notations></note>
{n('C',3,480,'quarter',2)}{n('G',3,480,'quarter',2)}{n('E',4,240,'eighth',2,-1)}{n('D',4,240,'eighth',2)}
<note><pitch><step>E</step><alter>-1</alter><octave>4</octave></pitch><duration>480</duration><type>quarter</type><staff>2</staff><notations><fermata/></notations></note>
<barline><bar-style>light-heavy</bar-style></barline>
</measure>
'''

mvmt += '''</part>
</score-partwise>'''

with open('scores/MastersPalette-Mvmt1-Excellent.musicxml', 'w', encoding='utf-8') as f:
    f.write(mvmt)
print("Created: MastersPalette-Mvmt1-Excellent.musicxml (32 bars)")





