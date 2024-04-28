n = int(input())
dns = []

for i in range(n):
    dns.append(int(input()))
new_dns = sorted(dns, reverse=True)

count = 1
current_position = new_dns[0]
for dn in new_dns:
    if dn < current_position:
        count+=1
        current_position = dn

print(count)