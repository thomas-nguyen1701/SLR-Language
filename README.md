# SLR-Language

### Tech Stack
- MatPlotLab
- MediaPipe
- Numpy
- Skitlearning
- TensorFlow
- React

## Contributors
- Bryce Chao
- Hamza Kassem
- Matthew Morello
- Ronit Narayan
- Thomas Nguyen

## Setup to Run Back-End Only
- Python version 3.9-3.12
- pip install mediapipe
- pip install seaborn
- pip install tensorflow
- pip install scikit-learn
- pip install opencv-python
Go to directory where app.py is located and >> python ./app.py

## Acknowledgments
This project utilizes code from [hand-gesture-recognition-using-mediapipe](https://github.com/Kazuhito00/hand-gesture-recognition-using-mediapipe) by [Kazuhito00, arky, taffarel55, PINTO0309] under the Apache License 2.0.

## Modifications
This project is a modified version of [hand-gesture-recognition-using-mediapipe](https://github.com/Kazuhito00/hand-gesture-recognition-using-mediapipe). The following changes have been made:
- Deleted and trained our own model using custom gestures
- Removed/refactored code that were deemed unnecessary for our project, increased performance
- Removed some existing files that were deemed unnecessary for our project, increased performance
- Modified existing code to support different/more parameters such as hand signing letters A-Z
- Now shows handmark location with landmark numbers 0-21
