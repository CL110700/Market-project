FILE=/my-project-env
if [ !  -d "$FILE" ]; then
	echo "installing Python"
	sudo apt install python3-venv
	python3 -m venv my-project-env
fi

source my-project-env/bin/activate
sh requirements.txt
python main.py
