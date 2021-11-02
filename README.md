# QR Code Decoder

tech: OpenCV / pyzbar <br>
version: v1.0.1

![opencv_frame_1](https://user-images.githubusercontent.com/84317349/139910252-11ffc888-718a-4c80-984f-d63cd033254d.png)
![opencv_frame_0](https://user-images.githubusercontent.com/84317349/139910232-ef733b23-f8f4-4cb2-a2a2-21bb47cfe886.png)

## Concept 
This application is a real-time QR Code Decoder via webcam feed.

+ If the QR Code contains an external link, the link is automatically opened on the user's default browser.
+ If the QR Code contains text, the text is displayed on the top left corner of the camera feed.

## Dependencies

1. Create a virtual environment :

        python -m venv virtual
        
2. Activate the virtual environment :

    on Linux:

        source virtual/Scripts/activate
        
    on Windows:
        
        .\virtual\Scripts\activate
        
3. Install the necessary librairies :

        pip install opencv-python
        pip install pyzbar

## Additional features

Basic keypress interactions have been implemented for better UX:
+ Press (q) to (q)uit and close camera feed
+ Press (s) to (s)ave current camera frame

## Credits

Inspired by [Jordan Kalebu](https://github.com/Kalebu)'s [barcode reader](https://github.com/Kalebu/Realtime-barcode-reader)
