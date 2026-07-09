# Created: 2026-06-30 by Antigravity AI
# Purpose: Local Marker PoC test script for parsing PDF documents

import os
import sys
from marker.convert import convert_single_pdf
from marker.models import load_all_models
from marker.output import save_markdown

def main():
    if len(sys.argv) < 2:
        print("Usage: python test_marker.py [pdf_path]")
        sys.exit(1)
        
    pdf_path = sys.argv[1]
    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
        sys.exit(1)
        
    print("Loading Marker models (This may take a moment on first run to download model weights)...")
    langs = ["ko", "en"]
    model_lst = load_all_models()
    
    print(f"Parsing document: {pdf_path}")
    full_text, images, out_meta = convert_single_pdf(pdf_path, model_lst, langs=langs)
    
    print("\n=== PARSED MARKDOWN (PREVIEW) ===")
    print(full_text[:2000])  # Print first 2000 characters
    print("==================================\n")
    
    # Save output
    output_dir = "/home/caiser77/dgx_workspace/scratch/output"
    os.makedirs(output_dir, exist_ok=True)
    
    subfolder, file_prefix = save_markdown(
        output_dir, 
        os.path.basename(pdf_path).replace(".pdf", ""), 
        full_text, 
        images, 
        out_meta
    )
    print(f"✓ Saved parsed markdown & images successfully to: {output_dir}")

if __name__ == "__main__":
    main()
