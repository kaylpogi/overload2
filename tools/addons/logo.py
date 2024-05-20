"""This module provides a function that prints the logo's application."""

import os

from colorama import Fore as F


def show_logo() -> None:
    """Print the application logo.

    Args:
        None

    Returns:
        None
    """
    logo = """
  ___    ___ ___      ___ _______   ________                              ___  __        ___    ___ ___       _______      
 |\  \  /  /|\  \    /  /|\  ___ \ |\   ____\                            |\  \|\  \     |\  \  /  /|\  \     |\  ___ \     
 \ \  \/  / | \  \  /  / | \   __/|\ \  \___|_         ____________      \ \  \/  /|_   \ \  \/  / | \  \    \ \   __/|    
  \ \    / / \ \  \/  / / \ \  \_|/_\ \_____  \       |\____________\     \ \   ___  \   \ \    / / \ \  \    \ \  \_|/__  
   \/  /  /   \ \    / /   \ \  \_|\ \|____|\  \      \|____________|      \ \  \\ \  \   \/  /  /   \ \  \____\ \  \_|\ \ 
 __/  / /      \ \__/ /     \ \_______\____\_\  \                           \ \__\\ \__\__/  / /      \ \_______\ \_______\
|\___/ /        \|__|/       \|_______|\_________\                           \|__| \|__|\___/ /        \|_______|\|_______|
\|___|/                               \|_________|                                     \|___|/                                                   
  """

    print(f"{F.RED}{logo}")
    print("├─── DOS TOOL")
    print("├─── AVAILABLE METHODS")
    print("├─── LAYER 7: HTTP | HTTP-PROXY | SLOWLORIS | SLOWLORIS-PROXY")
    if os.name != "nt":
        print("├─── LAYER 4: SYN-FLOOD")
        print("├─── LAYER 2: ARP-SPOOF | DISCONNECT")
    print("├───┐")
