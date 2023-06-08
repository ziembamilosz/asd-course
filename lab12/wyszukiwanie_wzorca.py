#!/usr/bin/python
# -*- coding: utf-8 -*-
import time

def naive(S, W):
    nr_of_comparisions = 0
    m = 0
    found_index = []
    while m < len(S) - len(W) + 1:
        found_pattern = True
        for i in range(len(W)):
            nr_of_comparisions += 1
            if S[m + i] != W[i]:
                found_pattern = False
                break
        if found_pattern:
            found_index.append(m)
        m += 1
    return len(found_index), nr_of_comparisions


def hash(word, d=256, q=101):
    hw = 0
    for i in range(len(word)):
        hw = (hw*d + ord(word[i])) % q
    return hw

def rabin_karp(S, W):
    nr_of_comparisions = 0
    hW = hash(W)
    found_patterns = []
    for m in range(len(S) - len(W) + 1):
        hS = hash(S[m : m + len(W)])
        nr_of_comparisions += 1
        if hS == hW:
            if S[m : m + len(W)] == W:
                found_patterns.append(m)
    return len(found_patterns), nr_of_comparisions

def get_h(W, d=256, q=101):
    h = 1
    for i in range(len(W)):
        h = (h * d) % q
    return h

def rabin_karp_rolling_hash(S, W, d=256, q=101):
    nr_of_comparisions = 0
    h = get_h(W)
    hW = hash(W)
    hS = hash(S[0 : len(W)])
    found_patterns = []
    different_patterns = 0
    for m in range(len(S) - len(W) + 1):
        if m > 0:
            hS = ((d * hS - ord(S[m - 1]) * h) + ord(S[m + len(W) - 1])) % q
            if hS < 0:
                hS += q
        nr_of_comparisions += 1
        if hS == hW:
            if S[m : m + len(W)] == W:
                found_patterns.append(m)
            else:
                different_patterns += 1
    return len(found_patterns), nr_of_comparisions, different_patterns

def get_T(W):
    T = [_ for _ in range(len(W) + 1)]
    pos = 1
    cnd = 0
    T[0] = -1
    while pos < len(W):
        if W[pos] == W[cnd]:
            T[pos] = T[cnd]
        else:
            T[pos] = cnd
            while cnd >= 0 and W[pos] != W[cnd]:
                cnd = T[cnd]
        pos += 1
        cnd += 1
    T[pos] = cnd
    return T

def knuth_morris_pratt(S, W):
    T = get_T(W)
    m = 0
    i = 0
    nr_of_comparisions = 0
    positions = []
    while m < len(S):
        nr_of_comparisions += 1
        if W[i] == S[m]:
            m += 1
            i += 1
            if i == len(W):
                positions.append(m - i)
                i = T[i]
        else:
            i = T[i]
            if i < 0:
                m += 1
                i += 1
    return len(positions), nr_of_comparisions, T

with open("lotr.txt", encoding='utf-8') as f:
    text = f.readlines()

S = ' '.join(text).lower()

t_start = time.perf_counter()
index, comp = naive(S, "time.")
t_stop = time.perf_counter()
print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
print(str(index) + ";" + str(comp))

t_start = time.perf_counter()
index, comp = rabin_karp(S, "time.")
t_stop = time.perf_counter()
print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
print(str(index) + ";" + str(comp))

t_start = time.perf_counter()
index, comp, diff = rabin_karp_rolling_hash(S, "time.")
t_stop = time.perf_counter()
print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
print(str(index) + ";" + str(comp) + ";" + str(diff))

t_start = time.perf_counter()
index, comp, T = knuth_morris_pratt(S, "time.")
t_stop = time.perf_counter()
print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
print(str(index) + ";" + str(comp) + ";" + str(T))