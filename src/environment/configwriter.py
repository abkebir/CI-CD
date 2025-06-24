from configparser import ConfigParser

config = ConfigParser()

config["dev"] = {
    "host": "dev.example.com",
    "port": "8080",
    "username": "dev_user",
    "password": "dev_password",
    "database": "dev_db",
}

config["prod"] = {
    "host": "prod.example.com",
    "port": "8080",
    "username": "prod_user",
    "password": "prod_password",
    "database": "prod_db",
}

with open("./environment/config.ini", "w") as configfile:
    config.write(configfile)
