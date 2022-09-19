name = input("file name: ")

ci_name = name.lower().strip()

dot_count = ci_name.count(".")

name_split = ci_name.split(".")

if dot_count == 0:
    print("application/octet-stream")

else:
    if name_split[-1] == "gif":
        print("image/gif")
    elif name_split[-1] == "jpg":
        print("image/jpeg")
    elif name_split[-1] == "jpeg":
        print("image/jpeg")
    elif name_split[-1] == "png":
        print("image/png")
    elif name_split[-1] == "pdf":
        print("application/pdf")
    elif name_split[-1] == "txt":
        print("text/plain")
    elif name_split[-1] == "zip":
        print("application/zip")
    else:
        print("application/octet-stream")