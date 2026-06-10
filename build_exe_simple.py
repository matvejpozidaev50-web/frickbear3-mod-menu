#!/usr/bin/env python
"""Build standalone Windows executable - Simplified version."""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def main():
    """Build executable using PyInstaller."""
    
    print("=" * 70)
    print("🚀 Building Frickbear 3 Mod Menu EXE")
    print("=" * 70)
    
    # Install PyInstaller if needed
    print("\n📦 Checking PyInstaller...")
    try:
        import PyInstaller
    except ImportError:
        print("Installing PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "PyInstaller", "-q"])
    
    # Ensure build directories exist
    build_dir = Path("build")
    dist_dir = Path("dist")
    
    print("\n🧹 Cleaning previous builds...")
    for folder in [build_dir, "build", "__pycache__"]:
        if Path(folder).exists():
            shutil.rmtree(folder)
    
    dist_dir.mkdir(exist_ok=True)
    
    # Build executable
    print("\n🔨 Building executable (this may take 1-2 minutes)...")
    print("   Please wait while PyInstaller bundles Python and dependencies...\n")
    
    try:
        cmd = [
            sys.executable,
            "-m", "PyInstaller",
            "--onefile",
            "--console",
            "--name", "FrickbearModMenu",
            "--distpath", str(dist_dir),
            "--buildpath", str(build_dir),
            "--specpath", ".",
            "--hidden-import=src.core",
            "--hidden-import=src.mods",
            "--hidden-import=src.utils",
            "src/__main__.py"
        ]
        
        result = subprocess.run(cmd, capture_output=False)
        
        if result.returncode != 0:
            print("\n❌ Build failed!")
            sys.exit(1)
            
    except Exception as e:
        print(f"\n❌ Error during build: {e}")
        sys.exit(1)
    
    # Verify executable
    exe_path = dist_dir / "FrickbearModMenu.exe"
    
    if exe_path.exists():
        exe_size = exe_path.stat().st_size / (1024 * 1024)
        print(f"\n✅ SUCCESS! EXE created!")
        print(f"   Location: {exe_path.absolute()}")
        print(f"   Size: {exe_size:.1f} MB")
        print(f"\n🎮 You can now:")
        print(f"   1. Double-click: {exe_path.absolute()}")
        print(f"   2. Or run: FrickbearModMenu.exe from dist/ folder")
        print(f"\n📦 Distribution ready in: {dist_dir.absolute()}")
        return 0
    else:
        print(f"\n❌ EXE not found at {exe_path}")
        print("Check the build output for errors.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
