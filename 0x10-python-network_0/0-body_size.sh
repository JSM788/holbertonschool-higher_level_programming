#!/usr/bin/bash
# This script takes a URL, sends a request to that URL, and displays the size of the body of the response
curl -sI  https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/HTTP_Basics.html | grep -i Content-Length | awk '{print $2}'
