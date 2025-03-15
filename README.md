# the_channel

A real-time chat web app.

## Tech stack
| Technology      | Usage                                                        |
|-----------------|--------------------------------------------------------------|
| Python          | Core scripting language used in the project                  |
| Django          | Web development framework used to create the main app        |
| Django Channels | Django library used to process asynchronous message delivery |
| PostgreSQL      | Relational database used for storing users and messages data |
| Redis           | In-memory message broker                                     |


## Features
1. User sign-up and sign-in.
2. Displaying a list of available contacts.
3. Real-time sending and receiving messages to/from the selected user.

## Project setup
The following instructions will work given that you have `git`, `Docker` and `Docker Compose` installed on your machine.

### 1. Clone the repository ###
```shell
git clone https://github.com/erykmika/the_channel.git
```

### 2. Start project containers ###
```shell
cd ./the_channel
docker compose up
```

### 3. After a few minutes you should be all set. Go to `localhost:8000` in your browser. ###