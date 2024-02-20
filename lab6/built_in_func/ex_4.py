# Write a Python program that invoke square root function after specific milliseconds.
from time import sleep

root = int(input())
delaychik = int(input())

sleep(delaychik / 1000)
print(f'Square root of {root} after {delaychik} miliseconds is {root ** 0.5}')