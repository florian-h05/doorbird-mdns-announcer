# DoorBird mDNS Announcer

This script announces a [DoorBird video doorbell](https://www.doorbird.com) via mDNS.
It is meant to be used if the DoorBird is on a different subnet or VLAN and mDNS discovery therefore fails.

mDNS discovery is required to work for the DoorBird Android and iOS apps.

# Usage

```shell
usage: app/main.py [-h] -a ADVERTISE [-i INTERFACE]

options:
  -h, --help            show this help message and exit
  -a ADVERTISE, --advertise ADVERTISE
                        <Required> Advertise DoorBird device, format is <mac>/<ipv4>
  -i INTERFACE, --interface INTERFACE
                        Interfaces to advertise from given by their IP address(es)
```

# Run with Docker

Execute the following command to run the with Docker:

```shell
docker run --network host -e ADVERTISE="mac/ip" ghcr.io/florian-h05/doorbird-mdns-announcer:latest
```

## Using Docker Compose

Use the [docker-compose.yml](docker-compose.yml) in this repository to run with Docker Compose.
Specify the `ADVERTISE` env variable in `mac/ip` format,
and optionally the `INTERFACES` env variable with the IP addresses of the interfaces to advertise from.

# Run with systemd

1. Ensure you have Python 3.13 or newer and `pip` installed.
1. cd into the `/opt` folder with `cd /opt`
1. Clone the git repo with `sudo git clone https://github.com/florian-h05/doorbird-mdns-announcer.git`
1. Change ownership to your user with `sudo chown -R $USER:$USER doorbird-mdns-announcer`
1. cd into that folder with `cd doorbird-mdns-announcer`
1. Install dependencies with `pip install -r app/requirements.txt`
1. Set up the systemd service file (`nano doorbird-mdns-announcer.service`):
   - Replace `%USER` with your username.
   - Replace `%ADVERTISE` with your DoorBird's mac and ip, format is `mac/ip`
   - Optionally set up the interfaces.
1. Copy the systemd service file with `sudo cp doorbird-mdns-announcer.service /etc/systemd/system`
1. Enable and start the service with `sudo systemctl enable --now doorbird-mdns-announcer`
