

# Example
gen_a = 65
gen_b = 8921

# My
gen_a = 679
gen_b = 771

matches = 0
for x in range(40000000):
#    print(x, gen_a, gen_b)
    gen_a = (gen_a * 16807) % 2147483647
    gen_b = (gen_b * 48271) % 2147483647
    if (gen_a & 0xffff) == (gen_b & 0xffff):
#        print('Matched')
        matches += 1
print('Matches:', matches)
