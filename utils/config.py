import ConfigParser

def get_config(section):
    conf = ConfigParser.ConfigParser()

    conf.read("heartbeat.ini")

    config = {}

    options = conf.options(section)

    for option in options:
        config[option] = conf.get(section, option)

    return config