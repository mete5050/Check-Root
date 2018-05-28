if os.geteuid() != 0:
    print("Super user olarak çalıştır ")
else:
    print("Sen root kulanıcısın")
