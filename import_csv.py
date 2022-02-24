## ------------- Libraries
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog

## ------------- Global Variables
#csvFileName = "pdfTools.csv"
#xmlFileName = "pdfTemplate.xml"
#outputDirectoryName = "pdfOutput\\"
## ------------- Functions

def browseXmlFile():
    global xmlFileName
    xmlFileName = filedialog.askopenfilename(initialdir = "/", title = "Select an XML template file", filetypes = (("XML files", "*.xml*"), ("All files",".")))
    labelXmlFile.configure(text = "XML file: " + xmlFileName)

def browseCsvFile():
    global csvFileName
    csvFileName = filedialog.askopenfilename(initialdir = "/", title = "Select an CSV data file", filetypes = (("CSV files", "*.csv*"), ("All files",".")))
    labelCsvFile.configure(text = "CSV file: " + csvFileName)

def browseOutputDirectory(): 
    global outputDirectoryName
    outputDirectoryName = filedialog.askdirectory()
    labelOutputDirectory.configure(text = "Output directory: " + outputDirectoryName)

def convertCsv2Xml(pdfToolsPath, pdfTemplatePath, pdfOutputPath):
    import csv
    with open(pdfToolsPath, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)   
        parameters = next(csv_reader)     
        print(parameters)
        for line in csv_reader:
            #print(line)
            pdfTemplate = open(pdfTemplatePath, 'r')      
            toolData=pdfTemplate.read()     
            parameterIndex = 0       
            for parameter in parameters:
                # print(parameter)
                # print(line[parameterIndex])
                toolData = toolData.replace(parameter, line[parameterIndex])
                parameterIndex += 1          
            pdfOutputXmlPath = pdfOutputPath + "/" + line[0] + ".xml"
            #print(toolData)
            with open(pdfOutputXmlPath, 'w') as pdfOutput:
                pdfOutput.write(toolData)
    labelCsv2Xml.configure(text = "Files converted")

# ------------- GUI

root = Tk()
root.title("PDF Assistant")
root.geometry('750x750')

label = Label(root, text = "Please select a XML template, CSV data file and output directory").pack() # Test

browseXmlBtn = Button(root, text = "Browse XML files", command = browseXmlFile).pack()

labelXmlFile = Label(root, text = "Select a XML template file")
labelXmlFile.pack()

browseCsvBtn = Button(root, text = "Browse CSV files", command = browseCsvFile).pack()

labelCsvFile = Label(root, text = "Select a CSV data file")
labelCsvFile.pack()

browseOutputDirectoryBtn = Button(root, text = "Browse output directories", command = browseOutputDirectory).pack()

labelOutputDirectory = Label(root, text = "Select an output directory")
labelOutputDirectory.pack()

convertCsv2XmlBtn = Button(root, text = "Convert selected files", command = lambda: convertCsv2Xml(csvFileName, xmlFileName, outputDirectoryName)).pack() 

labelCsv2Xml = Label(root, text = "Not done yet")
labelCsv2Xml.pack()

cancelBtn = Button(root, text = 'Cancel', command = root.destroy).pack(side = 'bottom')

root.mainloop()

# pdfToolsPath = "pdfTools.csv"
# pdfTemplatePath = "pdfTemplate.xml"
# pdfOutputPath = "pdfOutput\\"

# convertCsv2Xml("pdfTools.csv", "pdfTemplate.xml", "pdfOutput\\")