# This is a formatter file. Internal Usage ONLY. DO NOT PROPAGATE
import time

lista = dict(n=0,e=0,c=0,p=0,q=0)
print("Running RsaFormatter. Prepare items for input. Order as follows, n -> e -> c -> p -> q")
time.sleep(0.25)
print("n -> MODULUS\ne -> public exponent (usually 65537)\nc -> ciphertext\np -> prime number1\nq -> prime number2")
time.sleep(0.25)
print("If value is NOT available/missing/whatever, type in 0.")
time.sleep(0.25)

for i in lista:
    lista[i] = int(input("Please input {}: ".format(i)))
    if lista[i] != 0:
        lista[i] = str(lista[i])
        lista[i] = "-" + i + " " + lista[i]
    else:
        lista[i] = str(lista[i])
        lista[i] = ""

print("COPY AND PASTE SAID COMMAND: ./RsaCtfTool.py --decrypt {} {} {} {} {}".format(lista["c"], lista["n"], lista["e"], lista["p"], lista["q"]))


