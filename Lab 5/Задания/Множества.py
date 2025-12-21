#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    u = set("abcdefghijklmnopqrstuvwxyz")  # CORREÇÃO: estava "uvnxyz", correto é "uvwxyz"
    # Создание множеств
    a = {"a", "h", "m", "o", "r"}
    b = {"j", "k", "o", "u", "y"}
    c = {"g", "h", "j"}
    d = {"g", "j", "q"}

    print("Исходные множества:")
    print(f"a = {sorted(a)}")
    print(f"b = {sorted(b)}")
    print(f"c = {sorted(c)}")
    print(f"d = {sorted(d)}")
    print()

    # Вычисление X = (A ∩ C) ∪ (D ∩ B)
    print("1. Вычисление X = (A ∩ C) ∪ (D ∩ B)")

    A_intersection_C = a.intersection(c)
    print(f"   A ∩ C = {sorted(A_intersection_C)}")

    D_intersection_B = d.intersection(b)
    print(f"   D ∩ B = {sorted(D_intersection_B)}")

    x = A_intersection_C.union(D_intersection_B)
    print(f"   X = (A ∩ C) ∪ (D ∩ B) = {sorted(x)}")

    # Проверка вручную
    print("\n   Проверка вручную:")
    print("   A ∩ C = {'a', 'h', 'm', 'o', 'r'} ∩ {'g', 'h', 'j'} = {'h'}")
    print("   D ∩ B = {'g', 'j', 'q'} ∩ {'j', 'k', 'o', 'u', 'y'} = {'j'}")
    print("   X = {'h'} ∪ {'j'} = {'h', 'j'}")

    # Вычисление Y = (A ∩ B) ∪ (D/C)
    print("\n2. Вычисление Y = (A ∩ B) ∪ (D/C)")
    print("   (где D/C означает D - C)")

    A_intersection_B = a.intersection(b)
    print(f"   A ∩ B = {sorted(A_intersection_B)}")

    D_difference_C = d.difference(c)
    print(f"   D/C = D - C = {sorted(D_difference_C)}")

    y = A_intersection_B.union(D_difference_C)
    print(f"   Y = (A ∩ B) ∪ (D/C) = {sorted(y)}")

    # Проверка вручную
    print("\n   Проверка вручную:")
    print("   A ∩ B = {'a', 'h', 'm', 'o', 'r'} ∩ {'j', 'k', 'o', 'u', 'y'} = {'o'}")
    print("   D - C = {'g', 'j', 'q'} - {'g', 'h', 'j'} = {'q'}")
    print("   Y = {'o'} ∪ {'q'} = {'o', 'q'}")

    print("\n3. Итоговые результаты:")
    print(f"   x = {sorted(x)}")
    print(f"   y = {sorted(y)}")