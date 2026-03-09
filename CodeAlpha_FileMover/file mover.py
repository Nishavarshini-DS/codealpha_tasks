#file mover program 
import os
import shutil
import time
import sys

def print_with_delay(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

print("""
╔════════════════════════════════════╗
║        JPG FILE MOVER              ║
║     Keep your photos organized     ║
╚════════════════════════════════════╝
""")

# FIX: Change to the directory where the program is located
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print_with_delay("\nMake sure the folder which contains the photos are in the same folder as this program !", 0.05)
initial_folder = input("📂 Source folder: ")
print_with_delay("\nThe target folder also should be in the folder the program is in", 0.05)
final_folder = input("📂 Destination folder: ")


# Convert to absolute paths
initial_folder = os.path.abspath(initial_folder)
final_folder = os.path.abspath(final_folder)

print(f"\nDebug: Source folder (absolute): {initial_folder}")
print(f"Debug: Destination folder (absolute): {final_folder}")

if not os.path.exists(initial_folder):
    print_with_delay("\n❌ Error: The initial folder doesn't exist!", 0.05)
    print_with_delay("👀 Please check the path and try again.", 0.05)
    exit()

if not os.path.exists(final_folder):
    print_with_delay(f"\n📁 Creating folder: {final_folder}")
    os.makedirs(final_folder)
    print("✅ Folder created!")

all_files = os.listdir(initial_folder)
print(f"\n📊 Found {len(all_files)} files in the initial folder ")
print("-" * 40)

counter = 0
spinner = "|/-\\"
for filename in all_files:
    if filename.lower().endswith('.jpg'):
        initial_path = os.path.join(initial_folder, filename)
        final_path = os.path.join(final_folder, filename)
        try:
            shutil.move(initial_path, final_path)
            counter += 1
            for i in range(4):
                sys.stdout.write(f"\r{spinner[i % 4]} Moving: {filename}... ")
                sys.stdout.flush()
                time.sleep(0.1)
            print(f"✅ Moved : {filename}")
        except PermissionError:
            print(f"⚠️ Can't move {filename} - Permission denied (file might be open)")
        except FileNotFoundError:
            print(f"⚠️ Can't move {filename} - File disappeared!")
        except Exception as e:
            print(f"⚠️ Can't move {filename} - Error: {e}")

print("-" * 40)
if counter == 0:
    print_with_delay("\n📭 No JPG files found in the source folder.", 0.05)
else:
    print_with_delay(f"\n🎉 Done! Moved {counter} JPG file(s)", 0.05)
    print_with_delay("👋 Goodbye!", 0.05)

input("\nPress Enter to exit...")    