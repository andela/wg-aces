echo "Running pre-release scripts"
python setup.py develop
npm install
invoke bootstrap-wger --settings-path wger/settings.py --no-start-server
python manage.py makemigrations --merge
python manage.py migrate
python manage.py bower_install --allow-root 
echo "Done running pre-release.sh"
