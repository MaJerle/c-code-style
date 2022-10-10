import os
import glob
import argparse
import json


def get_parser():
    # Define parser structure
    parser = argparse.ArgumentParser(
        description='Runs clang-format with local format file. Local paths are scanned from local clang-format-config.json file')
    parser.add_argument(
        '--path', help='One or more paths to run the script', nargs='+', default='.')
    parser.print_help()
    return parser


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    paths = args.path
    for path in paths:
        path = os.path.join(os.getcwd(), path)
        path = os.path.normpath(path)

        if os.path.exists(path) and os.path.isdir(path):
            print("Path exists and is directory")
            configfile = os.path.join(path, "clang-format-config.json")
            config = {}
            with open(configfile, "r") as f:
                config = json.loads(f.read())

            if 'version' not in config or config['version'] != 1:
                print("Invalid configuration version - should be 1")
            elif 'paths' not in config:
                print("Paths key is missing")
            else:
                globdata = []
                for p in config['paths']:
                    recursive = False
                    if type(p) is dict:
                        recursive = p['recursive'] if 'recursive' in p else False
                        pp = p['path'] if 'path' in p else False
                    else:
                        pp = p

                    # Run glob
                    if pp:
                        globdata = globdata + \
                            glob.glob(os.path.join(path, pp),
                                      recursive=recursive)

                # Normalize all paths now
                globdata = [os.path.normpath(p) for p in globdata]
                print(json.dumps(globdata, indent=4))

                # Run clang-format
                if len(globdata) > 0:
                    os.chdir(path)
                    for file in globdata:
                        os.system(
                            "clang-format -style=file -i -verbose \"{:s}\"".format(file))
        else:
            print("Path {:s} does not exists or is not a path".format(path))
