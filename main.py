#!/usr/bin/env python3
import yaml, os, json

class Main:

    script_dir      = os.path.dirname(os.path.realpath(__file__))

    def execute(self):
        os.path.join("log", "sample.log")
        config = Config.load("config.yml")
        print(json.dumps(config, indent=4))

class Config:

    @staticmethod
    def load(config_file_path):
        with open(config_file_path, 'r') as stream:
            try:
                return yaml.load(stream, Loader)
            except yaml.YAMLError as e:
                print(e)
                raise e


class Loader(yaml.SafeLoader):

    def __init__(self, stream):
        self._root = os.path.split(stream.name)[0]
        super(Loader, self).__init__(stream)

    def include(self, node):
        filename = os.path.join(self._root, self.construct_scalar(node))
        with open(filename, 'r') as f:
            #return yaml.safe_load(f, Loader)
            return yaml.load(f, Loader)

Loader.add_constructor('!include', Loader.include)


if __name__ == "__main__":
    main = Main().execute()

