from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run when the form opens.
    self.QA_History.items = app_tables.history.search() # Gets the whole table from Anvil DB
    # Possible Mongo DB Call
    DB = anvil.server.call('Call_All_DB')
    print(DB)
#     self.QA_History.items = DB
  
  
  
  def image_loader_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    uploaded_image = self.image_Uploader.file # get image
    self.image_preview.source = uploaded_image # Set image for preview window
    print('image uploaded')
    pass

  def QA_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    uploaded_image = self.image_Uploader.file # get image
    QA = anvil.server.call('QandA_Generated', uploaded_image) # call function and pass image arg
    self.Caption_Text.text = QA[0] # Set and display the Caption
    self.Answer_Text_Editable.text = QA[1] # Set and display the Answer that is Editable
    self.Question_Text_Editable.text = QA[2] # Set and display the Question that is Editable
    print(QA)
    pass

  def Save_click(self, **event_args):
    """This method is called when the button is clicked"""
    Cap = self.Caption_Text.text # get Caption
    Ans = self.Answer_Text_Editable.text # get Answer
    Ques = self.Question_Text_Editable.text # get question
    uploaded_image = self.image_Uploader.file # get image
    
    # Alpha test of Mongo DB
    test = anvil.server.call('Add_DB', Cap, Ans, Ques, uploaded_image) # Call function and pass arg
    print(test)
    
    # Alpha test of Anvil DB
    app_tables.history.add_row(Answer=Ans, Caption=Cap, Question=Ques, Image=uploaded_image) # add new row to DB base on user inputs
    print("Inser Into Anvil DB")
    self.QA_History.items = app_tables.history.search() # Refreshes the Repeating Panel
    print("Reload QA History")
    pass