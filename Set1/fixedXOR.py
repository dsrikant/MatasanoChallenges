from bitstring import BitArray
import sys

inp1 = '1c0111001f010100061a024b53535009181c'
inp2 = '686974207468652062756c6c277320657965'

if len(inp1) != len(inp2):
  sys.exit('The two inputs were not the same length')

x = bin(int(inp1, base=16)).lstrip('0b')
y = bin(int(inp2, base=16)).lstrip('0b')

init = 0
chomp = 5
xor = ''

# Iterate over len(x) because we are guarenteed equal length buffers
while chomp <= len(x) :
  xor = xor +  
