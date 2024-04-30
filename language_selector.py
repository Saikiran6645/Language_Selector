import os
from pynput import keyboard

# ANSI color codes
BLUE = '\033[94m'
ENDC = '\033[0m'

# Dictionary containing language options
languages = {
    1: "English",
    2: "Spanish",
    3: "French",
    4: "German",
    5: "Telugu ",
    6: "Hindi",
    7: "Malayalam",
    8: "Korean",
    9: "Russian",
    10: "Arabic",
    11: "Portuguese",
    12: "Italian",
    13: "Dutch",
    14: "Swedish",
    15: "Turkish",
    16: "Polish",
    17: "Danish",
    18: "Finnish",
    19: "Norwegian",
    20: "Greek",
    21: "Czech",
    22: "Hungarian",
    23: "Thai",
    24: "Japanese",
    25: "Hebrew",
    26: "Indonesian",
    27: "Malay",
    28: "Vietnamese",
    29: "Romanian",
    30: "Ukrainian"
}

selected_language = 1

def show_languages():
    # Clear screen before displaying
    os.system('cls' if os.name == 'nt' else 'clear')

    # Print the list of languages with arrows
    print("Use arrow keys to select a language, then press Enter to confirm:\n")
    for key, value in languages.items():
        arrow = BLUE + "-->" + ENDC if key == selected_language else "   "
        print(f"{arrow} {key}. {value}")

def on_press(key):
    global selected_language
    try:
        if key == keyboard.Key.up:
            selected_language = max(1, selected_language - 1)
            show_languages()
        elif key == keyboard.Key.down:
            selected_language = min(30, selected_language + 1)
            show_languages()
        elif key == keyboard.Key.enter:
            print(f"\nYou selected {languages[selected_language]}.\n")
            exit()  # Exit directly after language selection
    except AttributeError:
        pass

def main():
    show_languages()
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
