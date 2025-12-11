#!/usr/bin/env python3
"""Generate Movement II - Gil Evans Pastel Cloud"""

def header(title):
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
<work><work-title>{title}</work-title></work>
<identification><creator type="composer">Michael Bryant</creator><rights>© 2025 Michael Bryant. All Rights Reserved.</rights></identification>
<part-list><score-part id="P1"><part-name>Piano</part-name></score-part></part-list>
<part id="P1">'''

def footer():
    return '''</part>
</score-partwise>'''

def n(step, octave, dur, typ, staff, alter=0, dot=False, slur_start=False, slur_stop=False, fermata=False, rest=False):
    s = '<note>'
    if rest:
        s += '<rest/>'
    else:
        s += f'<pitch><step>{step}</step>'
        if alter: s += f'<alter>{alter}</alter>'
        s += f'<octave>{octave}</octave></pitch>'
    s += f'<duration>{dur}</duration><type>{typ}</type>'
    if dot: s += '<dot/>'
    s += f'<staff>{staff}</staff>'
    if slur_start or slur_stop or fermata:
        s += '<notations>'
        if slur_start: s += '<slur type="start"/>'
        if slur_stop: s += '<slur type="stop"/>'
        if fermata: s += '<fermata/>'
        s += '</notations>'
    s += '</note>'
    return s

def chord(root, kind, alter=0, text=''):
    s = f'<harmony><root><root-step>{root}</root-step>'
    if alter: s += f'<root-alter>{alter}</root-alter>'
    s += f'</root><kind'
    if text: s += f' text="{text}"'
    s += f'>{kind}</kind></harmony>'
    return s

def attrs(div=480, fifths=0, beats=4, bt=4):
    return f'''<attributes><divisions>{div}</divisions><key><fifths>{fifths}</fifths></key>
<time><beats>{beats}</beats><beat-type>{bt}</beat-type></time><staves>2</staves>
<clef number="1"><sign>G</sign><line>2</line></clef><clef number="2"><sign>F</sign><line>4</line></clef></attributes>'''

def direction(text='', rehearsal='', tempo=0, dyn=''):
    s = '<direction placement="above"><direction-type>'
    if rehearsal: s += f'<rehearsal>{rehearsal}</rehearsal>'
    if tempo: s += f'<metronome><beat-unit>quarter</beat-unit><per-minute>{tempo}</per-minute></metronome>'
    if text: s += f'<words font-style="italic">{text}</words>'
    if dyn: s += f'<dynamics><{dyn}/></dynamics>'
    s += '</direction-type></direction>'
    return s

def bar(style='light-heavy'):
    return f'<barline><bar-style>{style}</bar-style></barline>'

# Movement II: Gil Evans Pastel Cloud
mvmt2 = header("The Master's Palette - II. Gil Evans Pastel Cloud")
mvmt2 += f'''
<measure number="1">
{attrs(480, -2, 4, 4)}
{direction(rehearsal='A', tempo=58)}
{direction(text='Floating, luminous', dyn='p')}
{chord('B','major-ninth',-1,'maj9(#11)')}
<note><rest/><duration>240</duration><type>eighth</type><staff>1</staff></note>
{n('B',4,360,'eighth',1,-1,dot=True,slur_start=True)}{n('D',5,120,'16th',1)}{n('F',5,480,'quarter',1)}
{n('A',5,720,'quarter',1,dot=True,slur_stop=True)}{n('G',5,240,'eighth',1)}
{n('B',2,960,'half',2,-1)}{n('F',3,240,'eighth',2)}{n('A',3,240,'eighth',2)}{n('D',4,240,'eighth',2)}{n('E',4,240,'eighth',2)}
</measure>
<measure number="2">
{chord('E','major-seventh',-1,'maj7(#11)')}
{n('G',5,720,'quarter',1,dot=True,slur_start=True)}{n('F',5,240,'eighth',1)}{n('E',5,960,'half',1,-1,slur_stop=True)}
{n('E',3,960,'half',2,-1)}{n('B',3,240,'eighth',2,-1)}{n('D',4,240,'eighth',2)}{n('G',4,240,'eighth',2,-1)}{n('A',4,240,'eighth',2)}
</measure>
<measure number="3">
{chord('A','major-ninth',-1,'maj9')}
<note><rest/><duration>240</duration><type>eighth</type><staff>1</staff></note>
{n('A',4,360,'eighth',1,-1,dot=True,slur_start=True)}{n('C',5,120,'16th',1)}{n('E',5,480,'quarter',1,-1)}
{n('G',5,720,'quarter',1,dot=True,slur_stop=True)}{n('F',5,240,'eighth',1)}
{n('A',2,960,'half',2,-1)}{n('E',3,240,'eighth',2,-1)}{n('G',3,240,'eighth',2)}{n('C',4,240,'eighth',2)}{n('B',3,240,'eighth',2,-1)}
</measure>
<measure number="4">
{chord('D','major-seventh',-1,'maj7(#11)')}
{n('F',5,720,'quarter',1,dot=True,slur_start=True)}{n('E',5,240,'eighth',1,-1)}{n('D',5,960,'half',1,-1,slur_stop=True)}
{n('D',3,960,'half',2,-1)}{n('A',3,240,'eighth',2,-1)}{n('C',4,240,'eighth',2)}{n('F',4,240,'eighth',2)}{n('G',4,240,'eighth',2)}
</measure>
<measure number="5">
{chord('G','major-ninth',-1,'maj9(#11)')}
<note><rest/><duration>240</duration><type>eighth</type><staff>1</staff></note>
{n('G',4,360,'eighth',1,-1,dot=True,slur_start=True)}{n('B',4,120,'16th',1,-1)}{n('D',5,480,'quarter',1,-1)}
{n('F',5,720,'quarter',1,dot=True,slur_stop=True)}{n('E',5,240,'eighth',1,-1)}
{n('G',2,960,'half',2,-1)}{n('D',3,240,'eighth',2,-1)}{n('F',3,240,'eighth',2)}{n('B',3,240,'eighth',2,-1)}{n('C',4,240,'eighth',2)}
</measure>
<measure number="6">
{chord('C','major-ninth',0,'maj9(#11)')}
{n('E',5,720,'quarter',1,dot=True,slur_start=True)}{n('D',5,240,'eighth',1)}{n('C',5,480,'quarter',1)}
{n('B',4,480,'quarter',1,slur_stop=True)}
{n('C',3,960,'half',2)}{n('G',3,240,'eighth',2)}{n('B',3,240,'eighth',2)}{n('E',4,240,'eighth',2)}{n('F',4,240,'eighth',2,1)}
</measure>
<measure number="7">
{chord('F','major-ninth',0,'maj9')}
{n('A',5,480,'quarter',1,slur_start=True)}{n('G',5,240,'eighth',1)}{n('F',5,240,'eighth',1)}
{n('E',5,960,'half',1,slur_stop=True)}
{n('F',2,960,'half',2)}{n('C',3,240,'eighth',2)}{n('E',3,240,'eighth',2)}{n('A',3,240,'eighth',2)}{n('G',3,240,'eighth',2)}
</measure>
<measure number="8">
{chord('B','major-seventh',-1,'maj7')}
{n('D',5,1440,'half',1,dot=True)}<note><rest/><duration>240</duration><type>eighth</type><staff>1</staff></note>
{n('F',5,240,'eighth',1)}
{n('B',2,960,'half',2,-1)}{n('F',3,240,'eighth',2)}{n('A',3,240,'eighth',2)}{n('D',4,240,'eighth',2)}{n('C',4,240,'eighth',2)}
</measure>
<measure number="9">
{direction(rehearsal='A2')}
{direction(text='Motif ascending - expanded')}
{chord('E','major-ninth',-1,'maj9(#11)')}
<note><rest/><duration>240</duration><type>eighth</type><staff>1</staff></note>
{n('E',5,360,'eighth',1,-1,dot=True,slur_start=True)}{n('G',5,120,'16th',1)}{n('B',5,480,'quarter',1,-1)}
{n('D',6,720,'quarter',1,dot=True,slur_stop=True)}{n('C',6,240,'eighth',1)}
{n('E',3,960,'half',2,-1)}{n('B',3,240,'eighth',2,-1)}{n('D',4,240,'eighth',2)}{n('G',4,240,'eighth',2,-1)}{n('A',4,240,'eighth',2)}
</measure>
<measure number="10">
{chord('A','major-seventh',-1,'maj7(#11)')}
{n('C',6,720,'quarter',1,dot=True,slur_start=True)}{n('B',5,240,'eighth',1,-1)}{n('A',5,960,'half',1,-1,slur_stop=True)}
{n('A',2,960,'half',2,-1)}{n('E',3,240,'eighth',2,-1)}{n('G',3,240,'eighth',2)}{n('C',4,240,'eighth',2)}{n('D',4,240,'eighth',2)}
</measure>
<measure number="11">
{chord('D','major-ninth',-1,'maj9(#11)')}
<note><rest/><duration>240</duration><type>eighth</type><staff>1</staff></note>
{n('D',5,360,'eighth',1,-1,dot=True,slur_start=True)}{n('F',5,120,'16th',1)}{n('A',5,480,'quarter',1,-1)}
{n('C',6,720,'quarter',1,dot=True,slur_stop=True)}{n('B',5,240,'eighth',1,-1)}
{n('D',3,960,'half',2,-1)}{n('A',3,240,'eighth',2,-1)}{n('C',4,240,'eighth',2)}{n('F',4,240,'eighth',2)}{n('G',4,240,'eighth',2)}
</measure>
<measure number="12">
{chord('G','major-seventh',-1,'maj7')}
{n('B',5,720,'quarter',1,-1,dot=True,slur_start=True)}{n('A',5,240,'eighth',1,-1)}{n('G',5,960,'half',1,-1,slur_stop=True)}
{n('G',2,960,'half',2,-1)}{n('D',3,240,'eighth',2,-1)}{n('F',3,240,'eighth',2)}{n('B',3,240,'eighth',2,-1)}{n('A',3,240,'eighth',2,-1)}
</measure>
<measure number="13">
{chord('C','major-ninth',0,'maj9(#11)')}
<note><rest/><duration>240</duration><type>eighth</type><staff>1</staff></note>
{n('C',5,360,'eighth',1,dot=True,slur_start=True)}{n('E',5,120,'16th',1)}{n('G',5,480,'quarter',1)}
{n('B',5,720,'quarter',1,dot=True,slur_stop=True)}{n('A',5,240,'eighth',1)}
{n('C',3,960,'half',2)}{n('G',3,240,'eighth',2)}{n('B',3,240,'eighth',2)}{n('E',4,240,'eighth',2)}{n('F',4,240,'eighth',2,1)}
</measure>
<measure number="14">
{chord('F','major-seventh',0,'maj7(#11)')}
{n('A',5,720,'quarter',1,dot=True,slur_start=True)}{n('G',5,240,'eighth',1)}{n('F',5,480,'quarter',1)}
{n('E',5,480,'quarter',1,slur_stop=True)}
{n('F',2,960,'half',2)}{n('C',3,240,'eighth',2)}{n('E',3,240,'eighth',2)}{n('A',3,240,'eighth',2)}{n('B',3,240,'eighth',2)}
</measure>
<measure number="15">
{chord('B','major-ninth',-1,'maj9(#11)')}
{n('D',5,480,'quarter',1,slur_start=True)}{n('C',5,240,'eighth',1)}{n('B',4,240,'eighth',1,-1)}
{n('A',4,960,'half',1,slur_stop=True)}
{n('B',2,960,'half',2,-1)}{n('F',3,240,'eighth',2)}{n('A',3,240,'eighth',2)}{n('D',4,240,'eighth',2)}{n('E',4,240,'eighth',2)}
</measure>
<measure number="16">
{chord('E','major-seventh',-1,'maj7')}
{n('G',5,1440,'half',1,dot=True)}<note><rest/><duration>240</duration><type>eighth</type><staff>1</staff></note>
{n('A',5,240,'eighth',1)}
{n('E',3,960,'half',2,-1)}{n('B',3,240,'eighth',2,-1)}{n('D',4,240,'eighth',2)}{n('G',4,240,'eighth',2,-1)}{n('F',4,240,'eighth',2)}
</measure>
<measure number="17">
{direction(rehearsal='B')}
{direction(text='Inverted motif - bitonal colors')}
{chord('A','major-seventh',0,'maj7(#11)')}
{n('A',5,480,'quarter',1,slur_start=True)}{n('F',5,240,'eighth',1,1)}{n('D',5,240,'eighth',1)}
{n('B',4,960,'half',1,slur_stop=True)}
{n('A',2,960,'half',2)}{n('E',3,240,'eighth',2)}{n('G',3,240,'eighth',2,1)}{n('C',4,240,'eighth',2,1)}{n('D',4,240,'eighth',2,1)}
</measure>
<measure number="18">
{chord('D','major-ninth',0,'maj9(#11)')}
{n('C',5,720,'quarter',1,1,dot=True,slur_start=True)}{n('B',4,240,'eighth',1)}{n('A',4,480,'quarter',1)}
{n('F',5,480,'quarter',1,1,slur_stop=True)}
{n('D',3,960,'half',2)}{n('A',3,240,'eighth',2)}{n('C',4,240,'eighth',2,1)}{n('E',4,240,'eighth',2)}{n('G',4,240,'eighth',2,1)}
</measure>
<measure number="19">
{chord('G','major-seventh',0,'maj7(#11)')}
{n('B',5,480,'quarter',1,slur_start=True)}{n('A',5,240,'eighth',1)}{n('F',5,240,'eighth',1,1)}
{n('D',5,960,'half',1,slur_stop=True)}
{n('G',2,960,'half',2)}{n('D',3,240,'eighth',2)}{n('F',3,240,'eighth',2,1)}{n('B',3,240,'eighth',2)}{n('C',4,240,'eighth',2,1)}
</measure>
<measure number="20">
{chord('C','major-ninth',0,'maj9')}
{n('E',5,1920,'whole',1)}
{n('C',3,960,'half',2)}{n('G',3,240,'eighth',2)}{n('B',3,240,'eighth',2)}{n('D',4,240,'eighth',2)}{n('E',4,240,'eighth',2)}
</measure>
<measure number="21">
{chord('F','major-ninth',0,'maj9(#11)')}
<note><rest/><duration>240</duration><type>eighth</type><staff>1</staff></note>
{n('F',5,360,'eighth',1,dot=True,slur_start=True)}{n('A',5,120,'16th',1)}{n('C',6,480,'quarter',1)}
{n('E',6,720,'quarter',1,dot=True,slur_stop=True)}{n('D',6,240,'eighth',1)}
{n('F',2,960,'half',2)}{n('C',3,240,'eighth',2)}{n('E',3,240,'eighth',2)}{n('A',3,240,'eighth',2)}{n('B',3,240,'eighth',2)}
</measure>
<measure number="22">
{chord('B','major-seventh',-1,'maj7(#11)')}
{n('D',6,720,'quarter',1,dot=True,slur_start=True)}{n('C',6,240,'eighth',1)}{n('B',5,960,'half',1,-1,slur_stop=True)}
{n('B',2,960,'half',2,-1)}{n('F',3,240,'eighth',2)}{n('A',3,240,'eighth',2)}{n('D',4,240,'eighth',2)}{n('E',4,240,'eighth',2)}
</measure>
<measure number="23">
{chord('E','major-ninth',-1,'maj9(#11)')}
{n('G',5,480,'quarter',1,slur_start=True)}{n('F',5,240,'eighth',1)}{n('E',5,240,'eighth',1,-1)}
{n('D',5,480,'quarter',1)}{n('C',5,480,'quarter',1,slur_stop=True)}
{n('E',3,960,'half',2,-1)}{n('B',3,240,'eighth',2,-1)}{n('D',4,240,'eighth',2)}{n('G',4,240,'eighth',2,-1)}{n('A',4,240,'eighth',2)}
</measure>
<measure number="24">
{chord('A','major-seventh',-1,'maj7')}
{n('C',5,1440,'half',1,dot=True)}<note><rest/><duration>240</duration><type>eighth</type><staff>1</staff></note>
{n('D',5,240,'eighth',1)}
{n('A',2,960,'half',2,-1)}{n('E',3,240,'eighth',2,-1)}{n('G',3,240,'eighth',2)}{n('C',4,240,'eighth',2)}{n('B',3,240,'eighth',2,-1)}
</measure>
<measure number="25">
{direction(rehearsal="A'/Coda")}
{direction(text='Final bloom')}
{chord('B','major-ninth',-1,'maj9(#11)')}
<note><rest/><duration>240</duration><type>eighth</type><staff>1</staff></note>
{n('B',4,360,'eighth',1,-1,dot=True,slur_start=True)}{n('D',5,120,'16th',1)}{n('F',5,480,'quarter',1)}
{n('A',5,720,'quarter',1,dot=True,slur_stop=True)}{n('G',5,240,'eighth',1)}
{n('B',2,960,'half',2,-1)}{n('F',3,240,'eighth',2)}{n('A',3,240,'eighth',2)}{n('D',4,240,'eighth',2)}{n('E',4,240,'eighth',2)}
</measure>
<measure number="26">
{chord('E','major-ninth',-1,'maj9(#11)')}
{n('C',6,720,'quarter',1,dot=True,slur_start=True)}{n('B',5,240,'eighth',1,-1)}{n('A',5,480,'quarter',1)}
{n('G',5,480,'quarter',1,slur_stop=True)}
{n('E',3,960,'half',2,-1)}{n('B',3,240,'eighth',2,-1)}{n('D',4,240,'eighth',2)}{n('G',4,240,'eighth',2,-1)}{n('A',4,240,'eighth',2)}
</measure>
<measure number="27">
{chord('A','major-seventh',-1,'maj7(#11)')}
{n('F',5,720,'quarter',1,dot=True,slur_start=True)}{n('E',5,240,'eighth',1,-1)}{n('D',5,480,'quarter',1)}
{n('C',5,480,'quarter',1,slur_stop=True)}
{n('A',2,960,'half',2,-1)}{n('E',3,240,'eighth',2,-1)}{n('G',3,240,'eighth',2)}{n('C',4,240,'eighth',2)}{n('D',4,240,'eighth',2)}
</measure>
<measure number="28">
{chord('B','major-seventh',-1,'maj7')}
{n('B',5,1920,'whole',1,-1,fermata=True)}
{n('B',2,960,'half',2,-1)}{n('F',3,240,'eighth',2)}{n('A',3,240,'eighth',2)}{n('D',4,480,'quarter',2,fermata=True)}
{bar()}
</measure>'''
mvmt2 += footer()

with open('scores/MastersPalette-Mvmt2-Excellent.musicxml', 'w', encoding='utf-8') as f:
    f.write(mvmt2)
print("Created: MastersPalette-Mvmt2-Excellent.musicxml (28 bars)")
print("  Motif: Bb-D-F-A Lydian | Form: A-A2-B-Coda | Internal Revisions: V10")

