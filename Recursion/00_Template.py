from unicodedata import name


class recursion:

  def printDecreasing(self,n):
    if n==0:
      return

    print(n)
    self.printDecreasing(n-1)

  def printIncreasing(self,n):
    if n==0:
      return
    self.printIncreasing(n-1)
    print(n)


if __name__=='__main__':
  out = recursion()
  # out.printDecreasing(int(input("Enter the number: ")))
  out.printIncreasing(int(input("Enter the number: ")))
