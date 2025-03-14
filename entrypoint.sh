#!/usr/bin/env sh

if [ -n "$INTERFACE" ]
then
  exec python /app/main.py --advertise "$ADVERTISE" --interface "$INTERFACE"
else
  exec python /app/main.py --advertise "$ADVERTISE"
fi
