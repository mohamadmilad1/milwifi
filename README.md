# milwifi


## Description
milwifi is a simple GUI-based file sharing application that allows users to share files over a local Wi-Fi network. The application uses a basic HTTP server with authentication to ensure that only authorized users can access the shared files.

## Features
- **Graphical User Interface (GUI)**: User-friendly interface for selecting files to share.
- **Local Network Sharing**: Share files across devices within the same Wi-Fi network.
- **Basic Authentication**: Protect access to shared files with a username and password.
- **Cross-platform**: Runs on any system with Python installed.

## Requirements
- Python 3.x
- Required Python libraries:
  - tkinter
  - http.server (included with Python standard library)
  - shutil (included with Python standard library)

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/mohamadmilad1/milwifi.git
   ```
2. Navigate to the project directory:
   ```
   cd milwifi
   ```
3. Install the required dependencies (if not already installed):
   ```
   pip install tkinter
   ```

## Usage
1. Run the application:
   ```
   python mil.py
   ```
2. A GUI window will open, allowing you to select files to share.
3. The shared files will be available to other devices on the same network via a web browser. Access the shared files by navigating to `http://<your-ip-address>:8000`.

## Authentication
- Username: `admin`
- Password: `Ariana@123`

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contribution
Feel free to fork this project and submit pull requests. All contributions are welcome!

## Contact
If you have any questions or suggestions, feel free to contact me via GitHub.

