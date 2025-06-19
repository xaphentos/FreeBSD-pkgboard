import os

def install(pkg_list):
    os.system(f"sudo pkg install -y {' '.join(pkg_list)}")

def main():
    while True:
        os.system("clear")
        print("--- Welcome to pkgboard - tool to install packages on FreeBSD ---\n")
        #list of all aviable packages:
        print("Web Browsers:")
        print("  1. Firefox")
        print("  2. Chromium")
        print("\nMedia Players:")
        print("  3. VLC")
        print("  4. mpv")
        print("\nDesktop Environments:")
        print("  5. XFCE")
        print("  6. GNOME")
        print("  7. KDE")
        print("\nTerminals & Editors:")
        print("  8. Alacritty")
        print("  9. Neovim")
        print(" 10. Nano")
        print("\nOther Tools:")
        print(" 11. htop")
        print(" 12. neofetch")
        print(" 13. git")
        print(" 14. PulseAudio Sound Server")
        print("\n  0. Exit")
        
        choice = input("\nEnter number to install: ")

        mapping = {
            "1": ["firefox"],
            "2": ["chromium"],
            "3": ["vlc"],
            "4": ["mpv"],
            "5": ["xfce", "xfce4-goodies", "thunar", "xfce4-appfinder"],
            "6": ["gnome", "gnome-tweaks", "gnome-utilities"],
            "7": ["kde5", "konsole", "dolphin", "okular"],
            "8": ["alacritty"],
            "9": ["neovim"],
            "10": ["nano"],
            "11": ["htop"],
            "12": ["neofetch"],
            "13": ["git"],
            "14": ["pulseaudio", "pulseaudio-alsa", "pulseaudio-module-x11", "pavucontrol"],
        }

        if choice == "0":
            print("Exiting pkgboard. Bye!")
            break
        elif choice in mapping:
            print(f"\nInstalling: {' '.join(mapping[choice])}...\n")
            install(mapping[choice])

            if choice == "14":
                print("\nSetting up PulseAudio to start automatically and enable ALSA compatibility...")

                # Enable PulseAudio in your user environment (add to ~/.bashrc or ~/.profile)
                # Usually no daemon needed because PulseAudio runs per user session.
                # But you can enable autostart by creating ~/.config/autostart/pulseaudio.desktop
                # or add a systemd user service on Linux. On FreeBSD, just start pulse manually or use rc.d.

                print("Make sure to start pulseaudio with `pulseaudio --start` after login.")
                print("You might want to add 'pulseaudio --start' to your ~/.xinitrc or desktop autostart.")

            input("\nPress Enter to return to menu...")
        else:
            print("Invalid selection.")
            input("Press Enter to try again...")

if __name__ == "__main__":
    main()
