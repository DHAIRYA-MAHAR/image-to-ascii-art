for i in range(50):          # adjust height if needed
    for j in range(120):     # adjust width if needed

        if i == 0:
            if j < 48:
                print(" ", end="")
            elif j == 48:
                print("-", end="")
            elif j in [49, 50]:
                print("#", end="")
            elif 51 <= j <= 68:
                print("%", end="")
            elif j == 69:
                print("#", end="")
            elif 70 <= j <= 86:
                print("%", end="")
            elif j == 87:
                print("#", end="")
            elif 88 <= j <= 90:
                print("%", end="")
            elif j == 91:
                print("*", end="")
            elif j == 92:
                print(".", end="")
            else:
                print(" ", end="")
        elif i == 1:
            if j < 59:
                print(" ", end="")
            elif j == 59:
                print(".", end="")
            elif j == 60:
                print("=", end="")
            elif j == 61:
                print("+", end="")
            elif j == 62:
                print("*", end="")
            elif j == 63:
                print("+", end="")
            elif j == 64:
                print("-", end="")
            elif j == 65:
                print("+", end="")
            elif j == 66:
                print("*", end="")
            elif j in [67, 68]:
                print("%", end="")
            elif j == 69:
                print("#", end="")
            elif j in [70, 71]:
                print("%", end="")
            elif j == 72:
                print("#", end="")
            elif j == 73:
                print("*", end="")
            elif j == 74:
                print("=", end="")
            elif j == 75:
                print(":", end="")
            elif j == 76:
                print("-", end="")
            elif j in [77, 78]:
                print("%", end="")
            elif j == 79:
                print("#", end="")
            elif j in [80, 81, 82]:
                print("%", end="")
            elif j == 83:
                print("*", end="")
            elif j == 84:
                print(".", end="")
            else:
                print(" ", end="")
        elif i == 2:
            if j < 54:
                print(" ", end="")
            elif j == 54:
                print("=", end="")
            elif 55 <= j <= 60:
                print("%", end="")
            elif j == 61:
                print("@", end="")
            elif j == 62:
                print("%", end="")
            elif j == 63:
                print("#", end="")
            elif 64 <= j <= 85:
                print("%", end="")
            else:
                print(" ", end="")
        elif i == 3:
            if j < 50:
                print(" ", end="")
            elif j == 50:
                print("+", end="")
            elif j == 51:
                print("#", end="")
            elif 52 <= j <= 53:
                print("%", end="")
            elif j == 54:
                print("#", end="")
            elif 55 <= j <= 57:
                print("%", end="")
            elif j == 58:
                print("#", end="")
            elif 59 <= j <= 61:
                print("%", end="")
            elif j == 62:
                print("#", end="")
            elif 63 <= j <= 87:
                print("%", end="")
            elif j == 88:
                print("+", end="")
            elif j == 89:
                print(":", end="")
            else:
                print(" ", end="")
        elif i == 4:
            if j < 48:
                print(" ", end="")
            elif j == 48:
                print("=", end="")
            elif j in [49, 50]:
                print("#", end="")
            elif j == 51:
                print("%", end="")
            elif j == 52:
                print("#", end="")
            elif 53 <= j <= 89:
                print("%", end="")
            elif j == 90:
                print("#", end="")
            elif j == 91:
                print(":", end="")
            else:
                print(" ", end="")
        elif i == 5:
            if j < 45:
                print(" ", end="")
            elif j == 45:
                print("=", end="")
            elif j == 46:
                print("#", end="")
            elif 47 <= j <= 66:
                print("%", end="")
            elif j == 67:
                print("#", end="")
            elif 68 <= j <= 85:
                print("%", end="")
            elif j in [86, 87]:
                print("#", end="")
            elif j == 88:
                print("%", end="")
            elif j == 89:
                print("#", end="")
            elif j == 90:
                print("%", end="")
            elif j == 91:
                print("*", end="")
            else:
                print(" ", end="")
        elif i == 6:
            if j < 43:
                print(" ", end="")
            elif j == 43:
                print(":", end="")
            elif j == 44:
                print("+", end="")
            elif j == 45:
                print("*", end="")
            elif j == 46:
                print("%", end="")
            elif j == 47:
                print("#", end="")
            elif 48 <= j <= 74:
                print("%", end="")
            elif 75 <= j <= 77:
                print("#", end="")
            elif 78 <= j <= 93:
                print("%", end="")
            elif j == 94:
                print("+", end="")
            else:
                print(" ", end="")
        elif i == 7:
            if j < 42:
                print(" ", end="")
            elif j == 42:
                print("+", end="")
            elif j == 43:
                print(".", end="")
            elif j == 44:
                print(":", end="")
            elif j == 45:
                print("=", end="")
            elif j == 46:
                print("#", end="")
            elif 47 <= j <= 95:
                print("%", end="")
            elif j == 96:
                print("=", end="")
            else:
                print(" ", end="")
        elif i == 8:
            if j < 42:
                print(" ", end="")
            elif j == 42:
                print(".", end="")
            elif j in [43, 44]:
                print(" ", end="")
            elif j == 45:
                print("-", end="")
            elif j == 46:
                print("#", end="")
            elif 47 <= j <= 97:
                print("%", end="")
            elif j == 98:
                print("#", end="")
            elif j == 99:
                print(".", end="")
            else:
                print(" ", end="")
        elif i == 9:
            if j < 43:
                print(" ", end="")
            elif j == 43:
                print(":", end="")
            elif j == 44:
                print("+", end="")
            elif j == 45:
                print("#", end="")
            elif 46 <= j <= 100:
                print("%", end="")
            elif j == 101:
                print("+", end="")
            elif j == 102:
                print(".", end="")
            else:
                print(" ", end="")
        elif i == 10:
            if j < 41:
                print(" ", end="")
            elif j == 41:
                print("-", end="")
            elif j == 42:
                print("#", end="")
            elif j == 43:
                print("%", end="")
            elif j == 44:
                print("#", end="")
            elif 45 <= j <= 103:
                print("%", end="")
            elif j == 104:
                print("*", end="")
            elif j == 105:
                print(".", end="")
            else:
                print(" ", end="")
        elif i == 11:
            if j < 39:
                print(" ", end="")
            elif j == 39:
                print(".", end="")
            elif j == 40:
                print("%", end="")
            elif j == 41:
                print("+", end="")
            elif 42 <= j <= 74:
                print("%", end="")
            elif 75 <= j <= 82:
                print("#", end="")
            elif 83 <= j <= 104:
                print("%", end="")
            elif j == 105:
                print("+", end="")
            else:
                print(" ", end="")
        elif i == 12:
            if j < 38:
                print(" ", end="")
            elif j in [38, 39]:
                print("*", end="")
            elif j == 40:
                print(":", end="")
            elif j in [41, 42]:
                print("#", end="")
            elif 43 <= j <= 73:
                print("%", end="")
            elif j == 74:
                print("#", end="")
            elif j == 75:
                print("*", end="")
            elif 76 <= j <= 88:
                print("+", end="")
            elif j == 89:
                print("*", end="")
            elif j in [90, 91]:
                print("#", end="")
            elif 92 <= j <= 106:
                print("%", end="")
            elif j == 107:
                print("=", end="")
            else:
                print(" ", end="")
        elif i == 13:
            if j < 37:
                print(" ", end="")
            elif j == 37:
                print("*", end="")
            elif j == 38:
                print(":", end="")
            elif j == 39:
                print("-", end="")
            elif 40 <= j <= 41:
                print("%", end="")
            elif j == 42:
                print("#", end="")
            elif 43 <= j <= 58:
                print("%", end="")
            elif j == 59:
                print("#", end="")
            elif 60 <= j <= 66:
                print("%", end="")
            elif j == 67:
                print("#", end="")
            elif 68 <= j <= 72:
                print("%", end="")
            elif j in [73, 74]:
                print("#", end="")
            elif j == 75:
                print("*", end="")
            elif j == 76:
                print("+", end="")
            elif 77 <= j <= 86:
                print("=", end="")
            elif 87 <= j <= 91:
                print("+", end="")
            elif j == 92:
                print("*", end="")
            elif j == 93:
                print("#", end="")
            elif 94 <= j <= 104:
                print("%", end="")
            elif j in [105, 106]:
                print("#", end="")
            elif j == 107:
                print("%", end="")
            elif j == 108:
                print("-", end="")
            else:
                print(" ", end="")
        elif i == 14:
            if j < 36:
                print(" ", end="")
            elif j == 36:
                print("-", end="")
            elif j == 37:
                print(":", end="")
            elif j == 38:
                print(".", end="")
            elif 39 <= j <= 41:
                print("%", end="")
            elif j == 42:
                print("#", end="")
            elif 43 <= j <= 57:
                print("%", end="")
            elif 58 <= j <= 71:
                print("#", end="")
            elif j in [72, 73]:
                print("*", end="")
            elif j in [74, 75]:
                print("+", end="")
            elif j in [76, 77]:
                print("=", end="")
            elif 78 <= j <= 80:
                print("-", end="")
            elif 81 <= j <= 87:
                print("=", end="")
            elif 88 <= j <= 92:
                print("+", end="")
            elif j == 93:
                print("*", end="")
            elif j in [94, 95]:
                print("#", end="")
            elif j == 96:
                print("%", end="")
            elif j == 97:
                print("#", end="")
            elif 98 <= j <= 106:
                print("%", end="")
            elif j == 107:
                print("#", end="")
            elif j == 108:
                print("*", end="")
            elif j == 109:
                print(".", end="")
            else:
                print(" ", end="")
        elif i == 15:
            if j < 37:
                print(" ", end="")
            elif j == 37:
                print(".", end="")
            elif j == 38:
                print("#", end="")
            elif 39 <= j <= 53:
                print("%", end="")
            elif 54 <= j <= 57:
                print("#", end="")
            elif 58 <= j <= 65:
                print("*", end="")
            elif 66 <= j <= 69:
                print("+", end="")
            elif 70 <= j <= 73:
                print("=", end="")
            elif 74 <= j <= 79:
                print("-", end="")
            elif 80 <= j <= 85:
                print("=", end="")
            elif 86 <= j <= 91:
                print("+", end="")
            elif 92 <= j <= 93:
                print("*", end="")
            elif j in [94, 95]:
                print("#", end="")
            elif 96 <= j <= 104:
                print("%", end="")
            elif j == 105:
                print("#", end="")
            elif j == 106:
                print("%", end="")
            elif j == 107:
                print("=", end="")
            else:
                print(" ", end="")
        elif i == 16:
            if j < 37:
                print(" ", end="")
            elif j == 37:
                print(":", end="")
            elif j == 38:
                print("#", end="")
            elif 39 <= j <= 51:
                print("%", end="")
            elif 52 <= j <= 54:
                print("#", end="")
            elif 55 <= j <= 58:
                print("*", end="")
            elif 59 <= j <= 62:
                print("+", end="")
            elif 63 <= j <= 71:
                print("=", end="")
            elif 72 <= j <= 81:
                print("-", end="")
            elif 82 <= j <= 86:
                print("=", end="")
            elif 87 <= j <= 91:
                print("+", end="")
            elif 92 <= j <= 93:
                print("*", end="")
            elif j in [94, 95]:
                print("#", end="")
            elif 96 <= j <= 102:
                print("%", end="")
            elif j == 103:
                print("#", end="")
            elif j == 104:
                print("%", end="")
            elif j == 105:
                print("#", end="")
            elif j == 106:
                print("=", end="")
            else:
                print(" ", end="")
        elif i == 17:
            if j < 38:
                print(" ", end="")
            elif j == 38:
                print("*", end="")
            elif j == 39:
                print("%", end="")
            elif j == 40:
                print("#", end="")
            elif j == 41:
                print("%", end="")
            elif j == 42:
                print("#", end="")
            elif 43 <= j <= 50:
                print("%", end="")
            elif 51 <= j <= 53:
                print("#", end="")
            elif 54 <= j <= 56:
                print("*", end="")
            elif 57 <= j <= 62:
                print("+", end="")
            elif 63 <= j <= 71:
                print("=", end="")
            elif j in [72, 73]:
                print("-", end="")
            elif 74 <= j <= 86:
                print("=", end="")
            elif 87 <= j <= 92:
                print("+", end="")
            elif 93 <= j <= 94:
                print("*", end="")
            elif j in [95, 96]:
                print("#", end="")
            elif 97 <= j <= 105:
                print("%", end="")
            elif j == 106:
                print("#", end="")
            elif j == 107:
                print(".", end="")
            else:
                print(" ", end="")
        elif i == 18:
            if j < 38:
                print(" ", end="")
            elif j == 38:
                print(".", end="")
            elif j == 39:
                print("%", end="")
            elif j == 40:
                print("#", end="")
            elif j == 41:
                print("%", end="")
            elif j == 42:
                print("#", end="")
            elif 43 <= j <= 48:
                print("%", end="")
            elif 49 <= j <= 52:
                print("#", end="")
            elif 53 <= j <= 56:
                print("*", end="")
            elif 57 <= j <= 62:
                print("+", end="")
            elif 63 <= j <= 68:
                print("=", end="")
            elif 69 <= j <= 75:
                print("-", end="")
            elif j == 76:
                print("=", end="")
            elif j in [77, 78]:
                print("-", end="")
            elif 79 <= j <= 85:
                print("=", end="")
            elif 86 <= j <= 91:
                print("+", end="")
            elif 92 <= j <= 93:
                print("*", end="")
            elif j in [94, 95]:
                print("#", end="")
            elif 96 <= j <= 104:
                print("%", end="")
            elif j == 105:
                print("#", end="")
            elif j == 106:
                print("%", end="")
            elif j == 107:
                print("+", end="")
            elif j == 108:
                print(":", end="")
            else:
                print(" ", end="")
        elif i == 19:
            if j < 38:
                print(" ", end="")
            elif j == 38:
                print(".", end="")
            elif j in [39, 40]:
                print("%", end="")
            elif j in [41, 42]:
                print("#", end="")
            elif 43 <= j <= 47:
                print("%", end="")
            elif 48 <= j <= 52:
                print("#", end="")
            elif 53 <= j <= 56:
                print("*", end="")
            elif 57 <= j <= 62:
                print("+", end="")
            elif 63 <= j <= 67:
                print("=", end="")
            elif 68 <= j <= 71:
                print("-", end="")
            elif 72 <= j <= 76:
                print("=", end="")
            elif 77 <= j <= 81:
                print("-", end="")
            elif 82 <= j <= 87:
                print("=", end="")
            elif 88 <= j <= 92:
                print("+", end="")
            elif 93 <= j <= 94:
                print("*", end="")
            elif 95 <= j <= 97:
                print("#", end="")
            elif 98 <= j <= 103:
                print("%", end="")
            elif 104 <= j <= 107:
                print("#", end="")
            elif j == 108:
                print(".", end="")
            
            else:
                print(" ", end="")
        elif i == 20:
            if j < 39:
                print(" ", end="")
            elif j == 39:
                print("=", end="")
            elif j == 40:
                print("%", end="")
            elif 41 <= j <= 43:
                print("#", end="")
            elif 44 <= j <= 47:
                print("%", end="")
            elif 48 <= j <= 52:
                print("#", end="")
            elif 53 <= j <= 55:
                print("*", end="")
            elif 56 <= j <= 60:
                print("+", end="")
            elif j == 61:
                print("=", end="")
            elif j == 62:
                print("+", end="")
            elif 63 <= j <= 65:
                print("=", end="")
            elif 66 <= j <= 71:
                print("-", end="")
            elif 72 <= j <= 73:
                print("=", end="")
            elif 74 <= j <= 83:
                print("-", end="")
            elif 84 <= j <= 88:
                print("=", end="")
            elif 89 <= j <= 93:
                print("+", end="")
            elif 94 <= j <= 95:
                print("*", end="")
            elif 96 <= j <= 97:
                print("#", end="")
            elif 98 <= j <= 103:
                print("%", end="")
            elif 104 <= j <= 105:
                print("#", end="")
            elif j == 106:
                print("*", end="")
            elif j in [107, 108]:
                print(".", end="")
            
            else:
                print(" ", end="")
        elif i == 21:
            if j < 39:
                print(" ", end="")
            elif j == 39:
                print(".", end="")
            elif j == 40:
                print("#", end="")
            elif j == 41:
                print("%", end="")
            elif j in [42, 43]:
                print("#", end="")
            elif 44 <= j <= 47:
                print("%", end="")
            elif 48 <= j <= 51:
                print("#", end="")
            elif 52 <= j <= 55:
                print("*", end="")
            elif 56 <= j <= 62:
                print("+", end="")
            elif 63 <= j <= 66:
                print("=", end="")
            elif 67 <= j <= 71:
                print("-", end="")
            elif 72 <= j <= 73:
                print("=", end="")
            elif 74 <= j <= 79:
                print("-", end="")
            elif 80 <= j <= 88:
                print("=", end="")
            elif 89 <= j <= 93:
                print("+", end="")
            elif j == 94:
                print("*", end="")
            elif j == 95:
                print("#", end="")
            elif 96 <= j <= 100:
                print("%", end="")
            elif j in [101, 102]:
                print("#", end="")
            elif j == 103:
                print("%", end="")
            elif j == 104:
                print("%", end="")
            elif j == 105:
                print("#", end="")
            elif j == 106:
                print("%", end="")
            elif j == 107:
                print(".", end="")
            else:
                print(" ", end="")
        elif i == 22:
            if j < 39:
                print(" ", end="")
            elif j == 39:
                print("-", end="")
            elif j == 40:
                print("*", end="")
            elif 41 <= j <= 42:
                print("%", end="")
            elif j == 43:
                print("#", end="")
            elif 44 <= j <= 46:
                print("%", end="")
            elif 47 <= j <= 56:
                print("#", end="")
            elif j == 57:
                print("%", end="")
            elif 58 <= j <= 61:
                print("#", end="")
            elif 62 <= j <= 63:
                print("*", end="")
            elif 64 <= j <= 65:
                print("+", end="")
            elif 66 <= j <= 68:
                print("=", end="")
            elif 69 <= j <= 71:
                print("-", end="")
            elif 72 <= j <= 77:
                print("=", end="")
            elif 78 <= j <= 81:
                print("+", end="")
            elif 82 <= j <= 85:
                print("*", end="")
            elif 86 <= j <= 87:
                print("+", end="")
            elif j == 88:
                print("+", end="")
            elif j == 89:
                print("=", end="")
            elif 90 <= j <= 93:
                print("+", end="")
            elif j == 94:
                print("*", end="")
            elif j == 95:
                print("#", end="")
            elif 96 <= j <= 100:
                print("%", end="")
            elif j == 101:
                print("%", end="")
            elif j == 102:
                print("#", end="")
            elif j == 103:
                print("%", end="")
            elif j == 104:
                print ("#", end="")
            elif j == 105:
                print("%", end="")
            elif j == 106:
                print("#", end="")
            elif j == 107:
                print(".", end="")
            else:
                print(" ", end="")
        elif i == 23:
            if j < 39:
                print(" ", end="")
            elif j == 39:
                print(":", end="")
            elif j == 40:
                print("*", end="")
            elif j == 41:
                print("%", end="")
            elif j == 42:
                print("#", end="")
            elif j == 43:
                print("%", end="")
            elif j == 44:
                print("#", end="")
            elif 45 <= j <= 46:
                print("%", end="")
            elif 47 <= j <= 51:
                print("#", end="")
            elif 52 <= j <= 64:
                print("%", end="")
            elif j == 65:
                print("#", end="")
            elif j == 66:
                print("*", end="")
            elif j == 67:
                print("+", end="")
            elif 68 <= j <= 70:
                print("=", end="")
            elif 71 <= j <= 72:
                print("-", end="")
            elif 73 <= j <= 74:
                print("=", end="")
            elif j == 75:
                print("+", end="")
            elif j == 76:
                print("*", end="")
            elif j == 77:
                print("#", end="")
            elif 78 <= j <= 82:
                print("%", end="")
            elif 83 <= j <= 89:
                print("#", end="")
            elif j == 90:
                print("*", end="")
            elif 91 <= j <= 94:
                print("+", end="")
            elif j == 95:
                print("*", end="")
            elif 96 <= j <= 101:
                print("%", end="")
            elif j in [102, 103]:
                print("#", end="")
            elif j == 104:
                print("%", end="")
        
            elif j == 105:
                print("#", end="")
            elif j == 106:
                print("#", end="")
            elif j == 107:
                print("=", end="")
            else:
                print(" ", end="")
        elif i == 24:
            if j < 38:
                print(" ", end="")
            elif j == 38:
                print("-", end="")
            elif j == 39:
                print("*", end="")
            elif j in [40, 41]:
                print("#", end="")
            elif 42 <= j <= 46:
                print("%", end="")
            elif j == 47:
                print("#", end="")
            elif j in [48, 49]:
                print("*", end="")
            elif 50 <= j <= 53:
                print("#", end="")
            elif j == 54:
                print("*", end="")
            elif 55 <= j <= 61:
                print("+", end="")
            elif j == 62:
                print("#", end="")
            elif j in [63, 64]:
                print("*", end="")
            elif 65 <= j <= 67:
                print("#", end="")
            elif j == 68:
                print("+", end="")
            elif 69 <= j <= 70:
                print("=", end="")
            elif 71 <= j <= 72:
                print("-", end="")
            elif j == 73:
                print("=", end="")
            elif j == 74:
                print("+", end="")
            elif j in [75, 76]:
                print("*", end="")
            elif j == 77:
                print("#", end="")
            elif j in [78, 79]:
                print("*", end="")
            elif j == 80:
                print("#", end="")
            elif j in [81, 82]:
                print("*", end="")
            elif j == 83:
                print("+", end="")
            elif j == 84:
                print("+", end="")
            elif j == 85:
                print("+", end="")
            elif j == 86:
                print("*", end="")
            elif j == 87:
                print("#", end="")
            elif j == 88:
                print("*", end="")
            elif j in [89, 90]:
                print("#", end="")
            elif j == 91:
                print("+", end="")
            elif j == 92:
                print("=", end="")
            elif j in [93, 94]:
                print("+", end="")
            elif j == 95:
                print("#", end="")
            elif 96 <= j <= 100:
                print("%", end="")
            elif j == 101:
                print("%", end="")
            elif j == 102:
                print("%", end="")
            elif j == 103:
                print("#", end="")
            elif j == 104:
                print("+", end="")
            elif j == 105:
                print("+", end="")
            elif j == 106:
                print(":", end="")
            else:
                print(" ", end="")
        elif i == 25:
            if j < 38:
                print(" ", end="")
            elif j == 38:
                print("*", end="")
            elif 39 <= j <= 42:
                print("#", end="")
            elif 43 <= j <= 45:
                print("%", end="")
            elif j == 46:
                print("#", end="")
            elif 47 <= j <= 49:
                print("*", end="")
            elif j == 50:
                print("#", end="")
            elif 51 <= j <= 54:
                print("*", end="")
            elif 55 <= j <= 57:
                print("#", end="")
            elif 58 <= j <= 59:
                print("%", end="")
            elif j == 60:
                print("*", end="")
            elif j == 61:
                print("+", end="")
            elif 62 <= j <= 63:
                print("#", end="")
            elif j == 64:
                print("*", end="")
            elif 65 <= j <= 66:
                print("#", end="")
            elif j == 67:
                print("*", end="")
            elif j == 68:
                print("+", end="")
            elif j == 69:
                print("=", end="")
            elif 70 <= j <= 72:
                print("-", end="")
            elif j == 73:
                print("=", end="")
            elif j == 74:
                print("+", end="")
            elif 75 <= j <= 76:
                print("*", end="")
            elif j == 77:
                print("#", end="")
            elif j == 78:
                print("*", end="")
            elif j == 79:
                print("#", end="")
            elif 80 <= j <= 81:
                print("%", end="")
            elif j == 82:
                print("#", end="")
            elif 83 <= j <= 84:
                print("%", end="")
            elif j == 85:
                print("#", end="")
            elif j == 86:
                print("*", end="")
            elif 87 <= j <= 89:
                print("+", end="")
            elif j == 90:
                print("*", end="")
            elif j == 91:
                print("+", end="")
            elif j == 92:
                print("=", end="")
            elif j == 93:
                print("+", end="")
            elif j == 94:
                print("+", end="")
            elif j == 95:
                print("*", end="")
            elif 96 <= j <= 100:
                print("%", end="")
            elif 101 <= j <= 103:
                print("#", end="")
            elif j == 104:
                print("=", end="")
            else:
                print(" ", end="")
        elif i == 26:
            if j < 38:
                print(" ", end="")
            elif j == 38:
                print("+", end="")
            elif 39 <= j <= 43:
                print("#", end="")
            elif 44 <= j <= 45:
                print("%", end="")
            elif j == 46:
                print("#", end="")
            elif 47 <= j <= 52:
                print("*", end="")
            elif 53 <= j <= 55:
                print("#", end="")
            elif j == 56:
                print("*", end="")
            elif j == 57:
                print("+", end="")
            elif j == 58:
                print("#", end="")
            elif j == 59:
                print("%", end="")
            elif j == 60:
                print("#", end="")
            elif j == 61:
                print("=", end="")
            elif j == 62:
                print(":", end="")
            elif j == 63:
                print("=", end="")
            elif j == 64:
                print("+", end="")
            elif j in [65, 66]:
                print("*", end="")
            elif j in [67, 68]:
                print("#", end="")
            elif j == 69:
                print("+", end="")
            elif j == 70:
                print("=", end="")
            elif j in [71, 72]:
                print("-", end="")
            elif 73 <= j <= 75:
                print("=", end="")
            elif 76 <= j <= 77:
                print("+", end="")
            elif j == 78:
                print("*", end="")
            elif j == 79:
                print("=", end="")
            elif j == 80:
                print("=", end="")
            elif j == 81:
                print("#", end="")
            elif j == 82:
                print("%", end="")
            elif j == 83:
                print("#", end="")
            elif j == 84:
                print("+", end="")
            elif j == 85:
                print("=", end="")
            elif j == 86:
                print("+", end="")
            elif j in [87, 88]:
                print("*", end="")
            elif j == 89:
                print("+", end="")
            elif 90 <= j <= 93:
                print("=", end="")
            elif j in [94, 95]:
                print("+", end="")
            elif j == 96:
                print("*", end="")
            elif j == 97:
                print("#", end="")
            elif 98 <= j <= 100:
                print("%", end="")
            elif 101 <= j <= 103:
                print("#", end="")
            elif j == 104:
                print("+", end="")
            else:
                print(" ", end="")
        elif i == 27:
            if j < 38:
                print(" ", end="")
            elif j == 38:
                print("-", end="")
            elif 39 <= j <= 45:
                print("#", end="")
            elif 46 <= j <= 50:
                print("*", end="")
            elif j == 51:
                print("+", end="")
            elif 52 <= j <= 54:
                print("*", end="")
            elif 55 <= j <= 57:
                print("+", end="")
            elif j == 58:
                print("=", end="")
            elif j == 59:
                print("+", end="")
            elif j == 60:
                print("+", end="")
            elif 61 <= j <= 65:
                print("=", end="")
            elif j in [66, 67]:
                print("#", end="")
            elif j == 68:
                print("*", end="")
            elif j == 69:
                print("+", end="")
            elif 70 <= j <= 75:
                print("=", end="")
            elif 76 <= j <= 81:
                print("+", end="")
            elif 82 <= j <= 87:
                print("+", end="")
            elif 88 <= j <= 96:
                print("=", end="")
            elif j == 97:
                print("*", end="")
            elif j == 98:
                print("#", end="")
            elif j == 99:
                print("%", end="")
            elif 100 <= j <= 102:
                print("#", end="")
            elif j == 103:
                print("*", end="")
            elif j == 104:
                print("+", end="")
            elif j == 105:
                print("*", end="")
            elif j == 106:
                print(".", end="")
            else:
                print(" ", end="")
        elif i == 28:
            if j < 38:
                print(" ", end="")
            elif j == 38:
                print(".", end="")
            elif j == 39:
                print("*", end="")
            elif 40 <= j <= 42:
                print("#", end="")
            elif 43 <= j <= 45:
                print("%", end="")
            elif j == 46:
                print("*", end="")
            elif 47 <= j <= 48:
                print("+", end="")
            elif 49 <= j <= 52:
                print("*", end="")
            elif 53 <= j <= 57:
                print("+", end="")
            elif 58 <= j <= 64:
                print("=", end="")
            elif j == 65:
                print("+", end="")
            elif j == 66:
                print("*", end="")
            elif j in [67, 68]:
                print("#", end="")
            elif j in [69, 70]:
                print("*", end="")
            elif j == 71:
                print("+", end="")
            elif 72 <= j <= 82:
                print("=", end="")
            elif j == 83:
                print("-", end="")
            elif 84 <= j <= 96:
                print("=", end="")
            elif j == 97:
                print("+", end="")
            elif j in [98, 99]:
                print("#", end="")
            elif 100 <= j <= 101:
                print("*", end="")
            elif j in [102, 103]:
                print("+", end="")
            elif j in [104, 105]:
                print("=", end="")
            elif j == 106:
                print ("*", end="")
            elif j == 107:
                print(".", end="")
            else:
                print(" ", end="")
        elif i == 29:
            if j < 39:
                print(" ", end="")
            elif j == 39:
                print("+", end="")
            elif j == 40:
                print("*", end="")
            elif j == 41:
                print("#", end="")
            elif 42 <= j <= 43:
                print("%", end="")
            elif j == 44:
                print("#", end="")
            elif j == 45:
                print("%", end="")
            elif j in [46, 47]:
                print("+", end="")
            elif 48 <= j <= 50:
                print("*", end="")
            elif 51 <= j <= 53:
                print("+", end="")
            elif 54 <= j <= 62:
                print("=", end="")
            elif j == 63:
                print("+", end="")
            elif 64 <= j <= 68:
                print("*", end="")
            elif j == 69:
                print("+", end="")
            elif 70 <= j <= 82:
                print("=", end="")
            elif 83 <= j <= 88:
                print("-", end="")
            elif 89 <= j <= 95:
                print("=", end="")
            elif j in [96, 98]:
                print("*", end="")
            elif j == 98:
                print("+", end="")
            elif j in [98, 104]:
                print("=", end="")
            elif j in [104, 106]:
                print("+", end="")
            elif j == 105:
                print(".", end="")
            else:
                print(" ", end="")

        elif i == 30:
            if j < 39:
                print(" ", end="")
            elif j == 39:
                print("-", end="")
            elif j == 40:
                print("*", end="")
            elif 41 <= j <= 43:
                print("#", end="")
            elif j == 44:
                print("*", end="")
            elif 45 <= j <= 46:
                print("#", end="")
            elif 47 <= j <= 49:
                print("+", end="")
            elif 50 <= j <= 51:
                print("*", end="")
            elif 52 <= j <= 54:
                print("+", end="")
            elif 55 <= j <= 61:
                print("=", end="")
            elif 62 <= j <= 64:
                print("+", end="")
            elif 65 <= j <= 69:
                print("*", end="")
            elif 70 <= j <= 72:
                print("+", end="")
            elif 73 <= j <= 79:
                print("=", end="")
            elif 80 <= j <= 90:
                print("-", end="")
            elif 91 <= j <= 97:
                print("=", end="")
            elif j == 98:
                print("+", end="")
            elif j in [99, 100]:
                print("=", end="")
            elif j in [101, 102]:
                print("-", end="")
            elif 103 <= j <= 106:
                print("+", end="")
            elif j == 107:
                print("-", end="")
            else:
                print(" ", end="")
        elif i == 31:
            if j < 39:
                print(" ", end="")
            elif j == 39:
                print(".", end="")
            elif 40 <= j <= 42:
                print("*", end="")
            elif 43 <= j <= 45:
                print("#", end="")
            elif j == 46:
                print("*", end="")
            elif 47 <= j <= 49:
                print("+", end="")
            elif j == 50:
                print("*", end="")
            elif 51 <= j <= 55:
                print("+", end="")
            elif 56 <= j <= 62:
                print("=", end="")
            elif 63 <= j <= 64:
                print("+", end="")
            elif 65 <= j <= 69:
                print("*", end="")
            elif 70 <= j <= 72:
                print("+", end="")
            elif 73 <= j <= 79:
                print("=", end="")
            elif 80 <= j <= 89:
                print("-", end="")
            elif 90 <= j <= 96:
                print("=", end="")
            elif 97 <= j <= 98:
                print("+", end="")
            elif j == 99:
                print("-", end="")
            elif j == 100:
                print("=", end="")
            elif j == 101:
                print("+", end="")
            elif 102 <= j <= 105:
                print("=", end="")
            else:
                print(" ", end="")
        elif i == 32:
            if j < 40:
                print(" ", end="")
            elif j == 40:
                print("-", end="")
            elif 41 <= j <= 44:
                print("*", end="")
            elif 45 <= j <= 46:
                print("#", end="")
            elif j == 47:
                print("*", end="")
            elif 48 <= j <= 49:
                print("+", end="")
            elif 50 <= j <= 52:
                print("*", end="")
            elif 53 <= j <= 55:
                print("+", end="")
            elif 56 <= j <= 62:
                print("=", end="")
            elif 63 <= j <= 64:
                print("+", end="")
            elif j == 65:
                print("*", end="")
            elif j == 66:
                print("#", end="")
            elif 67 <= j <= 69:
                print("*", end="")
            elif j == 70:
                print("+", end="")
            elif 71 <= j <= 77:
                print("=", end="")
            elif 78 <= j <= 87:
                print("-", end="")
            elif 88 <= j <= 94:
                print("=", end="")
            elif 95 <= j <= 96:
                print("+", end="")
            elif 97 <= j <= 99:
                print("=", end="")
            elif j == 100:
                print("-", end="")
            elif j == 101:
                print("=", end="")
            elif j == 102:
                print ("+", end="")
            elif j == 103:
                print(":", end="")
            else:
                print(" ", end="")
        elif i == 33:
            if j < 40:
                print(" ", end="")
            elif j == 40:
                print(".", end="")
            elif j == 41:
                print("=", end="")
            elif 42 <= j <= 44:
                print("*", end="")
            elif 45 <= j <= 46:
                print("#", end="")
            elif j == 47:
                print("*", end="")
            elif 48 <= j <= 49:
                print("+", end="")
            elif j == 50:
                print("*", end="")
            elif j == 51:
                print("+", end="")
            elif 52 <= j <= 53:
                print("*", end="")
            elif 54 <= j <= 55:
                print("+", end="")
            elif j == 56:
                print("=", end="")
            elif j == 57:
                print("+", end="")
            elif 58 <= j <= 63:
                print("=", end="")
            elif j == 64:
                print("*", end="")
            elif j == 65:
                print("#", end="")
            elif 66 <= j <= 68:
                print("*", end="")
            elif j == 69:
                print("+", end="")
            elif 70 <= j <= 71:
                print("=", end="")
            elif j == 72:
                print("-", end="")
            elif 73 <= j <= 75:
                print("=", end="")
            elif 76 <= j <= 77:
                print("+", end="")
            elif 78 <= j <= 86:
                print("-", end="")
            elif 87 <= j <= 94:
                print("=", end="")
            elif j == 95:
                print("+", end="")
            elif 96 <= j <= 98:
                print("=", end="")
            elif j == 99:
                print("-", end="")
            elif 100 <= j <= 101:
                print("=", end="")
            elif j == 102:
                print("-", end="")
            else:
                print(" ", end="")
        elif i == 34:
            if j < 42:
                print(" ", end="")
            elif j == 42:
                print(":", end="")
            elif 43 <= j <= 44:
                print("*", end="")
            elif 45 <= j <= 46:
                print("#", end="")
            elif j == 47:
                print("*", end="")
            elif 48 <= j <= 50:
                print("+", end="")
            elif 51 <= j <= 53:
                print("*", end="")
            elif 54 <= j <= 55:
                print("+", end="")
            elif 56 <= j <= 62:
                print("=", end="")
            elif j == 63:
                print("+", end="")
            elif 64 <= j <= 65:
                print("*", end="")
            elif 66 <= j <= 69:
                print("+", end="")
            elif j == 70:
                print("=", end="")
            elif 71 <= j <= 73:
                print("-", end="")
            elif 74 <= j <= 78:
                print("=", end="")
            elif 79 <= j <= 88:
                print("-", end="")
            elif 89 <= j <= 94:
                print("=", end="")
            elif j == 95:
                print("+", end="")
            elif 96 <= j <= 99:
                print("=", end="")
            elif j == 100:
                print("-", end="")
            elif j == 101:
                print(".", end="")
            else:
                print(" ", end="")
        elif i == 35:
            if j < 47:
                print(" ", end="")
            elif j == 47:
                print(".", end="")
            elif j == 48:
                print("=", end="")
            elif 49 <= j <= 50:
                print("+", end="")
            elif j == 51:
                print("*", end="")
            elif 52 <= j <= 56:
                print("+", end="")
            elif 57 <= j <= 61:
                print("=", end="")
            elif j == 62:
                print("+", end="")
            elif j == 63:
                print("*", end="")
            elif 64 <= j <= 68:
                print("#", end="")
            elif j == 69:
                print("*", end="")
            elif 70 <= j <= 73:
                print("+", end="")
            elif 74 <= j <= 75:
                print("*", end="")
            elif j == 76:
                print("+", end="")
            elif 77 <= j <= 85:
                print("-", end="")
            elif 86 <= j <= 95:
                print("=", end="")
            else:
                print(" ", end="")
        elif i == 36:
            if j < 48:
                print(" ", end="")
            elif j == 48:
                print("-", end="")
            elif 49 <= j <= 50:
                print("+", end="")
            elif j == 51:
                print("*", end="")
            elif 52 <= j <= 56:
                print("+", end="")
            elif 57 <= j <= 61:
                print("=", end="")
            elif 62 <= j <= 63:
                print("+", end="")
            elif 64 <= j <= 66:
                print("*", end="")
            elif 67 <= j <= 69:
                print("#", end="")
            elif 70 <= j <= 71:
                print("*", end="")
            elif 72 <= j <= 75:
                print("+", end="")
            elif 76 <= j <= 80:
                print("=", end="")
            elif 81 <= j <= 87:
                print("-", end="")
            elif 88 <= j <= 94:
                print("=", end="")
            elif j == 95:
                print(":", end="")
            else:
                print(" ", end="")
        elif i == 37:
            if j < 48:
                print(" ", end="")
            elif j == 48:
                print(".", end="")
            elif j == 49:
                print("=", end="")
            elif j == 50:
                print("+", end="")
            elif 51 <= j <= 53:
                print("*", end="")
            elif 54 <= j <= 57:
                print("+", end="")
            elif 58 <= j <= 59:
                print("=", end="")
            elif 60 <= j <= 62:
                print("+", end="")
            elif 63 <= j <= 67:
                print("*", end="")
            elif 68 <= j <= 70:
                print("+", end="")
            elif j == 71:
                print("*", end="")
            elif j == 72:
                print("+", end="")
            elif 73 <= j <= 83:
                print("=", end="")
            elif 84 <= j <= 85:
                print("-", end="")
            elif 86 <= j <= 94:
                print("=", end="")
            elif j == 95:
                print(".", end="")
            else:
                print(" ", end="")
        elif i == 38:
            if j < 48:
                print(" ", end="")
            elif j == 48:
                print(".", end="")
            elif j == 49:
                print("=", end="")
            elif 50 <= j <= 51:
                print("+", end="")
            elif 52 <= j <= 53:
                print("*", end="")
            elif 54 <= j <= 59:
                print("+", end="")
            elif 60 <= j <= 65:
                print("*", end="")
            elif 66 <= j <= 68:
                print("+", end="")
            elif 69 <= j <= 70:
                print("=", end="")
            elif j == 71:
                print("+", end="")
            elif j == 72:
                print("=", end="")
            elif j == 73:
                print("-", end="")
            elif 74 <= j <= 81:
                print("=", end="")
            elif j == 82:
                print("+", end="")
            elif 83 <= j <= 84:
                print("=", end="")
            elif j == 85:
                print("-", end="")
            elif 86 <= j <= 93:
                print("=", end="")
            elif j == 94:
                print("-", end="")
            else:
                print(" ", end="")
        elif i == 39:
            if j < 48:
                print(" ", end="")
            elif j == 48:
                print(".", end="")
            elif 49 <= j <= 50:
                print("=", end="")
            elif 51 <= j <= 52:
                print("+", end="")
            elif 53 <= j <= 56:
                print("*", end="")
            elif 57 <= j <= 62:
                print("+", end="")
            elif 63 <= j <= 70:
                print("*", end="")
            elif j == 71:
                print("+", end="")
            elif 72 <= j <= 76:
                print("*", end="")
            elif 77 <= j <= 79:
                print("+", end="")
            elif j == 80:
                print("*", end="")
            elif j == 81:
                print("+", end="")
            elif 82 <= j <= 88:
                print("=", end="")
            elif j == 89:
                print("-", end="")
            elif 90 <= j <= 93:
                print("=", end="")
            elif j == 94:
                print(":", end="")
            else:
                print(" ", end="")
        elif i == 40:
            if j < 48:
                print(" ", end="")
            elif j == 48:
                print(".", end="")
            elif j == 49:
                print("+", end="")
            elif 50 <= j <= 51:
                print("=", end="")
            elif 52 <= j <= 53:
                print("+", end="")
            elif 54 <= j <= 56:
                print("*", end="")
            elif 57 <= j <= 59:
                print("+", end="")
            elif j == 60:
                print("=", end="")
            elif 61 <= j <= 62:
                print("+", end="")
            elif 63 <= j <= 67:
                print("*", end="")
            elif 68 <= j <= 70:
                print("+", end="")
            elif j == 71:
                print("*", end="")
            elif 72 <= j <= 74:
                print("+", end="")
            elif j == 75:
                print("=", end="")
            elif 76 <= j <= 82:
                print("+", end="")
            elif 83 <= j <= 92:
                print("=", end="")
            elif j == 93:
                print("-", end="")
            elif j == 94:
                print(".", end="")
            else:
                print(" ", end="")
        elif i == 41:
            if j < 48:
                print(" ", end="")
            elif j == 48:
                print(".", end="")
            elif j == 49:
                print("+", end="")
            elif 50 <= j <= 51:
                print("*", end="")
            elif j == 52:
                print("+", end="")
            elif j == 53:
                print("=", end="")
            elif 54 <= j <= 55:
                print("*", end="")
            elif j == 56:
                print("+", end="")
            elif 57 <= j <= 58:
                print("*", end="")
            elif 59 <= j <= 74:
                print("+", end="")
            elif 75 <= j <= 94:
                print("=", end="")
            else:
                print(" ", end="")
        elif i == 42:
            if j < 48:
                print(" ", end="")
            elif j == 48:
                print("+", end="")
            elif j == 49:
                print("*", end="")
            elif 50 <= j <= 52:
                print("#", end="")
            elif j == 53:
                print("*", end="")
            elif 54 <= j <= 60:
                print("+", end="")
            elif 61 <= j <= 67:
                print("*", end="")
            elif 68 <= j <= 74:
                print("+", end="")
            elif 75 <= j <= 91:
                print("=", end="")
            elif j == 92:
                print("+", end="")
            
            elif j == 93:
                print("-", end="")
            else:
                print(" ", end="")
        elif i == 43:
            if j < 48:
                print(" ", end="")
            elif j == 48:
                print(".", end="")
            elif j == 49:
                print("+", end="")
            elif 50 <= j <= 51:
                print("*", end="")
            elif 52 <= j <= 55:
                print("#", end="")
            elif 56 <= j <= 63:
                print("*", end="")
            elif 64 <= j <= 69:
                print("+", end="")
            elif 70 <= j <= 89:
                print("=", end="")
            elif j == 90:
                print("+", end="")
            elif 91 <= j <= 93:
                print("=", end="")
            elif j == 94:
                print("-", end="")
            else:
                print(" ", end="")
        elif i == 44:
            if j < 48:
                print(" ", end="")
            elif j == 48:
                print(".", end="")
            elif j == 49:
                print("+", end="")
            elif j == 50:
                print("*", end="")
            elif 51 <= j <= 57:
                print("#", end="")
            elif 58 <= j <= 65:
                print("*", end="")
            elif 66 <= j <= 68:
                print("+", end="")
            elif 69 <= j <= 84:
                print("=", end="")
            elif 85 <= j <= 86:
                print("+", end="")
            elif j == 87:
                print("=", end="")
            elif 88 <= j <= 91:
                print("=", end="")
            elif j == 92:
                print("+", end="")
            elif j == 93:
                print("-", end="")
            else:
                print(" ", end="")
        elif i == 45:
            if j < 48:
                print(" ", end="")
            elif j == 48:
                print(".", end="")
            elif j == 49:
                print("+", end="")
            elif 50 <= j <= 51:
                print("*", end="")
            elif 52 <= j <= 59:
                print("#", end="")
            elif 60 <= j <= 65:
                print("*", end="")
            elif 66 <= j <= 69:
                print("+", end="")
            elif 70 <= j <= 79:
                print("=", end="")
            elif 80 <= j <= 85:
                print("+", end="")
            elif 86 <= j <= 91:
                print("=", end="")
            elif j == 92:
                print("-", end="")
            else:
                print(" ", end="")
        elif i == 46:
            if j < 48:
                print(" ", end="")
            elif j == 48:
                print(".", end="")
            elif j == 49:
                print("+", end="")
            elif 50 <= j <= 51:
                print("=", end="")
            elif 52 <= j <= 53:
                print("+", end="")
            elif 54 <= j <= 56:
                print("*", end="")
            elif 57 <= j <= 59:
                print("+", end="")
            elif j == 60:
                print("=", end="")
            elif 61 <= j <= 62:
                print("+", end="")
            elif 63 <= j <= 67:
                print("*", end="")
            elif 68 <= j <= 70:
                print("+", end="")
            elif j == 71:
                print("*", end="")
            elif 72 <= j <= 74:
                print("+", end="")
            elif j == 75:
                print("=", end="")
            elif 76 <= j <= 82:
                print("+", end="")
            elif 83 <= j <= 93:
                print("=", end="")
            elif j == 94:
                print("-", end="")
            elif j == 95:
                print(".", end="")
            else:
                print(" ", end="")
        elif i == 47:
            if j < 46:
                print(" ", end="")
            elif j == 46:
                print(".", end="")
            elif j == 47:
                print("-", end="")
            elif 48 <= j <= 52:
                print("*", end="")
            elif 53 <= j <= 60:
                print("#", end="")
            elif 61 <= j <= 65:
                print("*", end="")
            elif 66 <= j <= 68:
                print("+", end="")
            elif 69 <= j <= 78:
                print("=", end="")
            elif 79 <= j <= 82:
                print("+", end="")
            elif 83 <= j <= 92:
                print("=", end="")
            elif j == 93:
                print(":", end="")
            elif j == 94:
                print(":", end="")
            elif j == 95:
                print(".", end="")
            elif j == 96:
                print(".", end="")
            elif j == 97:
                print(".", end="")
            else:
                print(" ", end="")
        elif i == 48:
            if j < 44:
                print(" ", end="")
            elif j == 44:
                print(".", end="")
            elif j == 45:
                print(":", end="")
            elif j == 46:
                print("=", end="")
            elif 47 <= j <= 54:
                print("*", end="")
            elif 55 <= j <= 63:
                print("#", end="")
            elif 64 <= j <= 67:
                print("*", end="")
            elif 68 <= j <= 78:
                print("+", end="")
            elif 79 <= j <= 81:
                print("*", end="")
            elif j == 82:
                print("+", end="")
            elif 83 <= j <= 92:
                print("=", end="")
            elif 93 <= j <= 94:
                print("+", end="")
            elif j == 95:
                print("=", end="")
            elif 96 <= j <= 97:
                print("-", end="")
            elif 98 <= j <= 99:
                print(":", end="")
            elif 100 <= j <= 101:
                print(".", end="")
            else:
                print(" ", end="")
        elif i == 49:
            if j < 42:
                print(" ", end="")
            elif j == 42:
                print(".", end="")
            elif j == 43:
                print(":", end="")
            elif 44 <= j <= 45:
                print("-", end="")
            elif j == 46:
                print("+", end="")
            elif j == 47:
                print("#", end="")
            elif 48 <= j <= 56:
                print("*", end="")
            elif 57 <= j <= 68:
                print("#", end="")
            elif 69 <= j <= 78:
                print("*", end="")
            elif 79 <= j <= 80:
                print("+", end="")
            elif 81 <= j <= 83:
                print("=", end="")
            elif j == 84:
                print("-", end="")
            elif 85 <= j <= 92:
                print("=", end="")
            elif j == 93:
                print("+", end="")
            elif 94 <= j <= 96:
                print("*", end="")
            elif j == 97:
                print("+", end="")
            elif j == 98:
                print("=", end="")
            elif j == 99:
                print("-", end="")
            elif 100 <= j <= 101:
                print(":", end="")
            elif j == 102:
                print(".", end="")
            else:
                print(" ", end="")
        elif i == 50:
            if j < 41:
                print(" ", end="")
            elif j == 41:
                print(".", end="")
            elif j == 42:
                print(":", end="")
            elif j == 43:
                print("-", end="")
            elif j == 44:
                print(":", end="")
            elif j == 45:
                print("=", end="")
            elif j == 46:
                print("*", end="")
            elif j == 47:
                print("#", end="")
            elif 48 <= j <= 57:
                print("*", end="")
            elif 58 <= j <= 67:
                print("#", end="")
            elif 68 <= j <= 74:
                print("*", end="")
            elif 75 <= j <= 78:
                print("+", end="")
            elif 79 <= j <= 82:
                print("=", end="")
            elif 83 <= j <= 84:
                print("-", end="")
            elif 85 <= j <= 91:
                print("=", end="")
            elif 92 <= j <= 94:
                print("+", end="")
            elif 95 <= j <= 96:
                print("*", end="")
            elif j == 97:
                print("#", end="")
            elif j == 98:
                print("*", end="")
            elif 99 <= j <= 101:
                print("=", end="")
            elif 102 <= j <= 104:
                print(":", end="")
            elif 105 <= j <= 106:
                print(".", end="")
            else:
                print(" ", end="")
        elif i == 51:
            if j < 41:
                print(" ", end="")
            elif j == 41:
                print(":", end="")
            elif j == 42:
                print("-", end="")
            elif j == 43:
                print(":", end="")
            elif j == 44:
                print(":", end="")
            elif j == 45:
                print("+", end="")
            elif j == 46:
                print("%", end="")
            elif j == 47:
                print("#", end="")
            elif 48 <= j <= 69:
                print("*", end="")
            elif 70 <= j <= 73:
                print("+", end="")
            elif 74 <= j <= 93:
                print("=", end="")
            elif 94 <= j <= 97:
                print("+", end="")
            elif j == 98:
                print("*", end="")
            elif j == 99:
                print("#", end="")
            elif j == 100:
                print("%", end="")
            elif j == 101:
                print("#", end="")
            elif j == 102:
                print("=", end="")
            elif 103 <= j <= 106:
                print(":", end="")
            elif 107 <= j <= 108:
                print(".", end="")
            else:
                print(" ", end="")
        elif i == 52:
            if j < 40:
                print(" ", end="")
            elif j == 40:
                print(".", end="")
            elif 41 <= j <= 42:
                print("-", end="")
            elif j == 43:
                print(":", end="")
            elif j == 44:
                print(":", end="")
            elif j == 45:
                print("*", end="")
            elif j == 46:
                print("#", end="")
            elif j == 47:
                print("*", end="")
            elif j == 48:
                print("#", end="")
            elif 49 <= j <= 56:
                print("*", end="")
            elif 57 <= j <= 58:
                print("+", end="")
            elif 59 <= j <= 65:
                print("*", end="")
            elif 66 <= j <= 71:
                print("+", end="")
            elif 72 <= j <= 82:
                print("=", end="")
            elif 83 <= j <= 84:
                print("-", end="")
            elif 85 <= j <= 91:
                print("=", end="")
            elif 92 <= j <= 97:
                print("+", end="")
            elif 98 <= j <= 99:
                print("*", end="")
            elif j == 100:
                print("%", end="")
            elif j == 101:
                print("#", end="")
            elif j == 102:
                print("-", end="")
            elif 103 <= j <= 106:
                print(":", end="")
            elif 107 <= j <= 108:
                print(".", end="")
            else:
                print(" ", end="")
        elif i == 53:
            if j < 38:
                print(" ", end="")
            elif j == 38:
                print(".", end="")
            elif j == 39:
                print(":", end="")
            elif 40 <= j <= 42:
                print("-", end="")
            elif j == 43:
                print(":", end="")
            elif j == 44:
                print(":", end="")
            elif j == 45:
                print("=", end="")
            elif 46 <= j <= 47:
                print("#", end="")
            elif 48 <= j <= 52:
                print("*", end="")
            elif 53 <= j <= 60:
                print("+", end="")
            elif 61 <= j <= 63:
                print("*", end="")
            elif 64 <= j <= 67:
                print("+", end="")
            elif 68 <= j <= 79:
                print("=", end="")
            elif 80 <= j <= 84:
                print("-", end="")
            elif 85 <= j <= 90:
                print("=", end="")
            elif 91 <= j <= 92:
                print("+", end="")
            elif 93 <= j <= 95:
                print("=", end="")
            elif j == 96:
                print("+", end="")
            elif j == 97:
                print("*", end="")
            elif j == 98:
                print("#", end="")
            elif j == 99:
                print("%", end="")
            elif j == 100:
                print("-", end="")
            elif 101 <= j <= 106:
                print(":", end="")
            else:
                print(" ", end="")
        elif i == 54:
            if j < 36:
                print(" ", end="")
            elif j == 36:
                print(".", end="")
            elif 37 <= j <= 42:
                print("-", end="")
            elif j == 43:
                print(":", end="")
            elif j == 44:
                print(":", end="")
            elif j == 45:
                print(".", end="")
            elif j == 46:
                print("+", end="")
            elif j == 47:
                print("#", end="")
            elif 48 <= j <= 49:
                print("*", end="")
            elif 50 <= j <= 66:
                print("+", end="")
            elif 67 <= j <= 74:
                print("=", end="")
            elif 75 <= j <= 84:
                print("-", end="")
            elif 85 <= j <= 92:
                print("=", end="")
            elif j == 93:
                print("+", end="")
            elif 94 <= j <= 97:
                print("=", end="")
            elif j == 98:
                print("+", end="")
            elif 99 <= j <= 100:
                print("#", end="")
            elif 101 <= j <= 108:
                print(":", end="")
            elif 109 <= j <= 110:
                print(".", end="")
            else:
                print(" ", end="")
        elif i == 55:
            if j < 34:
                print(" ", end="")
            elif 34 <= j <= 35:
                print(":", end="")
            elif 36 <= j <= 42:
                print("-", end="")
            elif 43 <= j <= 44:
                print(":", end="")
            elif 45 <= j <= 46:
                print(":", end="")
            elif j == 47:
                print(".", end="")
            elif 48 <= j <= 49:
                print("*", end="")
            elif 50 <= j <= 60:
                print("+", end="")
            elif 61 <= j <= 62:
                print("=", end="")
            elif 63 <= j <= 67:
                print("+", end="")
            elif 68 <= j <= 72:
                print("=", end="")
            elif 73 <= j <= 86:
                print("-", end="")
            elif 87 <= j <= 93:
                print("=", end="")
            elif j == 94:
                print("+", end="")
            elif 95 <= j <= 97:
                print("=", end="")
            elif j == 98:
                print("+", end="")
            elif j == 99:
                print("*", end="")
            elif j == 100:
                print("#", end="")
            elif j == 101:
                print("-", end="")
            elif 102 <= j <= 112:
                print(":", end="")
            elif 113 <= j <= 115:
                print(".", end="")
            else:
                print(" ", end="")
        elif i == 56:
            if j < 29:
                print(" ", end="")
            elif 29 <= j <= 30:
                print(".", end="")
            elif 31 <= j <= 32:
                print(":", end="")
            elif 33 <= j <= 34:
                print("-", end="")
            elif j == 35:
                print("+", end="")
            elif 36 <= j <= 37:
                print("-", end="")
            elif j == 38:
                print("=", end="")
            elif 39 <= j <= 43:
                print("-", end="")
            elif 44 <= j <= 48:
                print(":", end="")
            elif 49 <= j <= 58:
                print("+", end="")
            elif 59 <= j <= 64:
                print("=", end="")
            elif 65 <= j <= 67:
                print("+", end="")
            elif 68 <= j <= 70:
                print("=", end="")
            elif 71 <= j <= 80:
                print("-", end="")
            elif 81 <= j <= 83:
                print("=", end="")
            elif 84 <= j <= 86:
                print("-", end="")
            elif 87 <= j <= 96:
                print("=", end="")
            elif 97 <= j <= 98:
                print("+", end="")
            elif j == 99:
                print("*", end="")
            elif j == 100:
                print("+", end="")
            elif j == 101:
                print(":", end="")
            elif 102 <= j <= 113:
                print(":", end="")
            elif j == 114:
                print("+", end="")
            elif 115 <= j <= 117:
                print(".", end="")
            else:
                print(" ", end="")
        elif i == 57:
            if j < 24:
                print(" ", end="")
            elif 24 <= j <= 26:
                print(".", end="")
            elif 27 <= j <= 33:
                print(":", end="")
            elif j == 34:
                print("-", end="")
            elif j == 35:
                print("+", end="")
            elif 36 <= j <= 39:
                print("-", end="")
            elif 40 <= j <= 41:
                print("=", end="")
            elif 42 <= j <= 44:
                print("-", end="")
            elif 45 <= j <= 49:
                print(":", end="")
            elif 50 <= j <= 52:
                print("+", end="")
            elif j == 53:
                print("=", end="")
            elif 54 <= j <= 57:
                print("+", end="")
            elif 58 <= j <= 81:
                print("=", end="")
            elif j == 82:
                print("-", end="")
            elif 83 <= j <= 95:
                print("=", end="")
            elif 96 <= j <= 97:
                print("+", end="")
            elif 98 <= j <= 99:
                print("*", end="")
            elif j == 100:
                print(":", end="")
            elif 101 <= j <= 113:
                print(":", end="")
            elif j == 114:
                print("-", end="")
            elif j == 115:
                print("+", end="")
            elif 116 <= j <= 119:
                print(":", end="")
            elif 120 <= j <= 122:
                print(".", end="")
            else:
                print(" ", end="")
        elif i == 58:
            if j < 20:
                print(" ", end="")
            elif 20 <= j <= 22:
                print(".", end="")
            elif 23 <= j <= 32:
                print(":", end="")
            elif j == 33:
                print(".", end="")
            elif j == 34:
                print("=", end="")
            elif j == 35:
                print("+", end="")
            elif 36 <= j <= 39:
                print("-", end="")
            elif 40 <= j <= 41:
                print("=", end="")
            elif 42 <= j <= 45:
                print("-", end="")
            elif 46 <= j <= 48:
                print(":", end="")
            elif j == 49:
                print(".", end="")
            elif 50 <= j <= 63:
                print("-", end="")
            elif 64 <= j <= 78:
                print("=", end="")
            elif j == 79:
                print("+", end="")
            elif j == 80:
                print("*", end="")
            elif j == 81:
                print("*", end="")
            elif j == 82:
                print("-", end="")
            elif 83 <= j <= 98:
                print(":", end="")
            elif j == 99:
                print("*", end="")
            elif 100 <= j <= 108:
                print(":", end="")
            elif 109 <= j <= 120:
                print(".", end="")
        elif i == 59:
            if j < 16:
                print(" ", end="")
            elif 16 <= j <= 17:
                print(".", end="")
            elif 18 <= j <= 22:
                print(":", end="")
            elif 23 <= j <= 31:
                print(":", end="")
            elif j == 32:
                print(".", end="")
            elif j == 33:
                print("-", end="")
            elif j == 34:
                print("+", end="")
            elif 35 <= j <= 39:
                print("-", end="")
            elif j == 40:
                print("=", end="")
            elif 41 <= j <= 44:
                print("-", end="")
            elif 45 <= j <= 50:
                print(":", end="")
            elif 51 <= j <= 53:
                print("-", end="")
            elif 54 <= j <= 92:
                print("=", end="")
            elif j == 93:
                print("-", end="")
            elif j == 94:
                print("=", end="")
            elif j == 95:
                print("-", end="")
            elif j == 96:
                print("=", end="")
            elif 97 <= j <= 99:
                print("=", end="")
            elif j == 100:
                print("+", end="")
            elif j == 101:
                print("+", end="")
            elif j == 102:
                print("#", end="")
            elif j == 103:
                print("=", end="")
            elif 104 <= j <= 119:
                print(":", end="")
            elif j == 120:
                print(".", end="")
            elif j == 121:
                print("+", end="")
            elif j == 122:
                print("-", end="")
            elif 123 <= j <= 134:
                print(":", end="")
            elif 135 <= j <= 137:
                print(".", end="")
        elif i == 60:
            if j < 12:
                print(" ", end="")
            elif 12 <= j <= 14:
                print(".", end="")
            elif 15 <= j <= 30:
                print(":", end="")
            elif j == 31:
                print(".", end="")
            elif j == 32:
                print("-", end="")
            elif j == 33:
                print("*", end="")
            elif j == 34:
                print("-", end="")
            elif j == 35:
                print(":", end="")
            elif 36 <= j <= 38:
                print("-", end="")
            elif 39 <= j <= 40:
                print("=", end="")
            elif 41 <= j <= 45:
                print("-", end="")
            elif 46 <= j <= 50:
                print(":", end="")
            elif 51 <= j <= 52:
                print("-", end="")
            elif 53 <= j <= 55:
                print("=", end="")
            elif j == 56:
                print("+", end="")
            elif 57 <= j <= 61:
                print("=", end="")
            elif j == 62:
                print("-", end="")
            elif 63 <= j <= 74:
                print("=", end="")
            elif j == 75:
                print("+", end="")
            elif j == 76:
                print("+", end="")
            elif 77 <= j <= 84:
                print("=", end="")
            elif 85 <= j <= 90:
                print("-", end="")
            elif 91 <= j <= 92:
                print("=", end="")
            elif j == 93:
                print("+", end="")
            elif j == 94:
                print("*", end="")
            elif j == 95:
                print("*", end="")
            elif j == 96:
                print(":", end="")
            elif j == 97:
                print(":", end="")
            elif 98 <= j <= 114:
                print(".", end="")
            elif j == 115:
                print("=", end="")
            elif j == 116:
                print("+", end="")
            elif 117 <= j <= 133:
                print(":", end="")
            elif 134 <= j <= 136:
                print(".", end="")

    print()
