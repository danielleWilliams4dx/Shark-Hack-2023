import random
import Alphanum
import Stringbreak

class Matrix:
  def __init__(self, n = 5, mat = []):
    self.mat = mat
    self.inv = []
    self.n = n
    if self.mat == []:
      self.generate()
    else:
      self.findInverse()

  # def rand5x5(self):
  #   self.mat = []
  #   for i in range(5):
  #     self.mat.append([])
  #     for j in range(5):
  #       self.mat[i].append(random.randint(-5,5))

  def generate(self):
    self.randNxN()
    self.findInverse()

  def rand5x5(self):
    tMat = [[raI(),0,0,0,0],[0,raI(),0,0,0],[0,0,raI(),0,0],[0,0,0,raI(),0],[0,0,0,0,raI()]]
    for i in range(5):
      for j in range(5):
        if i != j:
          tMat[j] = self.rowAdd(tMat[i], raI(), tMat[j])

    self.mat = tMat

  def randNxN(self):
    tMat = []
    for i in range(self.n):
      tMat.append([])
      for j in range(self.n):
        if i == j:
          tMat[i].append(1)
        else:
          tMat[i].append(0)
    for i in range(self.n):
      for j in range(self.n):
        if i != j:
          tMat[j] = self.rowAdd(tMat[i], raI(), tMat[j])
    self.mat = tMat
  
  def matPrint(self):
    for i in self.mat:
      print(i)

  def inv_matPrint(self):
    for i in self.inv:
      print(i)

  def multiply(self, li):
    if len(li) == len(self.mat):
      out = []
      for i in range(len(li)):
        sum = 0
        for j in range(len(li)):
          sum += li[j] * self.mat[j][i]
        out.append(sum)
      
      return out
    print("Length error")
    return li

  def invMult(self, li):
    if len(li) == len(self.inv):
      out = []
      for i in range(len(li)):
        sum = 0
        for j in range(len(li)):
          sum += li[j] * self.inv[j][i]
        out.append(int(round(sum)))
      return out
    print("Length error")
    return li

  def encode(self, msg):
    msg = Alphanum.alphanum(msg)
    msg = Stringbreak.stringbreak(msg, self.n)
    encode = []
    for i in msg:
      encode.append(self.multiply(i))
    return encode

  def getEncodedString(self,encoded):
    s = ""
    for i in encoded:
      for j in i:
        s += str(j)
    return(s)
    
  def decode(self, msg):
    decode = []
    for i in msg:
      decode.append(self.invMult(i))
    text = Alphanum.numalpha(decode)
    return text
  
  def getExtended(self):
    extMat = []
    for i in range(len(self.mat)):
      extMat.append([])
      for j in self.mat[i]:
        extMat[i].append(j)
    for i in range(len(self.mat)):
      # print(extMat)
      for j in range(len(self.mat)):
        #print(str(i),str(j))
        if i == j:
          extMat[i].append(1)
        else:
          extMat[i].append(0)
      
    return extMat

  def getHalf(self, ext):
    newMat = []
    for i in range(len(ext)):
      newMat.append(ext[i][len(ext):len(ext)*2])
    return newMat
  
  def findInverse(self):
    self.inv = self.getHalf(self.findRRE(self.getExtended()))
    
    return self.inv

  def findRRE(self,extMat = None):
    if(extMat != None):
      RRE_mat = extMat
    else:
      RRE_mat = self.mat
    for r in range(len(RRE_mat)):
      first = RRE_mat[r][r]
      if(first == 0):
          #perform swap with next valid row
          for k in range (r,len(RRE_mat)):
            if(RRE_mat[k][k] != 0):
              temp = RRE_mat[r]
              RRE_mat[r] = RRE_mat[k]
              RRE_mat[k] = temp
              first = RRE_mat[r][r]
              break
      if(first == 0):
        raise RuntimeError("can't divide by 0")
      if(first != 1):
        #divide entire row by the first non-zero entry
        RRE_mat[r] = self.rowMult(RRE_mat[r],(1/first))
      #add scalar*row to every other row
      for i in range(len(RRE_mat)):
        scalar = -RRE_mat[i][r]
        if(i != r):
          self.rowAdd(RRE_mat[r],scalar,RRE_mat[i])  
    return RRE_mat
  
  def rowMult(self, r1, mult):
    r = []
    for i in range(len(r1)):
      r.append(r1[i]*mult)
    return r

  def rowAdd(self, r1, mult, r2):
    r_mult = self.rowMult(r1, mult)
    for i in range(len(r2)):
      r2[i] += r_mult[i]
    return r2

  # def RRE_matPrint(self):
  #   RRE_mat = self.findRRE()
  #   for i in RRE_mat:
  #     print(i)

  # def ext_matPrint(self):
  #   ext_mat = self.findRRE(self.getExtended())
  #   for i in ext_mat:
  #     print(i)

def raI():
  num = random.randint(1,20)
  if random.randint(0,1) == 0:
    num *= -1
  return num