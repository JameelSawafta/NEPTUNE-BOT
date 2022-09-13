def ar_or_en(j):
  if j.startswith(">>tr "):
      x=j[5:].split()
  elif j.startswith(">>translate "):
      x=j[12:].split()
  #x=j.split()
  comsg=list()
  for w in x:
      for e in w:
          comsg.append(e)
  arab=['أ','ب','ت','ث','ج','ح','خ','د','ذ','ر','ز','س','ش','ص','ض','ط',',''ع', 'غ','ف','ق','ك','ل','م','ن','ه','و','ي','ظ','ا']

  en=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

  if (any(letter in comsg for letter in arab)and any(letter in comsg for letter in en)):
    return 3
  elif any(letter in comsg for letter in arab):
      return 1
  elif any(letter in comsg for letter in en):
    return 2
  
def ar_or_en0(j):
  x=j.split()
  comsg=list()
  for w in x:
      for e in w:
          comsg.append(e)
  arab=['أ','ب','ت','ث','ج','ح','خ','د','ذ','ر','ز','س','ش','ص','ض','ط',',''ع', 'غ','ف','ق','ك','ل','م','ن','ه','و','ي','ظ','ا']

  en=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

  if (any(letter in comsg for letter in arab)and any(letter in comsg for letter in en)):
    return 3
  elif any(letter in comsg for letter in arab):
      return 1
  elif any(letter in comsg for letter in en):
    return 2
  