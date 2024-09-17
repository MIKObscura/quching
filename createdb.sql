CREATE TABLE "audio_files" (
	"id"	INTEGER UNIQUE,
	"filename"	TEXT UNIQUE,
	"artist"	TEXT,
	"album"	TEXT,
	"title"	TEXT,
	"genre" TEXT,
	"tracknumber"	INTEGER,
	"duration" INTEGER,
	"year" INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE "cue_sheets" (
	"id"	INTEGER UNIQUE,
	"cue"	TEXT,
	"filename"	TEXT,
	"artist"	TEXT,
	"album"	TEXT,
	"genre" TEXT,
	"timestamp"	INTEGER,
	"title"	INTEGER,
	"duration"	INTEGER,
	"year" INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);