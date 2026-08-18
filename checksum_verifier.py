import hashlib
import os

def verify_sha256(file_path, expected_checksum):
    """
    Calculates the SHA-256 hash of a file and compares it to the expected checksum.
    """
    # Initialize the SHA-256 hash object
    sha256_hash = hashlib.sha256()

    try:
        # Open the file in binary mode ("rb")
        with open(file_path, "rb") as f:
            # Read the file in 4KB chunks so it doesn't crash on large files
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)

        # Get the final hexadecimal representation of the hash
        calculated_checksum = sha256_hash.hexdigest()

        print("\n--- Results ---")
        print(f"Calculated: {calculated_checksum}")
        print(f"Expected:   {expected_checksum.lower()}")

        # Compare the checksums (converting to lowercase to ignore case differences)
        if calculated_checksum == expected_checksum.lower().strip():
            print("\n✅ Match: The checksums are identical. The file is intact.")
            return True
        else:
            print("\n❌ Mismatch: The checksums DO NOT MATCH. The file may be corrupted or altered.")
            return False

    except FileNotFoundError:
        print(f"\n❌ Error: The file at '{file_path}' was not found.")
        return False
    except PermissionError:
        print(f"\n❌ Error: You do not have permission to read '{file_path}'.")
        return False
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")
        return False

if __name__ == "__main__":
    print("=== SHA-256 Checksum Verifier ===")
    
    # Get user input
    target_file = input("Enter the file path to verify: ").strip()
    
    # Strip quotes just in case the user dragged and dropped the file into the terminal
    target_file = target_file.strip('"').strip("'")
    
    target_hash = input("Enter the expected SHA-256 checksum: ").strip()
    
    if os.path.exists(target_file):
        verify_sha256(target_file, target_hash)
    else:
        print(f"\n❌ Error: The file path '{target_file}' does not exist.")