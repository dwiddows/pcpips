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

# Define x-coordinates for pip placement
LEFT = 0.1
MID = 0.5
RIGHT = 0.9

# Define the coordinates for each card value with the specified layouts for 8, 9, and 10
PIP_LAYOUTS = {
    '2': [(MID, 70), (MID, 10)],  # Vertical alignment
    '3': [(MID, 70), (MID, 40), (MID, 10)],  # Vertical alignment
    '4': [(LEFT, 70), (RIGHT, 70), (LEFT, 10), (RIGHT, 10)],
    '5': [(LEFT, 70), (RIGHT, 70), (MID, 40), (LEFT, 10), (RIGHT, 10)],
    '6': [(LEFT, 70), (RIGHT, 70), (LEFT, 40), (RIGHT, 40), (LEFT, 10), (RIGHT, 10)],
    '7': [(LEFT, 70), (RIGHT, 70), (LEFT, 40), (RIGHT, 40), (LEFT, 10), (RIGHT, 10), (MID, 55)],
    '8': [(LEFT, 70), (RIGHT, 70), (LEFT, 40), (RIGHT, 40), (LEFT, 10), (RIGHT, 10), (MID, 55), (MID, 25)],
    '9': [(LEFT, 70), (RIGHT, 70), (LEFT, 50), (RIGHT, 50),
          (LEFT, 30), (RIGHT, 30), (LEFT, 10), (RIGHT, 10),
          (MID, 40)],  # One pip in the middle
    '10': [(LEFT, 70), (RIGHT, 70), (LEFT, 50), (RIGHT, 50),
           (LEFT, 30), (RIGHT, 30), (LEFT, 10), (RIGHT, 10),
           (MID, 60), (MID, 20)]  # Two pips in the middle
}

# Define colors for the suits
RED_COLOR = '#E80000'  # You can experiment with colors here
COLORS = {
    'hearts': RED_COLOR,
    'diamonds': RED_COLOR,
    'clubs': 'black',
    'spades': 'black'
}


def setup_figure(corners=False):
    """Set up the figure size based on whether corners are included."""
    fig_size = (2.5, 3.5) if corners else (2, 3)
    fig, ax = plt.subplots(figsize=fig_size)
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 1)
    ax.axis('off')  # Hide axes
    return fig, ax


def add_corner_text(ax, value, symbol, color):
    """Add the corner text to the card."""
    ax.text(0, 1.2, f"{value}\n{symbol}", fontsize=24, color=color,
            ha='center', va='center', fontname='Times New Roman')
    ax.text(2.5, 0.05, f"{value}\n{symbol}", fontsize=24, color=color,
            ha='center', va='center', fontname='Times New Roman', rotation=180)


def save_card(value, suit, coords, output_dir, corners=False):
    """Save a single card as a PNG file."""
    fig, ax = setup_figure(corners)

    symbol = CARD_SUITS[suit]
    color = COLORS[suit]

    if corners:
        add_corner_text(ax, value, symbol, color)
        x_shift, y_shift = 0.12, 0.15
    else:
        x_shift, y_shift = 0, 0

    # Plot the pips on the card
    for x, y in coords:
        ax.text(2 * (x + x_shift), (y - 10) / 60 + y_shift, symbol, fontsize=60, color=color,
                ha='center', va='center', fontname='Times New Roman')

    filename = os.path.join(output_dir, f"{value}_{suit}.png")
    plt.savefig(filename, bbox_inches='tight', pad_inches=0.2)  # Added margin with pad_inches
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
