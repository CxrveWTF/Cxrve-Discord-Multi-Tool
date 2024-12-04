import os
import random
import time
import string
import sys

# Some random functions to make it look more complex
def random_string(length):
    """Generate a random string."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def random_int():
    """Return a random integer."""
    return random.randint(1, 100)

def fake_work():
    """A fake function to make it look like we're doing some work."""
    print("Working on some important task...")
    time.sleep(1)
    print(f"Generating a random string: {random_string(10)}")
    print(f"Random integer: {random_int()}")
    time.sleep(2)
    print("Almost there...")

# Main function to launch the tool
def launch_tool():
    print("Preparing to launch the tool...")
    time.sleep(2)  # Simulate some setup time

    fake_work()  # Fake work for show

    # Path to the executable (adjust if necessary)
    exe_path = "Discord-Multi-Tool.exe"
    
    if os.path.exists(exe_path):
        print(f"Launching {exe_path}...")
        os.startfile(exe_path)  # Launch the .exe file
    else:
        print(f"Error: Could not find {exe_path}.")

if __name__ == "__main__":
    launch_tool()
