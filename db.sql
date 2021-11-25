PRAGMA foreign_keys = off;
BEGIN TRANSACTION;


CREATE TABLE count (
    id            INTEGER PRIMARY KEY,
    django        INTEGER NOT NULL,
    flask         INTEGER NOT NULL,
    telegram_bot  INTEGER NOT NULL,
    instagram_bot INTEGER NOT NULL,
    vk_bot        INTEGER NOT NULL,
    sql           INTEGER NOT NULL,
    UNIQUE (
        django,
        flask,
        telegram_bot,
        instagram_bot,
        vk_bot,
        sql
    )
    ON CONFLICT IGNORE
);


CREATE TABLE stats (
    id       INTEGER PRIMARY KEY,
    id_count INTEGER REFERENCES count (id) ON DELETE CASCADE
                     NOT NULL,
    date     DATE    NOT NULL,
    UNIQUE (
        id_count,
        date
    )
    ON CONFLICT IGNORE
);


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;

