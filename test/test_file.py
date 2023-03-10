import json

import yaml

if __name__ == '__main__':

    with open("./gitlab-ci.yml", "r") as yml_file, open("./package.json", "r+", ) as cfgfile:
        file_data = yml_file.read()
        # print(file_data)
        ymldata = yaml.safe_load(file_data)
        i = 0
        for it in ymldata["build"]["script"]:
            its = str.split(it, " ")
            if len(its) < 2:
                raise Exception("无效指令")
            print( "".format("{}{}", it, i ))


        # lines = cfg_file.readlines()
        file_contents = cfgfile.read()
        # file_contents = "".join(lines)
        cfg = json.loads(file_contents)
        print(cfg)
