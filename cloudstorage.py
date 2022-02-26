import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb') 
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'Fr8UHqG7iXYAAAAAAAAAAWStc0XUYUBNVvEyYPmjnYxb5lSYlqwL8Yzna_uU1x6n'
    transferData = TransferData(access_token)

    file_from = input("Enter your file path here: ")
    file_to = input("Enter to upload a file for dropbox: ") 

    transferData.upload_file(file_from, file_to)
    print("File has been moved")

main()