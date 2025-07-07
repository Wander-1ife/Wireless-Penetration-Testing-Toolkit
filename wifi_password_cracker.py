import os

def crack_wifi_password():
    cmd=os.system("clear")
    print("\n=== Cracking Password Using HandShake File ===")
    print("\nEnter the ESSID of the network (case-sensitive, in quotes if it contains spaces):")
    essid = input(">>> ").strip()

    print("\nEnter the path to the captured handshake file:")
    path = input(">>> ").strip()

    print("\nEnter the minimum password length (8-64):")
    mini = int(input(">>> ").strip())

    print("\nEnter the maximum password length (8-64):")
    max_len = int(input(">>> ").strip())

    print("\nEnter the path to save the generated wordlist (e.g., wordlist.txt):")
    wordlist_path = input(">>> ").strip()

    print("""
---------------------------------------------------------------------------------------
(1)  Lowercase chars                                 (abcdefghijklmnopqrstuvwxyz)
(2)  Uppercase chars                                 (ABCDEFGHIJKLMNOPQRSTUVWXYZ)
(3)  Numeric chars                                   (0123456789)
(4)  Symbol chars                                    (!#$%/=?{}[]-*:;)
(5)  Lowercase + Uppercase
(6)  Lowercase + Numeric
(7)  Uppercase + Numeric
(8)  Symbol + Numeric
(9)  Lowercase + Uppercase + Numeric
(10) Lowercase + Uppercase + Symbols
(11) Lowercase + Uppercase + Numeric + Symbols
(12) Custom characters/words
-----------------------------------------------------------------------------------------
⚠️ Brute-force cracking can take hours, days, or even longer.
""")
    charset_options = {
        "1": "abcdefghijklmnopqrstuvwxyz",
        "2": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "3": "0123456789",
        "4": "!#$%/=?{}[]-*:;",
        "5": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "6": "abcdefghijklmnopqrstuvwxyz0123456789",
        "7": "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
        "8": "!#$%/=?{}[]-*:;0123456789",
        "9": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
        "10": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%/=?{}[]-*:;",
        "11": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%/=?{}[]-*:;",
    }

    print("\nEnter your choice (1-12):")
    choice = input(">>> ").strip()

    if choice in charset_options:
        charset = charset_options[choice]
    elif choice == "12":
        print("Enter your custom characters or words:")
        charset = input(">>> ").strip()
    else:
        print("❌ Invalid option selected.")
        return

    print("\n[+] Generating wordlist and saving to file...\n")
    try:
        # Generate the wordlist with crunch and save to file
        crunch_command = f"crunch {mini} {max_len} {charset} -o {wordlist_path}"
        os.system(crunch_command)

        print("\n[✓] Wordlist saved to", wordlist_path)
        print("[+] Starting password cracking using aircrack-ng...\n")

        aircrack_command = f"aircrack-ng {path} -e '{essid}' -w {wordlist_path}"
        os.system(aircrack_command)

    except KeyboardInterrupt:
        print("\n[!] Cracking interrupted by user.")
    finally:
        os.system("sleep 3")
        print("\n[✓] Cracking process finished. If successful, the password will be shown above.")
