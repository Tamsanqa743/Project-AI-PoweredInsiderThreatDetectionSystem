import os

class file_controller:
  
  @staticmethod
  def file_upload(file, storage_directory):
    '''save file to device storage'''
    target = os.path.join(storage_directory, file.filename)
    file.save(target)