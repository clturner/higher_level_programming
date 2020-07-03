#!/bin/bash
# takes a URL as an argument, sends GET request, displays the body of response
curl -s "$1" -H "X-CodeSchoolSFSchool-User-Id:98"
