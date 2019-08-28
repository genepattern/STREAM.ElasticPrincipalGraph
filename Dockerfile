FROM pinellolab/stream:0.3.8

RUN mkdir /stream
COPY epg_command_line.py /stream/epg_command_line.py

ENTRYPOINT []
