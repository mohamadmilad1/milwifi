import os
import shutil
from http.server import HTTPServer, SimpleHTTPRequestHandler, BaseHTTPRequestHandler
import tkinter as tk
from tkinter import filedialog, messagebox
import threading
from functools import partial
import base64

# Configuration
PORT = 8000
USERNAME = "admin"
PASSWORD = "Ariana@123"


# Custom request handler to add authentication
class AuthHandler(SimpleHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_AUTHHEAD(self):
        self.send_response(401)
        self.send_header('WWW-Authenticate', 'Basic realm="File Sharing"')
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        key = self.headers.get('Authorization')
        if key is None:
            self.do_AUTHHEAD()
            self.wfile.write(b'Authentication required.')
        elif key == 'Basic ' + base64.b64encode(f"{USERNAME}:{PASSWORD}".encode()).decode():
            SimpleHTTPRequestHandler.do_GET(self)
        else:
            self.do_AUTHHEAD()
            self.wfile.write(b'Invalid credentials.')


# Function to start the HTTP server
def start_http_server():
    if not os.path.exists("shared_files"):
        os.makedirs("shared_files")
    os.chdir("shared_files")  # Change directory to the folder containing files to be shared
    handler = partial(AuthHandler)
    httpd = HTTPServer(("", PORT), handler)
    print(f"Serving HTTP on 0.0.0.0 port {PORT} (http://localhost:{PORT}/) ...")
    httpd.serve_forever()


# GUI Application using Tkinter
root = tk.Tk()
root.title("File Sharing GUI - milwifi")
root.geometry("400x200")


# Function to handle file selection and copy to shared folder
def select_and_share_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        try:
            shared_folder = "shared_files"
            if not os.path.exists(shared_folder):
                os.makedirs(shared_folder)

            file_name = os.path.basename(file_path)
            target_path = os.path.join(shared_folder, file_name)
            shutil.copy(file_path, target_path)  # Copy the file instead of moving it
            messagebox.showinfo("File Sharing", f"File '{file_name}' is ready to be shared.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to share file: {str(e)}")


# GUI Elements
select_button = tk.Button(root, text="Select and Share File", command=select_and_share_file)
select_button.pack(pady=20)

# Start the HTTP server in a separate thread
server_thread = threading.Thread(target=start_http_server)
server_thread.daemon = True
server_thread.start()

# Run the Tkinter main loop
root.mainloop()
