#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <stdbool.h>

char* get_file_content(const char* path) {
    int fd = open(path, O_RDONLY, 0644);
    if (fd < 0) {
        return NULL;
    } else {
        const size_t buffer_size = 1024;
        char* content = (char*) malloc(buffer_size * (sizeof (char)));
        size_t content_size = buffer_size;
        size_t total_bytes_read = 0;
        char* next_read_ptr = content;
        bool done = false;
        while (!done) {
            size_t bytes_read = read(fd, next_read_ptr, buffer_size);
            total_bytes_read += bytes_read;
            done = bytes_read < buffer_size;
            if (!done) {
                char* new_content = (char*) malloc((content_size + buffer_size) * (sizeof (char)));
                memcpy(new_content, content, total_bytes_read);
                free(content);
                content = new_content;
                next_read_ptr = content + total_bytes_read;
            }
        }
        close(fd);
        return content;
    }
}

int main(int argc, char **argv) {
    if (argc != 2) {
        return EXIT_FAILURE;
    } else {
        char* file_content = get_file_content(argv[1]);
        if (file_content == NULL) {
            return EXIT_FAILURE;
        } else {
            printf("%s", file_content);
            free(file_content);
            return EXIT_SUCCESS;
        }
    }
}
