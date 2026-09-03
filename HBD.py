from PIL import Image, ImageDraw, ImageFont


def create_retro_birthday_card():
    img_width, img_height = 1000, 700

    # 1. Colors
    border_color = (66, 11, 102)  # Dark Purple
    green_bg = (156, 219, 78)  # Background Green
    pink_tile = (255, 182, 193)  # Pink background for letter boxes
    brown_face = (90, 42, 18)  # Brown letter face
    shadow_color = (230, 110, 140)  # Darker pink/brown for 3D extrude

    border_thickness = 40

    # Create main image canvas
    image = Image.new("RGB", (img_width, img_height), border_color)
    draw = ImageDraw.Draw(image)

    # Draw green background area
    inner_rect = [
        border_thickness,
        border_thickness,
        img_width - border_thickness,
        img_height - border_thickness
    ]
    draw.rectangle(inner_rect, fill=green_bg)

    # 2. Text Configuration
    lines = ["Happy Birthday", "FIZA BARI", "2026"]

    # Load Font
    font_size = 65
    font = None
    macos_fonts = [
        "/System/Library/Fonts/Supplemental/Impact.ttf",  # Impact gives a great retro block look
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/Library/Fonts/Arial Bold.ttf"
    ]

    for font_path in macos_fonts:
        try:
            font = ImageFont.truetype(font_path, font_size)
            break
        except OSError:
            continue
    if font is None:
        font = ImageFont.load_default()

    # Calculate line layout
    tile_padding = 8
    letter_spacing = 6
    line_spacing = 25

    # Calculate overall content height to center vertically
    total_height = 0
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        char_h = bbox[3] - bbox[1]
        total_height += (char_h + 2 * tile_padding) + line_spacing
    total_height -= line_spacing

    start_y = (img_height - total_height) // 2

    # 3. Draw each line with retro pink tiles & 3D brown text
    current_y = start_y
    for line in lines:
        # Measure line width
        line_width = 0
        for char in line:
            if char == ' ':
                line_width += 30
            else:
                bbox = draw.textbbox((0, 0), char, font=font)
                char_w = bbox[2] - bbox[0]
                line_width += (char_w + 2 * tile_padding) + letter_spacing
        line_width -= letter_spacing

        current_x = (img_width - line_width) // 2

        for char in line:
            if char == ' ':
                current_x += 30
                continue

            bbox = draw.textbbox((0, 0), char, font=font)
            char_w = bbox[2] - bbox[0]
            char_h = bbox[3] - bbox[1]

            box_w = char_w + 2 * tile_padding
            box_h = char_h + 2 * tile_padding

            # Pink background tile for each letter
            tile_rect = [current_x, current_y, current_x + box_w, current_y + box_h]
            draw.rectangle(tile_rect, fill=pink_tile)

            # Calculate letter placement inside tile
            text_x = current_x + tile_padding - bbox[0]
            text_y = current_y + tile_padding - bbox[1]

            # Draw 3D Extrusion Shadow (retro effect)
            depth = 5
            for i in range(depth, 0, -1):
                draw.text((text_x + i, text_y + i), char, font=font, fill=shadow_color)

            # Main Brown Letter Face
            draw.text((text_x, text_y), char, font=font, fill=brown_face)

            current_x += box_w + letter_spacing

        # Get line height for vertical increment
        bbox = draw.textbbox((0, 0), line, font=font)
        current_y += (bbox[3] - bbox[1] + 2 * tile_padding) + line_spacing

    # 4. Save and view result
    output_filename = "Retro_Fiza_Bari_Birthday.png"
    image.save(output_filename)
    print(f"Custom retro card saved as '{output_filename}'!")


create_retro_birthday_card()