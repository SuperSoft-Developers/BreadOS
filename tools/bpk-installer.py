import zipfile
import json
import os

APPS_DIR = "/opt/breados/apps"

def install_bpk(file):
    with zipfile.ZipFile(file, 'r') as z:
        z.extractall("/tmp/bread_install")

    with open("/tmp/bread_install/manifest.json") as f:
        manifest = json.load(f)

    app_name = manifest["name"]

    os.system(
        f"cp -r /tmp/bread_install {APPS_DIR}/{app_name}"
    )

if __name__ == "__main__":
    import sys
    install_bpk(sys.argv[1])
