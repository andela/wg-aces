npm install
invoke bootstrap-wger --settings-path ./settings.py --no-start-server
./manage.py makemigrations --merge
./manage.py migrate
echo "Done running release scripts"
