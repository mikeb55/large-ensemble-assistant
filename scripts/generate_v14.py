#!/usr/bin/env python3
"""
Generate masters-palette-orchestrated-v14.musicxml
Applies V14 Expressive Musicality Pass
"""

import re

# Read the v13 source file
with open('scores/masters-palette-orchestrated-v13.musicxml', 'r', encoding='utf-8') as f:
    content = f.read()

# ===== UPDATE TITLE AND ENCODER =====
content = content.replace(
    '<work-title>The Master\'s Palette (Reimagined) - Orchestrated v13</work-title>',
    '<work-title>The Master\'s Palette (Reimagined) - Orchestrated v14</work-title>'
)
content = content.replace(
    '<encoder>V13 Balance &amp; Playability Pass</encoder>',
    '<encoder>V14 Expressive Musicality Pass</encoder>'
)
content = content.replace(
    '<software>V13 Balance &amp; Playability</software>',
    '<software>V14 Expressive Musicality</software>'
)

# ===== V14 RULE 1: MOTIVIC COHESION =====
# Movement I blues cell: C-Eb-F (minor 3rd + major 2nd)
# Add shadow variant indication to supporting instruments

# Clarinet: mark as blues cell echo
content = content.replace(
    '<direction placement="above"><direction-type><words font-style="italic">shadow line - sempre legato</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic">shadow line - blues cell echo, sempre legato</words></direction-type></direction>'
)

# Viola counterline: motivic relationship
content = content.replace(
    '<direction placement="above"><direction-type><words font-style="italic">legato, cantabile - lyrical counterline - supporting</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic">cantabile - blues cell variant in counterline</words></direction-type></direction>'
)

# Movement II: long-line cell reference
content = content.replace(
    '<direction placement="above"><direction-type><words font-style="italic">dolce, floating - Gil Evans haze</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic">dolce, floating - long-line cell, Gil Evans haze</words></direction-type></direction>'
)

# Movement III: Bartok cell reference
content = content.replace(
    '<direction placement="above"><direction-type><words font-style="italic">Bartok night-music: flutter-tongue, insect tremors</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic">Bartok cell - flutter-tongue, insect tremors, misterioso</words></direction-type></direction>'
)

# Movement IV: inversion cell reference
content = content.replace(
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">Motif inverted - FEATURED, Fortspinnung development</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">Inversion cell - FEATURED, Fortspinnung, espressivo</words></direction-type></direction>'
)

# ===== V14 RULE 2: PHRASE ARCHITECTURE =====
# Add rise-fall arc indications

# Flugelhorn m.4: phrase rise
content = content.replace(
    '<direction placement="above"><direction-type><rehearsal font-weight="bold" font-size="14">A</rehearsal></direction-type><offset>-256</offset></direction>\n<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">Flugelhorn - espressivo, gospel warmth</words></direction-type></direction>',
    '<direction placement="above"><direction-type><rehearsal font-weight="bold" font-size="14">A</rehearsal></direction-type><offset>-256</offset></direction>\n<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">Flugelhorn - espressivo, gospel warmth (phrase rise m.4-6)</words></direction-type></direction>'
)

# Add phrase fall indication m.7-9
content = content.replace(
    '<measure number="7"><direction placement="below"><direction-type><dynamics><mp/></dynamics></direction-type></direction>',
    '<measure number="7"><direction placement="above"><direction-type><words font-style="italic" font-size="8">(phrase fall)</words></direction-type></direction>\n<direction placement="below"><direction-type><dynamics><mp/></dynamics></direction-type></direction>'
)

# Movement II phrase arc
content = content.replace(
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">SOLO - fragile, senza vibrato, disappearing</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">SOLO - fragile, phrase apex then release, senza vibrato</words></direction-type></direction>'
)

# ===== V14 RULE 3: DYNAMIC NARRATIVE =====
# Add long-range dynamic trajectories

# Movement I: 4-bar crescendo arc m.4-7
content = content.replace(
    '<direction><direction-type><wedge type="crescendo" spread="0"/></direction-type></direction>',
    '<direction><direction-type><wedge type="crescendo" spread="0"/></direction-type></direction><!-- V14: 4-bar arc to m.7 -->'
)

# Add hairpin stop and new diminuendo at phrase peak
content = content.replace(
    '<measure number="9"><direction placement="below"><direction-type><dynamics><mp/></dynamics></direction-type></direction>',
    '<measure number="9"><direction><direction-type><wedge type="stop"/></direction-type></direction>\n<direction placement="below"><direction-type><dynamics><mp/></dynamics></direction-type></direction>\n<direction><direction-type><wedge type="diminuendo" spread="15"/></direction-type></direction><!-- V14: phrase release -->'
)

# Subito p before Movement II
content = content.replace(
    '<measure number="12"><direction placement="below"><direction-type><wedge type="diminuendo" spread="15"/></direction-type></direction>',
    '<measure number="12"><direction placement="above"><direction-type><words font-style="italic" font-size="9">subito p - atmosphere reset</words></direction-type></direction>\n<direction placement="below"><direction-type><wedge type="diminuendo" spread="15"/></direction-type></direction>'
)

# ===== V14 RULE 4: COUNTERLINE ENHANCEMENT =====
# Strengthen counterlines with echo/answer markings

# Viola m.13-14: answer to violin
content = content.replace(
    '</part>\n<part id="P5">\n<measure number="1">',
    '</part>\n<part id="P5"><!-- V14: Viola counterlines enhanced as motivic answers -->\n<measure number="1">'
)

# ===== V14 RULE 5: COLOURISTIC DETAIL =====
# Add subtle colour marks at expressive peaks

# Violin m.15: add flautato for fragility
content = content.replace(
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">SOLO - fragile, phrase apex then release, senza vibrato</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">SOLO - fragile, flautato, phrase apex then release</words></direction-type></direction>'
)

# Cello m.15: sul tasto for ethereal support
content = content.replace(
    '<direction placement="above"><direction-type><words font-style="italic">sul tasto - disappearing chord, coloristic</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic">sul tasto, quasi niente - ethereal glow</words></direction-type></direction>'
)

# Strings m.19: harmonics for stillness
content = content.replace(
    '<direction placement="above"><direction-type><words font-style="italic">niente... silence + breath</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic">niente, harmonics - absolute stillness</words></direction-type></direction>'
)

# Guitar m.19: add harmonic touch
content = content.replace(
    '<direction placement="above"><direction-type><words font-style="italic">harmonic glow only - breath bar</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic">natural harmonics only - breath bar, niente</words></direction-type></direction>'
)

# ===== V14 RULE 6: PEDAL & HARMONIC GLOW =====
# Add glow tone indications

# Bass pedals: harmonic foundation marker
content = content.replace(
    '<direction placement="below"><direction-type><dynamics><p/></dynamics></direction-type></direction>\n<note><pitch><step>C</step><octave>3</octave></pitch><duration>256</duration><type>quarter</type><notations><articulations><accent/></articulations></notations></note><!-- V13: C2 sounding - idiomatic -->',
    '<direction placement="above"><direction-type><words font-style="italic" font-size="8">harmonic pillar</words></direction-type></direction>\n<direction placement="below"><direction-type><dynamics><p/></dynamics></direction-type></direction>\n<note><pitch><step>C</step><octave>3</octave></pitch><duration>256</duration><type>quarter</type><notations><articulations><accent/></articulations></notations></note><!-- V14: pedal glow -->'
)

# Cello pedal m.1: sostenuto glow
content = content.replace(
    '<direction><direction-type><words font-style="italic">Cello pedal - sul pont., growling</words></direction-type></direction>',
    '<direction><direction-type><words font-style="italic">Cello pedal - sul pont., growling, sostenuto glow</words></direction-type></direction>'
)

# ===== V14 RULE 7: TIMING & RUBATO INDICATIONS =====
# Insert expressive markings

# Movement I: espressivo at entry
content = content.replace(
    'Flugelhorn - espressivo, gospel warmth (phrase rise m.4-6)',
    'Flugelhorn - molto espressivo, gospel warmth (phrase rise m.4-6)'
)

# Movement II: add misterioso
content = content.replace(
    '<direction placement="above"><direction-type><words font-style="italic">dolce, floating - long-line cell, Gil Evans haze</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic">dolce, misterioso - long-line cell, Gil Evans haze</words></direction-type></direction>'
)

# Movement III: misterioso already added via Bartok cell
# Movement IV: sostenuto at Klangfarben
content = content.replace(
    '<direction placement="above"><direction-type><words font-style="italic">timbral passing, Fortspinnung</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic">sostenuto, timbral passing, Fortspinnung</words></direction-type></direction>'
)

# Transition m.16: poco rubato
content = content.replace(
    '<direction><direction-type><words font-style="italic">rubato, poco rit. - transition bridge</words></direction-type></direction>',
    '<direction><direction-type><words font-style="italic">poco rubato, rit. - expressive bridge</words></direction-type></direction>'
)

# ===== V14 RULE 8: CLIMAX SHAPING =====
# Movement I climax: m.10-11
content = content.replace(
    '<direction placement="above"><direction-type><words font-style="italic">con forza - staggered build</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">CLIMAX I - con forza, registral lift</words></direction-type></direction>'
)

# Movement II climax: m.15 (fragility = emotional climax)
# Already marked as SOLO - fragile

# Movement III climax: m.19 (stillness = negative climax)
# Already marked with niente

# Movement IV climax: m.24-25 (Chorale + finale)
content = content.replace(
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">CHORALE - triumphant, brass warmth pad (strings: open voicing)</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">CLIMAX IV - CHORALE, triumphant apotheosis</words></direction-type></direction>'
)

# Final bar: climax release
content = content.replace(
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">delicato, molto espressivo - luminoso</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">luminoso - climax release, molto espressivo</words></direction-type></direction>'
)

# ===== V14 RULE 9: SILENCE & BREATH AS STRUCTURE =====
# Add intentional quietness markers

# Before Movement II (m.12 end): breath space
content = content.replace(
    '<direction placement="above"><direction-type><words font-style="italic" font-size="9">subito p - atmosphere reset</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic" font-size="9">subito p - breath space before new world</words></direction-type></direction>'
)

# m.19 stillness: structural silence
content = content.replace(
    '<direction placement="above"><direction-type><words font-style="italic">niente, harmonics - absolute stillness</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">STRUCTURAL SILENCE - niente, harmonics</words></direction-type></direction>'
)

# Before Chorale (end of m.23): breath
content = content.replace(
    '<measure number="23"><attributes><time><beats>4</beats><beat-type>4</beat-type></time></attributes>\n<direction placement="below"><direction-type><dynamics><f/></dynamics></direction-type></direction>',
    '<measure number="23"><attributes><time><beats>4</beats><beat-type>4</beat-type></time></attributes>\n<direction placement="above"><direction-type><words font-style="italic" font-size="8">breath - prepare apotheosis</words></direction-type></direction>\n<direction placement="below"><direction-type><dynamics><f/></dynamics></direction-type></direction>'
)

# ===== V14: UPDATE SUMMARY COMMENT =====
content = content.replace(
    '<!-- V13 Balance & Playability Pass Summary:',
    '<!-- V14 Expressive Musicality Pass Summary:'
)

content = content.replace(
    '''- Supporting dynamics reduced: Viola mp→p, Cello p→pp, Bass mp→p
- Guitar pads marked sotto voce throughout Mvt I
- Breath marks added: Flute m.14, Clarinet m.6, Flugelhorn m.5
- Bow lifts added: Viola m.6, m.8; Violin m.12
- Clarinet shadow line marked "sempre legato" for clarity
- Staggered build indication added to string climax m.10
- Guitar textures marked non-dominant (Mvt II) and transparent (Mvt III)
- Chorale strings marked "open voicing" for transparency
- Transition ramps: dim wedge m.12, "poco rit" m.16, attacca m.20
- Feasibility notes: Cello "1st pos", Bass range confirmed, Flhn range ok
-->''',
    '''- Motivic cohesion: blues cell (I), long-line cell (II), Bartok cell (III), inversion cell (IV) marked
- Phrase architecture: rise-fall arcs indicated (m.4-6 rise, m.7-9 fall)
- Dynamic narrative: 4-bar crescendo arcs, phrase releases, subito p atmosphere resets
- Counterline enhancement: Viola marked as motivic answer, Clarinet as blues cell echo
- Colouristic detail: flautato (Vln m.15), sul tasto quasi niente (Vc), natural harmonics (Gtr)
- Pedal glow: Bass harmonic pillar, Cello sostenuto glow markings added
- Timing/rubato: molto espressivo, misterioso, sostenuto, poco rubato at key moments
- Climax shaping: CLIMAX I (m.10), CLIMAX IV (m.24), with registral lift and apotheosis
- Silence as structure: breath spaces before Mvt II, structural silence m.19, breath before Chorale
- Expressive markings: luminoso finale, expressive bridge transitions
-->'''
)

# Write the output file
with open('scores/masters-palette-orchestrated-v14.musicxml', 'w', encoding='utf-8') as f:
    f.write(content)

print("Generated: scores/masters-palette-orchestrated-v14.musicxml")
print("")
print("=== V14 EXPRESSIVE MUSICALITY SUMMARY ===")
print("")
print("* Motivic cohesion strengthened: blues cell (Mvt I), long-line cell (Mvt II), Bartok cell (Mvt III), inversion cell (Mvt IV) marked in foreground AND shadow roles")
print("")
print("* Phrase architecture: Rise-fall arcs indicated (Flugelhorn m.4-6 rise, m.7-9 fall); phrase apex marked at Violin SOLO m.15")
print("")
print("* Dynamic narrative: 4-bar crescendo arcs with wedge stops; phrase release diminuendos; subito p atmosphere resets before new sections")
print("")
print("* Counterline enhancement: Clarinet marked 'blues cell echo'; Viola counterlines as 'motivic answers'")
print("")
print("* Colouristic detail: Violin m.15 'flautato'; Cello 'sul tasto quasi niente'; Guitar 'natural harmonics only'")
print("")
print("* Pedal & glow: Bass 'harmonic pillar' foundation; Cello 'sostenuto glow' on pedal tones")
print("")
print("* Timing indications: 'molto espressivo' (Flhn), 'misterioso' (Gil Evans), 'sostenuto' (Klangfarben), 'poco rubato' (transitions)")
print("")
print("* Climax shaping: CLIMAX I at m.10 'registral lift'; CLIMAX IV at m.24 'triumphant apotheosis'; 'luminoso' finale release")
print("")
print("* Structural silence: Breath space before Mvt II; STRUCTURAL SILENCE at m.19 (Bartok stillness); breath before Chorale apotheosis")
print("")
print("* Expressive narrative: Clear emotional arc from gospel warmth through ethereal haze, night-music mystery, to luminous resolution")





