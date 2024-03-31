def read_segments_from_file(file_path):
    segments1 = []
    segments2 = []
    with open(file_path, 'r') as file:
        n = int(file.readline().strip())
        for _ in range(n):
            x1, y1, x2, y2 = map(int, file.readline().split())
            segments1.append(((x1, y1), (x2, y2)))
        for _ in range(n):
            x1, y1, x2, y2 = map(int, file.readline().split())
            segments2.append(((x1, y1), (x2, y2))) 
    return (segments1, segments2)


def process_segments(segments):
    vectors_and_shifts = set()
    for (x1, y1), (x2, y2) in segments:
        vector = (x2 - x1, y2 - y1)
        shift = (x2, y2)
        vectors_and_shifts.add((vector, shift))
        reverse_vector = (x1 - x2, y1 - y2)
        reverse_shift = (x1, y1)
        vectors_and_shifts.add((reverse_vector, reverse_shift))
    return vectors_and_shifts


def find_max_overlap(segments1, segments2):
    vectors_and_shifts1 = process_segments(segments1)
    vectors_and_shifts2 = process_segments(segments2)

    shift_counts = {}
    for vector_shift1 in vectors_and_shifts1:
        for vector_shift2 in vectors_and_shifts2:
            if vector_shift1[0] == vector_shift2[0]:
                shift_diff = (vector_shift2[1][0] - vector_shift1[1][0], vector_shift2[1][1] - vector_shift1[1][1])
                if shift_diff in shift_counts:
                    shift_counts[shift_diff] += 1
                else:
                    shift_counts[shift_diff] = 1

    max_overlap = max(shift_counts.values(), default=0) // 2
    return max_overlap


def main():
    segments1, segments2= read_segments_from_file('input.txt')
    n = len(segments1)
    max_overlap = find_max_overlap(segments1, segments2)
    print(n - max_overlap)

if __name__ == "__main__":
    main()
