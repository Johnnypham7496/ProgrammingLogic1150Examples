# for the code to be able to read docx, you will need to install docx packages
# this how create a word doc with adding in a paragraph
import docx

document = docx.Document()

document.add_paragraph('Hello Word!')

document.save('hello_word.docx')