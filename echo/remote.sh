#!/bin/bash
rm -f /tmp/f; mkfifo /tmp/f
cat /tmp/f | /bin/bash -i 2>&1 | nc -l 127.0.0.1 1234 > /tmp/f
