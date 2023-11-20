def count_min_sketch(a, b, w, p, stream):

    # Initialize the CMS counter array
    d_sketch = [[0 for _ in range(w)] for _ in range(len(a))]

    # Process the data stream
    for item in stream:
        # Compute the hash values using the specified hash function
        hash_values = [((a[i] * (item) + b[i]) % p) % w for i in range(len(a))]

        # Update the corresponding counters in the d-sketch
        for i, hash_value in enumerate(hash_values):
            d_sketch[i][hash_value] += 1

    return d_sketch


# if __name__ == '__main__':
#     a = [1, 2]
#     b = [3, 5]
#     w = 3
#     p = 100
#     stream = [10, 11, 10]
#     true_solution = [[0, 2, 1], [1, 2, 0]]

#     result = count_min_sketch(a, b, w, p, stream)

#     print(result)
