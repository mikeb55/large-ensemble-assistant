# Project File Structure Rules
Version: 2025.12.12

---

## Directory Structure

```
/large-ensemble-assistant/
├── system.md                    # Master system model
├── rules/                       # Modular rule files
│   ├── musicxml-duration-rules.md
│   ├── excellence-criteria.md
│   ├── movement-style-guides.md
│   ├── engraving-rules.md
│   ├── orchestration-rules.md
│   ├── anti-repetition-rules.md
│   ├── file-structure-rules.md
│   └── workflow-commands.md
├── scores/
│   ├── Movements/               # Individual movement files
│   ├── LeadSheets/              # Piano lead sheets
│   ├── FullScore/               # Combined full scores
│   ├── Bora Lesson on 14 Dec 2025/  # Lesson exports
│   └── Old versions/            # Archived versions
├── Parts/                       # Individual instrument parts
│   ├── Flute/
│   ├── Clarinet/
│   ├── Flugelhorn/
│   ├── Violin/
│   ├── Viola/
│   ├── Cello/
│   ├── Bass/
│   └── Guitar/
├── Publication/                 # Publication materials
│   ├── Parts-PDF/
│   ├── README.txt
│   ├── ProgramNotes.txt
│   ├── MovementIndex.txt
│   ├── License.txt
│   └── TitlePage.txt
├── Logs/                        # Generation logs
├── AudioMockups/                # Audio renderings
├── analysis/                    # Analysis documents
├── config/                      # Configuration files
├── scripts/                     # Python generation scripts
└── images/                      # Reference images
```

---

## File Sorting Rules

### MusicXML Files

| File Type | Location |
|-----------|----------|
| Movement files | `scores/Movements/` |
| Lead sheets | `scores/LeadSheets/` |
| Full scores | `scores/FullScore/` |
| Old/superseded versions | `scores/Old versions/` |
| Lesson exports | `scores/Bora Lesson on 14 Dec 2025/` |

### Other Files

| File Type | Location |
|-----------|----------|
| Sibelius files (.sib) | With corresponding .musicxml |
| Python scripts | `scripts/` |
| Analysis documents | `analysis/` |
| Configuration | `config/` |
| Rule files | `rules/` |
| Audio files | `AudioMockups/` |
| PDF parts | `Parts/[Instrument]/` or `Publication/Parts-PDF/` |

---

## File Naming Conventions

### Movement Files
```
Movement[N]-[Name]-[Version].musicxml
Movement1-Mingus-Excellent.musicxml
Movement3-Bartok-Orchestrated-Final.musicxml
```

### Lead Sheets
```
masters-palette-leadsheet-v[N].musicxml
masters-palette-leadsheet-v9.musicxml
```

### Full Scores
```
masters-palette-orchestrated-v[N].musicxml
masters-palette-orchestrated-v10.musicxml
Final-Suite-FullScore-[Descriptor].musicxml
Final-Suite-FullScore-Enhanced.musicxml
```

### Excellence Pass
```
Movement[N]-Excellent.musicxml
Movement[N]-Excellent-Final.musicxml
```

### Suite Enhanced
```
Movement[N]-FinalSuiteEnhanced.musicxml
```

---

## Version Numbering

### Major Versions (v1, v2, v3...)
- Significant structural changes
- New sections added
- Major reorchestration

### Minor Versions (v2.5, v12.5...)
- Refinements to existing version
- Bug fixes
- Polish passes

### Descriptive Suffixes
| Suffix | Meaning |
|--------|---------|
| -Excellent | Passed excellence criteria |
| -Final | Ready for publication |
| -Orchestrated | Full ensemble arrangement |
| -Engraved | Publication-ready layout |
| -Enhanced | Suite refinement applied |

---

## File Lifecycle

```
1. Initial Generation
   └── Movement1.musicxml

2. Excellence Pass
   └── Movement1-Excellent.musicxml

3. Final Excellence
   └── Movement1-Excellent-Final.musicxml

4. Orchestration
   └── Movement1-Orchestrated.musicxml

5. Orchestration Final
   └── Movement1-Orchestrated-Final.musicxml

6. Suite Enhancement
   └── Movement1-FinalSuiteEnhanced.musicxml
```

---

## Archival Rules

### When to Archive
- When a new version supersedes the old
- When making major structural changes
- Before experimental modifications

### Archive Location
- `scores/Old versions/`
- Keep original filename
- Add date if needed: `Movement1-Excellent-2025-12-10.musicxml`

### Never Delete
- Any .musicxml file without explicit user confirmation
- Final versions
- Files referenced in documentation

---

## Export Rules

### For Lessons/Collaboration
- Copy to dated folder: `scores/Bora Lesson on 14 Dec 2025/`
- Include all relevant movement files
- Include suite report if applicable

### For Publication
- Move finalized files to `Publication/`
- Export PDF parts to `Publication/Parts-PDF/`
- Update `MovementIndex.txt`

---

## Maintenance Commands

### Organize Project
```
"Sort files into proper folders"
"Clean up scores directory"
"Archive old versions"
```

### Export Tasks
```
"Copy to Bora folder"
"Prepare for publication"
"Generate parts"
```

