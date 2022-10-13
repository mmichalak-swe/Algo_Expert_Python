def maximumQuality(packets, channels):
    # Write your code here
    # packets, channels
    
    packets.sort()
    output = 0
    
    for i in range(channels - 1):
        output += packets.pop()

    if len(packets) % 2 == 0:
        idx = len(packets) // 2
        output += round((packets[idx] + packets[idx - 1]) / 2, 0)
    else:
        output += packets[len(packets) // 2]
    
    return int(output)
