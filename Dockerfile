from python:3.6-slim

run apt update && apt install -y curl

run python -m pip install --upgrade pip

add ./requirements.txt /tmp
run pip install -r /tmp/requirements.txt

add ./aggregator /aggregator

workdir /aggregator

#cmd python app.py
