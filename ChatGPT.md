# ChatGPT Collaboration Summary

This document summarizes the parallel work done with ChatGPT alongside the Cursor AI project.

---

## Key Contributions from ChatGPT Sessions

- **System Prompt Design**: Developed the master system prompt for Cursor AI based on Steven Feifke's *Lead Sheet to Large Ensemble* methodology, defining a structured 7-stage pipeline (word sketch → lead sheet → event map → orchestration → shout chorus → rhythm section → engraving)

- **Project State Schema**: Designed the `project_state` JSON structure to track all arrangement decisions including metadata, instrumentation (17-piece big band default), event mapping, voicing strategies, and engraving checklists

- **Folder & File Organization**: Created the Folder Initializer and File Sorter prompts to establish professional directory structure (`/Movements`, `/LeadSheets`, `/FullScore`, `/Parts`, `/Publication`, `/AudioMockups`, `/Logs`)

- **Excellence Engine Feedback**: Identified that Cursor needed an "Autonomous Excellence Loop" to self-score, self-correct, and only proceed when scores reach ≥8.0—preventing sub-excellent output from advancing

- **Engraving & Output Rules**: Established requirements for MusicXML + PDF output, copyright handling, clef safety, collision removal, and publication-grade layout standards now embedded in `system.md`

---

*Source: ChatGPT conversation exported 2025-12-11*

