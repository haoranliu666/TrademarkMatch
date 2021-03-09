#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define FILE_OK 0
#define FILE_NOT_EXIST 1
#define FILE_TO_LARGE 2
#define FILE_READ_ERROR 3

//fast compare, return 0 if equal
//https://mgronhol.github.io/fast-strcmp/
int fast_compare(const char *ptr0, const char *ptr1, int len);

int main(void)
{
    /*
    READ TWO FILES
    */
    char *buffer;

    size_t length_0, length_1;
    size_t read_length_0, read_length_1;
    
    FILE * f_0 = fopen("url_dict_1.txt", "rb");
    FILE * f_1 = fopen("url_crsp_random.txt", "rb");
    
    int err;

    if (f_0 && f_1)
    {
        // get file length
        fseek(f_0, 0, SEEK_END);
        length_0 = ftell(f_0);
        fseek(f_0, 0, SEEK_SET);

        fseek(f_1, 0, SEEK_END);
        length_1 = ftell(f_1);
        fseek(f_1, 0, SEEK_SET);

        // 1 GiB; best not to load a whole large file in one string
        if ((length_0 > 1073741824) || (length_0 > 1073741824))
        {
            err = FILE_TO_LARGE;
            printf("**err: %d", err);
            exit(1);
        }

        // assign memory, two file length + two \0
        buffer = (char *)malloc(length_0 + length_1 + 2);

        // check length
        if (length_0 && length_1)
        {
            read_length_0 = fread(buffer, 1, length_0, f_0);
            read_length_1 = fread(buffer + length_0 + 1, 1, length_1, f_1);

            if ((length_0 != read_length_0)||(length_1 != read_length_1))
            {
                free(buffer);
                err = FILE_READ_ERROR;
                printf("**err: %d", err);
                exit(1);
            }
        }

        fclose(f_0);
        fclose(f_1);

        printf("Read file, success\n");
        buffer[length_0] = '\0';
        buffer[length_0 + length_1 + 1] = '\0';
    }
    else
    {
        err = FILE_NOT_EXIST;
        printf("**err: %d", err);
        exit(1);
    }

    char * url_0 = buffer;
    char * url_1 = buffer + length_0 + 1;

    int url_len_0 = length_0;
    int url_len_1 = length_1;

    for(int i = 0; i < length_0; i++)
        if(url_0[i] == '\n')
            url_0[i] = '\0';

    for(int i = 0; i < length_1; i++)
        if(url_1[i] == '\n')
            url_1[i] = '\0';

    /*
    READ TWO FILES OVER
    */



    free(buffer);

    return 0;
}

int fast_compare(const char *ptr0, const char *ptr1, int len)
{
    int fast = len / sizeof(size_t) + 1;
    int offset = (fast - 1) * sizeof(size_t);
    int current_block = 0;

    if (len <= sizeof(size_t))
    {
        fast = 0;
    }

    size_t *lptr0 = (size_t *)ptr0;
    size_t *lptr1 = (size_t *)ptr1;

    while (current_block < fast)
    {
        if ((lptr0[current_block] ^ lptr1[current_block]))
        {
            int pos;
            for (pos = current_block * sizeof(size_t); pos < len; ++pos)
            {
                if ((ptr0[pos] ^ ptr1[pos]) || (ptr0[pos] == 0) || (ptr1[pos] == 0))
                {
                    return (int)((unsigned char)ptr0[pos] - (unsigned char)ptr1[pos]);
                }
            }
        }

        ++current_block;
    }

    while (len > offset)
    {
        if ((ptr0[offset] ^ ptr1[offset]))
        {
            return (int)((unsigned char)ptr0[offset] - (unsigned char)ptr1[offset]);
        }
        ++offset;
    }

    return 0;
}

