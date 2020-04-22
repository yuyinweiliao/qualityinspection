import json

from chronos.script import Script


def run(arguments, event):
    arguments = json.loads(arguments)
    script_uid = arguments["script_uid"]

    script = Script(script_uid)

    script.execute()