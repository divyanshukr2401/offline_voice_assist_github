import os
import subprocess
import webbrowser

CODE_CMD = r"D:\APP EXE\VSCode\Microsoft VS Code\bin\code.cmd"


class CodingMode:
    def __init__(self):
        self.status = "deactive"
        self.project_root = r"D:\Coding\Voice_assistance\project_code"

    def enter(self):
        self.status = "active"
        print("Coding mode activated")

        subprocess.Popen([CODE_CMD, self.project_root])
        webbrowser.open("https://codeforces.com")

    def exit(self):
        self.status = "deactive"
        print("Coding mode deactivated")

    def create_file(self, filename):
        path = os.path.join(self.project_root, filename)

        if os.path.exists(path):
            print("File already exists")
            return

        with open(path, "w"):
            pass

        print(f"File created: {filename}")
        subprocess.Popen([CODE_CMD, path])  

    def open_file(self, filename):
        path = os.path.join(self.project_root, filename)

        if not os.path.exists(path):
            print("File not found")
            return

        print(f"Opening file: {filename}")
        subprocess.Popen([CODE_CMD, path])  