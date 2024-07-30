"""
Buffering in Python is a technique used to optimize input and output (I/O) operations by temporarily 
storing data in a buffer (a block of memory) before it is written to or read from a file or other I/O 
device. This can significantly improve performance by reducing the number of I/O operations, which are 
typically slower than memory operations.

"""

## Note:
######## flush use  #########

"""
How Flush works:
When you set flush=True, it forces the buffer to be flushed immediately after the print() call, 
ensuring that all the data is written out right away. This is particularly useful in scenarios where 
you need real-time feedback, such as in logging, debugging, or interactive prompts.

The flush argument in the print() function is used to control the buffering behavior of the output stream.
By default, output to the console or a file is buffered, meaning that the data is collected in a buffer 
and written out in larger chunks for efficiency. This can sometimes cause delays in seeing the output 
immediately
"""
import time

# Without flush
# Default Behavior: Buffered output, which may delay the display.
# print("Processing...", end=" ")
# time.sleep(2)
# print("Done", end=" ")
# time.sleep(2)
# print("Done")

# With flush
# With flush=True: Immediate output, useful for real-time feedback.
# print("Processing...", end=" ", flush=True)
# time.sleep(2)
# print("Done", end=" ", flush=True)
# time.sleep(2)
# print("Done")


# """
# Practical Use Case
# A common use case for flush=True is when you want to prompt the user for input and ensure the prompt 
# is displayed immediately:
    
# """

# # This ensures that the prompt is visible to the user before the program waits for their input.
# print("Do you want to continue (Y/n): ", end="", flush=True)
# response = input()


# for i in range(5,0,-1):
#     print(i, end=" >> ", flush=True)
#     time.sleep(1)
# print('over')


for i in range(5,0,-1):
    print(i, end=" >> ", flush = False)
    time.sleep(1)
print('over')