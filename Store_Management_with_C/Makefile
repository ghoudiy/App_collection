# Directories containing source files
SRC_DIRS := src utils users users/gestionnaire

# Find all .c files in the specified directories
SRCS := $(foreach dir, $(SRC_DIRS), $(wildcard $(dir)/*.c))

# Output binary
OUTPUT := my_program

# Compiler and flags
CC := gcc
CFLAGS := -Wall -std=c11

# Compile the program
$(OUTPUT): $(SRCS)
	$(CC) $(CFLAGS) -o $@ $^ main.c

# Clean up
clean:
	rm -f $(OUTPUT)
