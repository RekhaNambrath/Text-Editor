import sys
from PyQt4 import QtGui,QtCore
from PyQt4.QtCore import Qt
from ext import *
def main():
	app=QtGui.QApplication(sys.argv)
	writr=Writer()
	sys.exit(app.exec_())

class Writer(QtGui.QMainWindow):
	
	def __init__(self,parent=None):
		super(Writer,self).__init__()
		self.filename = ""	
		self.initUI()
	def initToolbar(self):
		self.toolbar=QtGui.QToolBar()
		self.addToolBar(Qt.LeftToolBarArea,self.toolbar)
		self.addToolBarBreak()
		
		self.newAction = QtGui.QAction(QtGui.QIcon("icons/newfile.png"),"New",self)
  		self.newAction.setStatusTip("Create a new document from scratch.")
  		self.newAction.setShortcut("Ctrl+N")
  		self.newAction.triggered.connect(self.new)

  		self.openAction = QtGui.QAction(QtGui.QIcon("icons/open.png"),"Open file",self)
  		self.openAction.setStatusTip("Open existing document")
  		self.openAction.setShortcut("Ctrl+O")
  		self.openAction.triggered.connect(self.open)

  		self.saveAction = QtGui.QAction(QtGui.QIcon("icons/Save.png"),"Save",self)
  		self.saveAction.setStatusTip("Save document")
  		self.saveAction.setShortcut("Ctrl+S")
  		self.saveAction.triggered.connect(self.save)
		
		self.toolbar.addAction(self.newAction)
  		self.toolbar.addAction(self.openAction)
  		self.toolbar.addAction(self.saveAction)
		self.toolbar.addSeparator()
		
		self.printAction = QtGui.QAction(QtGui.QIcon("icons/print.png"),"Print document",self)
    		self.printAction.setStatusTip("Print document")
    		self.printAction.setShortcut("Ctrl+P")
    		self.printAction.triggered.connect(self.Print)

    		self.previewAction = QtGui.QAction(QtGui.QIcon("icons/preview.png"),"Page view",self)
    		self.previewAction.setStatusTip("Preview page before printing")
    		self.previewAction.setShortcut("Ctrl+Shift+P")
    		self.previewAction.triggered.connect(self.preview)

		self.toolbar.addAction(self.printAction)
		self.toolbar.addAction(self.previewAction)
		self.toolbar.addSeparator()
	
		self.cutAction = QtGui.QAction(QtGui.QIcon("icons/cut.png"),"Cut to clipboard",self)
    		self.cutAction.setStatusTip("Delete and copy text to clipboard")
    		self.cutAction.setShortcut("Ctrl+X")
    		self.cutAction.triggered.connect(self.text.cut)

    		self.copyAction = QtGui.QAction(QtGui.QIcon("icons/copy.png"),"Copy to clipboard",self)
    		self.copyAction.setStatusTip("Copy text to clipboard")
    		self.copyAction.setShortcut("Ctrl+C")
    		self.copyAction.triggered.connect(self.text.copy)

    		self.pasteAction = QtGui.QAction(QtGui.QIcon("icons/paste.png"),"Paste from clipboard",self)
    		self.pasteAction.setStatusTip("Paste text from clipboard")
    		self.pasteAction.setShortcut("Ctrl+V")
    		self.pasteAction.triggered.connect(self.text.paste)

    		self.undoAction = QtGui.QAction(QtGui.QIcon("icons/undo.png"),"Undo last action",self)
    		self.undoAction.setStatusTip("Undo last action")
    		self.undoAction.setShortcut("Ctrl+Z")
    		self.undoAction.triggered.connect(self.text.undo)

    		self.redoAction = QtGui.QAction(QtGui.QIcon("icons/redo.png"),"Redo last undone thing",self)
    		self.redoAction.setStatusTip("Redo last undone thing")
    		self.redoAction.setShortcut("Ctrl+Y")
    		self.redoAction.triggered.connect(self.text.redo)

		self.toolbar.addAction(self.cutAction)
    		self.toolbar.addAction(self.copyAction)
    		self.toolbar.addAction(self.pasteAction)
    		self.toolbar.addAction(self.undoAction)
    		self.toolbar.addAction(self.redoAction)
    		self.toolbar.addSeparator()

		bulletAction = QtGui.QAction(QtGui.QIcon("icons/bullets.png"),"Insert bullet List",self)
    		bulletAction.setStatusTip("Insert bullet list")
    		bulletAction.setShortcut("Ctrl+Shift+B")
   		bulletAction.triggered.connect(self.bulletList)

    		numberedAction = QtGui.QAction(QtGui.QIcon("icons/numbered.png"),"Insert numbered List",self)
    		numberedAction.setStatusTip("Insert numbered list")
    		numberedAction.setShortcut("Ctrl+Shift+L")
   		numberedAction.triggered.connect(self.numberList)		

	    	self.toolbar.addAction(bulletAction)
		self.toolbar.addAction(numberedAction)	
		self.toolbar.addSeparator()

		self.findAction = QtGui.QAction(QtGui.QIcon("icons/find.png"),"Find and replace",self)
	    	self.findAction.setStatusTip("Find and replace words in your document")
    		self.findAction.setShortcut("Ctrl+F")
    		self.findAction.triggered.connect(find.Find(self).show)
		
		self.toolbar.addSeparator()
	    	self.toolbar.addAction(self.findAction)

	def initFormatbar(self):
		fontBox = QtGui.QFontComboBox(self)
    		fontBox.currentFontChanged.connect(self.fontFamily)

    		fontSize = QtGui.QComboBox(self)
    		fontSize.setEditable(True)

    		# Minimum number of chars displayed
    		fontSize.setMinimumContentsLength(3)
    		fontSize.activated.connect(self.fontSize)

    		# Typical font sizes
    		fontSizes = ['6','7','8','9','10','11','12','13','14',
                	 '15','16','18','20','22','24','26','28',
                	 '32','36','40','44','48','54','60','66',
                	 '72','80','88','96']

	    	for i in fontSizes:
        		fontSize.addItem(i)

    		fontColor = QtGui.QAction(QtGui.QIcon("icons/font-color.png"),"Change font color",self)
    		fontColor.triggered.connect(self.fontColor)

    		backColor = QtGui.QAction(QtGui.QIcon("icons/highlight.png"),"Change background color",self)
    		backColor.triggered.connect(self.highlight)

		boldAction = QtGui.QAction(QtGui.QIcon("icons/bold.png"),"Bold",self)
		boldAction.triggered.connect(self.bold)

    		italicAction = QtGui.QAction(QtGui.QIcon("icons/italic.png"),"Italic",self)
    		italicAction.triggered.connect(self.italic)

    		underlAction = QtGui.QAction(QtGui.QIcon("icons/underline.png"),"Underline",self)
    		underlAction.triggered.connect(self.underline)

    		strikeAction = QtGui.QAction(QtGui.QIcon("icons/strike.jpg"),"Strike-out",self)
    		strikeAction.triggered.connect(self.strike)

    		superAction = QtGui.QAction(QtGui.QIcon("icons/superscript.png"),"Superscript",self)
    		superAction.triggered.connect(self.superScript)

    		subAction = QtGui.QAction(QtGui.QIcon("icons/subscript.png"),"Subscript",self)
    		subAction.triggered.connect(self.subScript)

    		alignLeft = QtGui.QAction(QtGui.QIcon("icons/align-left.png"),"Align left",self)
    		alignLeft.triggered.connect(self.alignLeft)

    		alignCenter = QtGui.QAction(QtGui.QIcon("icons/align-center.png"),"Align center",self)
    		alignCenter.triggered.connect(self.alignCenter)

    		alignRight = QtGui.QAction(QtGui.QIcon("icons/align-right.png"),"Align right",self)
    		alignRight.triggered.connect(self.alignRight)

    		alignJustify = QtGui.QAction(QtGui.QIcon("icons/align-justify.png"),"Align justify",self)
    		alignJustify.triggered.connect(self.alignJustify)
		self.formatbar = self.addToolBar("Format")

    		self.formatbar.addWidget(fontBox)
    		self.formatbar.addWidget(fontSize)

    		self.formatbar.addSeparator()

    		self.formatbar.addAction(fontColor)
    		self.formatbar.addAction(backColor)
		self.formatbar.addSeparator()
		
		self.formatbar.addAction(boldAction)
    		self.formatbar.addAction(italicAction)
    		self.formatbar.addAction(underlAction)
    		self.formatbar.addAction(strikeAction)
   	 	self.formatbar.addSeparator()
		self.formatbar.addAction(superAction)
    		self.formatbar.addAction(subAction)
		self.formatbar.addSeparator()
		
		self.formatbar.addAction(alignLeft)
	    	self.formatbar.addAction(alignCenter)
    		self.formatbar.addAction(alignRight)
    		self.formatbar.addAction(alignJustify)
	    	self.formatbar.addSeparator()

	def initMenubar(self):
		menubar=self.menuBar()
		file=menubar.addMenu("File")
		edit=menubar.addMenu("Edit")
		view=menubar.addMenu("View")
		file.addAction(self.newAction)
    		file.addAction(self.openAction)
    		file.addAction(self.saveAction)
		file.addAction(self.printAction)
		file.addAction(self.previewAction)
		edit.addAction(self.undoAction)
	    	edit.addAction(self.redoAction)
    		edit.addAction(self.cutAction)
    		edit.addAction(self.copyAction)
    		edit.addAction(self.pasteAction)
		edit.addAction(self.findAction) 
		   # Toggling actions for the various bars
    		toolbarAction = QtGui.QAction("Toggle Toolbar",self)
    		toolbarAction.triggered.connect(self.toggleToolbar)

    		formatbarAction = QtGui.QAction("Toggle Formatbar",self)
    		formatbarAction.triggered.connect(self.toggleFormatbar)

    		statusbarAction = QtGui.QAction("Toggle Statusbar",self)
    		statusbarAction.triggered.connect(self.toggleStatusbar)

    		view.addAction(toolbarAction)
    		view.addAction(formatbarAction)
    		view.addAction(statusbarAction)



	def setTooltip(self,btn):
		QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        	self.setToolTip('This is a <b>QWidget</b> widget')
        	btn.setToolTip('This is a <b>QPushButton</b> widget')
           
	def closeEvent(self,event):
		reply=QtGui.QMessageBox.question(self, 'Message', "Are you sure to quit?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
		if reply == QtGui.QMessageBox.Yes:
           		event.accept()
        	else:
            		event.ignore()        
        
	def initUI(self):
		self.text=QtGui.QTextEdit(self)
		self.setCentralWidget(self.text)
		self.initToolbar()
		self.initFormatbar()
		self.initMenubar()
		self.text.setTabStopWidth(33)
		self.statusbar=self.statusBar()
		self.setGeometry(100,100,1000,500)
		self.setWindowTitle('Scribble')
		self.setWindowIcon(QtGui.QIcon('icons/writer.png'))
		self.text.cursorPositionChanged.connect(self.cursorPosition)
		self.show()
	
	def new(self):
	        spawn = Writer()
	   	spawn.show()

    	def open(self):

        # Get filename and show only .writer files
        	self.filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File',".","(*.writer)")
        	if self.filename:
            		with open(self.filename,"rt") as file:
                		self.text.setText(file.read())

    	def save(self):

        # Only open dialog if there is no filename yet
        	if not self.filename:
            		self.filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File')

        # Append extension if not there yet
        	if not self.filename.endsWith(".writer"):
            		self.filename += ".writer"

        # We just store the contents of the text file along with the
        # format in html, which Qt does in a very nice way for us
      	        with open(self.filename,"wt") as file:
           		 file.write(self.text.toHtml())
	
	def preview(self):
        # Open preview dialog
        	preview = QtGui.QPrintPreviewDialog()

        # If a print is requested, open print dialog
        	preview.paintRequested.connect(lambda p: self.text.print_(p))
        	preview.exec_()

        def Print(self):
        # Open printing dialog
       		dialog = QtGui.QPrintDialog()
	        if dialog.exec_() == QtGui.QDialog.Accepted:
        		self.text.document().print_(dialog.printer())

	def bulletList(self):
        	cursor = self.text.textCursor()
        	# Insert bulleted list
        	cursor.insertList(QtGui.QTextListFormat.ListDisc)

    	def numberList(self):
	        cursor = self.text.textCursor()
	        # Insert list with numbers
        	cursor.insertList(QtGui.QTextListFormat.ListDecimal)
	
	def cursorPosition(self):
        	cursor = self.text.textCursor()
	        # Mortals like 1-indexed things
        	line = cursor.blockNumber() + 1
        	col = cursor.columnNumber()
        	self.statusbar.showMessage("Line: {} | Column: {}".format(line,col))

	def fontFamily(self,font):
     		 self.text.setCurrentFont(font)

    	def fontSize(self, fontsize):
        	self.text.setFontPointSize(int(fontsize))

    	def fontColor(self):

        	# Get a color from the text dialog
        	color = QtGui.QColorDialog.getColor()
	
        	# Set it as the new text color
        	self.text.setTextColor(color)

    	def highlight(self):

        	color = QtGui.QColorDialog.getColor()
        	self.text.setTextBackgroundColor(color)

	def bold(self):
	        if self.text.fontWeight() == QtGui.QFont.Bold:
        	    self.text.setFontWeight(QtGui.QFont.Normal)
	        else:
	            self.text.setFontWeight(QtGui.QFont.Bold)

    	def italic(self):
	        state = self.text.fontItalic()
	        self.text.setFontItalic(not state)
	
	def underline(self):
	        state = self.text.fontUnderline()
	        self.text.setFontUnderline(not state)

    	def strike(self):
	        # Grab the text's format
        	fmt = self.text.currentCharFormat()
        	# Set the fontStrikeOut property to its opposite
	        fmt.setFontStrikeOut(not fmt.fontStrikeOut())
	        # And set the next char format
        	self.text.setCurrentCharFormat(fmt)

        def superScript(self):
	        # Grab the current format
       	        fmt = self.text.currentCharFormat()
	        # And get the vertical alignment property
        	align = fmt.verticalAlignment()
	        # Toggle the state
        	if align == QtGui.QTextCharFormat.AlignNormal:
	            fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignSuperScript)
	        else:
	            fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignNormal)
        	# Set the new format
		self.text.setCurrentCharFormat(fmt)

    	def subScript(self):
	        # Grab the current format
	        fmt = self.text.currentCharFormat()
	        # And get the vertical alignment property
	        align = fmt.verticalAlignment()
	        # Toggle the state
	        if align == QtGui.QTextCharFormat.AlignNormal:
	            fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignSubScript)
	        else:
	            fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignNormal)
	        # Set the new format
        	self.text.setCurrentCharFormat(fmt)

	def alignLeft(self):
        	self.text.setAlignment(Qt.AlignLeft)

    	def alignRight(self):
        	self.text.setAlignment(Qt.AlignRight)

    	def alignCenter(self):
        	self.text.setAlignment(Qt.AlignCenter)

    	def alignJustify(self):
        	self.text.setAlignment(Qt.AlignJustify)

	def toggleToolbar(self):
	      	state = self.toolbar.isVisible()
      	# Set the visibility to its inverse
      		self.toolbar.setVisible(not state)

    	def toggleFormatbar(self):
	        state = self.formatbar.isVisible()
	        # Set the visibility to its inverse
        	self.formatbar.setVisible(not state)
	def toggleStatusbar(self):
	        state = self.statusbar.isVisible()
	        # Set the visibility to its inverse
	        self.statusbar.setVisible(not state)

if __name__=='__main__':
	main()
