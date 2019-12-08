import os
os.system('gitbook build WorkFlow/')
os.system('cp -r WorkFlow/_book/* .')
os.system('git add .')
os.system('git commit -m commit')
os.system('git push')
