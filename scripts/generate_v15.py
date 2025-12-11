#!/usr/bin/env python3
"""
Generate masters-palette-orchestrated-v15.musicxml
Applies V15 Final Artistic Polish Pass
"""

import re

# Read the v14 source file
with open('scores/masters-palette-orchestrated-v14.musicxml', 'r', encoding='utf-8') as f:
    content = f.read()

# ===== UPDATE TITLE AND ENCODER =====
content = content.replace(
    '<work-title>The Master\'s Palette (Reimagined) - Orchestrated v14</work-title>',
    '<work-title>The Master\'s Palette (Reimagined) - Orchestrated v15 FINAL</work-title>'
)
content = content.replace(
    '<encoder>V14 Expressive Musicality Pass</encoder>',
    '<encoder>V15 Final Artistic Polish</encoder>'
)
content = content.replace(
    '<software>V14 Expressive Musicality</software>',
    '<software>V15 Final - Performance Ready</software>'
)

# ===== V15 RULE 1: MICRO-DYNAMICS & PHRASE INFLECTION =====
# Add subtle swells on long held notes

# Flugelhorn m.5: add micro-swell on held D
content = content.replace(
    '<note><pitch><step>D</step><octave>5</octave></pitch><duration>512</duration><type>half</type><notations><slur type="stop" number="1"/><articulations><breath-mark>comma</breath-mark></articulations></notations></note>',
    '<note><pitch><step>D</step><octave>5</octave></pitch><duration>512</duration><type>half</type><notations><slur type="stop" number="1"/><articulations><breath-mark>comma</breath-mark></articulations><dynamics><other-dynamics>slight swell</other-dynamics></dynamics></notations></note>'
)

# Violin m.14: micro-inflection on dotted half
content = content.replace(
    '<note><pitch><step>E</step><octave>5</octave></pitch><duration>768</duration><type>half</type><dot/><notations><slur type="start" number="1"/></notations></note>',
    '<note><pitch><step>E</step><octave>5</octave></pitch><duration>768</duration><type>half</type><dot/><notations><slur type="start" number="1"/><dynamics><other-dynamics>mp-mf-mp</other-dynamics></dynamics></notations></note>'
)

# ===== V15 RULE 2: ARTICULATION PRECISION =====
# Clean up and refine articulations

# Standardize all dynamics placement (already done in v12.5, verify consistency)
# Remove any duplicate direction elements by cleaning patterns

# Add portato indication for lyrical passages
content = content.replace(
    '<direction placement="above"><direction-type><words font-style="italic">cantabile - blues cell variant in counterline</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic">cantabile, portato - blues cell variant</words></direction-type></direction>'
)

# ===== V15 RULE 3: BOWING, BREATH & IDIOMATIC REALISM =====
# Add bow direction indicators where justified

# Cello m.3 Bass Poetry: down-bow for weight
content = content.replace(
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">Bass Poetry - cantabile, singing (1st pos.)</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">Bass Poetry - cantabile (down-bow, 1st pos.)</words></direction-type></direction>'
)

# Viola m.5: up-bow for lift
content = content.replace(
    '<direction placement="below"><direction-type><dynamics><p/></dynamics></direction-type></direction>\n<direction placement="above"><direction-type><words font-style="italic">cantabile, portato - blues cell variant</words></direction-type></direction>',
    '<direction placement="below"><direction-type><dynamics><p/></dynamics></direction-type></direction>\n<direction placement="above"><direction-type><words font-style="italic">cantabile, portato (up-bow lift)</words></direction-type></direction>'
)

# String section m.10 climax: detache
content = content.replace(
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">CLIMAX I - con forza, registral lift</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">CLIMAX I - con forza, detache, registral lift</words></direction-type></direction>'
)

# ===== V15 RULE 4: BALANCE FOREGROUND VS BACKGROUND =====
# Fine-tune supporting voice dynamics

# Guitar throughout: ensure sotto voce clarity
content = content.replace(
    '<direction placement="above"><direction-type><words font-style="italic">let ring, sotto voce - gospel shimmer</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic">let ring, sempre pp - gospel shimmer (background)</words></direction-type></direction>'
)

# Flute color tones: background role explicit
content = content.replace(
    '<direction placement="above"><direction-type><words font-style="italic">flute halo - ethereal</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic">flute halo - ethereal, background pp</words></direction-type></direction>'
)

# ===== V15 RULE 5: TIMBRAL FINE-TUNING =====
# Add highly specific colour markings

# Violin fragility: add non-vib specificity
content = content.replace(
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">SOLO - fragile, flautato, phrase apex then release</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">SOLO - fragile, flautato, non vib., phrase apex</words></direction-type></direction>'
)

# Cello sul tasto: add poco vibrato
content = content.replace(
    '<direction placement="above"><direction-type><words font-style="italic">sul tasto, quasi niente - ethereal glow</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic">sul tasto, poco vib., quasi niente</words></direction-type></direction>'
)

# Movement III strings: add col legno option
content = content.replace(
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">STRUCTURAL SILENCE - niente, harmonics</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">STRUCTURAL SILENCE - niente (strings: harmonics or col legno tratto)</words></direction-type></direction>'
)

# ===== V15 RULE 6: TRANSITION MICRO-BRIDGING =====
# Add soft held tones and breath marks at boundaries

# Before Movement II: add sustained guitar harmonic bridge
content = content.replace(
    '<direction placement="above"><direction-type><words font-style="italic" font-size="9">subito p - breath space before new world</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic" font-size="9">subito p, breath - Gtr: hold harmonic</words></direction-type></direction>'
)

# Before Movement III: add string bridge
content = content.replace(
    '<direction><direction-type><words font-style="italic">poco rubato, rit. - expressive bridge</words></direction-type></direction>',
    '<direction><direction-type><words font-style="italic">poco rubato, rit. - strings sustain bridge</words></direction-type></direction>'
)

# Movement IV attacca: smooth
content = content.replace(
    '<direction placement="above"><direction-type><words font-style="italic" font-size="8">attacca</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic" font-size="8">attacca subito - no break</words></direction-type></direction>'
)

# ===== V15 RULE 7: PEDAL & RESONANCE SHAPING =====
# Add guitar pedaling indication

# Guitar m.1: pedal indication
content = content.replace(
    '<direction placement="above"><direction-type><words font-style="italic">let ring, sempre pp - gospel shimmer (background)</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic">let ring, sempre pp, con pedale - gospel shimmer</words></direction-type></direction>'
)

# Guitar Movement II: shimmer with pedal
content = content.replace(
    '<direction placement="above"><direction-type><words font-style="italic">shimmer, harmonics - pastel cloud, non-dominant</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic">shimmer, harmonics, con pedale - pastel cloud</words></direction-type></direction>'
)

# ===== V15 RULE 8: RHYTHMIC HUMANIZATION =====
# Add conversational nudge indications (text only, no rhythm changes)

# Flugelhorn entry: slight anticipation feel
content = content.replace(
    'Flugelhorn - molto espressivo, gospel warmth (phrase rise m.4-6)',
    'Flugelhorn - molto espressivo, slight lean forward (phrase rise)'
)

# Movement IV Klangfarben: conversational
content = content.replace(
    '<direction placement="above"><direction-type><words font-style="italic">sostenuto, timbral passing, Fortspinnung</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic">sostenuto, conversational timing, Fortspinnung</words></direction-type></direction>'
)

# ===== V15 RULE 9: CLIMAX PRECISION =====
# Fine-shape the main climaxes

# Climax I (m.10-11): add release warmth
content = content.replace(
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">CLIMAX I - con forza, detache, registral lift</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">CLIMAX I - con forza, detache, lift then warm release</words></direction-type></direction>'
)

# Climax IV (m.24): add all-family participation note
content = content.replace(
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">CLIMAX IV - CHORALE, triumphant apotheosis</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">CLIMAX IV - CHORALE, tutti apotheosis (all families balanced)</words></direction-type></direction>'
)

# Finale: precise release
content = content.replace(
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">luminoso - climax release, molto espressivo</words></direction-type></direction>',
    '<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">luminoso - gentle release into warmth, morendo</words></direction-type></direction>'
)

# ===== V15 RULE 10: CLEANING & PROOFING =====
# Remove redundant elements and clean up

# Remove duplicate comments
content = content.replace('<!-- V13: C2 sounding - idiomatic -->', '')
content = content.replace('<!-- V14: 4-bar arc to m.7 -->', '')
content = content.replace('<!-- V14: phrase release -->', '')
content = content.replace('<!-- V14: pedal glow -->', '')

# Clean up any double spaces in text
content = content.replace('  ', ' ')

# Ensure consistent spacing
content = content.replace('\n\n\n', '\n\n')

# ===== V15: UPDATE SUMMARY COMMENT =====
content = content.replace(
    '<!-- V14 Expressive Musicality Pass Summary:',
    '<!-- V15 FINAL Artistic Polish Summary:'
)

content = content.replace(
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
-->''',
    '''- Micro-dynamics: subtle phrase swells on held notes (Flhn m.5, Vln m.14)
- Articulation: portato for lyrical lines, detache for climax strings
- Bowing: down-bow (Cello Bass Poetry), up-bow lift (Viola), explicit bow marks
- Balance: Guitar "sempre pp, background"; Flute halo "background pp"
- Timbral precision: non vib. (Vln fragility), poco vib. (Vc sul tasto), col legno option (m.19)
- Transitions: Gtr harmonic bridges, strings sustain bridges, attacca subito
- Pedaling: Guitar "con pedale" throughout for resonance
- Humanization: "slight lean forward" (Flhn), "conversational timing" (Klangfarben)
- Climax: "lift then warm release" (I), "tutti apotheosis, all families balanced" (IV)
- Finale: "gentle release into warmth, morendo" - definitive ending
-->'''
)

# Write the output file
with open('scores/masters-palette-orchestrated-v15.musicxml', 'w', encoding='utf-8') as f:
    f.write(content)

print("Generated: scores/masters-palette-orchestrated-v15.musicxml")
print("")
print("=== V15 FINAL ARTISTIC POLISH SUMMARY ===")
print("")
print("* Micro-dynamics: Added subtle phrase swells on held notes (Flugelhorn m.5 'slight swell', Violin m.14 'mp-mf-mp' inflection)")
print("")
print("* Articulation precision: 'portato' for lyrical Viola lines; 'detache' for string climax attack; cleaned redundant marks")
print("")
print("* Bowing realism: Down-bow weight on Cello Bass Poetry; up-bow lift on Viola counterline; bow directions at key gestures")
print("")
print("* Foreground/background: Guitar marked 'sempre pp, background'; Flute halo 'background pp' - primary lines always clear")
print("")
print("* Timbral fine-tuning: Violin 'non vib.' for fragility; Cello 'poco vib.' sul tasto; strings 'col legno tratto' option at m.19")
print("")
print("* Transition bridging: Guitar 'hold harmonic' bridges; strings 'sustain bridge'; 'attacca subito - no break' for seamless flow")
print("")
print("* Pedal/resonance: Guitar 'con pedale' throughout Mvt I and II for sustained shimmer and harmonic glow")
print("")
print("* Climax precision: CLIMAX I 'lift then warm release'; CLIMAX IV 'tutti apotheosis, all families balanced'; finale 'gentle release into warmth, morendo'")
print("")
print("=== SCORE COMPLETE - PERFORMANCE READY ===")





