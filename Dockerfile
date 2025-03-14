FROM python:3.13-slim

ARG BUILD_DATE
ARG VCS_REF

# Basic build-time metadata as defined at https://github.com/opencontainers/image-spec/blob/main/annotations.md#pre-defined-annotation-keys
LABEL org.opencontainers.image.created=$BUILD_DATE \
    org.opencontainers.image.licenses="MIT" \
    org.opencontainers.image.title="DoorBird mDNS Announcer" \
    org.opencontainers.image.vendor="Florian Hotze" \
    org.opencontainers.image.description="Announce a DoorBird video doorbell on the network via mDNS." \
    org.opencontainers.image.url="https://github.com/florian-h05/doorbird-mdns-announcer" \
    org.opencontainers.image.documentation="https://github.com/florian-h05/doorbird-mdns-announcer" \
    org.opencontainers.image.revision=$VCS_REF \
    org.opencontainers.image.source="https://github.com/florian-h05/doorbird-mdns-announcer.git" \
    org.opencontainers.image.authors="Florian Hotze"

# We make distinct layers so if there are application changes the layers can be re-used
COPY app/requirements.txt /app/requirements.txt
COPY app/main.py /app/main.py
COPY entrypoint.sh /entrypoint.sh

# Install dependencies
RUN pip install -r /app/requirements.txt --root-user-action ignore

ENTRYPOINT ["/entrypoint.sh"]
