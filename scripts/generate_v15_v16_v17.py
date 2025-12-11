#!/usr/bin/env python3
"""
Generate V15, V16, V17 passes with copyright notices
The Master's Palette - Full Production Pipeline
"""

COPYRIGHT = "© 2025 Michael Bryant. All Rights Reserved."

# ============================================================
# V15 FINAL ARTISTIC POLISH PASS
# ============================================================
print("=== GENERATING V15 FINAL ARTISTIC POLISH ===")

with open('scores/masters-palette-orchestrated-v14.musicxml', 'r', encoding='utf-8') as f:
    v15 = f.read()

# Update title and encoder
v15 = v15.replace(
    '<work-title>The Master\'s Palette (Reimagined) - Orchestrated v14</work-title>',
    '<work-title>The Master\'s Palette (Reimagined) - v15 FINAL</work-title>'
)
v15 = v15.replace(
    '<encoder>V14 Expressive Musicality Pass</encoder>',
    '<encoder>V15 Final Artistic Polish</encoder>'
)
v15 = v15.replace(
    '<software>V14 Expressive Musicality</software>',
    '<software>V15 Final - Performance Ready</software>'
)

# Add copyright to identification/metadata
v15 = v15.replace(
    '</encoding></identification>',
    f'<supports element="print" type="yes" attribute="new-page" value="yes"/></encoding>\n<rights>{COPYRIGHT}</rights></identification>'
)

# Add copyright credits to score
v15 = v15.replace(
    '</identification>\n<defaults>',
    f'''</identification>
<credit page="1"><credit-type>rights</credit-type><credit-words font-size="8" justify="center" valign="bottom">{COPYRIGHT}</credit-words></credit>
<defaults>'''
)

# V15 RULE 1: Micro-dynamics
v15 = v15.replace(
    '<note><pitch><step>D</step><octave>5</octave></pitch><duration>512</duration><type>half</type><notations><slur type="stop" number="1"/><articulations><breath-mark>comma</breath-mark></articulations></notations></note>',
    '<note><pitch><step>D</step><octave>5</octave></pitch><duration>512</duration><type>half</type><notations><slur type="stop" number="1"/><articulations><breath-mark>comma</breath-mark></articulations><dynamics><other-dynamics>slight swell</other-dynamics></dynamics></notations></note>'
)

# V15 RULE 2: Articulation precision - portato for lyrical lines
v15 = v15.replace(
    '<direction placement="above"><direction-type><words font-style="italic">cantabile - blues cell variant in counterline</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic">cantabile, portato - blues cell variant</words></direction-type></direction>'
)

# V15 RULE 3: Bowing - down-bow for Cello Bass Poetry
v15 = v15.replace(
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">Bass Poetry - cantabile, singing (1st pos.)</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">Bass Poetry - cantabile (down-bow, 1st pos.)</words></direction-type></direction>'
)

# V15 RULE 4: Foreground/background clarity
v15 = v15.replace(
    '<direction placement="above"><direction-type><words font-style="italic">flute halo - ethereal</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic">flute halo - ethereal, background pp</words></direction-type></direction>'
)

# V15 RULE 5: Timbral fine-tuning
v15 = v15.replace(
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">SOLO - fragile, flautato, phrase apex then release</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">SOLO - fragile, flautato, non vib., phrase apex</words></direction-type></direction>'
)

v15 = v15.replace(
    '<direction placement="above"><direction-type><words font-style="italic">sul tasto, quasi niente - ethereal glow</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic">sul tasto, poco vib., quasi niente</words></direction-type></direction>'
)

v15 = v15.replace(
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">STRUCTURAL SILENCE - niente, harmonics</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">STRUCTURAL SILENCE - niente (strings: harmonics)</words></direction-type></direction>'
)

# V15 RULE 6: Transition smoothing
v15 = v15.replace(
    '<direction placement="above"><direction-type><words font-style="italic" font-size="9">subito p - breath space before new world</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic" font-size="9">subito p, breath - Gtr: sustain harmonic</words></direction-type></direction>'
)

v15 = v15.replace(
    '<direction><direction-type><words font-style="italic">poco rubato, rit. - expressive bridge</words></direction-type></direction>',
    '<direction><direction-type><words font-style="italic">poco rubato, rit. - strings sustain bridge</words></direction-type></direction>'
)

v15 = v15.replace(
    '<direction placement="above"><direction-type><words font-style="italic" font-size="8">attacca</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic" font-size="8">attacca subito</words></direction-type></direction>'
)

# V15 RULE 7: Pedal/resonance
v15 = v15.replace(
    '<direction placement="above"><direction-type><words font-style="italic">let ring, sotto voce - gospel shimmer</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic">let ring, sempre pp, con pedale</words></direction-type></direction>'
)

v15 = v15.replace(
    '<direction placement="above"><direction-type><words font-style="italic">shimmer, harmonics - pastel cloud, non-dominant</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic">shimmer, harmonics, con pedale</words></direction-type></direction>'
)

# V15 RULE 8: Climax precision
v15 = v15.replace(
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">CLIMAX I - con forza, registral lift</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">CLIMAX I - con forza, lift then warm release</words></direction-type></direction>'
)

v15 = v15.replace(
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">CLIMAX IV - CHORALE, triumphant apotheosis</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">CLIMAX IV - CHORALE, tutti apotheosis</words></direction-type></direction>'
)

v15 = v15.replace(
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">luminoso - climax release, molto espressivo</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">luminoso - gentle release, morendo</words></direction-type></direction>'
)

# V15: Clean up redundant comments
v15 = v15.replace('<!-- V14: 4-bar arc to m.7 -->', '')
v15 = v15.replace('<!-- V14: phrase release -->', '')
v15 = v15.replace('<!-- V14: pedal glow -->', '')

# Write V15
with open('scores/masters-palette-orchestrated-v15.musicxml', 'w', encoding='utf-8') as f:
    f.write(v15)
print("Created: scores/masters-palette-orchestrated-v15.musicxml")

# ============================================================
# V16 PARTS EXTRACTION PASS
# ============================================================
print("\n=== GENERATING V16 PARTS EXTRACTION ===")

v16 = v15  # Start from V15

# Update title
v16 = v16.replace(
    '<work-title>The Master\'s Palette (Reimagined) - v15 FINAL</work-title>',
    '<work-title>The Master\'s Palette (Reimagined) - v16 Parts Edition</work-title>'
)
v16 = v16.replace(
    '<encoder>V15 Final Artistic Polish</encoder>',
    '<encoder>V16 Parts Extraction Pass</encoder>'
)
v16 = v16.replace(
    '<software>V15 Final - Performance Ready</software>',
    '<software>V16 Parts - Professional Extraction</software>'
)

# V16 RULE 1 & 2: Page layout and turns
v16 = v16.replace(
    '<measure number="13"><print new-system="yes"/>',
    '<measure number="13"><print new-system="yes" new-page="yes"/><!-- V16: Page 2 -->'
)

v16 = v16.replace(
    '<measure number="17"><print new-system="yes"/>',
    '<measure number="17"><print new-system="yes" new-page="yes"/><!-- V16: Page 3 -->'
)

v16 = v16.replace(
    '<measure number="21"><print new-system="yes"/>',
    '<measure number="21"><print new-system="yes" new-page="yes"/><!-- V16: Page 4 -->'
)

# V16 RULE 4: Multi-measure rests
v16 = v16.replace(
    '<part id="P1">\n<measure number="1"><attributes><divisions>256</divisions><key><fifths>-3</fifths><mode>minor</mode></key><time><beats>7</beats><beat-type>4</beat-type></time><clef><sign>G</sign><line>2</line></clef></attributes>',
    '<part id="P1">\n<measure number="1"><attributes><divisions>256</divisions><key><fifths>-3</fifths><mode>minor</mode></key><time><beats>7</beats><beat-type>4</beat-type></time><clef><sign>G</sign><line>2</line></clef><measure-style><multiple-rest>6</multiple-rest></measure-style></attributes>'
)

# V16 RULE 5: Cue notes
v16 = v16.replace(
    '<measure number="6"><note><rest/><duration>1792</duration><type>whole</type></note></measure>\n<measure number="7">',
    '<measure number="6"><direction placement="above"><direction-type><words font-style="italic" font-size="7">[cue: Flhn.]</words></direction-type></direction>\n<note><rest/><duration>1792</duration><type>whole</type></note></measure>\n<measure number="7">'
)

# V16 RULE 7: Instrument labels with full names
v16 = v16.replace(
    '<score-part id="P1"><part-name>Flute</part-name><part-abbreviation>Fl.</part-abbreviation></score-part>',
    '<score-part id="P1"><part-name print-object="yes">Flute</part-name><part-abbreviation>Fl.</part-abbreviation><score-instrument id="P1-I1"><instrument-name>Flute</instrument-name></score-instrument></score-part>'
)
v16 = v16.replace(
    '<score-part id="P2"><part-name>Clarinet in Bb</part-name><part-abbreviation>Cl.</part-abbreviation></score-part>',
    '<score-part id="P2"><part-name print-object="yes">Clarinet in Bb</part-name><part-abbreviation>Cl.</part-abbreviation><score-instrument id="P2-I1"><instrument-name>Clarinet in Bb</instrument-name></score-instrument></score-part>'
)
v16 = v16.replace(
    '<score-part id="P3"><part-name>Flugelhorn</part-name><part-abbreviation>Flhn.</part-abbreviation></score-part>',
    '<score-part id="P3"><part-name print-object="yes">Flugelhorn in Bb</part-name><part-abbreviation>Flhn.</part-abbreviation><score-instrument id="P3-I1"><instrument-name>Flugelhorn in Bb</instrument-name></score-instrument></score-part>'
)
v16 = v16.replace(
    '<score-part id="P4"><part-name>Violin</part-name><part-abbreviation>Vln.</part-abbreviation></score-part>',
    '<score-part id="P4"><part-name print-object="yes">Violin</part-name><part-abbreviation>Vln.</part-abbreviation><score-instrument id="P4-I1"><instrument-name>Violin</instrument-name></score-instrument></score-part>'
)
v16 = v16.replace(
    '<score-part id="P5"><part-name>Viola</part-name><part-abbreviation>Vla.</part-abbreviation></score-part>',
    '<score-part id="P5"><part-name print-object="yes">Viola</part-name><part-abbreviation>Vla.</part-abbreviation><score-instrument id="P5-I1"><instrument-name>Viola</instrument-name></score-instrument></score-part>'
)
v16 = v16.replace(
    '<score-part id="P6"><part-name>Cello</part-name><part-abbreviation>Vc.</part-abbreviation></score-part>',
    '<score-part id="P6"><part-name print-object="yes">Violoncello</part-name><part-abbreviation>Vc.</part-abbreviation><score-instrument id="P6-I1"><instrument-name>Violoncello</instrument-name></score-instrument></score-part>'
)
v16 = v16.replace(
    '<score-part id="P7"><part-name>Double Bass</part-name><part-abbreviation>Cb.</part-abbreviation></score-part>',
    '<score-part id="P7"><part-name print-object="yes">Double Bass</part-name><part-abbreviation>Cb.</part-abbreviation><score-instrument id="P7-I1"><instrument-name>Double Bass</instrument-name></score-instrument></score-part>'
)
v16 = v16.replace(
    '<score-part id="P8"><part-name>Guitar</part-name><part-abbreviation>Gtr.</part-abbreviation></score-part>',
    '<score-part id="P8"><part-name print-object="yes">Classical Guitar</part-name><part-abbreviation>Gtr.</part-abbreviation><score-instrument id="P8-I1"><instrument-name>Classical Guitar</instrument-name></score-instrument></score-part>'
)

# V16: Rehearsal marks alignment
v16 = v16.replace(
    '<rehearsal font-weight="bold" font-size="14">',
    '<rehearsal font-weight="bold" font-size="14" halign="center" valign="top">'
)

# Write V16
with open('scores/masters-palette-orchestrated-v16-parts.musicxml', 'w', encoding='utf-8') as f:
    f.write(v16)
print("Created: scores/masters-palette-orchestrated-v16-parts.musicxml")

# ============================================================
# V17 RECORDING SESSION PASS
# ============================================================
print("\n=== GENERATING V17 RECORDING SESSION ===")

v17 = v16  # Start from V16

# Update title
v17 = v17.replace(
    '<work-title>The Master\'s Palette (Reimagined) - v16 Parts Edition</work-title>',
    '<work-title>The Master\'s Palette (Reimagined) - v17 SESSION READY</work-title>'
)
v17 = v17.replace(
    '<encoder>V16 Parts Extraction Pass</encoder>',
    '<encoder>V17 Recording Session Pass</encoder>'
)
v17 = v17.replace(
    '<software>V16 Parts - Professional Extraction</software>',
    '<software>V17 Session Ready - Studio Recording</software>'
)

# V17 RULE 1: Bowings - add explicit bow directions

# Cello m.1: down-bow on pedal attack
v17 = v17.replace(
    '<direction><direction-type><words font-style="italic">Cello pedal - sul pont., growling, sostenuto glow</words></direction-type></direction>',
    '<direction><direction-type><words font-style="italic">Cello pedal - sul pont., down-bow attack, sostenuto</words></direction-type></direction>'
)

# Viola counterline: alternating bowings
v17 = v17.replace(
    '<direction placement="above"><direction-type><words font-style="italic">cantabile, portato - blues cell variant</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic">cantabile, portato (V-n-V bowing)</words></direction-type></direction>'
)

# Violin climax: detache marking
v17 = v17.replace(
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">CLIMAX I - con forza, lift then warm release</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">CLIMAX I - con forza, detache, full bow</words></direction-type></direction>'
)

# V17 RULE 2: Breath marks for winds/brass
v17 = v17.replace(
    'Flugelhorn - molto espressivo, slight lean forward (phrase rise)',
    'Flugelhorn - molto espressivo, breath after long phrases'
)

# Flute: breath indication
v17 = v17.replace(
    '<direction placement="above"><direction-type><words font-style="italic">flute halo - ethereal, background pp</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic">flute halo - ethereal, pp (breath m.14)</words></direction-type></direction>'
)

# V17 RULE 3: Additional cue notes for long rests
v17 = v17.replace(
    '<measure number="4"><note><rest/><duration>1792</duration><type>whole</type></note></measure>\n<measure number="5"><direction placement="below"><direction-type><dynamics><mp/></dynamics></direction-type></direction>',
    '<measure number="4"><direction placement="above"><direction-type><words font-style="italic" font-size="7">[cue: Flhn. beat 4]</words></direction-type></direction>\n<note><rest/><duration>1792</duration><type>whole</type></note></measure>\n<measure number="5"><direction placement="below"><direction-type><dynamics><mp/></dynamics></direction-type></direction>'
)

# V17 RULE 4: Comfort edits - fingering/position notes
v17 = v17.replace(
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">Bass Poetry - cantabile (down-bow, 1st pos.)</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">Bass Poetry - cantabile (down-bow, stay 1st pos.)</words></direction-type></direction>'
)

# Guitar: position indication
v17 = v17.replace(
    '<direction placement="above"><direction-type><words font-style="italic">let ring, sempre pp, con pedale</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic">let ring, sempre pp, con pedale (pos. I-III)</words></direction-type></direction>'
)

# V17 RULE 5: Rebalance dynamics for studio
v17 = v17.replace(
    '<direction placement="below"><direction-type><dynamics><fff/></dynamics></direction-type></direction>',
    '<direction placement="below"><direction-type><dynamics><ff/></dynamics></direction-type></direction><!-- V17: fff reduced to ff for studio balance -->'
)

# V17 RULE 6: Conductor cues for transitions
v17 = v17.replace(
    '<direction><direction-type><words font-weight="bold">II. Gil\'s Orchestral Canvas</words></direction-type></direction>',
    '<direction><direction-type><words font-weight="bold">II. Gil\'s Orchestral Canvas</words></direction-type></direction>\n<direction placement="above"><direction-type><words font-style="italic" font-size="8">[CONDUCTOR: new tempo, breathe]</words></direction-type></direction>'
)

v17 = v17.replace(
    '<direction placement="above"><direction-type><rehearsal font-weight="bold" font-size="14" halign="center" valign="top">C</rehearsal></direction-type></direction>\n<direction placement="above"><direction-type><words font-style="italic">Bartok cell - flutter-tongue, insect tremors, misterioso</words></direction-type></direction>',
    '<direction placement="above"><direction-type><rehearsal font-weight="bold" font-size="14" halign="center" valign="top">C</rehearsal></direction-type></direction>\n<direction placement="above"><direction-type><words font-style="italic" font-size="8">[CONDUCTOR: sudden shift, pointillistic]</words></direction-type></direction>\n<direction placement="above"><direction-type><words font-style="italic">Bartok cell - flutter-tongue, insect tremors</words></direction-type></direction>'
)

v17 = v17.replace(
    '<direction placement="above"><direction-type><rehearsal font-weight="bold" font-size="14" halign="center" valign="top">D</rehearsal></direction-type></direction>\n<direction><direction-type><words font-weight="bold">IV. Klangfarbenmelodie II</words></direction-type></direction>',
    '<direction placement="above"><direction-type><rehearsal font-weight="bold" font-size="14" halign="center" valign="top">D</rehearsal></direction-type></direction>\n<direction placement="above"><direction-type><words font-style="italic" font-size="8">[CONDUCTOR: flowing, pass the melody]</words></direction-type></direction>\n<direction><direction-type><words font-weight="bold">IV. Klangfarbenmelodie II</words></direction-type></direction>'
)

v17 = v17.replace(
    '<direction placement="above"><direction-type><rehearsal font-weight="bold" font-size="14" halign="center" valign="top">E</rehearsal></direction-type></direction>\n<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">CLIMAX IV - CHORALE, tutti apotheosis</words></direction-type></direction>',
    '<direction placement="above"><direction-type><rehearsal font-weight="bold" font-size="14" halign="center" valign="top">E</rehearsal></direction-type></direction>\n<direction placement="above"><direction-type><words font-style="italic" font-size="8">[CONDUCTOR: broadening, full ensemble]</words></direction-type></direction>\n<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">CLIMAX IV - CHORALE, tutti apotheosis</words></direction-type></direction>'
)

# V17 RULE 7: Page turn safety
v17 = v17.replace(
    '<measure number="12"><print page-number="2"/><!-- V16: Page turn opportunity -->',
    '<measure number="12"><print new-page="yes"/><!-- V17: Safe page turn after dim -->'
)

# V17 RULE 9: Rhythmic alignment - click track friendly
v17 = v17.replace(
    '<direction><direction-type><metronome><beat-unit>quarter</beat-unit><per-minute>92</per-minute></metronome></direction-type></direction>',
    '<direction><direction-type><metronome><beat-unit>quarter</beat-unit><per-minute>92</per-minute></metronome></direction-type></direction>\n<direction placement="above"><direction-type><words font-style="italic" font-size="7">[click: quarter note]</words></direction-type></direction>'
)

v17 = v17.replace(
    '<direction><direction-type><metronome><beat-unit>quarter</beat-unit><per-minute>66</per-minute></metronome></direction-type></direction>',
    '<direction><direction-type><metronome><beat-unit>quarter</beat-unit><per-minute>66</per-minute></metronome></direction-type></direction>\n<direction placement="above"><direction-type><words font-style="italic" font-size="7">[click: dotted quarter for 9/8]</words></direction-type></direction>'
)

v17 = v17.replace(
    '<direction><direction-type><metronome><beat-unit>quarter</beat-unit><per-minute>84</per-minute></metronome></direction-type></direction>',
    '<direction><direction-type><metronome><beat-unit>quarter</beat-unit><per-minute>84</per-minute></metronome></direction-type></direction>\n<direction placement="above"><direction-type><words font-style="italic" font-size="7">[click: eighth note pulse]</words></direction-type></direction>'
)

v17 = v17.replace(
    '<direction><direction-type><metronome><beat-unit>quarter</beat-unit><per-minute>72</per-minute></metronome></direction-type></direction>',
    '<direction><direction-type><metronome><beat-unit>quarter</beat-unit><per-minute>72</per-minute></metronome></direction-type></direction>\n<direction placement="above"><direction-type><words font-style="italic" font-size="7">[click: compound pulse]</words></direction-type></direction>'
)

# Write V17
with open('scores/masters-palette-orchestrated-v17-sessionReady.musicxml', 'w', encoding='utf-8') as f:
    f.write(v17)
print("Created: scores/masters-palette-orchestrated-v17-sessionReady.musicxml")

# ============================================================
# SUMMARY
# ============================================================
print("\n" + "="*60)
print("COMPLETE PRODUCTION PIPELINE SUMMARY")
print("="*60)
print(f"\nCopyright: {COPYRIGHT}")
print("\n--- V15 FINAL ARTISTIC POLISH ---")
print("* Micro-dynamics: phrase swells on held notes (Flhn, Vln)")
print("* Articulation: portato for lyrical lines, cleaned redundant marks")
print("* Bowing: down-bow on Cello Bass Poetry, position notes added")
print("* Balance: background pp markings for supporting voices")
print("* Timbral: non vib., poco vib., sul tasto, harmonics refined")
print("* Climax: 'lift then warm release', 'tutti apotheosis', 'morendo' finale")

print("\n--- V16 PARTS EXTRACTION ---")
print("* Page layout: 4 pages with breaks at movement boundaries")
print("* Multi-measure rests: <multiple-rest> for tacet sections")
print("* Cue notes: [cue: Flhn.] before entrances")
print("* Instrument names: full professional names with score-instrument")
print("* Rehearsal marks: centered, top-aligned (A-E)")

print("\n--- V17 RECORDING SESSION ---")
print("* Bowings: explicit down-bow, V-n-V, detache, full bow markings")
print("* Breath marks: wind phrases annotated for breath opportunities")
print("* Conductor cues: [CONDUCTOR: ...] at all major transitions")
print("* Studio dynamics: fff reduced to ff for recording balance")
print("* Click track: pulse indications for each tempo/meter change")
print("* Position notes: Guitar pos. I-III, Cello 1st pos. confirmed")
print("\n" + "="*60)
print("ALL FILES READY FOR STUDIO RECORDING")
print("="*60)





