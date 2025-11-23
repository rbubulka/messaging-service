CREATE TYPE message_type as ENUM('sms','mms','email');

DROP TABLE IF EXISTS "Conversations";
CREATE TABLE IF NOT EXISTS "Conversations"(
    id SERIAL PRIMARY KEY,
    member_1 varchar(255),
    member_2 varchar(255)
);

DROP TABLE IF EXISTS "Messages";
CREATE TABLE "Messages"(
    id SERIAL PRIMARY KEY,
    sent_by varchar(255) NOT NULL,
    recieved_by varchar(255) NOT NULL,
    conversation_id int REFERENCES "Conversations"("id") NOT NULL,
    date_sent TIMESTAMP NOT NULL,
    body TEXT,
    "message_type" message_type NOT NULL,
    attachment TEXT,
    "provider" TEXT
);