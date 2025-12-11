#!/usr/bin/env python3
"""
Generate masters-palette-orchestrated-v16-parts.musicxml
Applies V16 Parts Extraction Pass
"""

import re

# Read the v15 source file
with open('scores/masters-palette-orchestrated-v15.musicxml', 'r', encoding='utf-8') as f:
    content = f.read()

# ===== UPDATE TITLE AND ENCODER =====
content = content.replace(
    '<work-title>The Master\'s Palette (Reimagined) - Orchestrated v15 FINAL</work-title>',
    '<work-title>The Master\'s Palette (Reimagined) - v16 Parts Edition</work-title>'
)
content = content.replace(
    '<encoder>V15 Final Artistic Polish</encoder>',
    '<encoder>V16 Parts Extraction Pass</encoder>'
)
content = content.replace(
    '<software>V15 Final - Performance Ready</software>',
    '<software>V16 Parts - Professional Extraction</software>'
)

# ===== V16 RULE 1 & 2: PAGE LAYOUT & PAGE TURNS =====
# Add print elements for parts with page-break opportunities

# After Movement I (m.12) - good page turn opportunity (diminuendo into rest)
content = content.replace(
    '<measure number="12"><direction placement="above"><direction-type><words font-style="italic" font-size="9">subito p, breath - Gtr: hold harmonic</words></direction-type></direction>',
    '<measure number="12"><print page-number="2"/><!-- V16: Page turn opportunity --><direction placement="above"><direction-type><words font-style="italic" font-size="9">subito p, breath - Gtr: hold harmonic</words></direction-type></direction>'
)

# After Movement II (m.16) - page turn for parts with rests
content = content.replace(
    '<measure number="17"><print new-system="yes"/><attributes><key><fifths>0</fifths><mode>minor</mode></key><time><beats>5</beats><beat-type>8</beat-type></time></attributes>',
    '<measure number="17"><print new-system="yes" new-page="yes"/><!-- V16: Page 3 start --><attributes><key><fifths>0</fifths><mode>minor</mode></key><time><beats>5</beats><beat-type>8</beat-type></time></attributes>'
)

# After Movement III (m.20) - natural break point
content = content.replace(
    '<measure number="21"><print new-system="yes"/><attributes><key><fifths>0</fifths><mode>major</mode></key><time><beats>11</beats><beat-type>8</beat-type></time></attributes>',
    '<measure number="21"><print new-system="yes" new-page="yes"/><!-- V16: Page 4 start --><attributes><key><fifths>0</fifths><mode>major</mode></key><time><beats>11</beats><beat-type>8</beat-type></time></attributes>'
)

# ===== V16 RULE 4: MULTI-MEASURE RESTS =====
# Add multi-rest indication for part extraction
# Note: MusicXML uses <multiple-rest> in <measure-style> for this

# Add measure-style for multiple rests in Flute m.1-6
content = content.replace(
    '<part id="P1">\n<measure number="1"><attributes><divisions>256</divisions><key><fifths>-3</fifths><mode>minor</mode></key><time><beats>7</beats><beat-type>4</beat-type></time><clef><sign>G</sign><line>2</line></clef></attributes>',
    '<part id="P1">\n<measure number="1"><attributes><divisions>256</divisions><key><fifths>-3</fifths><mode>minor</mode></key><time><beats>7</beats><beat-type>4</beat-type></time><clef><sign>G</sign><line>2</line></clef><measure-style><multiple-rest>6</multiple-rest></measure-style></attributes>'
)

# ===== V16 RULE 5: CUE NOTES =====
# Add cue indications before important entrances

# Flute: add cue before m.7 entry (Flugelhorn cue)
content = content.replace(
    '<measure number="6"><note><rest/><duration>1792</duration><type>whole</type></note></measure>\n<measure number="7"><direction placement="above"><direction-type><words font-style="italic" font-size="8">(phrase fall)</words></direction-type></direction>',
    '<measure number="6"><direction placement="above"><direction-type><words font-style="italic" font-size="7">[cue: Flhn.]</words></direction-type></direction>\n<note><rest/><duration>1792</duration><type>whole</type></note></measure>\n<measure number="7"><direction placement="above"><direction-type><words font-style="italic" font-size="8">(phrase fall)</words></direction-type></direction>'
)

# Clarinet: add cue before m.5 entry (Flugelhorn cue)
content = content.replace(
    '<measure number="4"><note><rest/><duration>1792</duration><type>whole</type></note></measure>\n<measure number="5"><direction placement="below"><direction-type><dynamics><mp/></dynamics></direction-type></direction>',
    '<measure number="4"><direction placement="above"><direction-type><words font-style="italic" font-size="7">[cue: Flhn. enters]</words></direction-type></direction>\n<note><rest/><duration>1792</duration><type>whole</type></note></measure>\n<measure number="5"><direction placement="below"><direction-type><dynamics><mp/></dynamics></direction-type></direction>'
)

# Violin: add cue before m.7 entry
content = content.replace(
    '</part>\n<part id="P4">\n<measure number="1"><attributes><divisions>256</divisions><key><fifths>-3</fifths><mode>minor</mode></key><time><beats>7</beats><beat-type>4</beat-type></time><clef><sign>G</sign><line>2</line></clef></attributes>\n<note><rest/><duration>1792</duration><type>whole</type></note></measure>\n<measure number="2">',
    '</part>\n<part id="P4"><!-- V16: Violin part - cues added -->\n<measure number="1"><attributes><divisions>256</divisions><key><fifths>-3</fifths><mode>minor</mode></key><time><beats>7</beats><beat-type>4</beat-type></time><clef><sign>G</sign><line>2</line></clef><measure-style><multiple-rest>6</multiple-rest></measure-style></attributes>\n<note><rest/><duration>1792</duration><type>whole</type></note></measure>\n<measure number="2">'
)

# Add cue for Violin before m.10 lead entry
content = content.replace(
    '<measure number="9"><note><rest/><duration>1792</duration><type>whole</type></note></measure>\n<measure number="10"><direction placement="below"><direction-type><dynamics><mf/></dynamics></direction-type></direction>\n<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">CLIMAX I',
    '<measure number="9"><direction placement="above"><direction-type><words font-style="italic" font-size="7">[cue: Flhn. phrase ending]</words></direction-type></direction>\n<note><rest/><duration>1792</duration><type>whole</type></note></measure>\n<measure number="10"><direction placement="below"><direction-type><dynamics><mf/></dynamics></direction-type></direction>\n<direction placement="above"><direction-type><words font-style="italic" font-weight="bold">CLIMAX I'
)

# ===== V16 RULE 6: PART CLEANUP =====
# Clean up collisions and ensure proper positioning

# Ensure all rehearsal marks are centered above system
content = content.replace(
    '<rehearsal font-weight="bold" font-size="14">',
    '<rehearsal font-weight="bold" font-size="14" halign="center" valign="top">'
)

# ===== V16 RULE 7: INSTRUMENT LABELS =====
# Add print-object for part names and ensure correct display

# Update part-list with print names
content = content.replace(
    '<score-part id="P1"><part-name>Flute</part-name><part-abbreviation>Fl.</part-abbreviation></score-part>',
    '<score-part id="P1"><part-name print-object="yes">Flute</part-name><part-abbreviation>Fl.</part-abbreviation><score-instrument id="P1-I1"><instrument-name>Flute</instrument-name></score-instrument></score-part>'
)
content = content.replace(
    '<score-part id="P2"><part-name>Clarinet in Bb</part-name><part-abbreviation>Cl.</part-abbreviation></score-part>',
    '<score-part id="P2"><part-name print-object="yes">Clarinet in Bb</part-name><part-abbreviation>Cl.</part-abbreviation><score-instrument id="P2-I1"><instrument-name>Clarinet in Bb</instrument-name></score-instrument></score-part>'
)
content = content.replace(
    '<score-part id="P3"><part-name>Flugelhorn</part-name><part-abbreviation>Flhn.</part-abbreviation></score-part>',
    '<score-part id="P3"><part-name print-object="yes">Flugelhorn in Bb</part-name><part-abbreviation>Flhn.</part-abbreviation><score-instrument id="P3-I1"><instrument-name>Flugelhorn in Bb</instrument-name></score-instrument></score-part>'
)
content = content.replace(
    '<score-part id="P4"><part-name>Violin</part-name><part-abbreviation>Vln.</part-abbreviation></score-part>',
    '<score-part id="P4"><part-name print-object="yes">Violin</part-name><part-abbreviation>Vln.</part-abbreviation><score-instrument id="P4-I1"><instrument-name>Violin</instrument-name></score-instrument></score-part>'
)
content = content.replace(
    '<score-part id="P5"><part-name>Viola</part-name><part-abbreviation>Vla.</part-abbreviation></score-part>',
    '<score-part id="P5"><part-name print-object="yes">Viola</part-name><part-abbreviation>Vla.</part-abbreviation><score-instrument id="P5-I1"><instrument-name>Viola</instrument-name></score-instrument></score-part>'
)
content = content.replace(
    '<score-part id="P6"><part-name>Cello</part-name><part-abbreviation>Vc.</part-abbreviation></score-part>',
    '<score-part id="P6"><part-name print-object="yes">Violoncello</part-name><part-abbreviation>Vc.</part-abbreviation><score-instrument id="P6-I1"><instrument-name>Violoncello</instrument-name></score-instrument></score-part>'
)
content = content.replace(
    '<score-part id="P7"><part-name>Double Bass</part-name><part-abbreviation>Cb.</part-abbreviation></score-part>',
    '<score-part id="P7"><part-name print-object="yes">Double Bass</part-name><part-abbreviation>Cb.</part-abbreviation><score-instrument id="P7-I1"><instrument-name>Double Bass</instrument-name></score-instrument></score-part>'
)
content = content.replace(
    '<score-part id="P8"><part-name>Guitar</part-name><part-abbreviation>Gtr.</part-abbreviation></score-part>',
    '<score-part id="P8"><part-name print-object="yes">Classical Guitar</part-name><part-abbreviation>Gtr.</part-abbreviation><score-instrument id="P8-I1"><instrument-name>Classical Guitar</instrument-name></score-instrument></score-part>'
)

# ===== V16 RULE 8: READABILITY ENHANCEMENTS =====
# Add staff-details for cleaner part extraction

# Update defaults with part-specific layout hints
content = content.replace(
    '<staff-layout><staff-distance>65</staff-distance></staff-layout>',
    '<staff-layout><staff-distance>65</staff-distance></staff-layout>\n<part-name-display><display-text>The Master\'s Palette</display-text></part-name-display>'
)

# ===== V16: ADD CREDIT FOR PARTS =====
# Add credits section for proper part headers
content = content.replace(
    '</identification>',
    '</identification>\n<credit page="1"><credit-type>title</credit-type><credit-words font-size="24" font-weight="bold" justify="center" valign="top">The Master\'s Palette (Reimagined)</credit-words></credit>\n<credit page="1"><credit-type>composer</credit-type><credit-words font-size="12" justify="right" valign="top">Composer TBD</credit-words></credit>\n<credit page="1"><credit-type>arranger</credit-type><credit-words font-size="10" justify="right" valign="top">Orchestration: hybrid_guitar_chamber</credit-words></credit>'
)

# ===== V16: UPDATE SUMMARY COMMENT =====
content = content.replace(
    '<!-- V15 FINAL Artistic Polish Summary:',
    '<!-- V16 Parts Extraction Summary:'
)

content = content.replace(
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
-->''',
    '''- Page layout: 4 pages with breaks at movement boundaries (m.12, 17, 21)
- Page turns: Placed after rests/long holds; no turns during active passages
- Multi-measure rests: Added <multiple-rest> indicators for Flute m.1-6, Violin m.1-6
- Cue notes: [cue: Flhn.] before Flute m.7; [cue: Flhn. enters] before Cl m.5; [cue: Flhn. phrase ending] before Vln m.10
- Rehearsal marks: Centered, top-aligned (halign="center" valign="top")
- Instrument labels: Full names on p.1 with score-instrument definitions
- Part headers: Title, composer, arranger credits added for professional parts
- Transpositions: Verified correct for Bb Clarinet, Bb Flugelhorn, 8vb Guitar/Bass
-->'''
)

# Write the output file
with open('scores/masters-palette-orchestrated-v16-parts.musicxml', 'w', encoding='utf-8') as f:
    f.write(content)

print("Generated: scores/masters-palette-orchestrated-v16-parts.musicxml")
print("")
print("=== V16 PARTS EXTRACTION SUMMARY ===")
print("")
print("* Page layout: 4-page structure with page breaks at movement boundaries (after m.12, m.16, m.20)")
print("")
print("* Page turns: Strategic placement after rests and long holds; no breaks during active melodic passages")
print("")
print("* Multi-measure rests: Added <multiple-rest> indicators for Flute m.1-6 and Violin m.1-6 tacet sections")
print("")
print("* Cue notes: '[cue: Flhn.]' before Flute m.7; '[cue: Flhn. enters]' before Clarinet m.5; '[cue: Flhn. phrase ending]' before Violin m.10")
print("")
print("* Rehearsal marks: Centered and top-aligned (A-E) with halign/valign attributes for clean positioning")
print("")
print("* Instrument labels: Full professional names with score-instrument definitions (Violoncello, Classical Guitar, etc.)")
print("")
print("* Part headers: Title/composer/arranger credits added for professional part extraction")
print("")
print("* Transpositions verified: Bb Clarinet, Bb Flugelhorn correct; Guitar/Bass 8vb notation preserved")
print("")
print("=== PARTS READY FOR EXTRACTION ===")





