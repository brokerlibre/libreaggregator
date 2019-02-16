from python:3.6-slim

run apt update && apt install -y curl

run python -m pip install --upgrade pip

add ./requirements.txt /tmp
run pip install -r /tmp/requirements.txt

add ./aggregator /libre/aggregator
add ./api /libre/api
add ./manage.py /libre/manage.py
add ./config.sh /tmp/config.sh

workdir libre/

entrypoint "/tmp/config.sh"
