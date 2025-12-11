# MusicXML Duration Calculation Rules

## The Core Problem in V9

The V9 orchestration had **incorrect measure durations** in compound meters (9/8, etc.), causing red/incomplete measures when rendered in notation software.

### Error Analysis

With `<divisions>256</divisions>` (256 divisions = 1 quarter note):

| Measure | Time Sig | Required Duration | Actual Duration | Error |
|---------|----------|-------------------|-----------------|-------|
| m.13 | 9/8 | 1152 | 1280 | +128 ❌ |
| m.14 | 9/8 | 1152 | 1280 | +128 ❌ |
| m.15 | 9/8 | 1152 | 1408 | +256 ❌ |
| m.16 | 9/8 | 1152 | 1280 | +128 ❌ |
| m.17 | 5/8 | 640 | 640 | ✓ |
| m.18 | 7/8 | 896 | 896 | ✓ |
| m.19 | 5/8 | 640 | 640 | ✓ |

**Root cause:** Calculated 9/8 as if it were 10/8, adding 128 extra divisions.

---

## RULE 1: Master Formula for Measure Duration

```
MEASURE_DURATION = (BEATS × DIVISIONS × 4) / BEAT_TYPE
```

Where:
- **BEATS** = numerator of time signature
- **DIVISIONS** = value from `<divisions>` element
- **BEAT_TYPE** = denominator of time signature

### Why multiply by 4?

Because `<divisions>` defines divisions per **quarter note** (beat-type 4).
To convert to any beat-type, multiply by 4 then divide by the actual beat-type.

---

## RULE 2: Quick Reference Table

With **divisions = 256**:

| Time Signature | Formula | Measure Duration |
|----------------|---------|------------------|
| **4/4** | (4 × 256 × 4) / 4 | **1024** |
| **3/4** | (3 × 256 × 4) / 4 | **768** |
| **2/4** | (2 × 256 × 4) / 4 | **512** |
| **7/4** | (7 × 256 × 4) / 4 | **1792** |
| **6/8** | (6 × 256 × 4) / 8 | **768** |
| **9/8** | (9 × 256 × 4) / 8 | **1152** |
| **12/8** | (12 × 256 × 4) / 8 | **1536** |
| **5/8** | (5 × 256 × 4) / 8 | **640** |
| **7/8** | (7 × 256 × 4) / 8 | **896** |
| **11/8** | (11 × 256 × 4) / 8 | **1408** |
| **2/2** | (2 × 256 × 4) / 2 | **1024** |
| **3/2** | (3 × 256 × 4) / 2 | **1536** |

---

## RULE 3: Note Duration Values

With **divisions = 256**:

| Note Type | Base Duration | Dotted | Double-Dotted |
|-----------|---------------|--------|---------------|
| Whole | 1024 | 1536 | 1792 |
| Half | 512 | 768 | 896 |
| Quarter | 256 | 384 | 448 |
| Eighth | 128 | 192 | 224 |
| Sixteenth | 64 | 96 | 112 |
| 32nd | 32 | 48 | 56 |

**Dotted formula:** `base × 1.5`
**Double-dotted formula:** `base × 1.75`

---

## RULE 4: Validation Checklist

Before writing any measure:

1. **Calculate required duration** using Rule 1
2. **Sum all note durations** in the measure
3. **Verify:** Sum must EXACTLY equal required duration
4. **Check rests:** Rests count toward duration too

```
✓ VALID:   Sum of durations == Measure duration
✗ INVALID: Sum of durations != Measure duration
```

---

## RULE 5: Common Pitfalls

### Pitfall 1: Confusing beat-type 4 vs 8
- 9/8 ≠ 9/4
- In 9/8: quarter note = 2 beats, not 1
- Always divide by beat-type

### Pitfall 2: Forgetting dots affect duration
- Dotted half in 9/8 = 768 (6 eighth notes)
- Dotted quarter in 9/8 = 384 (3 eighth notes)
- A dotted half + quarter = 768 + 256 = 1024 ≠ 1152 ❌

### Pitfall 3: Using "whole rest" in odd meters
- Whole rest duration should match the TIME SIGNATURE, not 1024
- In 9/8: use duration="1152" for full-bar rest
- In 7/8: use duration="896" for full-bar rest
- In 5/8: use duration="640" for full-bar rest

### Pitfall 4: Compound meter mental model
- Think in EIGHTH NOTES for /8 meters
- 9/8 = 9 eighth notes = 9 × 128 = 1152
- 7/8 = 7 eighth notes = 7 × 128 = 896
- 11/8 = 11 eighth notes = 11 × 128 = 1408

---

## RULE 6: Step-by-Step Measure Writing

### Example: Writing a measure in 9/8

**Step 1:** Calculate measure duration
```
(9 × 256 × 4) / 8 = 1152
```

**Step 2:** Plan note values
```
Dotted quarter (384) + Quarter (256) + Quarter (256) + Dotted quarter (384)
= 384 + 256 + 256 + 256 = 1152 ✓

OR

Dotted half (768) + Dotted quarter (384)
= 768 + 384 = 1152 ✓
```

**Step 3:** Write XML with exact durations
```xml
<note><pitch>...</pitch><duration>384</duration><type>quarter</type><dot/></note>
<note><pitch>...</pitch><duration>256</duration><type>quarter</type></note>
<note><pitch>...</pitch><duration>256</duration><type>quarter</type></note>
<note><pitch>...</pitch><duration>256</duration><type>quarter</type></note>
```

**Step 4:** Verify
```
384 + 256 + 256 + 256 = 1152 ✓
```

---

## RULE 7: Full-Bar Rest Durations

**CRITICAL:** Full-bar rests must use the MEASURE DURATION, not a fixed "whole note" value.

| Time Signature | Full-Bar Rest Duration |
|----------------|------------------------|
| 4/4 | 1024 |
| 7/4 | 1792 |
| 9/8 | 1152 |
| 7/8 | 896 |
| 5/8 | 640 |
| 11/8 | 1408 |

```xml
<!-- WRONG: Using 1024 for all full-bar rests -->
<note><rest/><duration>1024</duration><type>whole</type></note>

<!-- CORRECT: 9/8 full-bar rest -->
<note><rest/><duration>1152</duration><type>whole</type></note>

<!-- CORRECT: 7/8 full-bar rest -->
<note><rest/><duration>896</duration><type>whole</type></note>
```

---

## RULE 8: Divisions Choice

**Recommended:** Use `divisions="256"` for complex rhythms.

This allows clean division for:
- Whole notes: 1024
- Halves: 512
- Quarters: 256
- Eighths: 128
- Sixteenths: 64
- 32nds: 32
- Triplets: 85.33... (use 256 for triplet-heavy music)

For triplet-heavy music, use `divisions="768"`:
- Quarter triplet = 256
- Eighth triplet = 128

---

## Summary: V9→V10 Fix Required

To fix V9 orchestration for V10:

1. **All 9/8 measures:** Change total duration from 1280 to **1152**
2. **Full-bar rests in 9/8:** Change from 1280/1408 to **1152**
3. **Verify all /8 meter measures** against the formula
4. **Re-sum every measure** before outputting

---

## Quick Validation Script (Pseudocode)

```python
def validate_measure(time_beats, time_type, divisions, note_durations):
    required = (time_beats * divisions * 4) // time_type
    actual = sum(note_durations)
    if actual != required:
        raise Error(f"Measure invalid: {actual} != {required}")
    return True
```

---

*These rules ensure accurate measure counting in any time signature.*











