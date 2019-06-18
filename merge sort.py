def merge(left, right):
  """Merge sort merging function."""

  left_index, right_index = 0, 0
  result = []
  while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
             result.append(left[left_index])
             left_index += 1
             print("left_indix",left_index)
        else:
             result.append(right[right_index])
             right_index += 1
             print("Right_indix",right_index)

  result += left[left_index:]
  print("left",result)
  result += right[right_index:]
  print("right",result)
  return result


def merge_sort(array):
  """Merge sort algorithm implementation."""

  if len(array) <= 1:
        return array

  # divide array in half and merge sort recursively
  half = len(array) // 2
  left = merge_sort(array[:half])
  right = merge_sort(array[half:])


  return merge(left, right)
array = [4, 2, 3, 8, 8, 43, 6,1, 0]
ar = merge_sort(array)
print (" ".join(str(x) for x in ar))

