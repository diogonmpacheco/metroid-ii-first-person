# Architecture — development outline

The prototype runs the original Game Boy program and adds a separate first-person presentation. The original simulation owns movement, enemy behaviour, collision, pickups, combat, progression and the original audio stream.

```text
Player's local game copy
    → validated original simulation
    → read-only map, sprite, audio and gameplay observations
    → first-person renderer and interface
```

Original game data is decoded locally. The public repository is intended to contain project code and the tooling needed to prepare that data, rather than pre-extracted content.

## Presentation

Chamber depth follows structural open-space spans. Low tunnels and narrow shafts remain close; broad caverns gain distant side walls. The renderer and lighting share the width profile, while live original floors and openings retain their actual state.

The camera can look freely, but traversal stays on the original plane. Shooting retains the original permitted directions, poses and damage rules. Visor feedback reports observed damage; directional hints do not predict a successful hit.

Original station saves and Continue remain authoritative. Local cartridge saves and preferences are separate from distributable code and assets.

## Validation boundary

Original-input replays, CPU/audio comparisons and selected GPU views guide development. Desktop frame-pacing measurements are separate from offline video exports and Switch performance. The current public scaffold contains no runnable implementation of this architecture yet.
