import os
import time

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    END = '\033[0m'

def show_banner():
    print(f"{Colors.CYAN}{Colors.BOLD}")
    print("  ════════════════════════════════════════════════════════════")
    print(f"  {Colors.MAGENTA}{Colors.BOLD}           ██████╗ ██████╗ ██╗████████╗ ██████╗           {Colors.CYAN}")
    print(f"  {Colors.MAGENTA}{Colors.BOLD}          ██╔═══██╗██╔══██╗██║╚══██╔══╝██╔═══██╗          {Colors.CYAN}")
    print(f"  {Colors.MAGENTA}{Colors.BOLD}          ██║   ██║██████╔╝██║   ██║   ██║   ██║          {Colors.CYAN}")
    print(f"  {Colors.MAGENTA}{Colors.BOLD}          ██║   ██║██╔══██╗██║   ██║   ██║   ██║          {Colors.CYAN}")
    print(f"  {Colors.MAGENTA}{Colors.BOLD}          ╚██████╔╝██████╔╝██║   ██║   ╚██████╔╝          {Colors.CYAN}")
    print(f"  {Colors.MAGENTA}{Colors.BOLD}           ╚═════╝ ╚═════╝ ╚═╝   ╚═╝    ╚═════╝           {Colors.CYAN}")
    print("  ────────────────────────────────────────────────────────")
    print(f"  {Colors.MAGENTA}{Colors.BOLD}                O B I T Ō   C I P H E R                  {Colors.CYAN}")
    print("  ────────────────────────────────────────────────────────")
    print(f"  {Colors.YELLOW}            Playfair Cipher Tool v1.0                   {Colors.CYAN}")
    print(f"  {Colors.GREEN}           Live Matrix Animation Tool                   {Colors.CYAN}")
    print("  ════════════════════════════════════════════════════════════")
    print(f"{Colors.END}")

def show_contact_info():
    print(f"{Colors.BLUE}{'═' * 60}{Colors.END}")
    print(f"{Colors.WHITE}    Telegram: {Colors.CYAN}https://t.me/Mr_WEBts{Colors.END}")
    print(f"{Colors.WHITE}    GitHub:   {Colors.CYAN}https://github.com/pango40{Colors.END}")
    print(f"{Colors.BLUE}{'═' * 60}{Colors.END}\n")

class PlayfairCipher:
    def __init__(self, key="MONARCHY"):
        self.matrix = self.generate_matrix(key)

    def generate_matrix(self, key):
        key = key.upper().replace('J', 'I')
        seen = set()
        matrix = []
        for char in key:
            if char not in seen and char.isalpha():
                seen.add(char)
                matrix.append(char)
        for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
            if char not in seen:
                seen.add(char)
                matrix.append(char)
        return [matrix[i:i+5] for i in range(0, 25, 5)]

    def show_matrix_with_cursor(self, char1_pos, char2_pos, cursor_pos=None, step_description=""):
        os.system('cls' if os.name == 'nt' else 'clear')
        show_banner()
        show_contact_info()
        print(f"{Colors.CYAN}{Colors.BOLD}Playfair Cipher - Live Animation{Colors.END}")
        print(f"{Colors.BLUE}=================================================={Colors.END}")
        if step_description:
            print(f"{Colors.YELLOW}{step_description}{Colors.END}")
        print(f"\n{Colors.MAGENTA}{Colors.BOLD}Playfair Matrix:{Colors.END}")
        print(f"{Colors.BLUE}   0   1   2   3   4{Colors.END}")
        print(f"{Colors.BLUE}  +---+---+---+---+---+{Colors.END}")
        for i in range(5):
            print(f"{i} |", end="")
            for j in range(5):
                char = self.matrix[i][j]
                if cursor_pos and (i, j) == cursor_pos:
                    print(f"{Colors.CYAN} >{char}{Colors.END}|", end="")
                elif (i, j) == char1_pos and (i, j) == char2_pos:
                    print(f"{Colors.RED}{Colors.BOLD} {char} {Colors.END}|", end="")
                elif (i, j) == char1_pos:
                    print(f"{Colors.RED}{Colors.BOLD} {char} {Colors.END}|", end="")
                elif (i, j) == char2_pos:
                    print(f"{Colors.GREEN}{Colors.BOLD} {char} {Colors.END}|", end="")
                else:
                    print(f" {char} |", end="")
            print()
            if i < 4:
                print(f"{Colors.BLUE}  +---+---+---+---+---+{Colors.END}")
        print(f"{Colors.BLUE}  +---+---+---+---+---+{Colors.END}")
        if char1_pos and char2_pos:
            char1 = self.matrix[char1_pos[0]][char1_pos[1]]
            char2 = self.matrix[char2_pos[0]][char2_pos[1]]
            print(f"\n{Colors.WHITE}Current Pair: {Colors.RED}{char1}{Colors.WHITE} {Colors.GREEN}{char2}{Colors.END}")

    def animate_cursor_movement(self, start_pos, end_pos, description):
        if start_pos == end_pos:
            return
        row1, col1 = start_pos
        row2, col2 = end_pos
        current_col = col1
        while current_col != col2:
            if current_col < col2:
                current_col += 1
            else:
                current_col -= 1
            self.show_matrix_with_cursor(start_pos, end_pos, (row1, current_col), f"{description} - Moving to column {current_col}")
            time.sleep(0.5)
        current_row = row1
        while current_row != row2:
            if current_row < row2:
                current_row += 1
            else:
                current_row -= 1
            self.show_matrix_with_cursor(start_pos, end_pos, (current_row, col2), f"{description} - Moving to row {current_row}")
            time.sleep(0.5)

    def find_position(self, char):
        char = char.upper().replace('J', 'I')
        for i in range(5):
            for j in range(5):
                if self.matrix[i][j] == char:
                    return (i, j)
        return None

    def prepare_text(self, text):
        text = text.upper().replace('J', 'I')
        prepared = ""
        i = 0
        while i < len(text):
            if text[i].isalpha():
                if i + 1 < len(text) and text[i+1].isalpha():
                    if text[i] == text[i+1]:
                        prepared += text[i] + 'X'
                        i += 1
                    else:
                        prepared += text[i] + text[i+1]
                        i += 2
                else:
                    prepared += text[i] + 'X'
                    i += 1
            else:
                i += 1
        if len(prepared) % 2 != 0:
            prepared += 'X'
        return prepared

    def encode_pair_with_animation(self, pair):
        a, b = pair[0], pair[1]
        pos1 = self.find_position(a)
        pos2 = self.find_position(b)
        print(f"\n{Colors.MAGENTA}Encoding Pair: '{a}{b}'{Colors.END}")
        time.sleep(1)
        self.show_matrix_with_cursor(pos1, pos2, None, f"Found positions: {a}({pos1[0]},{pos1[1]}) {b}({pos2[0]},{pos2[1]})")
        time.sleep(2)
        if pos1[0] == pos2[0]:
            self.show_matrix_with_cursor(pos1, pos2, None, "Same Row - Moving right")
            time.sleep(1)
            new_pos1 = (pos1[0], (pos1[1] + 1) % 5)
            new_pos2 = (pos2[0], (pos2[1] + 1) % 5)
            self.animate_cursor_movement(pos1, new_pos1, f"Moving {a} right")
            self.show_matrix_with_cursor(new_pos1, pos2, None, f"{a} moved to {self.matrix[new_pos1[0]][new_pos1[1]]}")
            time.sleep(1)
            self.animate_cursor_movement(pos2, new_pos2, f"Moving {b} right")
            self.show_matrix_with_cursor(new_pos1, new_pos2, None, f"{b} moved to {self.matrix[new_pos2[0]][new_pos2[1]]}")
            time.sleep(1)
        elif pos1[1] == pos2[1]:
            self.show_matrix_with_cursor(pos1, pos2, None, "Same Column - Moving down")
            time.sleep(1)
            new_pos1 = ((pos1[0] + 1) % 5, pos1[1])
            new_pos2 = ((pos2[0] + 1) % 5, pos2[1])
            self.animate_cursor_movement(pos1, new_pos1, f"Moving {a} down")
            self.show_matrix_with_cursor(new_pos1, pos2, None, f"{a} moved to {self.matrix[new_pos1[0]][new_pos1[1]]}")
            time.sleep(1)
            self.animate_cursor_movement(pos2, new_pos2, f"Moving {b} down")
            self.show_matrix_with_cursor(new_pos1, new_pos2, None, f"{b} moved to {self.matrix[new_pos2[0]][new_pos2[1]]}")
            time.sleep(1)
        else:
            self.show_matrix_with_cursor(pos1, pos2, None, "Rectangle - Swapping columns")
            time.sleep(1)
            new_pos1 = (pos1[0], pos2[1])
            new_pos2 = (pos2[0], pos1[1])
            self.animate_cursor_movement(pos1, new_pos1, f"Moving {a} to column {pos2[1]}")
            self.show_matrix_with_cursor(new_pos1, pos2, None, f"{a} moved to {self.matrix[new_pos1[0]][new_pos1[1]]}")
            time.sleep(1)
            self.animate_cursor_movement(pos2, new_pos2, f"Moving {b} to column {pos1[1]}")
            self.show_matrix_with_cursor(new_pos1, new_pos2, None, f"{b} moved to {self.matrix[new_pos2[0]][new_pos2[1]]}")
            time.sleep(1)
        new_a = self.matrix[new_pos1[0]][new_pos1[1]]
        new_b = self.matrix[new_pos2[0]][new_pos2[1]]
        self.show_matrix_with_cursor(new_pos1, new_pos2, None, f"Final: '{a}{b}' -> '{new_a}{new_b}'")
        time.sleep(2)
        return new_a + new_b

    def encode(self, text):
        prepared = self.prepare_text(text)
        result = ""
        print(f"\n{Colors.MAGENTA}Starting Playfair Encoding{Colors.END}")
        print(f"{Colors.WHITE}Original: {text}{Colors.END}")
        print(f"{Colors.WHITE}Prepared: {prepared}{Colors.END}")
        time.sleep(2)
        pairs = [prepared[i:i+2] for i in range(0, len(prepared), 2)]
        for i, pair in enumerate(pairs):
            result += self.encode_pair_with_animation(pair)
        return result

    def decode_pair_with_animation(self, pair):
        a, b = pair[0], pair[1]
        pos1 = self.find_position(a)
        pos2 = self.find_position(b)
        print(f"\n{Colors.MAGENTA}Decoding Pair: '{a}{b}'{Colors.END}")
        time.sleep(1)
        self.show_matrix_with_cursor(pos1, pos2, None, f"Found positions: {a}({pos1[0]},{pos1[1]}) {b}({pos2[0]},{pos2[1]})")
        time.sleep(2)
        if pos1[0] == pos2[0]:
            self.show_matrix_with_cursor(pos1, pos2, None, "Same Row - Moving left")
            time.sleep(1)
            new_pos1 = (pos1[0], (pos1[1] - 1) % 5)
            new_pos2 = (pos2[0], (pos2[1] - 1) % 5)
            self.animate_cursor_movement(pos1, new_pos1, f"Moving {a} left")
            self.show_matrix_with_cursor(new_pos1, pos2, None, f"{a} moved to {self.matrix[new_pos1[0]][new_pos1[1]]}")
            time.sleep(1)
            self.animate_cursor_movement(pos2, new_pos2, f"Moving {b} left")
            self.show_matrix_with_cursor(new_pos1, new_pos2, None, f"{b} moved to {self.matrix[new_pos2[0]][new_pos2[1]]}")
            time.sleep(1)
        elif pos1[1] == pos2[1]:
            self.show_matrix_with_cursor(pos1, pos2, None, "Same Column - Moving up")
            time.sleep(1)
            new_pos1 = ((pos1[0] - 1) % 5, pos1[1])
            new_pos2 = ((pos2[0] - 1) % 5, pos2[1])
            self.animate_cursor_movement(pos1, new_pos1, f"Moving {a} up")
            self.show_matrix_with_cursor(new_pos1, pos2, None, f"{a} moved to {self.matrix[new_pos1[0]][new_pos1[1]]}")
            time.sleep(1)
            self.animate_cursor_movement(pos2, new_pos2, f"Moving {b} up")
            self.show_matrix_with_cursor(new_pos1, new_pos2, None, f"{b} moved to {self.matrix[new_pos2[0]][new_pos2[1]]}")
            time.sleep(1)
        else:
            self.show_matrix_with_cursor(pos1, pos2, None, "Rectangle - Swapping columns")
            time.sleep(1)
            new_pos1 = (pos1[0], pos2[1])
            new_pos2 = (pos2[0], pos1[1])
            self.animate_cursor_movement(pos1, new_pos1, f"Moving {a} to column {pos2[1]}")
            self.show_matrix_with_cursor(new_pos1, pos2, None, f"{a} moved to {self.matrix[new_pos1[0]][new_pos1[1]]}")
            time.sleep(1)
            self.animate_cursor_movement(pos2, new_pos2, f"Moving {b} to column {pos1[1]}")
            self.show_matrix_with_cursor(new_pos1, new_pos2, None, f"{b} moved to {self.matrix[new_pos2[0]][new_pos2[1]]}")
            time.sleep(1)
        new_a = self.matrix[new_pos1[0]][new_pos1[1]]
        new_b = self.matrix[new_pos2[0]][new_pos2[1]]
        self.show_matrix_with_cursor(new_pos1, new_pos2, None, f"Final: '{a}{b}' -> '{new_a}{new_b}'")
        time.sleep(2)
        return new_a + new_b

    def decode(self, text):
        result = ""
        print(f"\n{Colors.MAGENTA}Starting Playfair Decoding{Colors.END}")
        print(f"{Colors.WHITE}Encoded: {text}{Colors.END}")
        time.sleep(2)
        pairs = [text[i:i+2] for i in range(0, len(text), 2)]
        for i, pair in enumerate(pairs):
            result += self.decode_pair_with_animation(pair)
        return result

def main():
    cipher = PlayfairCipher()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        show_banner()
        show_contact_info()
        cipher.show_matrix_with_cursor(None, None, None, "Ready for encryption/decryption")
        print(f"\n{Colors.GREEN}1. Encode text{Colors.END}")
        print(f"{Colors.GREEN}2. Decode text{Colors.END}")
        print(f"{Colors.MAGENTA}3. Demo with 'HELLO'{Colors.END}")
        print(f"{Colors.RED}4. Exit{Colors.END}")
        choice = input(f"\n{Colors.WHITE}Choose option (1-4): {Colors.END}")
        if choice == "1":
            text = input(f"\n{Colors.WHITE}Enter text to encode: {Colors.END}")
            result = cipher.encode(text)
            print(f"\n{Colors.GREEN}FINAL RESULT:{Colors.END}")
            print(f"{Colors.CYAN}Original: {text}{Colors.END}")
            print(f"{Colors.GREEN}Encoded:  {result}{Colors.END}")
            input(f"\n{Colors.WHITE}Press Enter to continue...{Colors.END}")
        elif choice == "2":
            text = input(f"\n{Colors.WHITE}Enter text to decode: {Colors.END}")
            result = cipher.decode(text)
            print(f"\n{Colors.GREEN}FINAL RESULT:{Colors.END}")
            print(f"{Colors.CYAN}Encoded: {text}{Colors.END}")
            print(f"{Colors.GREEN}Decoded: {result}{Colors.END}")
            input(f"\n{Colors.WHITE}Press Enter to continue...{Colors.END}")
        elif choice == "3":
            print(f"\n{Colors.MAGENTA}Running Demo: 'HELLO'{Colors.END}")
            result = cipher.encode("HELLO")
            print(f"\n{Colors.GREEN}Demo Complete! 'HELLO' -> '{result}'{Colors.END}")
            input(f"\n{Colors.WHITE}Press Enter to continue...{Colors.END}")
        elif choice == "4":
            print(f"{Colors.CYAN}Goodbye!{Colors.END}")
            break
        else:
            print(f"{Colors.RED}Invalid choice{Colors.END}")
            time.sleep(1)

if __name__ == "__main__":
    main()