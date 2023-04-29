# Databricks notebook source
num = 4
for i in range(num):
    for j in range(i):
        print('*', end="")
    print()
for i in range(1, num):
    for j in range(num-i):
        print('*', end="")
    print()
