# YouTube to Article

A Codex skill that turns saved YouTube transcripts into readable, complete Markdown articles. It preserves the original language, reasoning, examples, qualifications, and topic order while removing speech clutter. It includes a fidelity review and an optional, separate editorial critique.

Use it in conjunction with the [Obsidian Web Clipper extension for Chrome](https://obsidian.md/clipper): first save a YouTube transcript as a Markdown note, then ask your agent to convert it. The skill processes existing transcripts; it does not download videos or extract transcripts from YouTube URLs.

## Installation

Download or clone this repository. Copy the entire **`youtube-to-article`** folder, including its `references`, `scripts`, and `agents` subfolders, into the appropriate location:

| Tool | macOS / Linux | Windows |
|---|---|---|
| Codex | `~/.agents/skills/youtube-to-article/` | `%USERPROFILE%\.agents\skills\youtube-to-article\` |
| Claude Code | `~/.claude/skills/youtube-to-article/` | `%USERPROFILE%\.claude\skills\youtube-to-article\` |

**macOS and Linux:** in Finder or your file manager, open your home folder, show hidden files, and create `.agents/skills` (or `.claude/skills`) if necessary. Copy the skill folder there. Alternatively, from this repository's root:

```sh
mkdir -p ~/.agents/skills
cp -R youtube-to-article ~/.agents/skills/
```

**Windows:** paste `%USERPROFILE%` into File Explorer's address bar. Create `.agents\skills` (or `.claude\skills`) if necessary, then copy the skill folder into it.

The final layout must contain `skills/youtube-to-article/SKILL.md`. If an installation already exists, back it up or remove it before copying. Start a new agent session if the skill does not appear.

Requires an agent with local file access and Python 3 for the bundled helper; no additional Python packages or separate API key are needed. Tested in Codex; Claude Code compatibility has not yet been tested.

## Usage

1. Use Web Clipper to save the video transcript, including timestamps where available. Check that the note contains the actual transcript under a clearly marked heading such as `## Transcript`, rather than only the video description.
2. Open your agent in a workspace with access to the saved note.
3. In Codex, enter:

```text
$youtube-to-article "notes/My lecture.md"
```

For Claude Code, use `/youtube-to-article` instead of `$youtube-to-article`.

By default, the skill uses **Polished** mode, includes section timestamps, comments identifying passages that depend on visuals, and a separate **Editorial Critique**. External fact-checking is off. The source stays unchanged; the article is saved beside it as `My lecture.article.md`. Existing outputs are preserved using `.article.2.md`, `.article.3.md`, and so on.

More examples:

```text
$youtube-to-article help
$youtube-to-article "notes/My lecture.md" mode=conservative critique=false
$youtube-to-article "notes/My lecture.md" output_path="articles"
$youtube-to-article "notes/My lecture.md" external_verification=true
```

**Conservative** mode keeps more of the original wording; **Polished** mode improves phrasing and flow while preserving substantive content. Use `help` for all options and defaults.

For a directory, ask the agent:

> Use the youtube-to-article skill to process every transcript Markdown file in `notes/` with default settings. Skip existing `.article.md` and numbered `.article.N.md` outputs. Process and review each source separately, and report any failures.

Long transcripts are processed in sequential segments and reviewed against the source. Ambiguous wording or speaker attribution may remain flagged; review important claims before publishing.

## License

[MIT](LICENSE) © 2026 Andrey Vasyliev. A copy is included in the skill folder for standalone installations. This license covers the project's original code and documentation; it does not grant rights to third-party transcripts or other source content processed by the skill.
