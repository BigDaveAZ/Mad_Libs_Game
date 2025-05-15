# Mad Libs Game by Devin Lawrence

This project includes three Python scripts and a CSV file to create a Mad Libs game, progressing from basic to complex implementations. Each script builds on the previous one, adding features and complexity. The CSV file stores multiple Mad Lib stories used by the complex version. Below is an explanation of how to use the files, their development progression, and instructions for editing the CSV file to add or remove Mad Lib options.

## Files Overview

1. **Mad_Libs_Devin_Lawrence_Basic.py**: A simple console-based Mad Libs game with one hardcoded story.
2. **Mad_Libs_Devin_Lawrence_mid.py**: An enhanced console-based version with input validation and a longer, more dynamic story.
3. **Mad_Libs_Devin_Lawrence_Complex.py**: A GUI-based version (with console fallback) that reads stories from a CSV file, supports multiple stories, and includes advanced features like a logo and row selection.
4. **mad_libs.csv**: A CSV file containing 50 Mad Lib stories, used by the complex version.

## Prerequisites

- **Python 3.6+**: Ensure Python is installed (download from [python.org](https://www.python.org)).
- **Required Libraries** (for the complex version):
  - Install using pip:
    ```bash
    pip install Pillow requests
    ```
  - **Tkinter**: Usually included with Python. If not, install it:
    - **Ubuntu/Debian**: `sudo apt-get install python3-tk`
    - **Fedora**: `sudo dnf install python3-tkinter`
    - **macOS/Windows**: Typically bundled with Python.
- **Files**: Place all four files (`Mad_Libs_Devin_Lawrence_Basic.py`, `Mad_Libs_Devin_Lawrence_mid.py`, `Mad_Libs_Devin_Lawrence_Complex.py`, `mad_libs.csv`) in the same directory.

## Using the Files

### 1. Basic Version (`Mad_Libs_Devin_Lawrence_Basic.py`)

**Description**: This is the simplest version, designed as a starting point. It prompts the user for seven words (animal, place, object, action, color, food, adjective) and inserts them into a single hardcoded story. The story is printed to the console.

**How to Use**:
1. Open a terminal or command prompt.
2. Navigate to the directory containing the file.
3. Run the script:
   ```bash
   python Mad_Libs_Devin_Lawrence_Basic.py
   ```
4. Enter the prompted words (e.g., "penguin" for animal, "zoo" for place).
5. View the generated story in the console, e.g.:
   ```
   In the sparkly land of zoo, a blue penguin named Steve roamed...
   ```

**Features**:
- Simple input/output via console.
- One fixed story.
- No input validation (accepts any input, including numbers or symbols).

### 2. Mid Version (`Mad_Libs_Devin_Lawrence_mid.py`)

**Description**: This version improves on the basic version by adding input validation, a welcome message, and a longer, more engaging story. It ensures adjectives contain only letters and provides clearer prompts tailored to a young audience.

**How to Use**:
1. Open a terminal or command prompt.
2. Navigate to the directory containing the file.
3. Run the script:
   ```bash
   python Mad_Libs_Devin_Lawrence_mid.py
   ```
4. Follow the prompts to enter seven words (adjective, noun, verb ending in -ing, animal, place, object, another adjective). Invalid inputs (e.g., numbers for adjectives) will prompt re-entry.
5. View the multi-sentence story in the console, e.g.:
   ```
   In the sparkly zoo, a fuzzy penguin was running with a donut! Suddenly, the heroic Devin zoomed in...
   ```

**Features**:
- Input validation for adjectives (letters only).
- Descriptive prompts (e.g., "Pick a cool adjective (like 'sparkly' or 'gross')").
- Longer, more dynamic story with Devin as the hero.
- Fun welcome and closing messages.

### 3. Complex Version (`Mad_Libs_Devin_Lawrence_Complex.py`)

**Description**: The most advanced version, featuring a Tkinter GUI (with a console fallback if Tkinter fails). It reads 50 stories from `mad_libs.csv`, allows users to select a specific story or a random one, displays a logo, and supports replaying with different stories or inputs. The GUI includes buttons for submitting, resetting, and resubmitting with a different story.

**How to Use**:
1. Ensure dependencies are installed:
   ```bash
   pip install Pillow requests
   ```
2. Place `mad_libs.csv` in the same directory as the script.
3. Open a terminal or command prompt and navigate to the directory.
4. Run the script:
   ```bash
   python Mad_Libs_Devin_Lawrence_Complex.py
   ```
5. **GUI Mode** (default):
   - A window (500x850) opens with a logo, a dropdown to select a story (Row ID or "Random"), and seven input fields.
   - Enter words in the fields (e.g., "sparkly", "pizza", "running").
   - Click "Submit" to view the story in a new window (1000x800).
   - Use buttons ("Done?", "Close All", "Restart", "Run Different Mad Lib") to continue, reset, or try another story.
   - If inputs are invalid (e.g., numbers or empty fields), a warning appears.
6. **Console Mode** (if Tkinter fails):
   - Lists available Row IDs (1–50).
   - Enter a Row ID or press Enter for random.
   - Input seven words as prompted, with validation (letters only, verb must end in -ing).
   - View the story and choose options (1: new Mad Lib, 2: different Mad Lib with same inputs, 3: quit).

**Features**:
- GUI with a teal background, logo, and wide input fields.
- Reads stories from `mad_libs.csv` (50 unique stories).
- Story selection via dropdown (GUI) or input (console).
- Input validation (letters only, verb ends in -ing).
- Buttons to reset inputs or reuse inputs with a different story.
- Console fallback for systems without Tkinter.
- Error handling for missing CSV or invalid inputs.

## Development Progression

The scripts were developed in order of increasing complexity, each building on the previous one to enhance functionality and user experience. The development reflects a learning progression suitable for a young coder.

1. **Basic Version** (May 9, 2025):
   - **Purpose**: Introduce basic Python concepts (input, print, string formatting).
   - **Development**: Created as a simple script to collect seven inputs and format them into a short story. The focus was on understanding user input and string concatenation.
   - **Challenges**: No input validation, so users could enter numbers or symbols, potentially breaking the story's flow.
   - **Outcome**: A functional but limited script, easy to understand for beginners.

2. **Mid Version** (May 9, 2025):
   - **Purpose**: Add input validation and improve story engagement.
   - **Development**: Built on the basic version by introducing a function (`is_valid_word`) to check for letters-only inputs for adjectives. The story was expanded to multiple sentences, with more creative prompts and a heroic narrative featuring Devin. Welcome and closing messages were added for a polished feel.
   - **Challenges**: Ensuring validation didn’t frustrate users; prompts were made descriptive (e.g., suggesting "sparkly" or "gross") to guide input.
   - **Outcome**: A more robust script with better user interaction, still console-based but with a professional touch.

3. **Complex Version** (May 14, 2025):
   - **Purpose**: Create a professional-grade application with a GUI and multiple stories.
   - **Development**: Transitioned to a GUI using Tkinter, with a fallback console mode. Integrated CSV reading (`mad_libs.csv`) to support 50 stories, each with unique prompts and narratives. Added features like a logo (fetched via `requests` and displayed with `Pillow`), story selection, and buttons for flexible gameplay. Input validation was enhanced (verb must end in -ing), and error handling was added for missing CSV or invalid inputs.
   - **Challenges**: Managing Tkinter’s event-driven model, ensuring CSV compatibility, and handling network errors for the logo. The console fallback was added to ensure accessibility.
   - **Outcome**: A feature-rich application suitable for classroom or personal use, with a modern GUI and robust functionality.

## Editing and Modifying the CSV File (`mad_libs.csv`)

The `mad_libs.csv` file contains 50 Mad Lib stories, each with a unique `row_id`, story template, and prompts for seven inputs (`adjective1`, `noun1`, `verb1`, `animal`, `place`, `object`, `adjective2`). You can edit this file to add new stories, modify existing ones, or remove stories. The file is used only by the complex version.

### CSV Structure

Each row has the following columns:
- `row_id`: A unique identifier (e.g., "1", "2"). Must be unique and non-empty.
- `story`: The story template with placeholders (e.g., `{adjective1}`, `{noun1}`). Must include all seven placeholders exactly once.
- `adjective1_prompt`, `noun1_prompt`, `verb1_prompt`, `animal_prompt`, `place_prompt`, `object_prompt`, `adjective2_prompt`: Prompts for each input, displayed in the GUI or console (e.g., "Pick a sick adjective (like 'rad' or 'gross'): ").

### Editing Guidelines

1. **Open the CSV**:
   - Use a text editor (e.g., Notepad, VS Code) or a spreadsheet program (e.g., Excel, Google Sheets).
   - If using a spreadsheet, save as CSV with UTF-8 encoding to avoid formatting issues.

2. **Add a New Story**:
   - Append a new row with a unique `row_id` (e.g., "51").
   - Write a story template using the seven placeholders `{adjective1}`, `{noun1}`, `{verb1}`, `{animal}`, `{place}`, `{object}`, `{adjective2}`. Ensure each placeholder appears exactly once.
   - Provide prompts for each input, keeping the tone fun and age-appropriate (e.g., "Pick a wacky animal (like 'zebra' or 'sloth'): ").
   - Example new row:
     ```csv
     51,"Devin found a {adjective1} {animal} in a {place}, {verb1} with a {object}! He grabbed a {noun1} and said, 'This {adjective2} {place} needs chaos!' They built a {adjective2} {noun1} castle, {verb1} like pros. The {animal} shouted, 'This {adjective1} day rocks!'","Pick a crazy adjective (like 'wild' or 'goofy'): ","Pick a noun (like 'ball' or 'cake'): ","Pick a verb ending in -ing (like 'jumping' or 'spinning'): ","Pick a cool animal (like 'zebra' or 'sloth'): ","Pick a fun place (like 'jungle' or 'mall'): ","Pick a weird object (like 'spoon' or 'wig'): ","Pick another adjective (like 'awesome' or 'strange'): "
     ```

3. **Modify an Existing Story**:
   - Locate the row by `row_id`.
   - Edit the `story` or prompt fields as needed, ensuring all seven placeholders remain in the story.
   - Example: Change the story for `row_id` 1:
     ```csv
     1,"Devin and a {adjective1} {animal} were {verb1} in a {place} with a {object}! He used a {noun1} to make a {adjective2} party. The {animal} said, 'This {adjective1} {place} is awesome!'","Pick a sick adjective (like 'rad' or 'gross'): ","Pick a random noun (like 'sneaker' or 'pizza'): ","Pick a verb ending in -ing (like 'smashing' or 'dabbing'): ","Pick a weird animal (like 'dinosaur' or 'axolotl'): ","Pick a dope place (like 'skate park' or 'haunted house'): ","Pick a funny object (like 'burrito' or 'slime'): ","Pick another adjective (like 'lit' or 'sketchy'): "
     ```

4. **Remove a Story**:
   - Delete the entire row for the desired `row_id`.
   - Ensure at least one row remains, as an empty CSV will cause an error in the complex version.
   - Example: To remove `row_id` 50, delete its row.

5. **Save the File**:
   - Save as `mad_libs.csv` in the same directory as `Mad_Libs_Devin_Lawrence_Complex.py`.
   - Use UTF-8 encoding to support special characters.
   - If using a spreadsheet, export as CSV (comma-separated, no extra formatting).

6. **Test Changes**:
   - Run the complex version:
     ```bash
     python Mad_Libs_Devin_Lawrence_Complex.py
     ```
   - Select the modified/added `row_id` in the GUI dropdown or console prompt to verify the story and prompts.
   - Check for errors (e.g., missing placeholders or invalid CSV format).

### CSV Editing Tips

- **Consistency**: Ensure all rows have exactly nine columns (`row_id`, `story`, seven prompts).
- **Placeholders**: The story must use `{adjective1}`, `{noun1}`, `{verb1}`, `{animal}`, `{place}`, `{object}`, `{adjective2}` exactly once. Missing or extra placeholders will cause errors.
- **Unique Row IDs**: Avoid duplicate `row_id` values to prevent selection issues.
- **Tone**: Keep stories and prompts fun, silly, and appropriate for a young audience (e.g., a 13-year-old’s perspective).
- **Backup**: Save a copy of `mad_libs.csv` before editing to avoid accidental data loss.
- **Validation**: The script validates inputs (letters only, verb ends in -ing), so prompts should reflect these constraints (e.g., "Pick a verb ending in -ing").

### Common CSV Errors

- **Missing CSV**: Ensure `mad_libs.csv` is in the same directory as the script.
- **Invalid Format**: Check for correct commas and no extra spaces or quotes.
- **Placeholder Mismatch**: Verify each story has all seven placeholders.
- **Empty File**: Keep at least one valid row to avoid errors.

## Troubleshooting

- **Basic/Mid Versions**:
  - If the script doesn’t run, ensure Python is installed (`python --version`).
  - Check for typos in the filename or path.
- **Complex Version**:
  - **GUI Fails**: If Tkinter is unavailable, the script falls back to console mode. Install Tkinter (see Prerequisites).
  - **Logo Fails**: If the logo doesn’t load (network issue), the script skips it.
  - **CSV Errors**: Verify `mad_libs.csv` exists and follows the structure above.
  - **Dependency Issues**: Reinstall Pillow and requests:
    ```bash
    pip install Pillow requests
    ```
- **General**: Ensure all files are in the same directory. Use `python3` instead of `python` if needed on Linux/macOS.

## Notes

- The scripts are designed for a young audience, with a 13-year-old’s voice in the stories (e.g., slang like "yo", "bruh", "lit").
- The complex version is the most versatile, supporting multiple stories and a user-friendly GUI.
- Editing `mad_libs.csv` allows infinite customization without changing the Python code.
- The project was developed as a school assignment (5th Hour, May 2025) by Devin Lawrence.

For questions or issues, refer to the console/GUI error messages or contact the developer (hypothetically, Devin Lawrence). Have fun creating wacky Mad Libs!