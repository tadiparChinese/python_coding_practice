# swap the elements

left = 'knife'
right = 'fork'

print(f'Before: {left}, {right}')

left, right = right, left

print(f'After: {left}, {right}')