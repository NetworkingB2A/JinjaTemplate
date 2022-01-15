#!/usr/bin/env python
import csv
from jinja2 import Template

templateFileName = input("What is the name of the file? (Without extensions): ")
templateFileJinja = f"templateData/jinjaTemplateFile/{templateFileName}.j2"
templateFileCsv = f"templateData/csvVarFile/{ templateFileName }.csv"


with open(templateFileJinja) as templateFile:
    template = Template(templateFile.read())

with open(templateFileCsv, newline="") as csvfile:
    csvDictVar = csv.DictReader(csvfile)
    for row in csvDictVar:
        scriptOutputData = template.render(row)
        scriptOutputLocation = f"scriptOutput/{row['fileName']}"
        with open(scriptOutputLocation, "w") as scriptName:
            scriptName.write(scriptOutputData)
        print(f"{row['fileName']} has been created")
