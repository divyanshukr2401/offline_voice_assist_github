import webbrowser
import os

def dispatch(text):
    if not text:
        return

    print("Heard:", text)

    words=text.split()
    if ( "browser" in text) or ("chrome" in text):
        os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

    if("codeforces" in text) or ("forces" in text) or ("code" in text):
        webbrowser.open("https://codeforces.com")

    if("create" in text and "folder" in text):
        if("named" in text) :
            folder_name= words[words.index("named")+1]
            path= fr"C:\Users\Divyanshu Kumar\Desktop\{folder_name}"
            os.mkdir(path)
            
        elif("name" in text):
            folder_name= words[words.index("name")+1]
            path= fr"C:\Users\Divyanshu Kumar\Desktop\{folder_name}"
            os.mkdir(path)
        
        


