# HBD_Retro_card_maker
This code generates a retro image of saying HBD and year

A Python script using **Pillow (PIL)** to generate a customized 3D retro-style birthday card. The card features custom color palettes, multiline text handling, and individual pink tiles with a 3D block-extruded shadow effect for each character.

## Features

* **Custom Color Palette**: Dark purple border, vibrant green canvas, pink text tiles, and deep brown letter faces.
* **3D Retro Text Effect**: Simulates a 3D block-extrusion shadow on each character for a vintage look.
* **Dynamic Centering**: Automatically calculates letter dimensions and padding to center multiline text blocks on any canvas size.
* **macOS & Cross-Platform Font Support**: Configured to look for bold fonts like `Impact` or `Arial Bold` with automatic fallbacks.

## Output Preview

The script generates an image with the following structure:
* **Background**: Dark purple border surrounding a green inner canvas.
* **Text Block**: 
  ```text
  Happy Birthday
    Friend's Name
      2026 or Year
