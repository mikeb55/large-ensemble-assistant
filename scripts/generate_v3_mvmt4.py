#!/usr/bin/env python3
"""Generate Movement IV - German Development / Fortspinnung"""

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

def r(dur, typ, staff, dot=False):
    return n('',0,dur,typ,staff,rest=True,dot=dot)

def attrs(div=480, fifths=-3, beats=4, bt=4, mode='minor'):
    return f'''<attributes><divisions>{div}</divisions><key><fifths>{fifths}</fifths><mode>{mode}</mode></key>
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

# Movement IV: German Development - C-Eb-F cell, Fortspinnung
mvmt4 = header("The Master's Palette - IV. German Development (Fortspinnung)")
mvmt4 += f'''
<measure number="1">
{attrs(480, -3, 4, 4, 'minor')}
{direction(rehearsal='A', tempo=80)}
{direction(text='Motivic argument - Fortspinnung', dyn='mf')}
{n('C',5,120,'16th',1,slur_start=True)}{n('E',5,120,'16th',1,-1)}{n('F',5,360,'eighth',1,dot=True)}
{n('G',5,120,'16th',1)}{n('A',5,480,'quarter',1,-1)}{n('G',5,480,'quarter',1,slur_stop=True)}
{n('C',3,240,'eighth',2)}{n('G',3,120,'16th',2)}{n('E',4,120,'16th',2,-1)}{n('F',3,240,'eighth',2)}
{n('A',3,240,'eighth',2,-1)}{n('E',4,240,'eighth',2,-1)}{n('C',4,240,'eighth',2)}{n('G',3,240,'eighth',2)}
</measure>
<measure number="2">
{n('F',5,360,'eighth',1,dot=True,slur_start=True)}{n('E',5,120,'16th',1,-1)}{n('C',5,240,'eighth',1)}{n('B',4,240,'eighth',1,-1)}
{n('A',4,960,'half',1,-1,slur_stop=True)}
{n('A',2,240,'eighth',2,-1)}{n('E',3,240,'eighth',2,-1)}{n('G',3,120,'16th',2)}{n('B',3,120,'16th',2,-1)}
{n('C',4,240,'eighth',2)}{n('E',4,240,'eighth',2,-1)}{n('G',3,240,'eighth',2)}{n('A',3,240,'eighth',2,-1)}
</measure>
<measure number="3">
{direction(text='Sequence up M2')}
{n('D',5,120,'16th',1,slur_start=True)}{n('F',5,120,'16th',1)}{n('G',5,360,'eighth',1,dot=True)}
{n('A',5,120,'16th',1)}{n('B',5,480,'quarter',1,-1)}{n('A',5,480,'quarter',1,slur_stop=True)}
{n('D',3,240,'eighth',2)}{n('A',3,120,'16th',2)}{n('F',4,120,'16th',2)}{n('G',3,240,'eighth',2)}
{n('B',3,240,'eighth',2,-1)}{n('F',4,240,'eighth',2)}{n('D',4,240,'eighth',2)}{n('A',3,240,'eighth',2)}
</measure>
<measure number="4">
{n('G',5,360,'eighth',1,dot=True,slur_start=True)}{n('F',5,120,'16th',1)}{n('D',5,240,'eighth',1)}{n('C',5,240,'eighth',1)}
{n('B',4,960,'half',1,-1,slur_stop=True)}
{n('B',2,240,'eighth',2,-1)}{n('F',3,240,'eighth',2)}{n('A',3,120,'16th',2)}{n('D',4,120,'16th',2)}
{n('C',4,240,'eighth',2)}{n('F',4,240,'eighth',2)}{n('A',3,240,'eighth',2)}{n('B',3,240,'eighth',2,-1)}
</measure>
<measure number="5">
{direction(text='Fragmentation')}
{n('C',5,120,'16th',1,slur_start=True)}{n('E',5,120,'16th',1,-1)}{r(120,'16th',1)}{n('F',5,120,'16th',1)}
{n('G',5,120,'16th',1,slur_stop=True)}{r(120,'16th',1)}{n('E',5,480,'quarter',1,-1)}
{n('D',5,120,'16th',1,slur_start=True)}{n('F',5,120,'16th',1)}{r(240,'eighth',1)}{n('G',5,480,'quarter',1,slur_stop=True)}
{n('E',3,120,'16th',2,-1)}{n('B',3,120,'16th',2,-1)}{r(120,'16th',2)}{n('G',3,120,'16th',2)}
{n('C',4,120,'16th',2)}{r(120,'16th',2)}{n('F',3,480,'quarter',2)}{n('A',3,120,'16th',2,-1)}{n('C',4,120,'16th',2)}{r(240,'eighth',2)}
</measure>
<measure number="6">
{n('D',5,480,'quarter',1,slur_start=True)}{n('C',5,240,'eighth',1)}{n('B',4,240,'eighth',1,-1)}
{n('A',4,960,'half',1,-1,slur_stop=True)}
{n('G',2,240,'eighth',2)}{n('D',3,240,'eighth',2)}{n('F',3,120,'16th',2)}{n('B',3,120,'16th',2,-1)}
{n('A',3,240,'eighth',2,-1)}{n('D',4,240,'eighth',2)}{n('F',3,240,'eighth',2)}{n('G',3,240,'eighth',2)}
</measure>
<measure number="7">
{n('C',5,120,'16th',1,slur_start=True)}{n('E',5,120,'16th',1,-1)}{n('F',5,240,'eighth',1)}{n('G',5,360,'eighth',1,dot=True)}
{n('A',5,120,'16th',1,-1)}{n('B',5,480,'quarter',1,-1)}{n('A',5,480,'quarter',1,-1,slur_stop=True)}
{n('C',3,240,'eighth',2)}{n('G',3,120,'16th',2)}{n('B',3,120,'16th',2,-1)}{n('E',4,240,'eighth',2,-1)}
{n('F',4,240,'eighth',2)}{n('A',3,240,'eighth',2,-1)}{n('C',4,240,'eighth',2)}{n('E',4,240,'eighth',2,-1)}
</measure>
<measure number="8">
{n('F',5,1440,'half',1,dot=True)}{r(240,'eighth',1)}{n('G',5,240,'eighth',1)}
{n('F',2,240,'eighth',2)}{n('C',3,240,'eighth',2)}{n('E',3,120,'16th',2,-1)}{n('A',3,120,'16th',2,-1)}
{n('C',4,240,'eighth',2)}{n('E',4,240,'eighth',2,-1)}{n('A',3,240,'eighth',2,-1)}{n('C',3,240,'eighth',2)}
</measure>
<measure number="9">
{direction(rehearsal='A2')}
{direction(text='Inversion - register shifts')}
{n('C',5,120,'16th',1,slur_start=True)}{n('A',4,120,'16th',1)}{n('G',4,360,'eighth',1,dot=True)}
{n('F',4,120,'16th',1)}{n('E',4,480,'quarter',1,-1)}{n('F',4,480,'quarter',1,slur_stop=True)}
{n('A',2,240,'eighth',2)}{n('E',3,240,'eighth',2)}{n('C',4,120,'16th',2)}{n('G',3,120,'16th',2)}
{n('F',3,240,'eighth',2)}{n('A',3,240,'eighth',2)}{n('E',3,240,'eighth',2)}{n('C',3,240,'eighth',2)}
</measure>
<measure number="10">
{n('G',4,360,'eighth',1,dot=True,slur_start=True)}{n('A',4,120,'16th',1)}{n('C',5,240,'eighth',1)}{n('D',5,240,'eighth',1)}
{n('E',5,960,'half',1,-1,slur_stop=True)}
{n('E',3,240,'eighth',2,-1)}{n('B',3,240,'eighth',2,-1)}{n('D',4,120,'16th',2)}{n('G',3,120,'16th',2)}
{n('A',3,240,'eighth',2,-1)}{n('C',4,240,'eighth',2)}{n('E',3,240,'eighth',2,-1)}{n('G',3,240,'eighth',2)}
</measure>
<measure number="11">
{direction(text='Klangfarben - passing')}
{n('C',4,120,'16th',1)}{n('E',5,120,'16th',1,-1)}{n('F',4,120,'16th',1)}{n('G',5,120,'16th',1)}
{n('E',4,480,'quarter',1,-1)}{n('C',5,480,'quarter',1)}{n('A',4,480,'quarter',1,-1)}
{n('C',3,120,'16th',2)}{n('G',3,120,'16th',2)}{n('E',4,120,'16th',2,-1)}{n('B',3,120,'16th',2,-1)}
{n('F',3,480,'quarter',2)}{n('A',3,480,'quarter',2,-1)}{n('C',4,480,'quarter',2)}
</measure>
<measure number="12">
{n('F',5,480,'quarter',1,slur_start=True)}{n('E',5,240,'eighth',1,-1)}{n('D',5,240,'eighth',1)}
{n('C',5,960,'half',1,slur_stop=True)}
{n('D',3,240,'eighth',2)}{n('A',3,240,'eighth',2)}{n('F',4,120,'16th',2)}{n('C',4,120,'16th',2)}
{n('G',3,240,'eighth',2)}{n('B',3,240,'eighth',2,-1)}{n('D',4,240,'eighth',2)}{n('A',3,240,'eighth',2)}
</measure>
<measure number="13">
{direction(text='Augmentation')}
{n('C',5,960,'half',1,slur_start=True)}{n('E',5,960,'half',1,-1)}
{n('G',2,240,'eighth',2)}{n('D',3,240,'eighth',2)}{n('F',3,120,'16th',2)}{n('B',3,120,'16th',2,-1)}
{n('E',4,240,'eighth',2,-1)}{n('G',3,240,'eighth',2)}{n('C',4,240,'eighth',2)}{n('E',4,240,'eighth',2,-1)}
</measure>
<measure number="14">
{n('F',5,1920,'whole',1,slur_stop=True)}
{n('F',2,240,'eighth',2)}{n('C',3,240,'eighth',2)}{n('E',3,120,'16th',2,-1)}{n('A',3,120,'16th',2,-1)}
{n('C',4,240,'eighth',2)}{n('E',4,240,'eighth',2,-1)}{n('A',3,240,'eighth',2,-1)}{n('C',3,240,'eighth',2)}
</measure>
<measure number="15">
{n('G',5,960,'half',1,slur_start=True)}{n('F',5,960,'half',1)}
{n('C',3,240,'eighth',2)}{n('G',3,240,'eighth',2)}{n('B',3,120,'16th',2,-1)}{n('E',4,120,'16th',2,-1)}
{n('F',4,240,'eighth',2)}{n('A',3,240,'eighth',2,-1)}{n('C',4,240,'eighth',2)}{n('E',4,240,'eighth',2,-1)}
</measure>
<measure number="16">
{n('E',5,960,'half',1,-1)}{n('C',5,960,'half',1,slur_stop=True)}
{n('A',2,240,'eighth',2,-1)}{n('E',3,240,'eighth',2,-1)}{n('G',3,120,'16th',2)}{n('C',4,120,'16th',2)}
{n('E',4,240,'eighth',2,-1)}{n('G',3,240,'eighth',2)}{n('A',3,240,'eighth',2,-1)}{n('C',3,240,'eighth',2)}
</measure>
<measure number="17">
{direction(rehearsal='B')}
{direction(text='Diminution - stretto', dyn='f')}
{n('C',5,60,'32nd',1,slur_start=True)}{n('E',5,60,'32nd',1,-1)}{n('F',5,120,'16th',1)}
{n('D',5,60,'32nd',1)}{n('F',5,60,'32nd',1)}{n('G',5,120,'16th',1)}
{n('E',5,60,'32nd',1)}{n('G',5,60,'32nd',1)}{n('A',5,120,'16th',1)}
{n('F',5,480,'quarter',1,slur_stop=True)}
{n('G',5,120,'16th',1,slur_start=True)}{n('A',5,120,'16th',1)}{n('B',5,240,'eighth',1,-1)}{n('A',5,480,'quarter',1,slur_stop=True)}
{n('D',3,120,'16th',2)}{n('A',3,120,'16th',2)}{n('F',4,120,'16th',2)}{n('G',3,120,'16th',2)}
{n('B',3,240,'eighth',2,-1)}{n('E',4,240,'eighth',2,-1)}{n('G',3,480,'quarter',2)}{n('A',3,480,'quarter',2,-1)}
</measure>
<measure number="18">
{n('G',5,60,'32nd',1,slur_start=True)}{n('F',5,60,'32nd',1)}{n('E',5,120,'16th',1,-1)}{n('C',5,240,'eighth',1)}
{n('B',4,960,'half',1,-1)}{n('A',4,480,'quarter',1,-1,slur_stop=True)}
{n('A',2,240,'eighth',2,-1)}{n('E',3,240,'eighth',2)}{n('C',4,120,'16th',2)}{n('G',3,120,'16th',2)}
{n('F',3,240,'eighth',2)}{n('A',3,240,'eighth',2,-1)}{n('C',3,480,'quarter',2)}{n('G',3,480,'quarter',2)}
</measure>
<measure number="19">
{direction(text='Stretto')}
{n('C',5,120,'16th',1,slur_start=True)}{n('E',5,120,'16th',1,-1)}{n('F',5,120,'16th',1)}{n('C',5,120,'16th',1)}
{n('A',4,120,'16th',1)}{n('G',4,120,'16th',1)}{n('F',4,240,'eighth',1)}
{n('E',5,120,'16th',1,-1)}{n('C',5,120,'16th',1)}{n('B',4,240,'eighth',1,-1)}{n('A',4,480,'quarter',1,-1,slur_stop=True)}
{n('F',2,240,'eighth',2)}{n('C',3,240,'eighth',2)}{n('E',3,120,'16th',2,-1)}{n('A',3,120,'16th',2,-1)}
{n('B',3,240,'eighth',2,-1)}{n('C',4,240,'eighth',2)}{n('F',3,480,'quarter',2)}{n('A',3,480,'quarter',2,-1)}
</measure>
<measure number="20">
{n('E',5,360,'eighth',1,-1,dot=True,slur_start=True)}{n('F',5,120,'16th',1)}{n('G',5,240,'eighth',1)}{n('A',5,240,'eighth',1)}
{n('B',5,960,'half',1,-1,slur_stop=True)}
{n('E',3,240,'eighth',2,-1)}{n('B',3,240,'eighth',2,-1)}{n('D',4,120,'16th',2)}{n('G',3,120,'16th',2)}
{n('A',3,240,'eighth',2,-1)}{n('C',4,240,'eighth',2)}{n('E',3,240,'eighth',2,-1)}{n('G',3,240,'eighth',2)}
</measure>
<measure number="21">
{direction(dyn='ff')}
{n('C',6,360,'eighth',1,dot=True,slur_start=True)}{n('B',5,120,'16th',1,-1)}{n('A',5,240,'eighth',1)}{n('G',5,240,'eighth',1)}
{n('F',5,480,'quarter',1)}{n('E',5,480,'quarter',1,-1,slur_stop=True)}
{n('B',2,240,'eighth',2,-1)}{n('F',3,240,'eighth',2)}{n('A',3,120,'16th',2)}{n('D',4,120,'16th',2)}
{n('E',4,240,'eighth',2,-1)}{n('F',4,240,'eighth',2)}{n('A',3,240,'eighth',2,-1)}{n('B',3,240,'eighth',2,-1)}
</measure>
<measure number="22">
{n('C',5,120,'16th',1,slur_start=True)}{n('E',5,120,'16th',1,-1)}{n('F',5,240,'eighth',1)}{n('G',5,360,'eighth',1,dot=True)}
{n('A',5,120,'16th',1,-1)}{n('G',5,960,'half',1,slur_stop=True)}
{n('C',3,240,'eighth',2)}{n('G',3,120,'16th',2)}{n('B',3,120,'16th',2,-1)}{n('E',4,240,'eighth',2,-1)}
{n('F',4,240,'eighth',2)}{n('A',3,240,'eighth',2,-1)}{n('C',4,240,'eighth',2)}{n('E',4,240,'eighth',2,-1)}
</measure>
<measure number="23">
{n('A',5,480,'quarter',1,slur_start=True)}{n('G',5,240,'eighth',1)}{n('F',5,240,'eighth',1)}
{n('E',5,480,'quarter',1,-1)}{n('C',5,480,'quarter',1,slur_stop=True)}
{n('F',2,240,'eighth',2)}{n('C',3,240,'eighth',2)}{n('E',3,120,'16th',2,-1)}{n('A',3,120,'16th',2,-1)}
{n('C',4,240,'eighth',2)}{n('E',4,240,'eighth',2,-1)}{n('A',3,240,'eighth',2,-1)}{n('C',3,240,'eighth',2)}
</measure>
<measure number="24">
{n('C',5,1440,'half',1,dot=True)}{r(240,'eighth',1)}{n('G',5,240,'eighth',1)}
{n('C',3,240,'eighth',2)}{n('G',3,240,'eighth',2)}{n('E',4,120,'16th',2,-1)}{n('B',3,120,'16th',2,-1)}
{n('C',4,240,'eighth',2)}{n('G',3,240,'eighth',2)}{n('E',3,240,'eighth',2,-1)}{n('C',3,240,'eighth',2)}
</measure>
<measure number="25">
{direction(rehearsal='Coda')}
{direction(text='Triumphant return', dyn='f')}
{n('C',5,120,'16th',1,slur_start=True)}{n('E',5,120,'16th',1,-1)}{n('F',5,360,'eighth',1,dot=True)}
{n('G',5,120,'16th',1)}{n('A',5,480,'quarter',1,-1)}{n('B',5,480,'quarter',1,-1,slur_stop=True)}
{n('C',3,240,'eighth',2)}{n('G',3,120,'16th',2)}{n('B',3,120,'16th',2,-1)}{n('E',4,240,'eighth',2,-1)}
{n('F',4,240,'eighth',2)}{n('A',3,240,'eighth',2,-1)}{n('C',4,240,'eighth',2)}{n('E',4,240,'eighth',2,-1)}
</measure>
<measure number="26">
{n('C',6,360,'eighth',1,dot=True,slur_start=True)}{n('B',5,120,'16th',1,-1)}{n('A',5,240,'eighth',1)}{n('G',5,240,'eighth',1)}
{n('F',5,480,'quarter',1)}{n('E',5,480,'quarter',1,-1,slur_stop=True)}
{n('F',2,240,'eighth',2)}{n('C',3,240,'eighth',2)}{n('E',3,120,'16th',2,-1)}{n('A',3,120,'16th',2)}
{n('G',3,240,'eighth',2)}{n('C',4,240,'eighth',2)}{n('E',4,240,'eighth',2,-1)}{n('A',3,240,'eighth',2,-1)}
</measure>
<measure number="27">
{n('E',5,240,'eighth',1,-1,slur_start=True)}{n('C',5,120,'16th',1)}{n('E',5,120,'16th',1,-1)}{n('F',5,360,'eighth',1,dot=True)}
{n('G',5,120,'16th',1)}{n('A',5,480,'quarter',1,-1)}{n('G',5,480,'quarter',1,slur_stop=True)}
{n('C',3,240,'eighth',2)}{n('G',3,120,'16th',2)}{n('B',3,120,'16th',2,-1)}{n('E',4,240,'eighth',2,-1)}
{n('D',4,240,'eighth',2)}{n('B',3,240,'eighth',2,-1)}{n('G',3,240,'eighth',2)}{n('E',4,240,'eighth',2,-1)}
</measure>
<measure number="28">
{n('F',5,360,'eighth',1,dot=True,slur_start=True)}{n('E',5,120,'16th',1,-1)}{n('D',5,240,'eighth',1)}{n('C',5,240,'eighth',1)}
{n('B',4,960,'half',1,-1,slur_stop=True)}
{n('F',2,240,'eighth',2)}{n('C',3,240,'eighth',2)}{n('E',3,120,'16th',2,-1)}{n('A',3,120,'16th',2,-1)}
{n('B',3,240,'eighth',2,-1)}{n('C',4,240,'eighth',2)}{n('F',3,240,'eighth',2)}{n('A',3,240,'eighth',2,-1)}
</measure>
<measure number="29">
{direction(text='Broadening')}
{n('E',5,960,'half',1,-1,slur_start=True)}{n('F',5,960,'half',1)}
{n('A',2,240,'eighth',2,-1)}{n('E',3,240,'eighth',2,-1)}{n('G',3,120,'16th',2)}{n('C',4,120,'16th',2)}
{n('E',4,240,'eighth',2,-1)}{n('G',3,240,'eighth',2)}{n('A',3,240,'eighth',2,-1)}{n('C',3,240,'eighth',2)}
</measure>
<measure number="30">
{n('G',5,960,'half',1)}{n('A',5,960,'half',1,slur_stop=True)}
{n('G',2,240,'eighth',2)}{n('D',3,240,'eighth',2)}{n('F',3,120,'16th',2)}{n('B',3,120,'16th',2,-1)}
{n('D',4,240,'eighth',2)}{n('F',3,240,'eighth',2)}{n('G',3,240,'eighth',2)}{n('B',3,240,'eighth',2,-1)}
</measure>
<measure number="31">
{direction(text='Final statement')}
{n('G',5,1440,'half',1,dot=True,slur_start=True)}{n('F',5,480,'quarter',1,slur_stop=True)}
{n('F',2,240,'eighth',2)}{n('C',3,240,'eighth',2)}{n('E',3,120,'16th',2,-1)}{n('A',3,120,'16th',2,-1)}
{n('C',4,240,'eighth',2)}{n('E',4,240,'eighth',2,-1)}{n('A',3,240,'eighth',2,-1)}{n('C',3,240,'eighth',2)}
</measure>
<measure number="32">
{n('C',5,1920,'whole',1,fermata=True)}
{n('C',3,240,'eighth',2)}{n('G',3,240,'eighth',2)}{n('E',4,120,'16th',2,-1)}{n('C',4,120,'16th',2)}
{n('E',4,240,'eighth',2,-1)}{n('G',3,240,'eighth',2)}{n('C',4,480,'quarter',2,fermata=True)}
{bar()}
</measure>'''
mvmt4 += footer()

with open('scores/MastersPalette-Mvmt4-Excellent.musicxml', 'w', encoding='utf-8') as f:
    f.write(mvmt4)
print("Created: MastersPalette-Mvmt4-Excellent.musicxml (32 bars)")
print("  Motif: C-Eb-F Fortspinnung | Form: A-A2-B-Coda | Internal Revisions: V10")

