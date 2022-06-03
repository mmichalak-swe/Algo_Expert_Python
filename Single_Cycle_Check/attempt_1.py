def hasSingleCycle(array):
    length = len(array)
    idx = 0

    for i in range(length):
        # handle loop between idx = 0 and idx = something else
        if (0 < i < length - 1) and idx == 0:
            return False

        # array[idx] %= length       # modifies the existing array
        idx = (idx + array[idx]) % length # does not modify existing array

        # if idx > (length - 1):
            # idx -= length
        if idx < 0:
            idx += length

    return (idx == 0)
