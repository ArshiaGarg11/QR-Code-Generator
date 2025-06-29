#  QR Code Generator 

A lightweight Python project that generates a QR code from any text or URL entered by the user in the terminal. The generated QR code is saved as a PNG image that can easily be scanned or shared.


## Features

- Generate QR codes from any input text or URL
- Saves the QR code as `qr_code.png`
- Super beginner-friendly and easy to use
  

##  Sample Output

After entering a URL like: [https://www.linkedin.com/feed/](https://www.linkedin.com/feed/)  
A file named `qr_code.png` will be created containing the QR code (like below):  

![QR Code Example](qr_code.png)


##  How to Run

### 1. Clone the repository

```
git clone https://github.com/ArshiaGarg11/QR-Code-Generator.git
cd QR-Code-Generator
```
### 2. Install the required package
```
pip install qrcode[pil]
```
### 3. Run the script


## Project Files

-**qr_generator.py**:	Python script that generates the QR code  
-**qr_code.png**:	Sample output image of the QR code  
-**.gitignore**:	Git configuration to ignore system files  
-**README.md**:	Project description (this file)


## How It Works:
You enter the text or link in the terminal — and this Python script instantly generates and saves a QR code as an image file.


## To-Do / Future Improvements: 

-Allow custom file names for saving QR  
-Add option to display QR code in the terminal  
-Support for batch QR generation from a text file

## Author
Arshia Garg  
Feel free to fork, star, or suggest improvements!
