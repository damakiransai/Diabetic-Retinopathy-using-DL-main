"""
Helper script to download dr_binary_model.h5 from Google Drive.

Usage:
1. Get a shareable link from Google Drive (right-click file -> Get link -> Anyone with the link)
2. Extract the FILE_ID from the link (the long string between /d/ and /view)
3. Run: python download_model.py FILE_ID

Example:
If your link is: https://drive.google.com/file/d/1ABC123xyz456/view?usp=sharing
Then FILE_ID is: 1ABC123xyz456
Run: python download_model.py 1ABC123xyz456
"""

import sys
import os

def download_from_drive(file_id, output_path="dr_binary_model.h5"):
    """Download a file from Google Drive using gdown."""
    try:
        import gdown
    except ImportError:
        print("Installing gdown...")
        os.system("pip install gdown")
        import gdown
    
    # Construct the Google Drive download URL
    url = f"https://drive.google.com/uc?id={file_id}"
    
    print(f"Downloading model from Google Drive...")
    print(f"File ID: {file_id}")
    print(f"Output: {output_path}")
    
    gdown.download(url, output_path, quiet=False)
    
    if os.path.exists(output_path):
        file_size = os.path.getsize(output_path) / (1024 * 1024)  # MB
        print(f"\n✅ Success! Model downloaded: {output_path} ({file_size:.2f} MB)")
    else:
        print("\n❌ Error: File not found after download")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        print("\n" + "="*60)
        print("ERROR: Please provide the Google Drive FILE_ID")
        print("="*60)
        sys.exit(1)
    
    file_id = sys.argv[1]
    download_from_drive(file_id)
