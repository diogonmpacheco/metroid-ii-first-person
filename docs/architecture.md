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

The Queen uses original background, window and sprite graphics rather than ordinary enemy metasprites; those parts are decoded separately from cave rock. Her original swallowing and stomach-bomb logic remains in the cartridge. The friendly baby clears the original crystal tiles, and the original ending is presented full screen.

Original station saves and Continue remain authoritative. Local cartridge saves and preferences are separate from distributable code and assets.

## Validation boundary

Original-input replays, CPU/audio comparisons and selected GPU views guide development. Desktop frame-pacing measurements are separate from offline video exports and Switch performance. The current public scaffold contains no runnable implementation of this architecture yet.

## Visual fidelity

The original live tile atlas and palette provide the material images. Source-authored background tiles keep their positions; blank space can receive a depth wall extended from a nearby original structural metatile, with its source-cell provenance retained. Texture density stays tied to the original8px tile scale. The current renderer removes arbitrary cave-contour deformation and calibrates a symmetric added depth from the smaller original air span. This is a reproducible interpretation of depth, not an original hidden3D map.

Weapon identification uses the original live cannon and projectile sprites. The custom3D cannon is removed. Shared original artwork, such as Spazer/Plasma, remains shared and is distinguished by its weapon name. Original firing directions, speed, collisions, ammunition and damage continue to come from the cartridge.
