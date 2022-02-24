import csv
with open(('pdfTools.csv'), 'r') as csv_file:
    csv_reader = csv.reader(csv_file)   
    parameters=next(csv_reader)     
    for line in csv_reader:
        pdfTemplate = open('pdfTemplate.xml', 'r')      
        toolData=pdfTemplate.read()     
        parameterIndex=0       
        for parameter in parameters:
            toolData=toolData.replace(parameter, line[parameterIndex])
            parameterIndex += 1          
        pdfOutputPath="pdfOutput\\" + line[0] + ".xml"
        with open(pdfOutputPath, 'w') as pdfOutput:
            pdfOutput.write(toolData)