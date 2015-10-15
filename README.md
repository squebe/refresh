Refresh will run a command and reload it when any files matching the specified pattern in the specified directory are changed.  

To run refresh.py:

    refresh 'echo "There has been a change!"'  

A more complex example of how to run refresh.py:

    refresh 'echo "There has been a change!"' --directory 'mydir' --patterns '*.py;*.txt*'

To install from private repo:

    pip install git+https://github.com/squebe/refresh.git