# Original game files stay with the player

Players must provide their own supported original game copy. All original-game content used by the presentation will come from that local copy.

## Public repository

The current scaffold contains documentation, issue templates and a content check. A future code release may add original project code, extraction/decoding utilities and setup instructions after their publication review.

## Local files only

ROM images, rebuilt ROMs, extracted graphics, authored game maps, enemy/sprite data, game music, sound recordings, cartridge saves, emulator states and generated asset caches are excluded from the repository and release packages. The complete private development workspace is not a release package.

New renderer code and procedural geometry are distinct from original game data. Game-derived screenshots, videos and other media are also outside this initial text-only template.

## Contributions and reports

Do not attach game files or extracted content to issues or pull requests. Report a checksum, prototype version, platform, original room and reproducible controls instead. Redact personal paths from logs.

The publication check uses an explicit file allowlist and rejects binary payloads and symlinks. It is a practical guard for this scaffold, not an ownership or rights determination. The content policy applies to Git history and release attachments as well as the current tree.
