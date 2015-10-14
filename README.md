Refresh will run a command and reload it when any files matching the specified pattern in the specified directory are changed.  

To run:  
refresh 'echo hello'  
OR  
refresh 'echo hello; sleep 1000' --directory 'mydir' --patterns '*.py;*.txt*'  

To install from private repo:  
git+https://<github-personal-access-token>:x-oauth-basic@github.com/squebe/refresh.git