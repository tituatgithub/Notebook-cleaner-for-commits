#!/usr/bin/env python3
"""
JupyterClean - Notebook Cleaner Tool
-------------------------------------

Removes metadata, outputs, and execution counts from Jupyter notebooks (.ipynb)
to make them clean and version-control friendly.

Usage:
    python clean_notebook.py notebook.ipynb
    python clean_notebook.py notebook1.ipynb notebook2.ipynb notebook3.ipynb

Author: Your Name
License: MIT
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path


def clean_notebook(notebook_path):
    """
    Clean a single Jupyter notebook by removing outputs, execution counts, and metadata.
    
    Args:
        notebook_path (str): Path to the notebook file
        
    Returns:
        bool: True if successful, False otherwise
    """
    if not os.path.exists(notebook_path):
        print(f"❌ File not found: {notebook_path}")
        return False
    
    if not notebook_path.endswith('.ipynb'):
        print(f"⚠️  Skipping {notebook_path} (not a .ipynb file)")
        return False

    print(f"🧹 Cleaning notebook: {notebook_path}")

    cmd = [
        "jupyter", "nbconvert",
        "--ClearOutputPreprocessor.enabled=True",
        "--ClearMetadataPreprocessor.enabled=True",
        "--to", "notebook",
        "--inplace",
        notebook_path
    ]

    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(f"✅ Successfully cleaned: {notebook_path}\n")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error while cleaning {notebook_path}:")
        print(f"   {e.stderr}")
        return False
    except FileNotFoundError:
        print("❌ Error: 'jupyter' command not found.")
        print("   Please install jupyter with: pip install jupyter nbconvert")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Clean Jupyter notebooks by removing outputs, execution counts, and metadata.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python clean_notebook.py notebook.ipynb
  python clean_notebook.py notebook1.ipynb notebook2.ipynb
  python clean_notebook.py notebooks/*.ipynb
        """
    )
    
    parser.add_argument(
        'notebooks',
        nargs='+',
        help='Path(s) to notebook file(s) to clean'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='JupyterClean 1.0.0'
    )
    
    args = parser.parse_args()
    
    if len(args.notebooks) == 0:
        parser.print_help()
        sys.exit(1)
    
    # Process all notebooks
    total = len(args.notebooks)
    success = 0
    
    print(f"\n{'='*60}")
    print(f"JupyterClean - Cleaning {total} notebook(s)")
    print(f"{'='*60}\n")
    
    for notebook_path in args.notebooks:
        if clean_notebook(notebook_path):
            success += 1
    
    print(f"{'='*60}")
    print(f"✨ Cleaned {success}/{total} notebook(s) successfully")
    print(f"{'='*60}\n")
    
    if success < total:
        sys.exit(1)


if __name__ == "__main__":
    main()
