# BME590 
# bme590hrm
* The main file that the user uses is "HRM_Main.py"
* There are two main inputs for HRM_Main: direcLocation, interval
## direcLocation
* This variable leads the program to a user-directed folder with the .csv files.
* If the user leaves this empty, the default is a subfolder named 'data'
## interval
* This variable lets the user define an interval of interest in the EKGs.
* If the user leaves this empty, the default is [0,0] (in seconds), but the HrmClass changes this to match the entire time scale of the EKG as default.


# Badge
[![Build Status](https://travis-ci.org/ML273/bme590hrm.svg?branch=master)](https://travis-ci.org/ML273/bme590hrm)

# License
MIT License

Copyright (c) [2018] [Marianne Lee]

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
