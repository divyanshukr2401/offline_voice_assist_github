from core.listener import Listener
from core.parser import parse_text
from core.dispatcher import dispatch
from modules.coding_mode import CodingMode

def main():
    Cmode = CodingMode()
    listener = Listener(r"D:\Coding\Voice_assistance\models\vosk-model-small-en-in-0.4")      
    
    while True:
        result = listener.listen()
        text = parse_text(result)
        
        if not text:
            continue

        if text and ("terminate" in text or "end" in text):
            dispatch(text)
            break
        
        
        if text and ("coding" in text and "activate" in text) or ("coding" in text and "enter" in text):
            Cmode.enter()
            continue  
        
        # Handle coding_mode commands
        if text and Cmode.status == "active":
            if "deactivate coding" in text or "exit coding" in text:
                Cmode.exit()
                continue
            
            elif "create" in text and "file" in text and "java" in text:
                words = text.split()
                filename= words[-1]+".java"
                Cmode.create_file(filename)
                continue

            elif "create" in text and "file" in text and "python" in text:
                words = text.split()
                filename= words[-1]+".py"
                Cmode.create_file(filename)
                continue
            
            elif "open" in text and "file" in text and "java" in text:
                words = text.split()
                filename= words[-1]+".java"
                Cmode.open_file(filename)
                continue
            
            # Anything else while coding mode is active
            else:
                print(f"[CODING MODE] {text}")
                continue
        
           
        # Normal mode commands
        if text and Cmode.status == "deactive":
            dispatch(text)

if __name__ == "__main__":
    main()