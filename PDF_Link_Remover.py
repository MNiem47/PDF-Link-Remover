import pikepdf
import sys
import os

def remove_links(input_path, output_path):
    try:
        with pikepdf.open(input_path) as pdf:
            removed_count = 0
            
            for page in pdf.pages:
                if "/Annots" in page:
                    new_annots = [
                        annot for annot in page.Annots 
                        if annot.get("/Subtype") != "/Link"
                    ]
                    
                    if len(new_annots) != len(page.Annots):
                        removed_count += (len(page.Annots) - len(new_annots))
                        
                    if not new_annots:
                        del page.Annots
                    else:
                        page.Annots = new_annots

            pdf.save(output_path)
            print(f"Success! Removed links: {removed_count}")
            print(f"File saved as: {output_path}")

    except Exception as e:
        print(f"Error occured: {e}")


def main():
    args = sys.argv[1:]

    if len(args) >= 1:
        source = args[0]
    else:
        source = input("Path to source file: ").strip().replace('"', '')

    if not os.path.exists(source):
        print(f"Error occured: File '{source}' does not exist.")
        return

    if len(args) >= 2:
        destination = args[1]
    else:
        base, ext = os.path.splitext(source)
        destination = f"{base}_wolinks{ext}"
        print(f"Destination file path not provided. Saved as: {os.path.basename(destination)}")

    remove_links(source, destination)

if __name__ == "__main__":
    main()
    input("Press Enter to exit...")