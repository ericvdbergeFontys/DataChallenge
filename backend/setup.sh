# create virtual environment for packages install
python -m venv ./venv/

# activate the virtual environment and 
# perform commands in the new virtual environment
venv/Scripts/activate

# install all packages required in the requirements.txt 
# in the virtual environment
pip install -r requirements.txt