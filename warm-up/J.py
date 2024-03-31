from dataclasses import dataclass
import collections


def read_file():
    with open("input.txt", "r", encoding="utf-8") as file:
        return file.readlines()


@dataclass
class Image:
    layout: str
    height: int
    width: int


def get_image_info(image: str):
    params = image.split()
    props = {}
    for param in params:
        if "=" in param:
            param, value = param.split("=")
            props[param] = value
    return Image(
        layout=props["layout"], height=props["height"], width=props["width"]
    )


def process_line(line):
    line = line.strip()
    elements = []
    i = 0
    while i < len(line):
        if line[i] != "(":
            tmp_index = i
            while tmp_index < len(line) and line[tmp_index] != " ":
                tmp_index += 1
            elements.append(line[i:tmp_index])
            i = tmp_index
        else:
            tmp_index = i
            while line[tmp_index] != ")":
                tmp_index += 1
            elements.append(get_image_info(line[i:tmp_index]))
            i = tmp_index
        i += 1
    return elements


def solution():
    lines = read_file()
    answer = []
    w, h, c = lines[0].strip().split()
    w, h, c = map(int, [w, h, c])
    curr_line_index = 0
    next_line_constraints = []
    strings = [([(0, w)], 0, w)]
    elems = []
    lines = [line.strip() for line in lines]
    for line in lines[1:]:
        if line:
            for elem in process_line(line):
                elems.append(elem)
        else:
            elems.append("")
    for elem in elems:
        element_placed = False
        while not element_placed:
            curr_string = strings[curr_line_index]
            last_line_index = len(strings) - 1
            if elem is str:
                elem_len = len(elem) * c
                while curr_line_index <= last_line_index:
                    if elem_len > curr_line_index[2]:
                        curr_line_index += 1
                    else:
                        
                strings.append(([0, w], 0, w))


if __name__ == "__main__":
    solution()
