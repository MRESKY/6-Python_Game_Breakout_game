#!/usr/bin/env python3
"""
Simple Level Editor for Breakout Game
Creates and edits JSON level patterns
"""

import json
import os
from typing import List, Dict, Any

class LevelEditor:
    def __init__(self):
        self.current_pattern = []
        self.rows = 8
        self.cols = 8
        self.brick_types = {
            '0': 'Empty',
            '1': 'Basic (Red)',
            '2': 'Medium (Blue)', 
            '3': 'Strong (Green)',
            '4': 'Super (Yellow)',
            '5': 'Special (Purple)'
        }
    
    def create_empty_pattern(self, rows: int = 8, cols: int = 8) -> List[List[int]]:
        """Create an empty pattern"""
        return [[0 for _ in range(cols)] for _ in range(rows)]
    
    def display_pattern(self, pattern: List[List[int]]) -> None:
        """Display the current pattern"""
        print("\nCurrent Pattern:")
        print("  " + "".join([f"{i:2}" for i in range(len(pattern[0]))]))
        for i, row in enumerate(pattern):
            print(f"{i:2}" + "".join([f"{cell:2}" for cell in row]))
        print()
    
    def edit_pattern_interactive(self) -> List[List[int]]:
        """Interactive pattern editor"""
        pattern = self.create_empty_pattern(self.rows, self.cols)
        
        print("=== Breakout Level Editor ===")
        print("Commands:")
        print("  set <row> <col> <type>  - Set brick at position")
        print("  show                    - Show current pattern")
        print("  fill <type>             - Fill entire pattern")
        print("  clear                   - Clear pattern")
        print("  save                    - Save and exit")
        print("  help                    - Show commands")
        print("\nBrick types:")
        for key, value in self.brick_types.items():
            print(f"  {key}: {value}")
        print()
        
        while True:
            try:
                command = input("Editor> ").strip().lower().split()
                if not command:
                    continue
                
                if command[0] == 'set' and len(command) == 4:
                    row, col, brick_type = int(command[1]), int(command[2]), int(command[3])
                    if 0 <= row < self.rows and 0 <= col < self.cols and str(brick_type) in self.brick_types:
                        pattern[row][col] = brick_type
                        print(f"Set brick at ({row}, {col}) to type {brick_type}")
                    else:
                        print("Invalid position or brick type")
                
                elif command[0] == 'show':
                    self.display_pattern(pattern)
                
                elif command[0] == 'fill' and len(command) == 2:
                    brick_type = int(command[1])
                    if str(brick_type) in self.brick_types:
                        pattern = [[brick_type for _ in range(self.cols)] for _ in range(self.rows)]
                        print(f"Filled pattern with brick type {brick_type}")
                    else:
                        print("Invalid brick type")
                
                elif command[0] == 'clear':
                    pattern = self.create_empty_pattern(self.rows, self.cols)
                    print("Pattern cleared")
                
                elif command[0] == 'save':
                    break
                
                elif command[0] == 'help':
                    print("Commands:")
                    print("  set <row> <col> <type>  - Set brick at position")
                    print("  show                    - Show current pattern")
                    print("  fill <type>             - Fill entire pattern")
                    print("  clear                   - Clear pattern")
                    print("  save                    - Save and exit")
                
                else:
                    print("Unknown command. Type 'help' for available commands.")
            
            except ValueError:
                print("Invalid input. Please check your command format.")
            except KeyboardInterrupt:
                print("\nExiting editor...")
                return pattern
        
        return pattern
    
    def create_level_template(self, level_number: int, name: str, description: str, pattern: List[List[int]]) -> Dict[str, Any]:
        """Create a level template"""
        return {
            "name": name,
            "description": description, 
            "pattern": pattern
        }
    
    def add_level_to_json(self, json_path: str, level_number: int, level_data: Dict[str, Any]) -> None:
        """Add a level to existing JSON file"""
        try:
            with open(json_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except FileNotFoundError:
            print(f"JSON file not found: {json_path}")
            return
        
        # Add level to data
        data["levels"][str(level_number)] = level_data
        
        # Save updated data
        with open(json_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        
        print(f"Level {level_number} added successfully!")
    
    def create_new_level(self) -> None:
        """Create a new level"""
        print("=== Create New Level ===")
        
        # Get level info
        level_number = int(input("Enter level number: "))
        level_name = input("Enter level name: ")
        level_description = input("Enter level description: ")
        
        # Create pattern
        print("\nNow create the level pattern...")
        pattern = self.edit_pattern_interactive()
        
        # Show final pattern
        self.display_pattern(pattern)
        
        # Confirm save
        confirm = input("Save this level? (y/n): ").lower()
        if confirm == 'y':
            level_data = self.create_level_template(level_number, level_name, level_description, pattern)
            
            # Get JSON path
            current_dir = os.path.dirname(os.path.abspath(__file__))
            json_path = os.path.join(current_dir, 'levels', 'level_patterns.json')
            
            self.add_level_to_json(json_path, level_number, level_data)
        else:
            print("Level not saved.")

def main():
    """Main function"""
    editor = LevelEditor()
    
    print("Welcome to the Breakout Level Editor!")
    print("1. Create new level")
    print("2. Exit")
    
    choice = input("Choose option (1-2): ")
    
    if choice == '1':
        editor.create_new_level()
    else:
        print("Goodbye!")

if __name__ == "__main__":
    main()