_list = {
    "gif" : "image/gif",
    "jpg" : "image/jpeg",
    "jpeg" : "image/jpeg",
    "png" : "image/png",
    "pdf" : "application/pdf",
    "txt" : "text/plain",
    "zip" : "application/zip"
}

txt = input("File name: ").strip().lower()

if "." in txt:
    extension = txt.split(".")[-1]
    if extension in _list:
        print(_list[extension])
    else:
        print("application/octet-stream")
else:
    print("application/octet-stream")
