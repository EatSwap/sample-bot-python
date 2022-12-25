#!/bin/bash
python main.py &
caddy reverse-proxy --from :8880 --to :8080
