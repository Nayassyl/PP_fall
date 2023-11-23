from configparser import ConfigParser

def configuration(filename="database.ini", section="postgresql"):
    parser = ConfigParser()
    parser.read(filename)
    data_base = {}
    if parser.has_section(section):
        parameters=parser.items(section)
        for parameter in parameters:
            data_base[parameter[0]]=parameter[1]
    else:

        raise Exception("Section {0} not found in the {1} file".format(section,filename))
    return data_base
