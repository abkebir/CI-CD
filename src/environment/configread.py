from configparser import ConfigParser
import pathlib


def get_env_config(env: str) -> ConfigParser:
    """Retrieve configuration for a specific environment."""
    config_file_path = pathlib.Path(__file__).\
        parent.absolute().joinpath("config.ini")
    config = ConfigParser()
    config.read(config_file_path)
    try:  
        if env in config:
            return config[env]
    except KeyError:
        raise KeyError(f"Environment '{env}' not found in configuration.")


# Example usage
# config = get_env_config("dev")
# print(f"Host: {config['host']}")
