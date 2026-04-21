# PDF Link Remover

A lightweight, lossless command-line tool to remove interactive "Point-and-Click" links from PDF files. Can be used with all PDF files, but originally created to get rid of the "blue boxes" in forScore app while reading LiliPond PDF files.

## Overview
By default, LilyPond embeds clickable links into PDFs that point back to the `.ly` source code. This tool allows you to strip these links in bulk while maintaining:
* **Perfect Vector Quality**: No re-rendering or rasterization occurs.
* **Small File Size**: No unnecessary metadata or bloat added.
* **Searchable Text**: Preserves the text layer (lyrics, titles, etc.) for easy searching.

## Download (Windows Users)
1. Download the latest `.exe` file from the **[Releases](../../releases)** section.
2. **Easy method** Simply drag and drop your PDF file onto the `.exe` file.
3. **To run via prompt:** Open the `.exe` file. When prompted, provide the path to your PDF. 
   > **Tip:** You can right-click your `.pdf` file in File Explorer, select **"Copy as path"**, and then paste it into the program window.
4. **To run via CMD/PowerShell:**
    ```bash
    ./PDF_Link_Remover.exe [Source_file_path] [Output_file_path]
    ```
    *If you don't provide an output path, the program will create a new file ending in `_wolinks.pdf` in the same folder.*

---

## Usage (Python Users)
1. **Clone the repository:**
    ```bash
    git clone https://github.com/MNiem47/PDF-Link-Remover.git
    cd PDF-Llink-Remover
    ```
2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *Remember that you can use virtual enviroments.*
3. **Run the script:**
    ```bash
    python PDF_Link_Remover.py [Source_file_path] [Output_file_path]
    ```
    *If no output path is specified, the script automatically generates a file with the `_wolinks.pdf` ending.*

---

## License
This project is licensed under the MIT License. Feel free to modify and distribute it as you wish.
