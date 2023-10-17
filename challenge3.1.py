def lidef linerSearchProduct(productlist,targetProduct):nerSearchProduct(productlist,targetProduct):
  indices=[]

  for index,product in enumerate(productlist):
    if product == targetProduct:
      indices.append(index)

  return indices



products=["shoes","boot","loafer","shoes","sandal","shoes"]
target="shoes"
result=linerSearchProduct(products,target)
print(result)