from dataclasses import dataclass


@dataclass
class File:
    id: int
    name: str
    categories: list[str]
    parent: int
    size: int


"""
Task 1
"""

NO_PARENT = -1


def leafFiles(files: list[File]) -> list[str]:
    # Explanation:
    # Create a set of parent ids, that we can use to filter out the 'files' input

    # Time Complexity: O(2 * n) = O(n)
    # Space Complexity: O(n)

    is_parent = set()
    result = []

    for file in files:
        if file.parent != NO_PARENT:
            is_parent.add(file.parent)

    for file in files:
        if file.id not in is_parent:
            result.append(file.name)

    return result


"""
Task 2
"""


def kLargestCategories(files: list[File], k: int) -> list[str]:
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)

    category_map = {}
    for file in files:
        for category in file.categories:
            if category in category_map:
                category_map[category] += 1
            else:
                category_map[category] = 1

    # turn the hashmap into an array
    category_list = [(key, value) for key, value in category_map.items()]

    # sort it by the frequency of a category occuring
    category_list = sorted(category_list, key=lambda x: (-x[1], x[0]))

    # transform the tuple with frequency information into just an array with strings
    result = list(map(lambda x: x[0], category_list))

    # finally, truncate the array using k
    result = result[0 : min(k, len(files))]

    return result


"""
Task 3
"""


def largestFileSize(files: list[File]) -> int:
    return 0


if __name__ == "__main__":
    testFiles = [
        File(1, "Document.txt", ["Documents"], 3, 1024),
        File(2, "Image.jpg", ["Media", "Photos"], 34, 2048),
        File(3, "Folder", ["Folder"], -1, 0),
        File(5, "Spreadsheet.xlsx", ["Documents", "Excel"], 3, 4096),
        File(8, "Backup.zip", ["Backup"], 233, 8192),
        File(13, "Presentation.pptx", ["Documents", "Presentation"], 3, 3072),
        File(21, "Video.mp4", ["Media", "Videos"], 34, 6144),
        File(34, "Folder2", ["Folder"], 3, 0),
        File(55, "Code.py", ["Programming"], -1, 1536),
        File(89, "Audio.mp3", ["Media", "Audio"], 34, 2560),
        File(144, "Spreadsheet2.xlsx", ["Documents", "Excel"], 3, 2048),
        File(233, "Folder3", ["Folder"], -1, 4096),
        File(234, "Folder4", ["Folder"], -1, 4096),  # Add empty folder
    ]

    assert sorted(leafFiles(testFiles)) == [
        "Audio.mp3",
        "Backup.zip",
        "Code.py",
        "Document.txt",
        "Folder4",  # NOTE: Add test case for empty folder
        "Image.jpg",
        "Presentation.pptx",
        "Spreadsheet.xlsx",
        "Spreadsheet2.xlsx",
        "Video.mp4",
    ]

    assert kLargestCategories(testFiles, 3) == ["Documents", "Folder", "Media"]

    assert largestFileSize(testFiles) == 20992
