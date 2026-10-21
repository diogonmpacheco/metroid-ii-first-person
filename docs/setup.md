# Setup — planned workflow

**There is no public installer or extraction utility yet.** These steps describe the intended release experience, not commands that work today.

1. Obtain your own copy of the supported original game and make it available locally.
2. Select that file in the future local setup tool.
3. Check the file's exact revision before extraction or launch.
4. Extract or decode original game graphics, maps, sprites, music and sound locally as needed by the runtime.
5. Keep generated content, preferences and saves in local directories excluded from version control.
6. Launch the presentation using that local content.

The game file will remain on your computer. No online ROM upload, hosted asset pack or bundled game copy is part of this plan.

## Current compatibility target

The development adapter targets the original Game Boy **Metroid II: Return of Samus (World)** image with SHA-256:

```text
3080bcc2eb9965de463f5f4e02f0dabbb13b060e1654a18da8b50948c10af4a6
```

The checksum identifies compatible bytes; it does not establish ownership. Other revisions, modified ROMs, AM2R, Samus Returns and Dread are not announced as supported inputs.

Desktop development currently focuses on Apple Silicon macOS. Public dependency versions and portable installation commands will be documented when the setup tools are released. Switch installation instructions are not available.

[Asset policy](asset-policy.md) · [Roadmap](roadmap.md)
