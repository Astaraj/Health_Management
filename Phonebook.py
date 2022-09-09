phonebook={}
while True:
  print("1.Add")
  print("2.Update")
  print("3.Remove")
  print("4.Search")
  print("5.List")
  print("6.Exit")
  opt=int(input("Select option:"))
  if opt==1:
    name=input("Enter Name:")
    if name in phonebook:
      print(name,"Exist in phonebook")
    else:
      no=int(input("Enter phone number:"))
      phonebook[name]=no
      print("contact created")
  elif opt==2:
      name=input("Enter Name:")
      if name not in phonebook:
        print(name,"notfound in phonebook")
      else:
        phone=int(input("Enter phone number:"))
        phonebook[name]=phone
        print("number is updated")
  elif opt==3:
      name=input("Enter name to delete the number:")
      if name in phonebook:
        del phonebook[name]
        print(name,"is removed from phonebook")
      else:
        print(name,"not in phonebook")
  elif opt==4:
      name=input("Enter name:")
      if name in phonebook:
        print(name,phonebook[name])
      else:
        print(name,"not found")
  elif opt==5:
      for name,phone in phonebook.items():
        print(name,phone)
  elif opt==6:
      break
