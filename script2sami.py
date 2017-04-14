from xml.etree.ElementTree import parse
from jinja2 import Template,Environment,FileSystemLoader
import os
import sys


def mkSami(script):
    vlist = parse(script).getroot().getiterator("data")
    plist = [
                {
                    "time":d.findtext("time"),
                    "kor":d.findtext("kor"),
                    "eng":d.findtext("eng")
                }
                for d in vlist
            ]
    for phrase in plist:
        phrase['time'] = str(int(phrase['time'])*1000)  # sec --> milli sec
        if phrase['kor'] == "...":
            phrase['kor'] = "&nbsp;"
        if phrase['eng'] == "...":
            phrase['eng'] = "&nbsp;"
    currFileDirPath = os.path.dirname(os.path.abspath(__file__))
    env = Environment(
        loader=FileSystemLoader(currFileDirPath)
    )
    template = env.get_template('sami_template.txt')
    result = template.render(title="SAMI Subtitles", plist=plist)
    return result


def main():
    if len(sys.argv) == 2:
        inputPath = sys.argv[1]
    else:
        inputPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "script_sample.xml")
    print(mkSami(inputPath))

if __name__ == "__main__":
    main()
