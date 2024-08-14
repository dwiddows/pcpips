import matplotlib.pyplot as plt
import os
import argparse

# Define card suits with their Unicode symbols
CARD_SUITS = {
    'hearts': '\u2665',
    'diamonds': '\u2666',
    'clubs': '\u2663',
    'spades': '\u2660'
}

SIDE_MARGIN = 0.5
TOP_MARGIN = 0.5
BOX_WIDTH = 2
BOX_HEIGHT = 3

# Define colors for the suits
RED_COLOR = '#E80000'  # You can experiment with colors here
COLORS = {
    'hearts': RED_COLOR,
    'diamonds': RED_COLOR,
    'clubs': 'black',
    'spades': 'black'
}

# Define the coordinates for the pips for each number card.
PIP_LAYOUTS = {
    '2': [(0.5, 60), (0.5, 0)],  # Vertical alignment
    '3': [(0.5, 60), (0.5, 30), (0.5, 0)],  # Vertical alignment
    '4': [(0.1, 60), (0.9, 60), (0.1, 0), (0.9, 0)],
    '5': [(0.1, 60), (0.9, 60), (0.5, 30), (0.1, 0), (0.9, 0)],
    '6': [(0.1, 60), (0.9, 60), (0.1, 30), (0.9, 30), (0.1, 0), (0.9, 0)],
    '7': [(0.1, 60), (0.9, 60), (0.1, 30), (0.9, 30), (0.1, 0), (0.9, 0), (0.5, 45)],
    '8': [(0.1, 60), (0.9, 60), (0.1, 30), (0.9, 30), (0.1, 0), (0.9, 0), (0.5, 45), (0.5, 15)],
    '9': [(0.1, 60), (0.9, 60), (0.1, 40), (0.9, 40), (0.1, 20), (0.9, 20), (0.1, 0), (0.9, 0),
          (0.5, 30)],  # One pip in the middle
    '10': [(0.1, 60), (0.9, 60), (0.1, 40), (0.9, 40), (0.1, 20), (0.9, 20), (0.1, 0), (0.9, 0),
           (0.5, 50), (0.5, 10)]  # Two pips in the middle column
}


def save_card(value, suit, coords, output_dir, corners=False):
    """Save a single card as a PNG file."""
    fig_size = (BOX_WIDTH + 2*SIDE_MARGIN, BOX_HEIGHT + 2*TOP_MARGIN) if corners else (BOX_WIDTH, BOX_HEIGHT)
    fig, ax = plt.subplots(figsize=fig_size)

    ax.set_xlim(0, BOX_WIDTH + 2 * SIDE_MARGIN if corners else BOX_WIDTH)
    ax.set_ylim(0, BOX_HEIGHT + 2 * TOP_MARGIN if corners else BOX_HEIGHT)
    ax.axis('off')  # Hide axes

    symbol = CARD_SUITS[suit]
    color = COLORS[suit]

    x_shift, y_shift = 0, 0
    if corners:
        x_shift, y_shift = SIDE_MARGIN, TOP_MARGIN
        ax.text(0, BOX_HEIGHT + TOP_MARGIN * 2, f"{value}\n{symbol}", fontsize=24, color=color,
                ha='center', va='center', fontname='Times New Roman')
        ax.text(2 * SIDE_MARGIN + BOX_WIDTH, 0, f"{value}\n{symbol}", fontsize=24, color=color,
                ha='center', va='center', fontname='Times New Roman', rotation=180)

    # Plot the pips on the card
    for x, y in coords:
        ax.text(x * BOX_WIDTH + x_shift, (y / 60) * BOX_HEIGHT + y_shift, symbol,
                fontsize=60, color=color, ha='center', va='center', fontname='Times New Roman')

    filename = os.path.join(output_dir, f"{value}_{suit}.png")
    plt.savefig(filename, bbox_inches=None)  # Added margin with pad_inches
    plt.close(fig)


def generate_cards(output_dir, corners=False):
    """Generate all playing cards and save them to the specified directory."""
    os.makedirs(output_dir, exist_ok=True)

    for value, coords in PIP_LAYOUTS.items():
        for suit in CARD_SUITS:
            save_card(value, suit, coords, output_dir, corners=corners)


def main():
    parser = argparse.ArgumentParser(description="Generate playing cards as PNG images.")
    parser.add_argument('--output-dir', type=str, default='playing_cards',
                        help='Directory to save the generated playing cards.')
    parser.add_argument('--corners', action='store_true',
                        help='Add the number and suit symbol to the top left and bottom right corners.')
    args = parser.parse_args()

    generate_cards(args.output_dir, args.corners)


if __name__ == '__main__':
    main()
