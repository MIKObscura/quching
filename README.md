# Quching
Quching (pronouned kuching) is a music player written in Python and based on Qt. This is still a prototype so it's still bare bones and may heavily change in the future.

![screenshot](screenshot.png)


# Run
To run it, create a venv and install the requirements, then run it with:
```
python main.py path/to/audio/file
```
Note: for now the indexing is not done automatically so you'll have to do it manually, like in the Python console for example:
```
$ python
>>> import quching.indexer.index as index
>>> index.make_index()
```
This should create an index.db file that will contain all the audio files it found in the `~/Music` directory  
Yes, the implementation is currently very slow, this will be improved upon in the future

# Credits
Cat image used as default cover is from here: https://www.svgrepo.com/svg/452952/cat
Default artist picture: https://www.svgrepo.com/svg/512729/profile-round-1342