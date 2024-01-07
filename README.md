# Image Steganography with Morse Code

Why just share memes with friends when you can also subtly plot world domination? It's all fun and laughs until the cat meme reveals the covert strategy for taking over the world! 🌍😼

This Python application enables image steganography using Morse Code. It allows you to hide messages within image pixels using Morse Code encryption.

## Requirements
- Python 3.x

## Installation
1. **Clone the Repository:**
    ```bash
    git clone https://github.com/Akashram28/Morse_Code_Image_Steganography.git
    cd Morse_Code_Image_Steganography
    ```

2. **Install Dependencies:**
    - Install the required Python packages by running:
        ```bash
        pip install -r requirements.txt
        ```

## Usage
1. **Run the Application:**
    - Run the Python file `stego_morse.py`:
        ```bash
        cd Stego_Morse
        python stego_morse.py
        ```

2. **Using the Application:**
    - Upon running the application, a GUI window will open.
    - Click on the "Browse Image" button to select an image for encoding or decoding.
    - To encode a message within the image:
        - Enter your message in the "Enter something" field.
        - Click on the "Encode Image" button.
        - The encoded image will be saved as `{original}_stego.png` in the same directory.
    - To decode a message from an encoded image:
        - Click on the "Decode Image" button.
        - The decoded message will be displayed below the image.

3. **Notes:**
    - Encoded images will be saved as `{original}_stego.png` in the same directory.
    - Decoding requires an image that has previously been encoded using this application.
