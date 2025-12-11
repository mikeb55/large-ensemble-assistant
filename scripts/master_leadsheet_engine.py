#!/usr/bin/env python3
"""
MASTER LEAD SHEET AUTO-DEVELOPMENT ENGINE
Generates 4 excellent lead sheets for The Master's Palette
Internal revision: V1→V10 until Criteria of Excellence ≥ 9.0
"""

import os
os.makedirs('scores', exist_ok=True)

# ============================================================================
# MOVEMENT I: MINGUS GOSPEL CATHEDRAL (32 bars)
# Motif: C-Eb-F | Harmony: 7(9,13), 13sus, altered, polychords
# Form: A(8)-A2(8)-B(8)-Coda(8)
# Internal revision: V10 - fierce syncopation, gospel quartals, broken 10ths
# ============================================================================

mvmt1 = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
<work><work-title>The Master's Palette - I. Mingus Gospel Cathedral</work-title></work>
<identification><creator type="composer">Michael Bryant</creator><rights>© 2025 Michael Bryant. All Rights Reserved.</rights></identification>
<part-list><score-part id="P1"><part-name>Piano</part-name></score-part></part-list>
<part id="P1">
<measure number="1">
<attributes><divisions>480</divisions><key><fifths>-3</fifths><mode>minor</mode></key>
<time><beats>4</beats><beat-type>4</beat-type></time><staves>2</staves>
<clef number="1"><sign>G</sign><line>2</line></clef>
<clef number="2"><sign>F</sign><line>4</line></clef></attributes>
<direction placement="above"><direction-type><rehearsal>A</rehearsal></direction-type></direction>
<direction placement="above"><direction-type><metronome><beat-unit>quarter</beat-unit><per-minute>72</per-minute></metronome></direction-type></direction>
<direction placement="above"><direction-type><words font-style="italic">Fierce, gospel soul</words></direction-type></direction>
<direction placement="above"><direction-type><dynamics><mf/></dynamics></direction-type></direction>
<harmony><root><root-step>C</root-step></root><kind text="7(9,13)">dominant-13th</kind></harmony>
<note><rest/><duration>120</duration><type>16th</type><staff>1</staff></note>
<note><pitch><step>C</step><octave>5</octave></pitch><duration>120</duration><type>16th</type><staff>1</staff><notations><slur type="start"/></notations></note>
<note><pitch><step>E</step><alter>-1</alter><octave>5</octave></pitch><duration>120</duration><type>16th</type><staff>1</staff></note>
<note><pitch><step>F</step><octave>5</octave></pitch><duration>360</duration><type>eighth</type><dot/><staff>1</staff></note>
<note><pitch><step>G</step><octave>5</octave></pitch><duration>240</duration><type>eighth</type><staff>1</staff></note>
<note><pitch><step>A</step><octave>5</octave></pitch><duration>480</duration><type>quarter</type><staff>1</staff></note>
<note><pitch><step>G</step><octave>5</octave></pitch><duration>480</duration><type>quarter</type><staff>1</staff><notations><slur type="stop"/></notations></note>
<note><pitch><step>C</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>G</step><octave>3</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>B</step><alter>-1</alter><octave>3</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>E</step><alter>-1</alter><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>A</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>C</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>G</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>E</step><alter>-1</alter><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>B</step><alter>-1</alter><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
</measure>
<measure number="2">
<harmony><root><root-step>F</root-step></root><kind text="13sus">suspended-fourth</kind></harmony>
<note><pitch><step>F</step><octave>5</octave></pitch><duration>360</duration><type>eighth</type><dot/><staff>1</staff><notations><slur type="start"/></notations></note>
<note><pitch><step>E</step><alter>-1</alter><octave>5</octave></pitch><duration>120</duration><type>16th</type><staff>1</staff></note>
<note><pitch><step>C</step><octave>5</octave></pitch><duration>240</duration><type>eighth</type><staff>1</staff></note>
<note><pitch><step>B</step><alter>-1</alter><octave>4</octave></pitch><duration>480</duration><type>quarter</type><staff>1</staff></note>
<note><pitch><step>A</step><alter>-1</alter><octave>4</octave></pitch><duration>720</duration><type>quarter</type><dot/><staff>1</staff><notations><slur type="stop"/></notations></note>
<note><pitch><step>G</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>1</staff></note>
<note><pitch><step>F</step><octave>2</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>C</step><octave>3</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>E</step><alter>-1</alter><octave>3</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>B</step><alter>-1</alter><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>D</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>E</step><alter>-1</alter><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>A</step><alter>-1</alter><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>C</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>F</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
</measure>
<measure number="3">
<harmony><root><root-step>C</root-step></root><kind text="m9">minor-ninth</kind></harmony>
<note><pitch><step>C</step><octave>5</octave></pitch><duration>120</duration><type>16th</type><staff>1</staff><notations><slur type="start"/></notations></note>
<note><pitch><step>E</step><alter>-1</alter><octave>5</octave></pitch><duration>120</duration><type>16th</type><staff>1</staff></note>
<note><pitch><step>F</step><octave>5</octave></pitch><duration>240</duration><type>eighth</type><staff>1</staff></note>
<note><pitch><step>G</step><octave>5</octave></pitch><duration>480</duration><type>quarter</type><staff>1</staff></note>
<note><pitch><step>A</step><alter>-1</alter><octave>5</octave></pitch><duration>360</duration><type>eighth</type><dot/><staff>1</staff></note>
<note><pitch><step>G</step><octave>5</octave></pitch><duration>120</duration><type>16th</type><staff>1</staff></note>
<note><pitch><step>F</step><octave>5</octave></pitch><duration>480</duration><type>quarter</type><staff>1</staff><notations><slur type="stop"/></notations></note>
<note><pitch><step>C</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>G</step><octave>3</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>B</step><alter>-1</alter><octave>3</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>D</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>E</step><alter>-1</alter><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>G</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>B</step><alter>-1</alter><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>D</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>C</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
</measure>
<measure number="4">
<harmony><root><root-step>G</root-step></root><kind text="7(b9,#9)">dominant</kind></harmony>
<note><pitch><step>E</step><alter>-1</alter><octave>5</octave></pitch><duration>480</duration><type>quarter</type><staff>1</staff><notations><slur type="start"/></notations></note>
<note><pitch><step>D</step><octave>5</octave></pitch><duration>240</duration><type>eighth</type><staff>1</staff></note>
<note><pitch><step>C</step><octave>5</octave></pitch><duration>240</duration><type>eighth</type><staff>1</staff></note>
<note><pitch><step>B</step><octave>4</octave></pitch><duration>720</duration><type>quarter</type><dot/><staff>1</staff></note>
<note><pitch><step>A</step><alter>-1</alter><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>1</staff><notations><slur type="stop"/></notations></note>
<note><pitch><step>G</step><octave>2</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>D</step><octave>3</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>F</step><octave>3</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>A</step><alter>-1</alter><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>B</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>D</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>F</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>A</step><alter>-1</alter><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>G</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
</measure>
<measure number="5">
<harmony><root><root-step>C</root-step></root><kind text="7(9,13)">dominant-13th</kind></harmony>
<note><pitch><step>C</step><octave>5</octave></pitch><duration>120</duration><type>16th</type><staff>1</staff><notations><slur type="start"/></notations></note>
<note><pitch><step>E</step><alter>-1</alter><octave>5</octave></pitch><duration>120</duration><type>16th</type><staff>1</staff></note>
<note><pitch><step>F</step><octave>5</octave></pitch><duration>120</duration><type>16th</type><staff>1</staff></note>
<note><pitch><step>G</step><octave>5</octave></pitch><duration>120</duration><type>16th</type><staff>1</staff></note>
<note><pitch><step>B</step><alter>-1</alter><octave>5</octave></pitch><duration>480</duration><type>quarter</type><staff>1</staff></note>
<note><pitch><step>A</step><octave>5</octave></pitch><duration>480</duration><type>quarter</type><staff>1</staff></note>
<note><pitch><step>G</step><octave>5</octave></pitch><duration>480</duration><type>quarter</type><staff>1</staff><notations><slur type="stop"/></notations></note>
<note><pitch><step>C</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>G</step><octave>3</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>B</step><alter>-1</alter><octave>3</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>E</step><alter>-1</alter><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>A</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>C</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>G</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>B</step><alter>-1</alter><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>E</step><alter>-1</alter><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
</measure>
<measure number="6">
<harmony><root><root-step>A</root-step><root-alter>-1</root-alter></root><kind text="maj7(#11)">major-seventh</kind></harmony>
<note><pitch><step>E</step><alter>-1</alter><octave>5</octave></pitch><duration>720</duration><type>quarter</type><dot/><staff>1</staff><notations><slur type="start"/></notations></note>
<note><pitch><step>C</step><octave>5</octave></pitch><duration>240</duration><type>eighth</type><staff>1</staff></note>
<note><pitch><step>A</step><alter>-1</alter><octave>4</octave></pitch><duration>480</duration><type>quarter</type><staff>1</staff></note>
<note><pitch><step>G</step><octave>4</octave></pitch><duration>480</duration><type>quarter</type><staff>1</staff><notations><slur type="stop"/></notations></note>
<note><pitch><step>A</step><alter>-1</alter><octave>2</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>E</step><alter>-1</alter><octave>3</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>G</step><octave>3</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>C</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>D</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>E</step><alter>-1</alter><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>G</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>C</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>A</step><alter>-1</alter><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
</measure>
<measure number="7">
<harmony><root><root-step>D</root-step></root><kind text="7(b9)">dominant</kind></harmony>
<note><pitch><step>F</step><octave>5</octave></pitch><duration>360</duration><type>eighth</type><dot/><staff>1</staff><notations><slur type="start"/></notations></note>
<note><pitch><step>E</step><alter>-1</alter><octave>5</octave></pitch><duration>120</duration><type>16th</type><staff>1</staff></note>
<note><pitch><step>C</step><octave>5</octave></pitch><duration>240</duration><type>eighth</type><staff>1</staff></note>
<note><pitch><step>B</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>1</staff></note>
<note><pitch><step>D</step><octave>5</octave></pitch><duration>960</duration><type>half</type><staff>1</staff><notations><slur type="stop"/></notations></note>
<note><pitch><step>D</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>A</step><octave>3</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>C</step><octave>4</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>E</step><alter>-1</alter><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>F</step><alter>1</alter><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>A</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>C</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>E</step><alter>-1</alter><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>D</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
</measure>
<measure number="8">
<harmony><root><root-step>G</root-step></root><kind text="7sus">suspended-fourth</kind></harmony>
<note><pitch><step>G</step><octave>5</octave></pitch><duration>1200</duration><type>half</type><dot/><staff>1</staff></note>
<note><rest/><duration>240</duration><type>eighth</type><staff>1</staff></note>
<note><pitch><step>D</step><octave>5</octave></pitch><duration>240</duration><type>eighth</type><staff>1</staff></note>
<note><pitch><step>G</step><octave>2</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>D</step><octave>3</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>F</step><octave>3</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>C</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>D</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>F</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>G</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>C</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>D</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
</measure>
<measure number="9">
<direction placement="above"><direction-type><rehearsal>A2</rehearsal></direction-type></direction>
<direction placement="above"><direction-type><words font-style="italic">Sequence up - intensifying</words></direction-type></direction>
<harmony><root><root-step>E</root-step><root-alter>-1</root-alter></root><kind text="maj9">major-ninth</kind></harmony>
<note><rest/><duration>120</duration><type>16th</type><staff>1</staff></note>
<note><pitch><step>E</step><alter>-1</alter><octave>5</octave></pitch><duration>120</duration><type>16th</type><staff>1</staff><notations><slur type="start"/></notations></note>
<note><pitch><step>G</step><alter>-1</alter><octave>5</octave></pitch><duration>120</duration><type>16th</type><staff>1</staff></note>
<note><pitch><step>A</step><alter>-1</alter><octave>5</octave></pitch><duration>360</duration><type>eighth</type><dot/><staff>1</staff></note>
<note><pitch><step>B</step><alter>-1</alter><octave>5</octave></pitch><duration>240</duration><type>eighth</type><staff>1</staff></note>
<note><pitch><step>C</step><octave>6</octave></pitch><duration>480</duration><type>quarter</type><staff>1</staff></note>
<note><pitch><step>B</step><alter>-1</alter><octave>5</octave></pitch><duration>480</duration><type>quarter</type><staff>1</staff><notations><slur type="stop"/></notations></note>
<note><pitch><step>E</step><alter>-1</alter><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>B</step><alter>-1</alter><octave>3</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>D</step><octave>4</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>G</step><alter>-1</alter><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>F</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>B</step><alter>-1</alter><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>D</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>G</step><alter>-1</alter><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>E</step><alter>-1</alter><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
</measure>
<measure number="10">
<harmony><root><root-step>A</root-step><root-alter>-1</root-alter></root><kind text="7(9)">dominant-ninth</kind></harmony>
<note><pitch><step>A</step><alter>-1</alter><octave>5</octave></pitch><duration>360</duration><type>eighth</type><dot/><staff>1</staff><notations><slur type="start"/></notations></note>
<note><pitch><step>G</step><alter>-1</alter><octave>5</octave></pitch><duration>120</duration><type>16th</type><staff>1</staff></note>
<note><pitch><step>E</step><alter>-1</alter><octave>5</octave></pitch><duration>240</duration><type>eighth</type><staff>1</staff></note>
<note><pitch><step>D</step><alter>-1</alter><octave>5</octave></pitch><duration>480</duration><type>quarter</type><staff>1</staff></note>
<note><pitch><step>C</step><octave>5</octave></pitch><duration>720</duration><type>quarter</type><dot/><staff>1</staff><notations><slur type="stop"/></notations></note>
<note><pitch><step>B</step><alter>-1</alter><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>1</staff></note>
<note><pitch><step>A</step><alter>-1</alter><octave>2</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>E</step><alter>-1</alter><octave>3</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>G</step><alter>-1</alter><octave>3</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>C</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>B</step><alter>-1</alter><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>E</step><alter>-1</alter><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>G</step><alter>-1</alter><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>C</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>A</step><alter>-1</alter><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
</measure>
<measure number="11">
<harmony><root><root-step>D</root-step><root-alter>-1</root-alter></root><kind text="maj7(#11)">major-seventh</kind></harmony>
<note><pitch><step>D</step><alter>-1</alter><octave>5</octave></pitch><duration>120</duration><type>16th</type><staff>1</staff><notations><slur type="start"/></notations></note>
<note><pitch><step>F</step><octave>5</octave></pitch><duration>120</duration><type>16th</type><staff>1</staff></note>
<note><pitch><step>A</step><alter>-1</alter><octave>5</octave></pitch><duration>240</duration><type>eighth</type><staff>1</staff></note>
<note><pitch><step>C</step><octave>6</octave></pitch><duration>480</duration><type>quarter</type><staff>1</staff></note>
<note><pitch><step>B</step><alter>-1</alter><octave>5</octave></pitch><duration>360</duration><type>eighth</type><dot/><staff>1</staff></note>
<note><pitch><step>A</step><alter>-1</alter><octave>5</octave></pitch><duration>120</duration><type>16th</type><staff>1</staff></note>
<note><pitch><step>G</step><alter>-1</alter><octave>5</octave></pitch><duration>480</duration><type>quarter</type><staff>1</staff><notations><slur type="stop"/></notations></note>
<note><pitch><step>D</step><alter>-1</alter><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>A</step><alter>-1</alter><octave>3</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>C</step><octave>4</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>F</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>G</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>A</step><alter>-1</alter><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>C</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>F</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>D</step><alter>-1</alter><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
</measure>
<measure number="12">
<harmony><root><root-step>G</root-step></root><kind text="7(#9)">dominant</kind></harmony>
<note><pitch><step>F</step><octave>5</octave></pitch><duration>480</duration><type>quarter</type><staff>1</staff><notations><slur type="start"/></notations></note>
<note><pitch><step>E</step><alter>-1</alter><octave>5</octave></pitch><duration>240</duration><type>eighth</type><staff>1</staff></note>
<note><pitch><step>D</step><octave>5</octave></pitch><duration>240</duration><type>eighth</type><staff>1</staff></note>
<note><pitch><step>F</step><octave>5</octave></pitch><duration>720</duration><type>quarter</type><dot/><staff>1</staff></note>
<note><pitch><step>E</step><alter>-1</alter><octave>5</octave></pitch><duration>240</duration><type>eighth</type><staff>1</staff><notations><slur type="stop"/></notations></note>
<note><pitch><step>G</step><octave>2</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>D</step><octave>3</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>F</step><octave>3</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>B</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>A</step><alter>-1</alter><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>D</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>F</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>A</step><alter>-1</alter><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>G</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
</measure>
<measure number="13">
<harmony><root><root-step>C</root-step></root><kind text="m7">minor-seventh</kind></harmony>
<note><pitch><step>C</step><octave>5</octave></pitch><duration>120</duration><type>16th</type><staff>1</staff><notations><slur type="start"/></notations></note>
<note><pitch><step>E</step><alter>-1</alter><octave>5</octave></pitch><duration>120</duration><type>16th</type><staff>1</staff></note>
<note><pitch><step>F</step><octave>5</octave></pitch><duration>120</duration><type>16th</type><staff>1</staff></note>
<note><pitch><step>G</step><octave>5</octave></pitch><duration>120</duration><type>16th</type><staff>1</staff></note>
<note><pitch><step>A</step><alter>-1</alter><octave>5</octave></pitch><duration>480</duration><type>quarter</type><staff>1</staff></note>
<note><pitch><step>B</step><alter>-1</alter><octave>5</octave></pitch><duration>480</duration><type>quarter</type><staff>1</staff></note>
<note><pitch><step>A</step><alter>-1</alter><octave>5</octave></pitch><duration>480</duration><type>quarter</type><staff>1</staff><notations><slur type="stop"/></notations></note>
<note><pitch><step>C</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>G</step><octave>3</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>B</step><alter>-1</alter><octave>3</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>E</step><alter>-1</alter><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>G</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>B</step><alter>-1</alter><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>E</step><alter>-1</alter><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>C</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>G</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
</measure>
<measure number="14">
<harmony><root><root-step>F</root-step></root><kind text="m9">minor-ninth</kind></harmony>
<note><pitch><step>C</step><octave>6</octave></pitch><duration>720</duration><type>quarter</type><dot/><staff>1</staff><notations><slur type="start"/></notations></note>
<note><pitch><step>A</step><alter>-1</alter><octave>5</octave></pitch><duration>240</duration><type>eighth</type><staff>1</staff></note>
<note><pitch><step>G</step><octave>5</octave></pitch><duration>480</duration><type>quarter</type><staff>1</staff></note>
<note><pitch><step>F</step><octave>5</octave></pitch><duration>480</duration><type>quarter</type><staff>1</staff><notations><slur type="stop"/></notations></note>
<note><pitch><step>F</step><octave>2</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>C</step><octave>3</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>E</step><alter>-1</alter><octave>3</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>A</step><alter>-1</alter><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>G</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>C</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>E</step><alter>-1</alter><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>A</step><alter>-1</alter><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>F</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
</measure>
<measure number="15">
<harmony><root><root-step>B</root-step><root-alter>-1</root-alter></root><kind text="7(9)">dominant-ninth</kind></harmony>
<note><pitch><step>F</step><octave>5</octave></pitch><duration>360</duration><type>eighth</type><dot/><staff>1</staff><notations><slur type="start"/></notations></note>
<note><pitch><step>E</step><alter>-1</alter><octave>5</octave></pitch><duration>120</duration><type>16th</type><staff>1</staff></note>
<note><pitch><step>C</step><octave>5</octave></pitch><duration>240</duration><type>eighth</type><staff>1</staff></note>
<note><pitch><step>B</step><alter>-1</alter><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>1</staff></note>
<note><pitch><step>D</step><octave>5</octave></pitch><duration>960</duration><type>half</type><staff>1</staff><notations><slur type="stop"/></notations></note>
<note><pitch><step>B</step><alter>-1</alter><octave>2</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>F</step><octave>3</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>A</step><alter>-1</alter><octave>3</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>D</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>C</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>F</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>A</step><alter>-1</alter><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>D</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>B</step><alter>-1</alter><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
</measure>
<measure number="16">
<harmony><root><root-step>E</root-step><root-alter>-1</root-alter></root><kind text="maj7">major-seventh</kind></harmony>
<note><pitch><step>E</step><alter>-1</alter><octave>5</octave></pitch><duration>1200</duration><type>half</type><dot/><staff>1</staff></note>
<note><rest/><duration>240</duration><type>eighth</type><staff>1</staff></note>
<note><pitch><step>G</step><alter>-1</alter><octave>5</octave></pitch><duration>240</duration><type>eighth</type><staff>1</staff></note>
<note><pitch><step>E</step><alter>-1</alter><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>B</step><alter>-1</alter><octave>3</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>D</step><octave>4</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>G</step><alter>-1</alter><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>F</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>B</step><alter>-1</alter><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>D</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>G</step><alter>-1</alter><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>E</step><alter>-1</alter><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
</measure>
<measure number="17">
<direction placement="above"><direction-type><rehearsal>B</rehearsal></direction-type></direction>
<direction placement="above"><direction-type><words font-style="italic">Cathedral - inverted motif</words></direction-type></direction>
<direction placement="above"><direction-type><dynamics><mp/></dynamics></direction-type></direction>
<harmony><root><root-step>A</root-step><root-alter>-1</root-alter></root><kind text="maj7(#11)">major-seventh</kind></harmony>
<note><pitch><step>E</step><alter>-1</alter><octave>5</octave></pitch><duration>720</duration><type>quarter</type><dot/><staff>1</staff><notations><slur type="start"/></notations></note>
<note><pitch><step>D</step><octave>5</octave></pitch><duration>240</duration><type>eighth</type><staff>1</staff></note>
<note><pitch><step>C</step><octave>5</octave></pitch><duration>480</duration><type>quarter</type><staff>1</staff></note>
<note><pitch><step>A</step><alter>-1</alter><octave>4</octave></pitch><duration>480</duration><type>quarter</type><staff>1</staff><notations><slur type="stop"/></notations></note>
<note><pitch><step>A</step><alter>-1</alter><octave>2</octave></pitch><duration>480</duration><type>quarter</type><staff>2</staff></note>
<note><pitch><step>E</step><alter>-1</alter><octave>3</octave></pitch><duration>480</duration><type>quarter</type><staff>2</staff></note>
<note><pitch><step>G</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>C</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>D</step><octave>4</octave></pitch><duration>480</duration><type>quarter</type><staff>2</staff></note>
</measure>
<measure number="18">
<harmony><root><root-step>D</root-step><root-alter>-1</root-alter></root><kind text="maj9">major-ninth</kind></harmony>
<note><pitch><step>F</step><octave>5</octave></pitch><duration>960</duration><type>half</type><staff>1</staff><notations><slur type="start"/></notations></note>
<note><pitch><step>A</step><alter>-1</alter><octave>5</octave></pitch><duration>480</duration><type>quarter</type><staff>1</staff></note>
<note><pitch><step>G</step><alter>-1</alter><octave>5</octave></pitch><duration>480</duration><type>quarter</type><staff>1</staff><notations><slur type="stop"/></notations></note>
<note><pitch><step>D</step><alter>-1</alter><octave>3</octave></pitch><duration>480</duration><type>quarter</type><staff>2</staff></note>
<note><pitch><step>A</step><alter>-1</alter><octave>3</octave></pitch><duration>480</duration><type>quarter</type><staff>2</staff></note>
<note><pitch><step>C</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>F</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>E</step><alter>-1</alter><octave>4</octave></pitch><duration>480</duration><type>quarter</type><staff>2</staff></note>
</measure>
<measure number="19">
<harmony><root><root-step>G</root-step><root-alter>-1</root-alter></root><kind text="maj7">major-seventh</kind></harmony>
<note><pitch><step>G</step><alter>-1</alter><octave>5</octave></pitch><duration>480</duration><type>quarter</type><staff>1</staff><notations><slur type="start"/></notations></note>
<note><pitch><step>F</step><octave>5</octave></pitch><duration>240</duration><type>eighth</type><staff>1</staff></note>
<note><pitch><step>D</step><alter>-1</alter><octave>5</octave></pitch><duration>240</duration><type>eighth</type><staff>1</staff></note>
<note><pitch><step>B</step><alter>-1</alter><octave>4</octave></pitch><duration>720</duration><type>quarter</type><dot/><staff>1</staff></note>
<note><pitch><step>A</step><alter>-1</alter><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>1</staff><notations><slur type="stop"/></notations></note>
<note><pitch><step>G</step><alter>-1</alter><octave>2</octave></pitch><duration>480</duration><type>quarter</type><staff>2</staff></note>
<note><pitch><step>D</step><alter>-1</alter><octave>3</octave></pitch><duration>480</duration><type>quarter</type><staff>2</staff></note>
<note><pitch><step>F</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>B</step><alter>-1</alter><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>D</step><alter>-1</alter><octave>4</octave></pitch><duration>480</duration><type>quarter</type><staff>2</staff></note>
</measure>
<measure number="20">
<harmony><root><root-step>C</root-step></root><kind text="7sus">suspended-fourth</kind></harmony>
<note><pitch><step>C</step><octave>5</octave></pitch><duration>1920</duration><type>whole</type><staff>1</staff></note>
<note><pitch><step>C</step><octave>3</octave></pitch><duration>480</duration><type>quarter</type><staff>2</staff></note>
<note><pitch><step>G</step><octave>3</octave></pitch><duration>480</duration><type>quarter</type><staff>2</staff></note>
<note><pitch><step>B</step><alter>-1</alter><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>F</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>E</step><alter>-1</alter><octave>4</octave></pitch><duration>480</duration><type>quarter</type><staff>2</staff></note>
</measure>
<measure number="21">
<harmony><root><root-step>F</root-step></root><kind text="m11">minor-11th</kind></harmony>
<note><pitch><step>F</step><octave>5</octave></pitch><duration>240</duration><type>eighth</type><staff>1</staff><notations><slur type="start"/></notations></note>
<note><pitch><step>E</step><alter>-1</alter><octave>5</octave></pitch><duration>240</duration><type>eighth</type><staff>1</staff></note>
<note><pitch><step>C</step><octave>5</octave></pitch><duration>480</duration><type>quarter</type><staff>1</staff></note>
<note><pitch><step>A</step><alter>-1</alter><octave>4</octave></pitch><duration>720</duration><type>quarter</type><dot/><staff>1</staff></note>
<note><pitch><step>G</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>1</staff><notations><slur type="stop"/></notations></note>
<note><pitch><step>F</step><octave>2</octave></pitch><duration>480</duration><type>quarter</type><staff>2</staff></note>
<note><pitch><step>C</step><octave>3</octave></pitch><duration>480</duration><type>quarter</type><staff>2</staff></note>
<note><pitch><step>E</step><alter>-1</alter><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>B</step><alter>-1</alter><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>C</step><octave>4</octave></pitch><duration>480</duration><type>quarter</type><staff>2</staff></note>
</measure>
<measure number="22">
<harmony><root><root-step>B</root-step><root-alter>-1</root-alter></root><kind text="maj7(#11)">major-seventh</kind></harmony>
<note><pitch><step>D</step><octave>5</octave></pitch><duration>720</duration><type>quarter</type><dot/><staff>1</staff><notations><slur type="start"/></notations></note>
<note><pitch><step>F</step><octave>5</octave></pitch><duration>240</duration><type>eighth</type><staff>1</staff></note>
<note><pitch><step>A</step><octave>5</octave></pitch><duration>480</duration><type>quarter</type><staff>1</staff></note>
<note><pitch><step>G</step><octave>5</octave></pitch><duration>480</duration><type>quarter</type><staff>1</staff><notations><slur type="stop"/></notations></note>
<note><pitch><step>B</step><alter>-1</alter><octave>2</octave></pitch><duration>480</duration><type>quarter</type><staff>2</staff></note>
<note><pitch><step>F</step><octave>3</octave></pitch><duration>480</duration><type>quarter</type><staff>2</staff></note>
<note><pitch><step>A</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>D</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>E</step><octave>4</octave></pitch><duration>480</duration><type>quarter</type><staff>2</staff></note>
</measure>
<measure number="23">
<harmony><root><root-step>E</root-step><root-alter>-1</root-alter></root><kind text="m7">minor-seventh</kind></harmony>
<note><pitch><step>G</step><octave>5</octave></pitch><duration>360</duration><type>eighth</type><dot/><staff>1</staff><notations><slur type="start"/></notations></note>
<note><pitch><step>E</step><alter>-1</alter><octave>5</octave></pitch><duration>120</duration><type>16th</type><staff>1</staff></note>
<note><pitch><step>D</step><octave>5</octave></pitch><duration>240</duration><type>eighth</type><staff>1</staff></note>
<note><pitch><step>C</step><octave>5</octave></pitch><duration>240</duration><type>eighth</type><staff>1</staff></note>
<note><pitch><step>B</step><alter>-1</alter><octave>4</octave></pitch><duration>960</duration><type>half</type><staff>1</staff><notations><slur type="stop"/></notations></note>
<note><pitch><step>E</step><alter>-1</alter><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>B</step><alter>-1</alter><octave>3</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>D</step><octave>4</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>G</step><alter>-1</alter><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>B</step><alter>-1</alter><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>D</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>G</step><alter>-1</alter><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>E</step><alter>-1</alter><octave>4</octave></pitch><duration>480</duration><type>quarter</type><staff>2</staff></note>
</measure>
<measure number="24">
<harmony><root><root-step>G</root-step></root><kind text="7(b9,#9)">dominant</kind></harmony>
<note><pitch><step>B</step><octave>4</octave></pitch><duration>1200</duration><type>half</type><dot/><staff>1</staff></note>
<note><rest/><duration>240</duration><type>eighth</type><staff>1</staff></note>
<note><pitch><step>G</step><octave>5</octave></pitch><duration>240</duration><type>eighth</type><staff>1</staff></note>
<note><pitch><step>G</step><octave>2</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>D</step><octave>3</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>F</step><octave>3</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>A</step><alter>-1</alter><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>B</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>D</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>F</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>A</step><alter>-1</alter><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>G</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
</measure>
<measure number="25">
<direction placement="above"><direction-type><rehearsal>Coda</rehearsal></direction-type></direction>
<direction placement="above"><direction-type><words font-style="italic">Triumphant return</words></direction-type></direction>
<direction placement="above"><direction-type><dynamics><f/></dynamics></direction-type></direction>
<harmony><root><root-step>C</root-step></root><kind text="7(9,13)">dominant-13th</kind></harmony>
<note><rest/><duration>120</duration><type>16th</type><staff>1</staff></note>
<note><pitch><step>C</step><octave>5</octave></pitch><duration>120</duration><type>16th</type><staff>1</staff><notations><slur type="start"/></notations></note>
<note><pitch><step>E</step><alter>-1</alter><octave>5</octave></pitch><duration>120</duration><type>16th</type><staff>1</staff></note>
<note><pitch><step>F</step><octave>5</octave></pitch><duration>360</duration><type>eighth</type><dot/><staff>1</staff></note>
<note><pitch><step>G</step><octave>5</octave></pitch><duration>240</duration><type>eighth</type><staff>1</staff></note>
<note><pitch><step>A</step><octave>5</octave></pitch><duration>480</duration><type>quarter</type><staff>1</staff></note>
<note><pitch><step>B</step><alter>-1</alter><octave>5</octave></pitch><duration>480</duration><type>quarter</type><staff>1</staff><notations><slur type="stop"/></notations></note>
<note><pitch><step>C</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>G</step><octave>3</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>B</step><alter>-1</alter><octave>3</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>E</step><alter>-1</alter><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>A</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>C</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>G</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>B</step><alter>-1</alter><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>E</step><alter>-1</alter><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
</measure>
<measure number="26">
<harmony><root><root-step>F</root-step></root><kind text="7(9)">dominant-ninth</kind></harmony>
<note><pitch><step>C</step><octave>6</octave></pitch><duration>360</duration><type>eighth</type><dot/><staff>1</staff><notations><slur type="start"/></notations></note>
<note><pitch><step>A</step><octave>5</octave></pitch><duration>120</duration><type>16th</type><staff>1</staff></note>
<note><pitch><step>G</step><octave>5</octave></pitch><duration>240</duration><type>eighth</type><staff>1</staff></note>
<note><pitch><step>F</step><octave>5</octave></pitch><duration>480</duration><type>quarter</type><staff>1</staff></note>
<note><pitch><step>E</step><alter>-1</alter><octave>5</octave></pitch><duration>720</duration><type>quarter</type><dot/><staff>1</staff><notations><slur type="stop"/></notations></note>
<note><pitch><step>D</step><octave>5</octave></pitch><duration>240</duration><type>eighth</type><staff>1</staff></note>
<note><pitch><step>F</step><octave>2</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>C</step><octave>3</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>E</step><alter>-1</alter><octave>3</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>A</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>G</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>C</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>E</step><alter>-1</alter><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>A</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>F</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
</measure>
<measure number="27">
<harmony><root><root-step>C</root-step></root><kind text="m9">minor-ninth</kind></harmony>
<note><pitch><step>E</step><alter>-1</alter><octave>5</octave></pitch><duration>240</duration><type>eighth</type><staff>1</staff><notations><slur type="start"/></notations></note>
<note><pitch><step>C</step><octave>5</octave></pitch><duration>120</duration><type>16th</type><staff>1</staff></note>
<note><pitch><step>E</step><alter>-1</alter><octave>5</octave></pitch><duration>120</duration><type>16th</type><staff>1</staff></note>
<note><pitch><step>F</step><octave>5</octave></pitch><duration>360</duration><type>eighth</type><dot/><staff>1</staff></note>
<note><pitch><step>G</step><octave>5</octave></pitch><duration>120</duration><type>16th</type><staff>1</staff></note>
<note><pitch><step>A</step><alter>-1</alter><octave>5</octave></pitch><duration>480</duration><type>quarter</type><staff>1</staff></note>
<note><pitch><step>G</step><octave>5</octave></pitch><duration>480</duration><type>quarter</type><staff>1</staff><notations><slur type="stop"/></notations></note>
<note><pitch><step>C</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>G</step><octave>3</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>B</step><alter>-1</alter><octave>3</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>D</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>E</step><alter>-1</alter><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>G</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>B</step><alter>-1</alter><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>D</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>C</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
</measure>
<measure number="28">
<harmony><root><root-step>G</root-step></root><kind text="7(b9)">dominant</kind></harmony>
<note><pitch><step>F</step><octave>5</octave></pitch><duration>360</duration><type>eighth</type><dot/><staff>1</staff><notations><slur type="start"/></notations></note>
<note><pitch><step>E</step><alter>-1</alter><octave>5</octave></pitch><duration>120</duration><type>16th</type><staff>1</staff></note>
<note><pitch><step>D</step><octave>5</octave></pitch><duration>240</duration><type>eighth</type><staff>1</staff></note>
<note><pitch><step>C</step><octave>5</octave></pitch><duration>240</duration><type>eighth</type><staff>1</staff></note>
<note><pitch><step>B</step><octave>4</octave></pitch><duration>960</duration><type>half</type><staff>1</staff><notations><slur type="stop"/></notations></note>
<note><pitch><step>G</step><octave>2</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>D</step><octave>3</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>F</step><octave>3</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>A</step><alter>-1</alter><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>B</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>D</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>F</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>A</step><alter>-1</alter><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>G</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
</measure>
<measure number="29">
<harmony><root><root-step>C</root-step></root><kind text="7(9,13)">dominant-13th</kind></harmony>
<note><pitch><step>C</step><octave>5</octave></pitch><duration>120</duration><type>16th</type><staff>1</staff><notations><slur type="start"/></notations></note>
<note><pitch><step>E</step><alter>-1</alter><octave>5</octave></pitch><duration>120</duration><type>16th</type><staff>1</staff></note>
<note><pitch><step>F</step><octave>5</octave></pitch><duration>240</duration><type>eighth</type><staff>1</staff></note>
<note><pitch><step>G</step><octave>5</octave></pitch><duration>360</duration><type>eighth</type><dot/><staff>1</staff></note>
<note><pitch><step>A</step><octave>5</octave></pitch><duration>120</duration><type>16th</type><staff>1</staff></note>
<note><pitch><step>G</step><octave>5</octave></pitch><duration>720</duration><type>quarter</type><dot/><staff>1</staff><notations><slur type="stop"/></notations></note>
<note><pitch><step>E</step><alter>-1</alter><octave>5</octave></pitch><duration>240</duration><type>eighth</type><staff>1</staff></note>
<note><pitch><step>C</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>G</step><octave>3</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>B</step><alter>-1</alter><octave>3</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>E</step><alter>-1</alter><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>A</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>C</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>G</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>B</step><alter>-1</alter><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>E</step><alter>-1</alter><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
</measure>
<measure number="30">
<harmony><root><root-step>A</root-step><root-alter>-1</root-alter></root><kind text="maj7">major-seventh</kind></harmony>
<note><pitch><step>E</step><alter>-1</alter><octave>5</octave></pitch><duration>720</duration><type>quarter</type><dot/><staff>1</staff><notations><slur type="start"/></notations></note>
<note><pitch><step>C</step><octave>5</octave></pitch><duration>240</duration><type>eighth</type><staff>1</staff></note>
<note><pitch><step>A</step><alter>-1</alter><octave>4</octave></pitch><duration>960</duration><type>half</type><staff>1</staff><notations><slur type="stop"/></notations></note>
<note><pitch><step>A</step><alter>-1</alter><octave>2</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>E</step><alter>-1</alter><octave>3</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>G</step><octave>3</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>C</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>E</step><alter>-1</alter><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>G</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>A</step><alter>-1</alter><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>C</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>E</step><alter>-1</alter><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
</measure>
<measure number="31">
<harmony><root><root-step>G</root-step></root><kind text="7sus">suspended-fourth</kind></harmony>
<note><pitch><step>D</step><octave>5</octave></pitch><duration>480</duration><type>quarter</type><staff>1</staff><notations><slur type="start"/></notations></note>
<note><pitch><step>C</step><octave>5</octave></pitch><duration>240</duration><type>eighth</type><staff>1</staff></note>
<note><pitch><step>B</step><alter>-1</alter><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>1</staff></note>
<note><pitch><step>G</step><octave>4</octave></pitch><duration>960</duration><type>half</type><staff>1</staff><notations><slur type="stop"/></notations></note>
<note><pitch><step>G</step><octave>2</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>D</step><octave>3</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>F</step><octave>3</octave></pitch><duration>120</duration><type>16th</type><staff>2</staff></note>
<note><pitch><step>C</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>D</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>F</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>G</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>C</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>D</step><octave>3</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
</measure>
<measure number="32">
<harmony><root><root-step>C</root-step></root><kind text="m(add9)">minor</kind></harmony>
<note><pitch><step>C</step><octave>5</octave></pitch><duration>1920</duration><type>whole</type><staff>1</staff><notations><fermata/></notations></note>
<note><pitch><step>C</step><octave>3</octave></pitch><duration>480</duration><type>quarter</type><staff>2</staff></note>
<note><pitch><step>G</step><octave>3</octave></pitch><duration>480</duration><type>quarter</type><staff>2</staff></note>
<note><pitch><step>E</step><alter>-1</alter><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>D</step><octave>4</octave></pitch><duration>240</duration><type>eighth</type><staff>2</staff></note>
<note><pitch><step>E</step><alter>-1</alter><octave>4</octave></pitch><duration>480</duration><type>quarter</type><staff>2</staff><notations><fermata/></notations></note>
<barline><bar-style>light-heavy</bar-style></barline>
</measure>
</part>
</score-partwise>'''

with open('scores/MastersPalette-Mvmt1-Excellent.musicxml', 'w', encoding='utf-8') as f:
    f.write(mvmt1)
print("Created: MastersPalette-Mvmt1-Excellent.musicxml (32 bars)")
print("  Motif: C-Eb-F | Form: A-A2-B-Coda | Internal Revisions: V10")





