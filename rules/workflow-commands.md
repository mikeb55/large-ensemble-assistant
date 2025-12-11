# Workflow Shortcut Commands
Version: 2025.12.12

---

## Recognized Commands

These commands trigger immediate, specific actions without requiring additional explanation.

---

## Generation Commands

| Command | Action |
|---------|--------|
| `"Generate the lead sheet."` | Create piano lead sheet for specified movement |
| `"Generate the orchestration."` | Orchestrate for specified ensemble |
| `"Generate Movement [N]."` | Create specified movement from scratch |
| `"Generate all movements."` | Create complete 5-movement suite |

### Examples
```
"Generate the lead sheet for Movement 3."
"Generate the orchestration for Movement 1 using the hybrid chamber ensemble."
```

---

## Refinement Commands

| Command | Action |
|---------|--------|
| `"Run the Excellence Pass."` | Evaluate & refine to ≥8.5 score |
| `"Run the Anti-Repetition Pass."` | Remove loops, add variation |
| `"Make it human."` | Add phrase shapes, breath, expressivity |
| `"Refine until excellent."` | Loop refinement until all targets met |

### Examples
```
"Run the Excellence Pass on Movement 2."
"Make it human across all movements."
```

---

## Engraving Commands

| Command | Action |
|---------|--------|
| `"Generate final engraving."` | Apply engraving polish, copyright |
| `"Fix collisions."` | Clean up dynamics, slurs, articulations |
| `"Add copyright."` | Insert copyright footer per rules |
| `"Prepare for publication."` | Full publication-ready pass |

---

## Suite Commands

| Command | Action |
|---------|--------|
| `"Unify the suite."` | Apply suite-wide consistency pass |
| `"Run the Unified Suite Pass."` | Complete suite refinement (all passes) |
| `"Ensure contrast across movements."` | Check/improve inter-movement contrast |

---

## File Management Commands

| Command | Action |
|---------|--------|
| `"Show me the leadsheets."` | List all current lead sheet files |
| `"Show me the movements."` | List all movement files |
| `"Copy to Bora folder."` | Export to lesson folder |
| `"Sort files."` | Organize files into proper directories |
| `"Archive old versions."` | Move superseded files to archive |

---

## Information Commands

| Command | Action |
|---------|--------|
| `"What's the current version?"` | Report latest version numbers |
| `"Show project state."` | Display current project status |
| `"What's next?"` | Suggest next workflow step |
| `"Show excellence scores."` | Display scores for all movements |

---

## Combination Commands

| Command | Action |
|---------|--------|
| `"Full workflow for Movement [N]."` | Generate → Excellence → Orchestrate → Engrave |
| `"Complete the suite."` | All movements → Unify → Engrave → Publish |

---

## Command Modifiers

### Target Specification
Add movement number or range:
- `"...for Movement 3"`
- `"...for Movements 1-3"`
- `"...for all movements"`

### Ensemble Specification
Add ensemble type:
- `"...using hybrid chamber ensemble"`
- `"...for string quartet"`
- `"...for full orchestra"`

### Version Specification
Add version requirement:
- `"...based on v9"`
- `"...update from v10"`
- `"...as v11"`

---

## Workflow Chains

### Standard Lead Sheet Workflow
```
1. "Generate the lead sheet for Movement 1."
2. "Run the Excellence Pass."
3. "Make it human."
4. "Generate final engraving."
```

### Standard Orchestration Workflow
```
1. "Generate the orchestration for Movement 1."
2. "Run the Excellence Pass."
3. "Run the Anti-Repetition Pass."
4. "Generate final engraving."
```

### Full Suite Workflow
```
1. "Generate all movements."
2. "Run the Unified Suite Pass."
3. "Prepare for publication."
4. "Copy to Bora folder."
```

---

## Emergency Commands

| Command | Action |
|---------|--------|
| `"Start over."` | Regenerate from scratch |
| `"Revert to previous."` | Restore previous version |
| `"Fix duration errors."` | Recalculate all durations |
| `"Validate MusicXML."` | Check for structural errors |

---

## Custom Commands

Users can define custom commands by creating entries in this file.
Format:
```
| `"[Custom Command]"` | [Description of action] |
```

---

## Response Protocol

When a shortcut command is recognized:

1. Acknowledge the command briefly
2. Execute immediately without asking for confirmation
3. Report completion with:
   - Files created/modified
   - Scores achieved (if applicable)
   - Next suggested action

