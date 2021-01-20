def pascals_triangle_last_line(n):
    if n == 1:
        return [1]
    else:
        line2 = [1]
        line1 = pascals_triangle_last_line(n - 1)

        for i in range(len(line1) - 1):
            line2.append(line1[i] + line1[i + 1])

        line2 += [1]
        return line2


n = int(input("Please enter a number : "))
print(pascals_triangle_last_line(n))