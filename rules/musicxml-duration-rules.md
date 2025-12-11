# MusicXML Duration Rules
Version: 2025.12.12

## Duration Calculation Formula

```
MEASURE_DURATION = (BEATS × DIVISIONS × 4) / BEAT_TYPE
```

## Standard Divisions
Always use: **divisions = 256**

## Measure Duration Reference

| Time Signature | Calculation | Measure Duration |
|----------------|-------------|------------------|
| 4/4            | (4×256×4)/4 | 1024             |
| 3/4            | (3×256×4)/4 | 768              |
| 2/4            | (2×256×4)/4 | 512              |
| 5/4            | (5×256×4)/4 | 1280             |
| 6/4            | (6×256×4)/4 | 1536             |
| 7/4            | (7×256×4)/4 | 1792             |
| 6/8            | (6×256×4)/8 | 768              |
| 7/8            | (7×256×4)/8 | 896              |
| 9/8            | (9×256×4)/8 | 1152             |
| 11/8           | (11×256×4)/8| 1408             |
| 12/8           | (12×256×4)/8| 1536             |

## Note Duration Reference

| Note Type         | Base Value | Duration |
|-------------------|------------|----------|
| Whole             | 1          | 1024     |
| Half              | 1/2        | 512      |
| Dotted Half       | 3/4        | 768      |
| Quarter           | 1/4        | 256      |
| Dotted Quarter    | 3/8        | 384      |
| Eighth            | 1/8        | 128      |
| Dotted Eighth     | 3/16       | 192      |
| Sixteenth         | 1/16       | 64       |
| Dotted Sixteenth  | 3/32       | 96       |
| Thirty-second     | 1/32       | 32       |

## Critical Rules

1. **Full-bar rests MUST use the MEASURE duration** (not always 1024)
   - In 3/4: rest duration = 768
   - In 9/8: rest duration = 1152

2. **In /8 meters, think in eighth notes**
   - 9/8 = 9 × 128 = 1152
   - 7/8 = 7 × 128 = 896

3. **Dotted notes = base × 1.5**
   - Dotted half = 512 × 1.5 = 768
   - Dotted quarter = 256 × 1.5 = 384

4. **Always verify** that sum of all note durations in a measure equals the calculated measure duration exactly

5. **Never guess durations** — always calculate precisely

## Compound Meter Groupings

| Meter | Beat Grouping | Typical Feel |
|-------|---------------|--------------|
| 6/8   | 3+3           | 2 dotted quarters |
| 9/8   | 3+3+3         | 3 dotted quarters |
| 12/8  | 3+3+3+3       | 4 dotted quarters |
| 7/8   | 2+2+3 or 3+2+2| Irregular |
| 11/8  | 3+3+3+2       | Irregular |

## Tuplets

For triplets with divisions=256:
- Quarter-note triplet: 3 notes of duration 171 (rounds from 170.67)
- Eighth-note triplet: 3 notes of duration 85 (rounds from 85.33)

Always use `<time-modification>` element for tuplets.

