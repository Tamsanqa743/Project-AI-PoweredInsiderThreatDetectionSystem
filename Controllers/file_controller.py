import os

class file_controller:

  def __init__(self):
    self.uploaded_filename = ''

  
  def file_upload(self, file, storage_directory):
    '''save file to device storage'''
    self.uploaded_filename = file.filename
    target = os.path.join(storage_directory, file.filename)
    file.save(target)



def get_filename(self):
  '''returns name of uploaded file'''
  return self.uploaded_filename