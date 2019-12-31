pattern = [0,1,0,-1]
inp = "59764635797473718052486376718142408346357676818478503599633670059885748195966091103097769012608550645686932996546030476521264521211192035231303791868456877717957482002303790897587593845163033589025995509264282936119874431944634114034231860653524971772670684133884675724918425789232716494769777580613065860450960426147822968107966020797566015799032373298777368974345143861776639554900206816815180398947497976797052359051851907518938864559670396616664893641990595511306542705720282494028966984911349389079744726360038030937356245125498836945495984280140199805250151145858084911362487953389949062108285035318964376799823425466027816115616249496434133896"

t1 = "80871224585914546619083218645595"
t2 = "19617804207202209144916044189917"
t3 = "69317163492948606335995924319873"
a1 = "24176176"
a2 = "73745418"
a3 = "52432133"

#string to list
inplist = list()
for c in inp:
  inplist.append(int(c))


class fft:
  def __init__(self, pattern = list(), inp = list()):
    self.pattern = pattern
    self.inp = inp

  def addInput(self, inp):
    self.inp = inp


  def run(self):
    multipl = 1
    citer = 0
    itr = 0
    ret = list()
    while len(ret) < len(self.inp):
      new = 0
      miter = 1
      itr = 0
      for i in self.inp:
        if miter == multipl:
          miter = 0
          itr += 1
          if itr == len(self.pattern):
            itr = 0
        new += int(i) * int(pattern[itr])
        miter += 1
      ret.append(int(str(new)[-1]))
      multipl += 1
    return ret

def firstStar(pattern, inp):
  c = fft(pattern, inp)
  for i in range(100):
    ret = c.run()
    c.addInput(ret)

  answer=""
  for i in range(8):
    answer += str(ret[i])

  return answer


def testFS(pattern, inp, ans):
  if ans == firstStar(pattern, inp):
    print("TEST OK")
  else:
    print("TEST FAIL")

testFS(pattern, t1, a1)
testFS(pattern, t2, a2)
testFS(pattern, t3, a3)
print(firstStar(pattern,inp))