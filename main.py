# 这是一个示例 Python 脚本。
import json
import os
import subprocess
import sys

# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。

scripts_json = '''{"chain": "npx hardhat node --network hardhat",
    "test": "npx hardhat test --network hardhat",
    "compile": "npx hardhat compile",
    "generate": "scripts/generate.sh",
    "verify": "npx hardhat verify",
    "coverage": "npx hardhat clean && npx hardhat coverage --network hardhat",
    "typechain": "npx hardhat typechain",
    "clean": "npx hardhat clean",
    "slither": "npm run clean && slither . "
    }
'''


# # Hourse
#
# ## Overview
#
# The Hourse is include a Hourse NFT and a Lootbox.


def get_package_info():
    try:
        with open("./package.json", "r+") as user_file:
            file_contents = user_file.read()
            cfg = json.loads(file_contents)
            return cfg

    except  Exception as er:
        print(er)
    finally:
        user_file.close()


def process_readme(readmeFile):
    try:

        package_info = get_package_info()

        with open(readmeFile, "r+") as user_file:
            lines = user_file.readlines()

            i = 0
            for item in lines:
                if item == "# Hourse\n":
                    lines[i] = "# " + package_info["name"] + "\n"

                if item == "The Hourse is include a Hourse NFT and a Lootbox.\n":
                    lines[i] = package_info["description"] + "\n"

                i = i+1

            user_file.seek(0)
            user_file.writelines(lines)

    except  Exception as er:
        print(er)
    finally:
        user_file.close()


def process_package_config(cfgFile):
    try:
        with open(cfgFile, "r+") as user_file:
            file_contents = user_file.read()
            cfg = json.loads(file_contents)
            scripts = json.loads(scripts_json)
            cfg["scripts"] = scripts
            file_contents = json.dumps(cfg, indent=4)
            user_file.seek(0)
            user_file.write(file_contents)

    except  Exception as er:
        print(er)
    finally:
        user_file.close()

# 按间距中的绿色按钮以运行脚本。
# pyinstaller -F main.py -n process_config

if __name__ == '__main__':

    # "./example/package.json"
    process_package_config("./package.json")
    process_readme("./README.md")

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
