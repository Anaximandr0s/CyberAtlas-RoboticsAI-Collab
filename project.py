import time
import os

# Function to clear the terminal screen (works for Windows and Linux/macOS)
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to print a big "Cyber Atlas Club" ASCII art banner
def print_figlet(sleep=True):
    clear()

    # Manually define the ASCII art for "Cyber Atlas Club"
    banner_text = """
   _____      _                         _   _           
  / ____|    | |                   /\  | | | |          
 | |    _   _| |__   ___ _ __     /  \ | |_| | __ _ ___ 
 | |   | | | | '_ \ / _ \ '__|   / /\ \| __| |/ _` / __|
 | |___| |_| | |_) |  __/ |     / ____ \ |_| | (_| \__ |
  \_____\__, |_.__/ \___|_|    /_/    \_\__|_|\__,_|___/
         __/ |                                          
        |___/     

    """
    
    # Colorize the banner text and print it
    print(banner_text)

    # Optional: Pause to build suspense
    if sleep:
        time.sleep(3)

# Main script to simulate the hacking prank
def main():
    clear()
    
    # Print the initial "hacked" message with ASCII art
    print_figlet(sleep=True)
    print("===================================================")
    print("🔥 WARNING: You have been HACKED by Cyber Atlas Club! 🔥")
    print("===================================================")
    time.sleep(3)  # Wait for 3 seconds to build suspense
    
    # Reveal the prank
    clear()  # Clear the screen again
    print("Just kidding, it's just a prank! 😆😆😆😆")
    print("Thank you for being here in this amazing session!")
    time.sleep(3)  # Display the message for a few seconds
    
    # End the script with a final clear
    clear()

if __name__ == "__main__":
    main()