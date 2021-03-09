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

int main(int argc, char *argv[])
{
    
    char file_name_0[30] = "url_dict_";
    strcat (file_name_0, argv[1]);
    strcat (file_name_0, ".txt");

    char file_name_1[30] = "url_crsp_random.txt";

    char file_name_out[30] = "c_result_setlen_";
    strcat (file_name_out, argv[2]);
    strcat (file_name_out, "_");
    strcat (file_name_out, argv[1]);
    strcat (file_name_out, ".txt");

    int set_len = atoi(argv[2]);

    /***********************************************************************
    READ TWO FILES
    ************************************************************************/
    char *buffer;
    int err;

    size_t length_0, length_1;
    size_t read_length_0, read_length_1;
    
    FILE * f_0 = fopen(file_name_0, "rb");
    FILE * f_1 = fopen(file_name_1, "rb");
    
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

    // file start pointer
    char * url_0 = buffer;
    char * url_1 = buffer + length_0 + 1;

    // file length
    int url_len_0 = length_0;
    int url_len_1 = length_1;

    for(int i = 0; i < length_0; i++)
        if(url_0[i] == '\n')
            url_0[i] = '\0';

    for(int i = 0; i < length_1; i++)
        if(url_1[i] == '\n')
            url_1[i] = '\0';

    /***********************************************************************
    READ TWO FILES OVER, START MAKING THE MATRICES
    ************************************************************************/

    int url_count_0 = 0;
    int company_count_0 = 1;
    for(int i = 2; i < length_0; i++){
        if(url_0[i] == '\0'){
            url_count_0++;
            if(url_0[i+1] == '!' && url_0[i+2] == '\0'){
                company_count_0++;
                i++;
                i++;
            if(url_0[i+1] == '\0')
                break;
            }
        }
    }

    int url_count_1 = 0;
    int company_count_1 = 1;
    for(int i = 2; i < length_1; i++){
        if(url_1[i] == '\0'){
            url_count_1++;
            if(url_1[i+1] == '!' && url_1[i+2] == '\0'){
                company_count_1++;
                i++;
                i++;
            if(url_1[i+1] == '\0')
                break;
            }
        }
    }


    int matrix_0[company_count_0][50];
    for(int a = 0; a < company_count_0; a++)
        for(int b = 0; b < 50; b++)
            matrix_0[a][b] = -1;

    matrix_0[0][0] = 2;
    int a = 0;
    int b = 0;
    for(int i = 2; i < length_0; i++){
        if(url_0[i] == '\0'){
            b++;
            if(url_0[i+1] == '!' && url_0[i+2] == '\0'){
                i++;
                i++;
                a++;
                b=0;
            if(url_0[i+1] == '\0')
                break;
            }
            matrix_0[a][b] = i + 1;
        }
    }

    // for(int a = 0; a < company_count_0; a++)
    //     for(int b = 0; b < 50; b++)
    //         if(matrix_0[a][b] != -1){
    //             puts(url_0 + matrix_0[a][b]);
    //         } 


    int matrix_1[company_count_1][50];
        for(int a = 0; a < company_count_1; a++)
        for(int b = 0; b < 50; b++)
            matrix_1[a][b] = -1;

    matrix_1[0][0] = 2;
    a = 0;
    b = 0;
    for(int i = 2; i < length_1; i++){
        if(url_1[i] == '\0'){
            b++;
            if(url_1[i+1] == '!' && url_1[i+2] == '\0'){
                i++;
                i++;
                a++;
                b=0;
            if(url_1[i+1] == '\0')
                break;
            }
            matrix_1[a][b] = i + 1;
        }
    }

    // for(int a = 0; a < company_count_1; a++)
    //     for(int b = 0; b < 50; b++)
    //         if(matrix_1[a][b] != -1){
    //             puts(url_1 + matrix_1[a][b]);
    //         } 


    /***********************************************************************
    MAKING TWO MATRICES OVER, START MATCHING
    ************************************************************************/

    FILE *fp = NULL;
    fp = fopen(file_name_out, "w");

    for(int a_0 = 0; a_0 < company_count_0; a_0++){
        for(int a_1 = 0; a_1 < company_count_1; a_1++){
            int matched_count = 0;
            for(int b_0 = 0; b_0 < set_len; b_0++){
                for(int b_1 = 0; b_1 < set_len; b_1++){
                    if(matrix_0[a_0][b_0] == -1 || matrix_1[a_1][b_1] == -1)
                        continue;
                    int len_temp = strlen(url_0 + matrix_0[a_0][b_0]);
                    if(len_temp == strlen(url_1 + matrix_1[a_1][b_1])){
                        if(fast_compare(url_0 + matrix_1[a_0][b_0], url_1 + matrix_1[a_1][b_1], len_temp) == 0){
                            matched_count++;
                        }
                    }
                }
            }
            if(matched_count != 0)
                fprintf(fp, "(%d, %d): %d\n", a_0, a_1, matched_count);
        }
    }

    fclose(fp);
    printf("Match succeeded.\n");


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

