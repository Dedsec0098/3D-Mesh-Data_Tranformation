#!/usr/bin/env python3
"""
Script to create submission ZIP file for Mesh Data Transformation Assignment
Author: Shrish Mishra
Date: November 10, 2025
"""

import os
import zipfile
from pathlib import Path
from datetime import datetime

def create_submission_zip():
    """
    Creates a ZIP file containing all submission materials:
    - Jupyter notebook
    - README.md
    - Input meshes (8samples/)
    - Output meshes (processed_meshes/)
    - All visualizations are in the notebook
    """
    
    # Define the base directory
    base_dir = Path(__file__).parent
    
    # Create ZIP filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_filename = f"Mesh_Data_Transformation_Submission_{timestamp}.zip"
    zip_path = base_dir / zip_filename
    
    print(f"\n{'='*70}")
    print(f"Creating Submission ZIP File")
    print(f"{'='*70}\n")
    
    # Files and folders to include
    items_to_include = {
        'required': [
            'Mesh_Data_Transformation.ipynb',
            'README.md',
            '8samples',
            'processed_meshes'
        ],
        'optional': [
            'requirements.txt',
            'create_submission_zip.py'
        ]
    }
    
    # Create the ZIP file
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        files_added = 0
        
        # Add required items
        print("Adding required files and folders:\n")
        for item_name in items_to_include['required']:
            item_path = base_dir / item_name
            
            if item_path.exists():
                if item_path.is_file():
                    # Add single file
                    arcname = item_name
                    zipf.write(item_path, arcname)
                    file_size = item_path.stat().st_size
                    print(f"  ✓ Added file: {item_name} ({file_size:,} bytes)")
                    files_added += 1
                    
                elif item_path.is_dir():
                    # Add directory and all its contents
                    folder_files = 0
                    for root, dirs, files in os.walk(item_path):
                        # Add directory
                        arcname = os.path.relpath(root, base_dir)
                        zipf.write(root, arcname)
                        
                        # Add files in directory
                        for file in files:
                            file_path = Path(root) / file
                            arcname = os.path.relpath(file_path, base_dir)
                            zipf.write(file_path, arcname)
                            folder_files += 1
                            files_added += 1
                    
                    print(f"  ✓ Added folder: {item_name}/ ({folder_files} files)")
            else:
                print(f"  ✗ Warning: {item_name} not found - skipping")
        
        # Add optional items if they exist
        print("\nAdding optional files:\n")
        for item_name in items_to_include['optional']:
            item_path = base_dir / item_name
            if item_path.exists() and item_path.is_file():
                arcname = item_name
                zipf.write(item_path, arcname)
                file_size = item_path.stat().st_size
                print(f"  ✓ Added file: {item_name} ({file_size:,} bytes)")
                files_added += 1
            else:
                print(f"  - Skipped: {item_name} (not found)")
    
    # Get final ZIP file size
    zip_size = zip_path.stat().st_size
    zip_size_mb = zip_size / (1024 * 1024)
    
    # Print summary
    print(f"\n{'='*70}")
    print(f"ZIP File Created Successfully!")
    print(f"{'='*70}\n")
    print(f"Filename: {zip_filename}")
    print(f"Location: {zip_path}")
    print(f"Size: {zip_size:,} bytes ({zip_size_mb:.2f} MB)")
    print(f"Total files added: {files_added}")
    print(f"\n{'='*70}")
    print(f"Submission Checklist:")
    print(f"{'='*70}\n")
    print(f"  ✓ Python notebook (Mesh_Data_Transformation.ipynb)")
    print(f"  ✓ Output meshes (processed_meshes/ folder)")
    print(f"  ✓ Visualizations (embedded in notebook)")
    print(f"  ✓ README file (with instructions and observations)")
    print(f"\n{'='*70}")
    print(f"\nYour submission is ready! 🎉")
    print(f"\nNext steps:")
    print(f"  1. Verify the ZIP contents by extracting it")
    print(f"  2. Test run the notebook from the extracted folder")
    print(f"  3. Submit the ZIP file")
    print(f"\n{'='*70}\n")
    
    return zip_path

if __name__ == "__main__":
    try:
        zip_path = create_submission_zip()
        print(f"✓ Success! ZIP file created at:\n  {zip_path}\n")
    except Exception as e:
        print(f"\n✗ Error creating ZIP file: {e}\n")
        import traceback
        traceback.print_exc()
