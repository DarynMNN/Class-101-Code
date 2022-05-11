import dropbox
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)
def main():
    access_token = 'sl.BHM1R1sn2CapN9uEt6eOxhsziSjJzmRw1Zjgv1khS_cfBBpUSbHMBEaB03ICIp-SVQQt8uJzKauunDFhOmFNg0tTkelbJF55dRG9tOBRF0gOz4JemqHDOojD6N2DH5qK9113ZgNCifRq'
    transferdata = TransferData(access_token)
    file_from = input("enter the file path to transfer:-> ")
    file_to = input("enter the full path to upload to dropbox:->")
    transferdata.upload_file(file_from, file_to)
    print("file has been moved!")
main()