# Gesture Volume Control with OpenCV and Mediapipe

This project demonstrates a gesture-based volume control system using OpenCV, Mediapipe, and the Pycaw library to interact with system volume on a Windows-based system. It tracks hand movements via a webcam and adjusts the system volume based on the distance between specific finger landmarks.

## Features
-    Volume Control: Adjusts the system volume by tracking the distance between the index finger and thumb.
 -   Mute Functionality: Mutes the system volume if the index finger and thumb are brought very close together.
  -  Mouse Control: Tracks the index finger and controls the mouse cursor position on the screen. If the index and middle fingers are brought together, it emulates a mouse click.

## Requirements
-  Python 3.x
-  OpenCV
 - Mediapipe
    -    Pycaw
     -   Comtypes
  
## Installation
1.Clone the Repository
```bash
git clone <repository-url>
cd GestureControl-Volume-Edition
```
2. Install Dependencies
```bash
Make sure to have Python installed. Then install the necessary libraries:

```
## Usage
To run the volume control system, use the following command:
```bash
python volume_control.py
```
This command will open a window showing the webcam feed. It will draw lines and circles indicating the detected hand landmarks. It also displays the current frames per second (FPS).

## Gesture Instructions
 - Volume Control: Bring the index finger (ID 8) and thumb (ID 4) closer to increase the volume. Distance-based mapping is used to determine the exact volume level.
 - Mute: If the index finger and thumb are extremely close (distance < 30), the system volume is muted.
 - Mouse Control: When only the index finger is visible, the mouse moves accordingly. If the index and middle fingers are brought together, it triggers a mouse click.
## Troubleshooting
- Webcam Not Detected: Ensure that your webcam is properly connected and accessible.
- High CPU Usage: If the CPU usage is high, consider lowering the video feed resolution or reducing the processing complexity.
- Volume Control Not Working: Ensure the Pycaw library is installed correctly and has the appropriate permissions to modify system volume.
  ##  Contributing
We welcome contributions to enhance this project. Please fork the repository and submit a pull request with your changes.

## Author
This project is maintained by me Subhajit Lai. You can contact me via email: iamsubhajitlai@gmail.com
