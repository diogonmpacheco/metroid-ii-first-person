# Contributing

This repository starts as a documentation scaffold. Clear wording, setup questions and focused design feedback are welcome.

Before opening a report, check the [roadmap](docs/roadmap.md) and distinguish the local development prototype from the public documentation template. Describe the platform, prototype version, game checksum if relevant, original room and steps needed to reproduce the issue.

Do not upload ROMs, extracted assets, game audio, cartridge saves, emulator states or the private development workspace. Keep personal paths and credentials out of logs. See the [asset policy](docs/asset-policy.md).

Use a small pull request with a description of the change and how it was checked. The repository intentionally allows only reviewed text files during this stage. If you add a documentation file, update the explicit allowlist in `tools/check_public_content.py` and check its links.

Run the publication check after staging your intended files:

```sh
python3 tools/check_public_content.py
```

It checks Git's staged blobs, rather than relying only on ignored files. Original runtime code and its license will be prepared separately; this scaffold is not a request to upload game-derived implementation data.
