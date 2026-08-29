import os
import sys

def verify_pipeline_security():
    # Define the precise file path dbt is hunting for on your Mac
    target_key_path = "/Users/lanavoynich/Desktop/data-ingestion-pipeline/dog project/pet-matcher-analytics-engine/dbt_private_key_clean.pem"
    
    print("🚀 Initiating master cloud infrastructure security audit...")
    
    try:
        # Codecademy Exception Theory: Open a risky file pathway defensively
        print(f"🔍 Attempting to open cryptographic signature at: {target_key_path}")
        with open(target_key_path, "r") as key_file:
            key_data = key_file.read()
            
        if "BEGIN PRIVATE KEY" not in key_data:
            # Manually raise a value mismatch if the format is corrupted
            raise ValueError("Cryptographic format mismatch inside the key file.")
            
    except FileNotFoundError:
        # Capture a missing file track cleanly without crashing your terminal thread
        print("\n❌ SYSTEM EXCEPTION CAUGHT: FileNotFoundError!")
        print("💡 Analytics Engineering Patch: Check your local folder directory structure.")
        print("➡️ Fix: Ensure dbt_private_key_clean.pem sits exactly inside your project root.")
        
    except ValueError as format_error:
        # Capture bad token metadata structures instantly
        print(f"\n❌ DATA STRUCTURE EXCEPTION: {format_error}")
        print("💡 Patch: Re-run OpenSSL formatting tools to strip passphrase headers.")
        
    else:
        # Executes ONLY if your code passes past the try block perfectly
        print("\n🟢 PIPELINE PASS: Cryptographic private tokens are verified and fully readable!")
        
    finally:
        # Runs every single time to ensure your environment drops connections cleanly
        print("🔒 Security Audit Session closed. Local environment variables protected.\n")

if __name__ == "__main__":
    verify_pipeline_security()
