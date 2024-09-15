#run code here ig
import Matrix

# def encode(text, mat):
#   msg = Alphanum.alphanum(text)
#   msg = Stringbreak.stringbreak(msg)
#   msg = mat.encode(msg)
#   return msg

# def decode(msg, mat):
#   msg = mat.decode(msg)
#   text = Alphanum.numalpha(msg)
#   return text

# m = Matrix.Matrix()
# m.rand5x5()
# print("random encoding matrix:")
# m.matPrint()
# print()
# print("encode [1,2,3,4,5]:",m.multiply([1,2,3,4,5]))
# print()

# msg = Alphanum.alphanum("i say heck")
# print("i say heck -->", msg)
# msg = Stringbreak.stringbreak(msg)
# print("separate into 5s:",msg)

# msg = m.encode(msg)
# print("encoded:",msg)

# print()
# print("rowMult test:")
# r1 = [1,2,3,4,5]
# r2 = m.rowMult(r1,4)
# print("4 *",r1,"=",r2)
# print("rowAdd test:")
# print("7 *",r1,"+",r2,"=")
# print(m.rowAdd(r1,7,r2))

# # print()
# # print("RRE form of encoding matrix:")
# # m.RRE_matPrint()

# print()
# print("inverse of encoding matrix:")
# m.inv_matPrint()

# print()
# print("extended matrix:")
# m.ext_matPrint()
"""
coder = Matrix.Matrix(5)
text = "I love when my variables change without my consent!"
message = coder.encode(text)
print("encoded message:")
print(message)
print()
message = coder.decode(message)
print(message)
"""
# print(coder.mat)
# print(coder.inv)

coder = Matrix.Matrix(int(input("Matrix Size: ")))
name = input("Please enter your name: ")

rep = "Y"
while(rep == "Y" or rep == "y"):
  text = input("Type your message here: ")
  message = coder.encode(text)
  print()
  print(name + "'s encoded message:")
  print(coder.getEncodedString(message))
  print()
  message = coder.decode(message)
  ans = input("Enter Y to display encoding matrix: ")
  if(ans == 'Y' or ans == 'y'):
    print(coder.mat)
  print()
  ans = input("Enter Y to decrypt: ")
  if(ans == 'Y' or ans == 'y'):
    print(name + "'s decrypted message:", message)
  print()
  rep = input("Enter Y to Continue: ")
  print()

"""
coder = Matrix.Matrix(5)
message = coder.encode(text)
print("encoded message:")
print(coder.getEncodedString(message))
"""