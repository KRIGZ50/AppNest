
CREATE TABLE accounts(
    account_id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    display_name TEXT NOT NULL,
    password_hash TEXT,
    email TEXT UNIQUE NOT NULL,
    verified INTEGER NOT NULL,
    created_at TEXT NOT NULL
);

CREATE TABLE verification_codes(
    id INTEGER PRIMARY KEY,
    account_id INTEGER NOT NULL,
    code_hash TEXT NOT NULL,
    expires_at TEXT NOT NULL,
    email TEXT NOT NULL,
    reason TEXT NOT NULL,
    resends INTEGER NOT NULL,
    FOREIGN KEY(account_id) REFERENCES accounts(account_id)
);   

CREATE TABLE login_tokens(
    account_id INTEGER NOT NULL,
    token_hash TEXT NOT NULL,
    expires_at TEXT NOT NULL,
    FOREIGN KEY(account_id) REFERENCES accounts(account_id)
)