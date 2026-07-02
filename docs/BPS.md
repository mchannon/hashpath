# BPS: Beacon Positioning System

BPS is a proposed local source-of-truth layer for GPS-poor, indoor, or micro-precision environments.

## Definition

A BPS anchor is a fixed physical reference whose identifier resolves to a known global Hashsite, local Hashsite, or facility micro-region.

It tells a phone or task system: I am installed here. Seeing me is evidence that you are near this known region.

## Possible implementations

| Method | Role |
|---|---|
| BLE/iBeacon | cheap proximity / zone anchor |
| Directional BLE | aisle/corridor aperture evidence |
| UWB | higher precision local positioning |
| Wi-Fi RTT | indoor ranging where supported |
| QR code | passive exact tare/confirmation point |
| NFC tag | passive tap-to-confirm point |
| barcode | shelf/bin/product confirmation |
| camera marker | visual confirmation |
| light-fixture powered anchor | fixed ceiling source of truth |
| solar outdoor beacon | gate/yard/trailhead source of truth |

## Aperture

A BPS beacon may describe not only its point, but its intended coverage region or aperture.

```json
{
  "beacon": "BPS-AISLE-06-N",
  "anchor": "Store123:localHashsite:9F2K",
  "aperture": {"type": "corridor", "direction": "south", "lengthMeters": 24, "widthMeters": 2}
}
```

## Dead reckoning anchors / tare points

Dead reckoning should be short-term interpolation between sources of truth.

Workflow:

1. User reaches a known tare point.
2. User says or taps “I’m here.”
3. App resets local position estimate.
4. App uses dead reckoning for a short segment.
5. User confirms target by scan/photo/voice.
6. App resets again at next anchor.

## Voice-first picking

Example:

```text
Bot: Go to Aisle 9 North marker.
Picker: Here.
Bot: Tared. Walk forward 18 feet. Stop. Look right, second shelf from bottom. Pick four.
Picker: Picked four.
Bot: Next item...
```

BPS should not be sold as magic indoor GPS. It should be sold as a local truth layer for place-aware task execution.
