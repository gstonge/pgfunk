#!/bin/zsh

rm -r _build/
jb build .
ghp-import -n -p -f _build/html
