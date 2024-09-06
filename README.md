# Quching
Quching (pronouned kuching) is a music player written in Python and based on Qt. This is still a prototype so it's still bare bones and may heavily change in the future.

![screenshot](screenshot.png)


# Run
To run it, you first need to install python 3.8 or newer, create a venv and install the requirements:
```
mkdir venv
python -m venv venv/
source venv/bin/activate
pip install -r requirements.txt
```
```
python main.py path/to/audio/file
```
Note: the initial indexing may take some time if you have a lot of files, you'll also need to re-launch the application once it's done

# Credits
Cat image used as default cover is from here: https://www.svgrepo.com/svg/452952/cat
Default artist picture: https://www.svgrepo.com/svg/512729/profile-round-1342