#!/usr/bin/env sh

if [ -n "$INTERFACE" ]
then
  exec python -u /app/main.py --advertise "$ADVERTISE" --interface "$INTERFACE"
else
  exec python -u /app/main.py --advertise "$ADVERTISE"
fi
