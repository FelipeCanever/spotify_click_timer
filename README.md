# Spotify Click Timer

This program starts a 15-second timer every time the user clicks anywhere inside Spotify. When the timer runs out, a beep is played.

The motivation for this project came from my weekly need to update my personal Spotify playlist. I have a playlist called "Fresh" where I keep the songs I'm currently listening to. Every week I need to update it, removing songs I don't feel like listening to anymore and adding new ones. However I don't like having to listen to all of them in their entirety to see if I'm sick of a particular song or not, so I came up with this thing that I start the song, listen to the first 15 seconds and then do the same skipping ahead from 1/4, 1/5 and 3/4 of the song. And, so that I don't have to use a manual timer or mentally calculate when 15 seconds have passed, I created this program, that will count down from 15 seconds everytime I click inside Spotify, i.e. when I skip ahead on the timeline. When the timer runs out, it plays a beep to warn me. Call me lazy. :)

## Instalation

To run this program, you need to have at least Python 3.6 installed. This program will only run on Windows, since it depends on platform-specific modules.

These are the modules you're going to need, which can be installed by running ```pip install <module>``` at the console:

* ```psutil```,
* ```win32api```,
* ```win32gui```, and
* ```win32process```.

## Usage

If you have Python installed, just run ```main.py```. The program will start a 15-second timer every time you click inside Spotify and play a beep when it runs out.

## Contributing

If you have any suggestions to improve this program, feel free to suggest them.

## License

MIT License

Copyright (c) 2021 Felipe Canever Fernandes

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
