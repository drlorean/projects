# SHA-256 Checksum Verifier

## Summary
A Python utility that verifies the integrity of files by comparing their calculated SHA-256 hash against an expected checksum. This tool is useful for ensuring files haven't been corrupted or altered during transfer or storage.

## Features
- ✅ Calculates SHA-256 hash of files efficiently using 4KB chunk reads (works with large files)
- ✅ Compares calculated checksum with expected value (case-insensitive)
- ✅ Comprehensive error handling (file not found, permission denied, unexpected errors)
- ✅ User-friendly output with clear success/failure messages
- ✅ Handles quotes in file paths (supports drag-and-drop input)

## Usage
Run the script and provide:
1. The file path to verify
2. The expected SHA-256 checksum

## Example:
python checksum_verifier.py
Enter the file path to verify: /path/to/file.txt
Enter the expected SHA-256 checksum: a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3