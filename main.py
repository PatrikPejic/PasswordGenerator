import Generator as gen

if __name__ == "__main__": 
  password_length = input("Please Enter your desired Password length: ")
  password = gen.generate_password(int(password_length)) 
  print(f'Your Password is: {password}')
