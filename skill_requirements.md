# YouTube Transcript to Article — Requirements

## 1. Purpose

Convert YouTube transcripts saved as Markdown files by Obsidian Web Clipper into coherent, readable, well-structured articles.

The goal is to **preserve the original informational content, reasoning, examples, and perspective while removing artifacts of spoken language and transcription**.

Produce a faithful editorial transformation of the original presentation. Retain its substantive content and level of detail. Limit changes to transcription correction, removal of irrelevant material, structural organization, and readability improvements permitted by the selected editing mode.

The target reader is assumed to have sufficient background knowledge of the subject. Preserve technical depth and terminology.

### Core principles

1. **Fidelity over elegance:** Preserve meaning and substantive information before improving style.
2. **Completeness over brevity:** Retain relevant content even when a shorter version would be easier to produce.
3. **Source-grounded editing:** Every substantive statement in the article must be supported by the original transcript.
4. **Preservation of reasoning:** Retain the speaker's arguments, intermediate reasoning, examples, qualifications, and conclusions.
5. **Editorial separation:** Keep the speaker's content separate from editorial evaluation and corrections.

## 2. Input Processing

The input is a Markdown file created by Obsidian Web Clipper.

It may contain:

- YAML frontmatter with metadata such as title, source URL, author, publication date, description, and tags.
- Video embeds, descriptions, promotional text, and other material preceding the transcript.
- A `## Transcript` section containing timestamped transcript entries.
- Optional headings and subsections within the transcript.

### Requirements

1. Identify the transcript section and process it as the primary source of article content.
2. Preserve useful source metadata, including title, video URL, author/channel, and publication date when available.
3. Use metadata and descriptions as contextual information for interpreting names, terminology, and ambiguous passages.
4. Derive substantive article content from the transcript. Treat metadata and descriptions as supporting context rather than additional source material.
5. Exclude promotional material outside the transcript unless explicitly requested.
6. Preserve the original input file unchanged.
7. Preserve source timestamps during processing so article sections and editorial observations can be traced to the original video.

## 3. Content Fidelity

**Preservation of meaning, substantive information, and reasoning takes priority over brevity and stylistic improvements.**

### Content to retain

Preserve:

- Facts, figures, dates, names, and technical details.
- Claims, hypotheses, assumptions, and conclusions.
- Key insights and observations.
- Opinions, viewpoints, and evaluations.
- Arguments, supporting evidence, and counterarguments.
- Intermediate reasoning, causal relationships, and chains of thought expressed by the speaker.
- Examples, analogies, comparisons, and illustrative scenarios.
- Procedures, processes, instructions, and sequences of steps.
- Qualifications, exceptions, limitations, and expressions of uncertainty.
- Meaningful distinctions between similar concepts.
- Relevant contextual information necessary to understand an argument.

### Fidelity rules

1. Preserve every substantive claim, argument, example, and reasoning step.
2. Preserve the speaker's original conclusions, qualifications, and degree of certainty.
3. Retain examples and reasoning even when their conclusions have already been stated.
4. Preserve incomplete arguments and logical gaps as expressed in the source.
5. Preserve contradictions between statements. Identify significant contradictions separately in the Editorial Critique.
6. Restrict editorial additions to language corrections and clarification of relationships already established by the speaker.
7. Keep all substantive statements grounded in the transcript.
8. Preserve the distinction between established facts, the speaker's claims, speculation, and reported opinions.
9. Preserve the original argumentative function of material, including explanations, objections, concessions, and responses.

**Critical constraint:** Do not invent facts, reasoning steps, evidence, explanations, or conclusions to make the article more complete or convincing.

## 4. Transcription Correction

Correct transcription errors when the intended meaning can be established with reasonable confidence.

### Corrections include

- Grammar and punctuation errors.
- Incorrect sentence boundaries.
- Misrecognized words and phrases.
- Incorrectly transcribed technical terminology.
- Proper names, abbreviations, and acronyms when sufficiently identifiable.
- Numbers and units when the intended values are clear from context.
- Broken sentences caused by transcription or speech-recognition artifacts.

Use the transcript, surrounding context, and available metadata to resolve ambiguities.

### Confidence-dependent handling

**High confidence**

When the intended wording or meaning is clear, correct the error directly.

**Moderate confidence**

When one interpretation is strongly supported by context but some uncertainty remains, use the most defensible correction while preserving the original level of specificity and meaning.

Flag the correction in an editorial note if it materially affects a factual claim, technical explanation, or argument.

**Low confidence**

When multiple interpretations remain plausible:

- Preserve the original wording when it remains understandable.
- Use a minimal indication of uncertainty when necessary for comprehension.
- Record consequential ambiguities in the Editorial Critique.
- Prefer faithful ambiguity over unsupported precision.

### Additional rules

1. Distinguish transcription errors from factual errors made by the speaker.
2. Preserve the speaker's substantive claims even when they appear incorrect.
3. Address suspected factual errors in the Editorial Critique.
4. Keep minor, inconsequential transcription uncertainties out of the article when they do not affect understanding.
5. Preserve numbers, units, names, and technical terminology unless a correction is sufficiently supported.

## 5. Removal of Irrelevant Material

Remove speech and transcription artifacts that contribute neither substantive information nor meaningful argumentative or rhetorical function.

### Material to remove

- Filler words and speech disfluencies.
- False starts and abandoned sentence fragments that add no meaning.
- Unnecessary greetings and farewells.
- Requests to like, subscribe, comment, or share.
- Advertisements and promotional remarks unrelated to the subject.
- References to the recording process that add no useful information.
- Repeated phrases that add no information, clarification, or meaningful emphasis.
- Conversational transitions without informational value.
- Accidental repetitions caused by transcription.

### Material to preserve

- Repetitions that introduce nuance, clarification, or additional reasoning.
- Repetition used for meaningful rhetorical emphasis.
- Rhetorical questions that develop an argument.
- Relevant personal experiences and anecdotes.
- Examples that illustrate or reinforce important concepts.
- References to earlier or later parts of the discussion when needed for comprehension.
- Conversational passages that establish assumptions, qualifications, or relationships between ideas.

### Redundancy criterion

Evaluate redundancy according to informational and argumentative function rather than repeated wording alone.

Two passages may express similar conclusions while contributing different evidence, reasoning, emphasis, or context. Preserve these differences.

Remove repetition when its removal leaves the substantive content and argumentative function intact.

When uncertain whether material is redundant or meaningful, prioritize preservation.

## 6. Readability and Editing Modes

Support two editing modes for experimentation and comparison.

Both modes must preserve an equivalent set of substantive claims, reasoning steps, examples, qualifications, and conclusions.

The editing mode must be configurable, with **Conservative** as the default.

### Mode A — Conservative

Prioritize fidelity to the speaker's original wording, structure, and style.

Permitted transformations:

- Correct transcription, grammar, and punctuation errors.
- Remove irrelevant phrases and redundant wording.
- Reconstruct broken sentences.
- Divide long passages into readable paragraphs.
- Preserve original sentence structures where practical.
- Make minimal stylistic changes.
- Introduce section headings when useful.

The result should resemble a carefully edited transcript presented as an article.

### Mode B — Polished

Prioritize readability and coherence while preserving the same substantive content.

Apply all Conservative transformations, plus:

- Rewrite awkward sentences into natural written language.
- Improve sentence structure and paragraph organization.
- Clarify references and relationships already established in the transcript.
- Combine fragmented statements into coherent explanations.
- Improve transitions between related ideas.
- Reduce unnecessary linguistic complexity.
- Improve the flow of explanations within the original sequence of ideas.

### Boundaries shared by both modes

1. Preserve substantive content and the speaker's intended meaning.
2. Preserve the speaker's arguments, evidence, examples, and conclusions.
3. Preserve the original degree of certainty and qualification.
4. Keep editorial changes grounded in information already expressed in the transcript.
5. Maintain the original sequence of topics and reasoning.
6. Restrict differences between modes to wording, sentence construction, paragraph organization, transitions, and stylistic polish.

**Critical constraint:** Stylistic improvement must never introduce unsupported explanations or replace the speaker's reasoning with newly constructed arguments.

## 7. Language, Perspective, and Voice

1. Preserve the language of the transcript.
2. Preserve the speaker's grammatical perspective, including first-person and third-person narration.
3. Preserve the speaker's opinions, attitudes, and degree of certainty.
4. Preserve attribution when the speaker reports someone else's claims or opinions.
5. Maintain the speaker's characteristic tone where it contributes to meaning.
6. Remove unnecessary artifacts of spontaneous speech while preserving meaningful rhetorical style.
7. Keep subjective statements identifiable as the speaker's opinions or interpretations.
8. Preserve distinctions between the speaker's own position and positions attributed to other people.

The result should read as an edited version of the speaker's own presentation.

**Critical constraints:**

- Do not automatically translate the transcript.
- Do not introduce an external narrator or convert the article into a third-person account of the speaker unless the original perspective requires it.

## 8. Structure and Organization

Organize the article into meaningful sections when the content supports such division.

### Requirements

1. Preserve the original sequence of topics, arguments, and examples.
2. Group adjacent, closely related material into coherent paragraphs or sections.
3. Use descriptive headings that accurately reflect the content.
4. Preserve meaningful headings already present in the transcript, correcting them when necessary.
5. Prefer coherent prose over bullet lists.
6. Use lists when the original content naturally describes enumerations, procedures, alternatives, or comparisons.
7. Preserve the order of procedural steps and the sequence of arguments.
8. Choose section boundaries according to meaningful topic changes.
9. Keep closely connected reasoning within the same section when practical.
10. Preserve transitions that explain how one argument leads to another.

### Structural boundaries

- Maintain the original presentation order rather than reorganizing material into a conventional article structure.
- Use an introduction, conclusion, or summary only when corresponding substantive material exists in the original transcript.
- Avoid excessive fragmentation into short sections.
- Keep headings descriptive rather than interpretive or argumentative.

## 9. Timestamps and Visual References

Preserve source traceability while keeping the article readable.

### Requirements

1. Include timestamps at major section boundaries when available.
2. Preserve timestamps for passages requiring visual context.
3. Identify references to charts, diagrams, demonstrations, screen recordings, slides, or other visual information necessary for understanding.
4. Insert a short editorial comment containing the relevant timestamp or time range when visual inspection would improve comprehension.
5. Describe the nature of the visual dependency using information available from the transcript.
6. When the transcript provides insufficient information about the visual content, indicate that the original video requires inspection.
7. Use a consistent Markdown convention for visual-reference comments.
8. Keep timestamp references selective and useful.

### Suggested comment format

`<!-- Visual reference [00:12:35]: Inspect the diagram explaining the relationship between components. -->`

For a time range:

`<!-- Visual reference [00:12:35–00:14:10]: Screen demonstration; inspect the original video for details. -->`

**Critical constraint:** Do not invent visual details that cannot be established from the transcript or available source material.

## 10. Factual Integrity and Editorial Critique

Support an optional section titled **Editorial Critique**, placed at the end and clearly separated from the converted article.

The critique evaluates potential problems in the original material while leaving the speaker's claims and arguments intact in the article.

### Issues to consider

- Demonstrable factual errors.
- Claims that appear questionable or insufficiently supported.
- Internal contradictions.
- Incorrect or questionable causal relationships.
- Unsupported assumptions.
- Logical gaps and invalid inferences.
- Overgeneralizations.
- Missing qualifications or important exceptions.
- Potentially misleading terminology.
- Time-sensitive information that may be outdated.

### For each significant issue, provide

1. The relevant claim or a concise description of it.
2. Its location in the original transcript, preferably with a timestamp.
3. The nature of the concern.
4. A correction or alternative interpretation when sufficiently supported.
5. An indication of uncertainty or verification status.

### Issue classification

Use the following categories:

- **Confirmed error:** A demonstrable error supported by reliable evidence.
- **Internal inconsistency:** Conflicting statements within the source.
- **Potential issue:** A plausible concern requiring further verification.
- **Unverified claim:** An externally checkable claim for which sufficient evidence is unavailable.

Use classifications that accurately reflect the available evidence.

### Critique operations

Distinguish three separate activities:

**1. Internal analysis**

Evaluate logical consistency, argument structure, unsupported inferences, contradictions, and qualifications using the transcript itself.

**2. External fact verification**

When enabled, verify relevant factual claims using reliable external sources.

Cite sources supporting confirmed corrections and distinguish verification results from interpretation.

**3. Transcription ambiguity review**

Identify consequential passages where transcription uncertainty may affect meaning.

Keep these observations distinct from factual errors made by the speaker.

### Configuration

External fact verification must be explicitly configurable and **disabled by default**.

When external verification is disabled:

- Evaluate internal consistency and reasoning quality.
- Identify potential factual concerns as unverified.
- Reserve the label "Confirmed error" for errors demonstrable from the available source material.
- Distinguish suspected errors from established corrections.

### Critique boundaries

1. Prioritize significant issues that materially affect understanding or correctness.
2. Provide corrections only when sufficiently supported.
3. Express uncertainty explicitly.
4. Keep the critique separate from the converted article.
5. Preserve the speaker's original claims within the article.
6. If no meaningful issues are identified, state this briefly.
7. The critique must not become an independent review or rewrite of the entire presentation.

## 11. Output Format

Produce a separate Markdown file compatible with Obsidian.

### Output structure

1. Title based on the original video's title.
2. Relevant source metadata, including a link to the original video.
3. Converted article organized into meaningful sections.
4. Timestamp references and visual-reference comments where useful.
5. Optional Editorial Critique section at the end.

### Requirements

- Preserve valid Markdown formatting.
- Use headings, paragraphs, and lists according to the structure of the content.
- Prefer restrained formatting.
- Preserve source links when relevant.
- Preserve the original transcript file unchanged.
- Make output naming and location configurable.
- Use a deterministic default output filename derived from the input filename.
- Keep the article and critique clearly separated.

## 12. Quality Assurance

Before finalizing the output, perform a fidelity and completeness review against the original transcript.

The review must evaluate both directions of correspondence:

- **Source to article:** Verify that substantive information from the transcript is represented in the article.
- **Article to source:** Verify that substantive information in the article is supported by the transcript.

### Fidelity checks

Verify that:

1. Every substantive claim and fact in the transcript has a corresponding representation in the article.
2. Important arguments and intermediate reasoning remain intact.
3. Examples, explanations, qualifications, and counterarguments are preserved.
4. Numerical values, dates, names, and technical terminology are accurate.
5. The original sequence of ideas and reasoning is maintained.
6. The speaker's viewpoint, perspective, and level of certainty are preserved.
7. Every substantive statement in the article is grounded in the source.
8. Transcription corrections preserve the intended meaning.
9. Removed material satisfies the irrelevance or redundancy criteria.
10. The article reads naturally and coherently.
11. Visual dependencies and significant ambiguities are identified where appropriate.
12. Editorial observations are separated from the speaker's content.
13. The selected editing mode has been applied consistently.

### Review procedure

1. Divide the original transcript into manageable sequential segments.
2. Identify the substantive claims, reasoning, examples, qualifications, and conclusions in each segment.
3. Compare each segment against the corresponding article passage.
4. Identify missing content, altered meaning, unsupported additions, and significant changes in certainty or perspective.
5. Correct the article where discrepancies are found.
6. Review the article for unsupported substantive statements.
7. Verify that editorial critique and transcription notes remain separate from the speaker's presentation.
8. Complete the output only after resolving identified fidelity problems or explicitly flagging unresolved ambiguities.

The review should evaluate the actual source and output content rather than relying solely on a general impression of completeness.

A separate reviewer pass may be used when available. Such a pass provides additional checking but does not guarantee complete detection of errors.

### Priority order

When requirements conflict, apply the following priorities:

1. Preserve meaning and factual fidelity to the source.
2. Preserve substantive content and reasoning.
3. Preserve the original sequence and perspective.
4. Improve clarity and readability.
5. Remove redundancy and reduce length.
6. Improve stylistic elegance.

**Primary success criterion:** A knowledgeable reader should obtain substantially the same information, reasoning, examples, qualifications, and perspective from the article as from the original transcript, with less effort and without needing to reconstruct fragmented speech.

## 13. Configuration Requirements

The eventual skill should expose the following configurable behavior.

| Option | Default | Description |
|---|---|---|
| Editing mode | Conservative | Conservative or Polished editing |
| Editorial Critique | Enabled | Include or omit the critique section |
| External verification | Disabled | Verify factual claims using external sources |
| Section timestamps | Enabled | Include timestamps at major section boundaries |
| Visual-reference comments | Enabled | Mark passages requiring inspection of video content |
| Output path | Derived from input | Destination of the generated Markdown file |
| Output filename | Derived from input | Deterministic filename based on the source |

Configuration should be simple and suitable for invocation through a Codex skill.

When an option is unspecified, apply its documented default.

## 14. Acceptance Criteria

A conversion is considered successful when:

1. The generated Markdown file is readable and structurally coherent.
2. The article preserves the transcript's substantive information and reasoning.
3. The speaker's perspective, voice, and degree of certainty remain faithful to the source.
4. The original topic and argument sequence is maintained.
5. Transcription errors are corrected according to the confidence rules.
6. Irrelevant speech artifacts are removed while meaningful content remains intact.
7. The selected editing mode is applied consistently.
8. Visual dependencies are marked where appropriate.
9. The Editorial Critique, when enabled, is clearly separated and uses appropriate evidence classifications.
10. The source-to-article and article-to-source fidelity checks have been performed.
11. The original input file remains unchanged.
12. The output is valid Markdown suitable for use in Obsidian.

The overarching objective is **faithful transformation rather than content reduction**: improve how the original presentation is expressed while preserving what the speaker actually communicated.