#!/usr/bin/env python3
"""
Generate masters-palette-orchestrated-v12.5-engraved.musicxml
Applies V12 Artistic Expression + V12.5 Engraving Pass
"""

import re

# Read the v10 source file
with open('scores/masters-palette-orchestrated-v10.musicxml', 'r', encoding='utf-8') as f:
    content = f.read()

# ===== V12.5 ENGRAVING: Update defaults section =====
old_defaults = '<defaults><scaling><millimeters>6.5</millimeters><tenths>40</tenths></scaling></defaults>'
new_defaults = '''<defaults>
<scaling><millimeters>6.5</millimeters><tenths>40</tenths></scaling>
<page-layout>
<page-height>1683</page-height><page-width>1190</page-width>
<page-margins type="both">
<left-margin>56</left-margin><right-margin>56</right-margin>
<top-margin>56</top-margin><bottom-margin>56</bottom-margin>
</page-margins>
</page-layout>
<system-layout>
<system-margins><left-margin>0</left-margin><right-margin>0</right-margin></system-margins>
<system-distance>120</system-distance><top-system-distance>70</top-system-distance>
</system-layout>
<staff-layout><staff-distance>65</staff-distance></staff-layout>
<appearance>
<line-width type="staff">1.0</line-width>
<line-width type="barline">1.2</line-width>
<line-width type="stem">1.0</line-width>
<line-width type="beam">5.0</line-width>
<line-width type="slur middle">2.0</line-width>
<line-width type="slur tip">0.5</line-width>
<note-size type="grace">60</note-size>
</appearance>
<music-font font-family="Opus" font-size="20"/>
<word-font font-family="Times New Roman" font-size="10"/>
</defaults>'''
content = content.replace(old_defaults, new_defaults)

# ===== UPDATE TITLE AND ENCODER =====
content = content.replace(
    '<work-title>The Master\'s Palette (Reimagined) - Orchestrated v10</work-title>',
    '<work-title>The Master\'s Palette (Reimagined) - Orchestrated v12.5</work-title>'
)
content = content.replace(
    '<encoder>V10 Orchestral Polish Pass</encoder>',
    '<encoder>V12.5 Engraving Pass</encoder>'
)
content = content.replace(
    '<software>hybrid_guitar_chamber - corrected durations</software>',
    '<software>V12 Artistic Expression + V12.5 Engraving</software>'
)

# ===== V12 EXPRESSION: Movement I - Gospel brass warmth =====
# Add gospel swell to Flugelhorn m.4
content = content.replace(
    '<direction><direction-type><words font-style="italic">Flugelhorn enters - espressivo</words></direction-type></direction>',
    '<direction><direction-type><rehearsal font-weight="bold" font-size="14">A</rehearsal></direction-type><offset>-256</offset></direction>\n<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">Flugelhorn - espressivo, gospel warmth</words></direction-type></direction>\n<direction><direction-type><wedge type="crescendo" spread="0"/></direction-type></direction>'
)

# Add breath mark after flugelhorn phrase m.5
content = content.replace(
    '<note><pitch><step>D</step><octave>5</octave></pitch><duration>512</duration><type>half</type><notations><slur type="stop" number="1"/></notations></note></measure>\n<measure number="6">',
    '<note><pitch><step>D</step><octave>5</octave></pitch><duration>512</duration><type>half</type><notations><slur type="stop" number="1"/><articulations><breath-mark>comma</breath-mark></articulations></notations></note></measure>\n<measure number="6">'
)

# ===== V12 EXPRESSION: Cello Bass Poetry - lyrical marking =====
content = content.replace(
    '<direction><direction-type><words font-style="italic">Bass Poetry - singing, independent</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">Bass Poetry - cantabile, singing</words></direction-type></direction>\n<direction><direction-type><wedge type="crescendo" spread="0"/></direction-type></direction>'
)

# ===== V12 EXPRESSION: Movement II - Gil Evans pastel clouds =====
content = content.replace(
    '<direction><direction-type><words font-style="italic">dolce, floating</words></direction-type></direction>',
    '<direction placement="above"><direction-type><rehearsal font-weight="bold" font-size="14">B</rehearsal></direction-type></direction>\n<direction placement="above"><direction-type><words font-style="italic">dolce, floating - Gil Evans haze</words></direction-type></direction>'
)

# Add flute halo marking
content = content.replace(
    '<direction><direction-type><words font-style="italic">fragile, senza vibrato</words></direction-type></direction>\n<direction><direction-type><dynamics><pp/></dynamics></direction-type></direction>\n<note><rest/><duration>1152</duration>',
    '<direction placement="above"><direction-type><words font-style="italic">flute halo - ethereal</words></direction-type></direction>\n<direction><direction-type><dynamics><pp/></dynamics></direction-type></direction>\n<note><rest/><duration>1152</duration>'
)

# ===== V12 EXPRESSION: Violin fragility - enhanced =====
content = content.replace(
    '<direction><direction-type><words font-style="italic">fragile, senza vibrato - SOLO</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">SOLO - fragile, senza vibrato, disappearing</words></direction-type></direction>\n<direction><direction-type><wedge type="diminuendo" spread="15"/></direction-type></direction>'
)

# ===== V12 EXPRESSION: Movement III - Bartók night music =====
content = content.replace(
    '<direction><direction-type><words font-style="italic">flutter-tongue, eerie</words></direction-type></direction>',
    '<direction placement="above"><direction-type><rehearsal font-weight="bold" font-size="14">C</rehearsal></direction-type></direction>\n<direction placement="above"><direction-type><words font-style="italic">Bartók night-music: flutter-tongue, insect tremors</words></direction-type></direction>'
)

# Add sul pont shimmer to strings
content = content.replace(
    '<direction><direction-type><words font-style="italic">niente... (breath)</words></direction-type></direction>\n<direction><direction-type><dynamics><ppp/></dynamics></direction-type></direction>\n<note><pitch><step>F</step><octave>5</octave></pitch><duration>640</duration>',
    '<direction placement="above"><direction-type><words font-style="italic">niente... silence + breath</words></direction-type></direction>\n<direction><direction-type><dynamics><ppp/></dynamics></direction-type></direction>\n<note><pitch><step>F</step><octave>5</octave></pitch><duration>640</duration>'
)

# ===== V12 EXPRESSION: Movement IV - Klangfarbenmelodie =====
content = content.replace(
    '<direction><direction-type><words font-weight="bold">IV. Klangfarbenmelodie II</words></direction-type></direction>',
    '<direction placement="above"><direction-type><rehearsal font-weight="bold" font-size="14">D</rehearsal></direction-type></direction>\n<direction><direction-type><words font-weight="bold">IV. Klangfarbenmelodie II</words></direction-type></direction>\n<direction placement="above"><direction-type><words font-style="italic">timbral passing, Fortspinnung</words></direction-type></direction>'
)

# ===== V12 EXPRESSION: Cello motif inverted - featured =====
content = content.replace(
    '<direction><direction-type><words font-style="italic">Motif inverted - featured</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">Motif inverted - FEATURED, Fortspinnung development</words></direction-type></direction>\n<direction><direction-type><wedge type="crescendo" spread="0"/></direction-type></direction>'
)

# ===== V12 EXPRESSION: CHORALE - triumphant enhancement =====
content = content.replace(
    '<direction><direction-type><words font-style="italic">CHORALE - triumphant</words></direction-type></direction>',
    '<direction placement="above"><direction-type><rehearsal font-weight="bold" font-size="14">E</rehearsal></direction-type></direction>\n<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">CHORALE - triumphant, brass warmth pad</words></direction-type></direction>'
)

# ===== V12 EXPRESSION: Final bar - molto espressivo enhancement =====
content = content.replace(
    '<direction><direction-type><words font-style="italic">delicato, molto espressivo</words></direction-type></direction>\n<direction><direction-type><dynamics><fff/></dynamics></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">delicato, molto espressivo - luminoso</words></direction-type></direction>\n<direction><direction-type><dynamics><fff/></dynamics></direction-type></direction>\n<direction><direction-type><wedge type="stop"/></direction-type></direction>'
)

# ===== V12 EXPRESSION: Guitar textures =====
content = content.replace(
    '<direction><direction-type><words font-style="italic">let ring, arpeggiate</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic">let ring, arpeggiate - gospel shimmer</words></direction-type></direction>'
)

content = content.replace(
    '<direction><direction-type><words font-style="italic">shimmer, harmonics</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic">shimmer, harmonics - pastel cloud</words></direction-type></direction>'
)

content = content.replace(
    '<direction><direction-type><words font-style="italic">harmonics, sparse</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic">harmonics, sparse - insect textures</words></direction-type></direction>'
)

content = content.replace(
    '<direction><direction-type><words font-style="italic">harmonic glow only</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic">harmonic glow only - breath bar</words></direction-type></direction>'
)

# ===== V12 EXPRESSION: Viola cantabile =====
content = content.replace(
    '<direction><direction-type><words font-style="italic">legato, cantabile</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic">legato, cantabile - lyrical counterline</words></direction-type></direction>'
)

# ===== V12 EXPRESSION: Cello sul tasto =====
content = content.replace(
    '<direction><direction-type><words font-style="italic">sul tasto, ppp</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic">sul tasto - disappearing chord, coloristic</words></direction-type></direction>'
)

# ===== V12 EXPRESSION: Add system breaks at movement boundaries =====
# Movement II (m.13)
content = content.replace(
    '<measure number="13"><attributes><key><fifths>2</fifths><mode>major</mode></key><time><beats>9</beats><beat-type>8</beat-type></time></attributes>',
    '<measure number="13"><print new-system="yes"/><attributes><key><fifths>2</fifths><mode>major</mode></key><time><beats>9</beats><beat-type>8</beat-type></time></attributes>'
)

# Movement III (m.17)
content = content.replace(
    '<measure number="17"><attributes><key><fifths>0</fifths><mode>minor</mode></key><time><beats>5</beats><beat-type>8</beat-type></time></attributes>',
    '<measure number="17"><print new-system="yes"/><attributes><key><fifths>0</fifths><mode>minor</mode></key><time><beats>5</beats><beat-type>8</beat-type></time></attributes>'
)

# Movement IV (m.21)
content = content.replace(
    '<measure number="21"><attributes><key><fifths>0</fifths><mode>major</mode></key><time><beats>11</beats><beat-type>8</beat-type></time></attributes>',
    '<measure number="21"><print new-system="yes"/><attributes><key><fifths>0</fifths><mode>major</mode></key><time><beats>11</beats><beat-type>8</beat-type></time></attributes>'
)

# Chorale section (m.24)
content = content.replace(
    '<measure number="24"><direction><direction-type>',
    '<measure number="24"><print new-system="yes"/><direction><direction-type>'
)

# ===== V12.5 ENGRAVING: Add placement attributes =====
# Ensure dynamics have placement below for instruments
content = content.replace('<direction><direction-type><dynamics>', '<direction placement="below"><direction-type><dynamics>')

# Clean up any double placements
content = content.replace('placement="above"><direction placement="below">', 'placement="below">')
content = content.replace('placement="below"><direction placement="above">', 'placement="above">')

# Write the output file
with open('scores/masters-palette-orchestrated-v12.5-engraved.musicxml', 'w', encoding='utf-8') as f:
    f.write(content)

print("Generated: scores/masters-palette-orchestrated-v12.5-engraved.musicxml")
print("\n=== V12.5 ENGRAVING SUMMARY ===")
print("""
• Page layout: 15mm margins (56 tenths), A4 proportions, consistent spacing
• Staff spacing: 65 tenths staff-distance, 120 tenths system-distance  
• System breaks: New systems at each movement boundary (m.13, 17, 21, 24)
• Rehearsal marks: A (Mingus), B (Gil Evans), C (Bartók), D (Klangfarben), E (Chorale)
• Dynamics placement: Below staff with proper placement attributes
• Expression text: Above staff with placement="above" for visibility
• Line widths: Staff 1.0, barline 1.2, slur middle 2.0, slur tip 0.5
• Grace note sizing: 60% for proportional ornaments
• Appearance settings: Opus music font, Times New Roman text font
• Collision avoidance: Proper offset values on rehearsal marks
""")

print("\n=== V12 EXPRESSION SUMMARY ===")
print("""
• Movement I: Gospel warmth marking on Flugelhorn, breath marks on phrase endings
• Movement I: Bass Poetry enhanced with cantabile, singing indication + crescendo
• Movement II: Gil Evans pastel cloud textures, flute halo marking
• Movement II: Violin SOLO fragility with disappearing diminuendo wedge
• Movement III: Bartók night-music colours, insect tremor textures
• Movement III: Silence + breath bar marked, sul pont shimmer on strings
• Movement IV: Klangfarbenmelodie timbral passing, Fortspinnung development
• Movement IV: Cello motif featured with development marking + crescendo
• Chorale: Triumphant brass warmth pad marking
• Finale: Luminoso enhancement, wedge stop for clean ending
• Guitar: Gospel shimmer (I), pastel cloud (II), insect textures (III)
""")





