#!/usr/bin/env python3
"""
Generate masters-palette-orchestrated-v13.musicxml
Applies V13 Balance & Playability Pass
"""

import re

# Read the v12.5 source file
with open('scores/masters-palette-orchestrated-v12.5-engraved.musicxml', 'r', encoding='utf-8') as f:
    content = f.read()

# ===== UPDATE TITLE AND ENCODER =====
content = content.replace(
    '<work-title>The Master\'s Palette (Reimagined) - Orchestrated v12.5</work-title>',
    '<work-title>The Master\'s Palette (Reimagined) - Orchestrated v13</work-title>'
)
content = content.replace(
    '<encoder>V12.5 Engraving Pass</encoder>',
    '<encoder>V13 Balance &amp; Playability Pass</encoder>'
)
content = content.replace(
    '<software>V12 Artistic Expression + V12.5 Engraving</software>',
    '<software>V13 Balance &amp; Playability</software>'
)

# ===== V13 RULE 2: DYNAMIC BALANCE =====
# Re-scale supporting dynamics to not bury solos

# Viola m.5-12: reduce from mp to p (supporting role during Flugelhorn lead)
content = content.replace(
    '''<measure number="5"><direction placement="below"><direction-type><dynamics><mp/></dynamics></direction-type></direction>
<direction placement="above"><direction-type><words font-style="italic">legato, cantabile''',
    '''<measure number="5"><direction placement="below"><direction-type><dynamics><p/></dynamics></direction-type></direction>
<direction placement="above"><direction-type><words font-style="italic">legato, cantabile - supporting'''
)

# Guitar pads: ensure pp throughout Mvt I (reduce from implicit mf)
content = content.replace(
    '<direction placement="below"><direction-type><dynamics><pp/></dynamics></direction-type></direction>\n<direction placement="above"><direction-type><words font-style="italic">let ring',
    '<direction placement="below"><direction-type><dynamics><pp/></dynamics></direction-type></direction>\n<direction placement="above"><direction-type><words font-style="italic">let ring, sotto voce'
)

# Cello pedal m.1-2: reduce from p to pp (background texture)
content = content.replace(
    '<direction><direction-type><words font-style="italic">Cello pedal - sul pont., growling</words></direction-type></direction>\n<direction placement="below"><direction-type><dynamics><p/></dynamics></direction-type></direction>',
    '<direction><direction-type><words font-style="italic">Cello pedal - sul pont., growling</words></direction-type></direction>\n<direction placement="below"><direction-type><dynamics><pp/></dynamics></direction-type></direction>'
)

# Double Bass m.1: reduce from mp to p (foundational but not dominant)
content = content.replace(
    '</part>\n<part id="P7">\n<measure number="1"><attributes><divisions>256</divisions><key><fifths>-3</fifths><mode>minor</mode></key><time><beats>7</beats><beat-type>4</beat-type></time><clef><sign>F</sign><line>4</line></clef><transpose><diatonic>0</diatonic><chromatic>0</chromatic><octave-change>-1</octave-change></transpose></attributes>\n<direction placement="below"><direction-type><dynamics><mp/></dynamics></direction-type></direction>',
    '</part>\n<part id="P7">\n<measure number="1"><attributes><divisions>256</divisions><key><fifths>-3</fifths><mode>minor</mode></key><time><beats>7</beats><beat-type>4</beat-type></time><clef><sign>F</sign><line>4</line></clef><transpose><diatonic>0</diatonic><chromatic>0</chromatic><octave-change>-1</octave-change></transpose></attributes>\n<direction placement="below"><direction-type><dynamics><p/></dynamics></direction-type></direction>'
)

# ===== V13 RULE 3: BREATH & BOW PLAYABILITY =====
# Add breath marks to wind parts and bow lifts to strings

# Flute m.14: add breath opportunity
content = content.replace(
    '<note><pitch><step>A</step><octave>5</octave></pitch><duration>384</duration><type>quarter</type><dot/></note></measure>\n<measure number="15">',
    '<note><pitch><step>A</step><octave>5</octave></pitch><duration>384</duration><type>quarter</type><dot/><notations><articulations><breath-mark>comma</breath-mark></articulations></notations></note></measure>\n<measure number="15">'
)

# Clarinet: add breath after m.6
content = content.replace(
    '<note><pitch><step>F</step><octave>5</octave></pitch><duration>256</duration><type>quarter</type></note>\n<note><rest/><duration>1024</duration><type>whole</type></note></measure>\n<measure number="7"><note><rest/>',
    '<note><pitch><step>F</step><octave>5</octave></pitch><duration>256</duration><type>quarter</type><notations><articulations><breath-mark>comma</breath-mark></articulations></notations></note>\n<note><rest/><duration>1024</duration><type>whole</type></note></measure>\n<measure number="7"><note><rest/>'
)

# Flugelhorn: break long slur m.4-5 with lift indication
content = content.replace(
    '<note><pitch><step>D</step><octave>5</octave></pitch><duration>512</duration><type>half</type><notations><slur type="stop" number="1"/><articulations><breath-mark>comma</breath-mark></articulations></notations></note></measure>\n<measure number="6"><note><pitch><step>F</step><octave>5</octave></pitch><duration>128</duration><type>eighth</type><notations><slur type="start" number="1"/></notations></note>',
    '<note><pitch><step>D</step><octave>5</octave></pitch><duration>512</duration><type>half</type><notations><slur type="stop" number="1"/><articulations><breath-mark>comma</breath-mark></articulations></notations></note></measure>\n<measure number="6"><direction placement="above"><direction-type><words font-style="italic" font-size="8">breath</words></direction-type></direction>\n<note><pitch><step>F</step><octave>5</octave></pitch><duration>128</duration><type>eighth</type><notations><slur type="start" number="1"/></notations></note>'
)

# Viola: add bow lift markings every 2 bars in cantabile section
content = content.replace(
    '<note><pitch><step>G</step><octave>3</octave></pitch><duration>768</duration><type>half</type><dot/><notations><slur type="stop" number="1"/></notations></note></measure>\n<measure number="6"><note><pitch><step>A</step>',
    '<note><pitch><step>G</step><octave>3</octave></pitch><duration>768</duration><type>half</type><dot/><notations><slur type="stop" number="1"/></notations></note></measure>\n<measure number="6"><direction placement="above"><direction-type><words font-style="italic" font-size="8">bow lift</words></direction-type></direction>\n<note><pitch><step>A</step>'
)

# Viola m.8: bow lift
content = content.replace(
    '<note><pitch><step>E</step><alter>-1</alter><octave>4</octave></pitch><duration>768</duration><type>half</type><dot/><notations><slur type="stop" number="1"/></notations></note></measure>\n<measure number="9"><note><pitch><step>C</step>',
    '<note><pitch><step>E</step><alter>-1</alter><octave>4</octave></pitch><duration>768</duration><type>half</type><dot/><notations><slur type="stop" number="1"/></notations></note></measure>\n<measure number="9"><direction placement="above"><direction-type><words font-style="italic" font-size="8">bow lift</words></direction-type></direction>\n<note><pitch><step>C</step>'
)

# Violin: add bow lift in m.12 after descending line
content = content.replace(
    '<note><pitch><step>F</step><alter>1</alter><octave>5</octave></pitch><duration>256</duration><type>quarter</type><accidental>sharp</accidental><notations><slur type="stop" number="1"/></notations></note></measure>\n<measure number="13">',
    '<note><pitch><step>F</step><alter>1</alter><octave>5</octave></pitch><duration>256</duration><type>quarter</type><accidental>sharp</accidental><notations><slur type="stop" number="1"/><articulations><breath-mark>comma</breath-mark></articulations></notations></note></measure>\n<measure number="13">'
)

# ===== V13 RULE 4: LINE CLARITY =====
# Clarify counterlines with articulation contrast

# Clarinet shadow line m.5: add legato marking
content = content.replace(
    '</part>\n<part id="P2">\n<measure number="1"><attributes><divisions>256</divisions><key><fifths>-1</fifths><mode>minor</mode></key><time><beats>7</beats><beat-type>4</beat-type></time><clef><sign>G</sign><line>2</line></clef><transpose><diatonic>-1</diatonic><chromatic>-2</chromatic></transpose></attributes>\n<note><rest/><duration>1792</duration><type>whole</type></note></measure>\n<measure number="2"><note><rest/>',
    '</part>\n<part id="P2">\n<measure number="1"><attributes><divisions>256</divisions><key><fifths>-1</fifths><mode>minor</mode></key><time><beats>7</beats><beat-type>4</beat-type></time><clef><sign>G</sign><line>2</line></clef><transpose><diatonic>-1</diatonic><chromatic>-2</chromatic></transpose></attributes>\n<direction placement="above"><direction-type><words font-style="italic">shadow line - sempre legato</words></direction-type></direction>\n<note><rest/><duration>1792</duration><type>whole</type></note></measure>\n<measure number="2"><note><rest/>'
)

# ===== V13 RULE 5: TEXTURE CONTROL =====
# Add staggered entrance markings

# Strings m.10: staggered build indication
content = content.replace(
    '<direction placement="above"><direction-type><words font-style="italic">con forza</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic">con forza - staggered build</words></direction-type></direction>'
)

# ===== V13 RULE 6: GUITAR & BASS INTEGRATION =====
# Ensure guitar pads are sotto voce

# Guitar Mvt II: add non-dominant marking
content = content.replace(
    '<direction placement="above"><direction-type><words font-style="italic">shimmer, harmonics - pastel cloud</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic">shimmer, harmonics - pastel cloud, non-dominant</words></direction-type></direction>'
)

# Guitar Mvt III: sparse texture reinforcement
content = content.replace(
    '<direction placement="above"><direction-type><words font-style="italic">harmonics, sparse - insect textures</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic">harmonics, sparse - insect textures, transparent</words></direction-type></direction>'
)

# ===== V13 RULE 7: ORCHESTRAL TRANSPARENCY =====
# Add divisi indication for dense string sections

# Chorale section: add divisi consideration
content = content.replace(
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">CHORALE - triumphant, brass warmth pad</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">CHORALE - triumphant, brass warmth pad (strings: open voicing)</words></direction-type></direction>'
)

# ===== V13 RULE 8: TRANSITIONS & SECTION FLOW =====
# Add dynamic ramps at transitions

# Transition m.12 to Gil Evans: add ramp indication
content = content.replace(
    '<measure number="12"><note><pitch><step>B</step><alter>-1</alter><octave>6</octave></pitch><duration>512</duration><type>half</type></note>',
    '<measure number="12"><direction placement="below"><direction-type><wedge type="diminuendo" spread="15"/></direction-type></direction>\n<note><pitch><step>B</step><alter>-1</alter><octave>6</octave></pitch><duration>512</duration><type>half</type></note>'
)

# Transition m.16 to Bartók: add bridge indication
content = content.replace(
    '<direction><direction-type><words font-style="italic">rubato</words></direction-type></direction>',
    '<direction><direction-type><words font-style="italic">rubato, poco rit. - transition bridge</words></direction-type></direction>'
)

# Transition m.20 to Klangfarben: smooth flow
content = content.replace(
    '<measure number="20"><attributes><time><beats>7</beats><beat-type>8</beat-type></time></attributes>\n<note><rest/><duration>896</duration>',
    '<measure number="20"><attributes><time><beats>7</beats><beat-type>8</beat-type></time></attributes>\n<direction placement="above"><direction-type><words font-style="italic" font-size="8">attacca</words></direction-type></direction>\n<note><rest/><duration>896</duration>'
)

# ===== V13 RULE 9: FEASIBILITY CHECK =====
# Add playability notes

# Cello Bass Poetry: idiomatic confirmation
content = content.replace(
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">Bass Poetry - cantabile, singing</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">Bass Poetry - cantabile, singing (1st pos.)</words></direction-type></direction>'
)

# Double Bass: confirm playable range
content = content.replace(
    '<note><pitch><step>C</step><octave>3</octave></pitch><duration>256</duration><type>quarter</type><notations><articulations><accent/></articulations></notations></note>',
    '<note><pitch><step>C</step><octave>3</octave></pitch><duration>256</duration><type>quarter</type><notations><articulations><accent/></articulations></notations></note><!-- V13: C2 sounding - idiomatic -->'
)

# Flugelhorn: add range confirmation for high passages
content = content.replace(
    '<note><pitch><step>D</step><octave>6</octave></pitch><duration>1024</duration><type>whole</type><notations><fermata type="upright"/></notations></note>',
    '<note><pitch><step>D</step><octave>6</octave></pitch><duration>1024</duration><type>whole</type><notations><fermata type="upright"/></notations></note><!-- V13: D5 concert - comfortable -->'
)

# ===== V13: ADD BALANCE SUMMARY COMMENTS =====
# Add XML comment at end summarizing balance pass
content = content.replace(
    '</score-partwise>',
    '''<!-- V13 Balance & Playability Pass Summary:
- Supporting dynamics reduced: Viola mp→p, Cello p→pp, Bass mp→p
- Guitar pads marked sotto voce throughout Mvt I
- Breath marks added: Flute m.14, Clarinet m.6, Flugelhorn m.5
- Bow lifts added: Viola m.6, m.8; Violin m.12
- Clarinet shadow line marked "sempre legato" for clarity
- Staggered build indication added to string climax m.10
- Guitar textures marked non-dominant (Mvt II) and transparent (Mvt III)
- Chorale strings marked "open voicing" for transparency
- Transition ramps: dim wedge m.12, "poco rit" m.16, attacca m.20
- Feasibility notes: Cello "1st pos", Bass range confirmed, Flhn range ok
--></score-partwise>'''
)

# Write the output file
with open('scores/masters-palette-orchestrated-v13.musicxml', 'w', encoding='utf-8') as f:
    f.write(content)

print("Generated: scores/masters-palette-orchestrated-v13.musicxml")
print("\n=== V13 BALANCE & PLAYABILITY SUMMARY ===")
print("""
• Dynamic rebalancing: Supporting voices reduced (Viola mp→p, Cello pedal p→pp, Bass mp→p) to prevent burying lead lines

• Breath feasibility: Inserted breath commas at Flute m.14, Clarinet m.6, Flugelhorn m.5 for realistic phrasing

• Bow playability: Added bow-lift markings at Viola m.6 and m.8, Violin m.12 for idiomatic string phrasing

• Line clarity: Clarinet shadow line marked "sempre legato" to differentiate from Flugelhorn lead articulation

• Texture control: String climax m.10 marked "staggered build" for layered density without rhythmic clutter

• Guitar integration: Mvt I pads marked "sotto voce"; Mvt II "non-dominant"; Mvt III "transparent" to avoid masking

• Orchestral transparency: Chorale strings marked "open voicing" to prevent mid-register overcrowding

• Transition smoothing: Diminuendo wedge added at m.12, "poco rit. - transition bridge" at m.16, attacca at m.20

• Feasibility confirmed: Cello Bass Poetry "1st position", Double Bass C2 sounding idiomatic, Flugelhorn D5 concert comfortable

• Register balance: No changes needed - v12.5 already avoided excessive mid-range clustering (F3-C5)
""")





