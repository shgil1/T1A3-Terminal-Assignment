# sudo apt install python3.10-venv
#!/bin/bash
python3 -m venv virtualenv

#
source virtualenv/bin/activate

pip install -r requirements.txt

python3 src/main.py

deactivate